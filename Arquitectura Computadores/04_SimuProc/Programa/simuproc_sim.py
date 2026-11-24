import sys

class SimuProcVM:
    def __init__(self):
        self.mem = [0] * 4096
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.pc = 0
        self.z = 0
        self.n = 0
        self.c = 0
        self.o = 0
        self.halted = False
        self.logs = []
        self.screen = []

    def load_asm(self, filename):
        with open(filename, 'r', encoding='latin1') as f:
            lines = f.readlines()
        
        curr_addr = 0
        self.code = [] # list of (addr, op, args, comment)
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            if line.startswith('#SimuProc'):
                continue
            if line.startswith('#'):
                # Address directive
                addr_hex = line[1:].split()[0].split(';')[0].rstrip('hH')
                curr_addr = int(addr_hex, 16)
                continue
            
            # Remove inline comment
            if ';' in line:
                code_part, comment = line.split(';', 1)
            else:
                code_part, comment = line, ""
            
            code_part = code_part.strip()
            if not code_part:
                continue
            
            # Check if this is a binary data definition
            parts = code_part.split()
            if len(parts) == 1 and all(ch in '01' for ch in parts[0]):
                val = int(parts[0], 2) & 0xFFFF
                self.mem[curr_addr] = val
                curr_addr += 1
                continue
            
            parts = code_part.split(None, 1)
            op = parts[0].upper()
            args = parts[1].strip() if len(parts) > 1 else ""
            self.code.append((curr_addr, op, args, comment.strip()))
            curr_addr += 1

    def run(self, inputs=None):
        input_idx = 0
        inputs = inputs or []
        step_count = 0
        trace = []

        code_map = {addr: (op, args, comment) for addr, op, args, comment in self.code}

        while not self.halted and step_count < 2000:
            step_count += 1
            if self.pc not in code_map:
                print(f"PC {self.pc:03X} not in code!")
                break
            
            op, args, comment = code_map[self.pc]
            pc_before = self.pc
            self.pc += 1

            # Execute
            if op == "MSG":
                msg = args.strip('"\'')
                self.screen.append(f"[MSG] {msg}")
            elif op == "LDA":
                addr = int(args.rstrip('hH'), 16)
                self.ax = self.mem[addr]
            elif op == "STA":
                addr = int(args.rstrip('hH'), 16)
                self.mem[addr] = self.ax & 0xFFFF
            elif op == "CLA":
                self.ax = 0
            elif op == "MOV":
                p1, p2 = [x.strip() for x in args.split(',')]
                # resolve p2 (source)
                if p2.upper() == "AX":
                    src = self.ax
                elif p2.upper() == "BX":
                    src = self.bx
                elif p2.upper() == "CX":
                    src = self.cx
                else:
                    src = self.mem[int(p2.rstrip('hH'), 16)]
                
                # set p1 (dest)
                if p1.upper() == "AX":
                    self.ax = src
                elif p1.upper() == "BX":
                    self.bx = src
                elif p1.upper() == "CX":
                    self.cx = src
                else:
                    self.mem[int(p1.rstrip('hH'), 16)] = src & 0xFFFF
            elif op == "ADD":
                addr = int(args.rstrip('hH'), 16)
                res = self.ax + self.mem[addr]
                if res > 0xFFFF:
                    self.bx = (res >> 16) & 0xFFFF
                    self.o = 1
                else:
                    self.o = 0
                self.ax = res & 0xFFFF
                self.z = 1 if self.ax == 0 else 0
                self.n = 1 if (self.ax & 0x8000) else 0
            elif op == "SUB":
                addr = int(args.rstrip('hH'), 16)
                res = self.ax - self.mem[addr]
                self.ax = res & 0xFFFF
                self.z = 1 if self.ax == 0 else 0
                self.n = 1 if res < 0 else 0
            elif op == "MUL":
                addr = int(args.rstrip('hH'), 16)
                res = self.ax * self.mem[addr]
                self.bx = (res >> 16) & 0xFFFF
                self.ax = res & 0xFFFF
                self.o = 1 if self.bx > 0 else 0
                self.z = 1 if (self.ax == 0 and self.bx == 0) else 0
            elif op == "DIV":
                addr = int(args.rstrip('hH'), 16)
                divisor = self.mem[addr]
                if divisor == 0:
                    print("Division by zero!")
                    break
                quot = self.ax // divisor
                rem = self.ax % divisor
                self.ax = quot & 0xFFFF
                self.bx = rem & 0xFFFF
                self.z = 1 if self.ax == 0 else 0
            elif op == "CMP":
                addr = int(args.rstrip('hH'), 16)
                diff = self.ax - self.mem[addr]
                self.z = 1 if diff == 0 else 0
                self.n = 1 if diff < 0 else 0
            elif op == "JEQ":
                addr = int(args.rstrip('hH'), 16)
                if self.z == 1:
                    self.pc = addr
            elif op == "JMA":
                addr = int(args.rstrip('hH'), 16)
                if self.z == 0 and self.n == 0:
                    self.pc = addr
            elif op == "JME":
                addr = int(args.rstrip('hH'), 16)
                if self.z == 0 and self.n == 1:
                    self.pc = addr
            elif op == "LOOP":
                addr = int(args.rstrip('hH'), 16)
                self.cx = (self.cx - 1) & 0xFFFF
                if self.cx != 0:
                    self.pc = addr
            elif op == "JMP":
                addr = int(args.rstrip('hH'), 16)
                self.pc = addr
            elif op == "LDT":
                val = inputs[input_idx] if input_idx < len(inputs) else 0
                input_idx += 1
                self.ax = val & 0xFFFF
                self.screen.append(f"[LDT] {args} -> {val}")
            elif op == "EAP":
                self.screen.append(f"[EAP] {args} AX={self.ax} (0x{self.ax:04X})")
            elif op == "HLT":
                self.halted = True
                self.screen.append("[HLT] Fin de programa")
            
            trace.append({
                'step': step_count,
                'pc': pc_before,
                'op': f"{op} {args}".strip(),
                'ax': self.ax,
                'bx': self.bx,
                'cx': self.cx,
                'z': self.z,
                'n': self.n,
                'o': self.o
            })
        
        return trace

print("VM implementation complete")

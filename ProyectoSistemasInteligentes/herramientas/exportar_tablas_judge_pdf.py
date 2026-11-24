"""Síntesis del controlador general: tablas, Karnaugh y circuito por bloques."""
from pathlib import Path
from itertools import product
from math import atan2, sin, cos
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib import colors

ROOT=Path(__file__).resolve().parent.parent
OUTPUT=ROOT/'output/pdf/Tablas_Karnaugh_y_circuito_Judge.pdf'
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial',boldItalic='Arial-Bold')
W,H=1191,842
INK='#183346'; MUTED='#526775'; LINE='#d2dfe7'; GREEN='#16835b'
PHASES=['#2563a0','#7d4eb1','#087b78','#ba6320','#a33f60']
FILLS=['#eaf2fb','#f1ecf8','#e8f5f2','#fff1e6','#fbeef2']
c=canvas.Canvas(str(OUTPUT),pagesize=(W,H))
c.setTitle('Judge - Tablas de estados, salidas, Karnaugh y circuito')
c.setAuthor('Equipo de proyecto')
page=0

def text(s,x,top,size=12,width=200,align='left',bold=False,color=INK):
    style=ParagraphStyle('t',fontName='Arial-Bold' if bold else 'Arial',fontSize=size,leading=size*1.3,textColor=colors.HexColor(color),alignment={'left':0,'center':1,'right':2}[align])
    p=Paragraph(escape(s).replace('\n','<br/>'),style)
    _,h=p.wrap(width,1000)
    left=x-width/2 if align=='center' else x-width if align=='right' else x
    p.drawOn(c,left,top-h)
    return top-h

def begin(title,sub):
    global page
    page+=1
    text('JUDGE / JUGADOR 1 CONTRA JUGADOR 2 / CONTROLADOR GENERAL',40,817,10,1111,bold=True,color=MUTED)
    text(title,40,794,26,1111,bold=True)
    text(sub,40,754,12,1111,color=MUTED)
    c.setStrokeColor(colors.HexColor(LINE));c.setLineWidth(.8);c.line(40,728,1151,728)
    c.line(40,34,1151,34)
    text('Tablas y síntesis lógica | Q0 a Q4 son las fases del diagrama general',40,26,9,1000,color=MUTED)
    text(str(page),1151,26,9,35,'right',color=MUTED)

def end():c.showPage()

def cell(x,top,w,h,s,fill=None,bold=False,size=11,color=INK):
    c.setStrokeColor(colors.HexColor(LINE));c.setLineWidth(.6)
    if fill:c.setFillColor(colors.HexColor(fill))
    c.rect(x,top-h,w,h,fill=bool(fill),stroke=1)
    text(s,x+w/2,top-h/2+size*.6,size,w-6,'center',bold,color)

def table(rows,x,top,widths,rowh=36,header=True):
    for j,row in enumerate(rows):
        xx=x
        for w,s in zip(widths,row):
            cell(xx,top-j*rowh,w,rowh,str(s),INK if j==0 and header else '#f2f6f9' if j%2 else '#ffffff',j==0 and header,11,'#ffffff' if j==0 and header else INK)
            xx+=w

def wire(points,color=INK,dashed=False):
    c.saveState();c.setStrokeColor(colors.HexColor(color));c.setLineWidth(1.5)
    if dashed:c.setDash(4,3)
    p=c.beginPath();p.moveTo(*points[0])
    for xy in points[1:]:p.lineTo(*xy)
    c.drawPath(p);c.restoreState()

def arrow(points,color=INK):
    wire(points,color);x,y=points[-1];px,py=points[-2];a=atan2(y-py,x-px)
    p=c.beginPath();p.moveTo(x,y);p.lineTo(x-8*cos(a-.4),y-8*sin(a-.4));p.lineTo(x-8*cos(a+.4),y-8*sin(a+.4));p.close()
    c.setFillColor(colors.HexColor(color));c.drawPath(p,fill=1,stroke=0)

def leds(state):return [int(state==i) for i in range(5)]

def expected(state,S,P,F,V,R=0):
    if R or state>4:return 0
    if state==0:return int(S)
    if state==1:return 2
    if state==2:return 2+int(P)
    if state==3:return (4 if V else 2) if F else 3
    return 4

def equations(state,S,P,F,V,R=0):
    L1,L2,L3,L4,L5=leds(state)
    A=F and V;B=(not F) or (not V);C=not F;G=not R
    d2=G and ((L4 and A) or L5)
    d1=G and (L2 or L3 or (L4 and B))
    d0=G and ((L1 and S) or (L3 and P) or (L4 and C))
    return (int(d2)<<2)|(int(d1)<<1)|int(d0)

# Exhaustive mathematical check, including reset and all three unused codes.
for state in range(8):
    for R,S,P,F,V in product([0,1],repeat=5):
        assert equations(state,S,P,F,V,R)==expected(state,S,P,F,V,R)
assert sum(leds(0))==1 and leds(7)==[0]*5

begin('1 / Tabla de transición y salidas','Como en la pizarra: estado actual a la izquierda, entradas arriba y salidas L a la derecha.')
text('Q0 = espera; Q1 = inicialización; Q2 = preparación; Q3 = evaluación; Q4 = final. Son las mismas fases q0 a q4 del PDF de autómatas.',40,706,12,1111)
text('Los bits del estado son q2, q1 y q0 (en minúscula). Ejemplo: Q3 se guarda como 011. No confundir Q1, una fase, con q1, un bit.',40,680,12,1111)
text('Entradas en orden S P F V: S = Game B; P = preparación lista; F = ronda resuelta y puntos actualizados; V = hay ganador.',40,651,12,1111,bold=True)
first=128; cw=48; lw=39;x0=40;top=596;hh=39;rh=40
cell(x0,top,first,hh,'Q (q2 q1 q0)',INK,True,11,'#ffffff')
for inp in range(16):cell(x0+first+inp*cw,top,cw,hh,f'{inp:04b}',INK,True,10.5,'#ffffff')
outx=x0+first+16*cw
for i in range(5):cell(outx+i*lw,top,lw,hh,f'L{i+1}',PHASES[i],True,11,'#ffffff')
for st in range(8):
    y=top-hh-st*rh;fill=FILLS[st] if st<5 else '#f1f4f6'
    cell(x0,y,first,rh,f'Q{st} ({st:03b})' if st<5 else f'{st:03b} sin usar',fill,True)
    for inp in range(16):
        S,P,F,V=((inp>>k)&1 for k in [3,2,1,0]);n=expected(st,S,P,F,V)
        cell(x0+first+inp*cw,y,cw,rh,f'{n:03b}',fill,size=11)
    for i,L in enumerate(leds(st)):cell(outx+i*lw,y,lw,rh,str(L),fill,bold=bool(L))
c.setLineWidth(2.3);c.setStrokeColor(colors.HexColor(PHASES[0]));c.rect(x0+first+8*cw,top-hh-rh,cw,rh,fill=0,stroke=1)
text('Casilla marcada: en Q0 (000), entradas 1000 significan S = 1. El siguiente estado es 001, es decir Q1.',40,211,13,1111,bold=True)
text('Las L describen el estado actual, no el siguiente. L1 = espera, L2 = inicialización, L3 = preparación, L4 = evaluación, L5 = final. Se pueden visualizar con cinco LED.',40,173,12,1111)
text('Aquí 1 significa activo y 0 inactivo. Son indicadores de fase propuestos; no son las señales individuales de la pantalla ni incrementan directamente el puntaje.',40,134,11,1111,color=MUTED)
text('La tabla supone R = 0. Con reinicio R = 1, los bits siguientes son 000. Los códigos sin usar también regresan a 000 en el siguiente pulso.',40,95,11,1111,color=MUTED)
end()

begin('2 / Del estado actual a las entradas D','D2, D1 y D0 son los bits que los tres flip-flops cargarán en el siguiente pulso de reloj.')
rows=[['Actual','Condición','Siguiente','D2','D1','D0'],['Cualquiera','R = 1','Q0 (000)',0,0,0],['Q0 (000)','R = 0; S = 0','Q0 (000)',0,0,0],['Q0 (000)','R = 0; S = 1','Q1 (001)',0,0,1],['Q1 (001)','R = 0','Q2 (010)',0,1,0],['Q2 (010)','R = 0; P = 0','Q2 (010)',0,1,0],['Q2 (010)','R = 0; P = 1','Q3 (011)',0,1,1],['Q3 (011)','R = 0; F = 0','Q3 (011)',0,1,1],['Q3 (011)','R = 0; F = 1; V = 0','Q2 (010)',0,1,0],['Q3 (011)','R = 0; F = 1; V = 1','Q4 (100)',1,0,0],['Q4 (100)','R = 0','Q4 (100)',1,0,0],['101, 110, 111','R = 0','Q0 (000)',0,0,0]]
table(rows,40,695,[180,360,270,100,100,101],rowh=39)
text('En un flip-flop D: q(t + 1) = D(t). Los tres D se calculan con el estado y las entradas actuales; los tres q se actualizan juntos.',40,196,13,1111,bold=True)
text('Ejemplo: estás en Q3 = 011 y la ronda termina con ganador (F = 1, V = 1). La lógica entrega D2 D1 D0 = 100. Al siguiente pulso, el estado pasa a Q4 y L5 se enciende.',40,154,12,1111)
text('S, P, F y V son señales del controlador general. Los botones de atacar y esquivar de J1 y J2 se procesan dentro de Q3; su resultado se comunica mediante F y V.',40,100,11.5,1111,color=MUTED)
end()

def kmap3(x,top,i):
    text(f'L{i+1} / '+['Espera','Inicialización','Preparación','Evaluación','Final'][i],x,top,16,340,bold=True,color=PHASES[i])
    xx=x+50; yy=top-64;cw=64;ch=47;order=[0,1,3,2]
    text('q1 q0',xx+128,top-32,10.5,200,'center')
    text('q2',x+9,yy-36,10.5,35)
    for j,n in enumerate(order):cell(xx+j*cw,yy,cw,28,f'{n:02b}','#edf2f5',True)
    active=None
    for row in range(2):
        text(str(row),xx-14,yy-28-row*ch-16,12,20,'center')
        for col,low in enumerate(order):
            value=int(row*4+low==i);t=yy-28-row*ch
            cell(xx+col*cw,t,cw,ch,str(value),FILLS[i] if value else '#ffffff',value,size=15)
            if value:active=(xx+col*cw,t-ch)
    c.setStrokeColor(colors.HexColor(GREEN));c.setLineWidth(2)
    ax,ay=active;c.roundRect(ax+7,ay+5,cw-14,ch-10,10,fill=0,stroke=1)
    eq=['!q2 · !q1 · !q0','!q2 · !q1 · q0','!q2 · q1 · !q0','!q2 · q1 · q0','q2 · !q1 · !q0'][i]
    text(f'L{i+1} = {eq}',x,top-218,14,340,bold=True)

begin('3 / Mapas de Karnaugh de L1 a L5','Tres bits de estado: filas q2; columnas q1 q0 en orden Gray 00, 01, 11, 10.')
for x,top,i in [(40,698,0),(423,698,1),(806,698,2),(230,404,3),(613,404,4)]:kmap3(x,top,i)
text('! significa NO; · significa Y. Ejemplo: L3 = 1 solamente cuando q2 q1 q0 = 010, o sea en Q2.',40,116,12,1111,bold=True)
text('Cada mapa tiene un solo 1: su grupo es una casilla. Los códigos no usados se fijan en 0 para apagar las cinco L; por eso no se marcan X como en otros ejemplos.',40,79,11.5,1111,color=MUTED)
end()

def kmap2(x,top,name,vals,eq,groups):
    text(name,x,top,17,320,bold=True)
    xx=x+50;yy=top-60;cw=90;ch=60
    text('V',xx+90,top-30,12,180,'center');text('F',x+12,yy-52,12,30)
    for col in range(2):cell(xx+col*cw,yy,cw,30,str(col),'#edf2f5',True)
    for row in range(2):
        text(str(row),xx-15,yy-30-row*ch-21,12,20,'center')
        for col in range(2):cell(xx+col*cw,yy-30-row*ch,cw,ch,str(vals[row][col]),'#f3f8f5' if vals[row][col] else '#ffffff',size=17)
    c.setStrokeColor(colors.HexColor(GREEN));c.setLineWidth(2)
    for row,col,nr,nc in groups:c.roundRect(xx+col*cw+5,yy-30-(row+nr)*ch+5,nc*cw-10,nr*ch-10,10,fill=0,stroke=1)
    text(eq,x,top-239,17,340,bold=True)

begin('4 / Karnaugh de la decisión y ecuaciones','Separamos la decodificación de estado y la decisión de Q3 para trabajar con mapas pequeños.')
kmap2(60,695,'A / Ronda con ganador',[[0,0],[0,1]],'A = F · V',[(1,1,1,1)])
kmap2(440,695,'B / El bit D1 sigue en 1',[[1,1],[1,0]],'B = !F + !V',[(0,0,1,2),(0,0,2,1)])
kmap2(820,695,'C / Evaluación en curso',[[1,1],[0,0]],'C = !F',[(0,0,1,2)])
text('Ecuaciones de los tres bits siguientes',40,401,18,1111,bold=True)
text('D2 = !R · (L4 · A + L5)',65,354,20,1000,bold=True)
text('D1 = !R · (L2 + L3 + L4 · B)',65,308,20,1000,bold=True)
text('D0 = !R · (L1 · S + L3 · P + L4 · C)',65,262,20,1000,bold=True)
text('+ significa O. Cuando R = 1, los tres D valen 0; el reinicio es síncrono y se hace efectivo en el siguiente pulso.',40,191,12,1111)
text('Ejemplo en Q3: solo L4 vale 1. Con F = 1 y V = 1, A = 1, B = 0, C = 0; por tanto D2 D1 D0 = 100.',40,151,12,1111)
text('La tabla completa combina 3 bits de estado y 4 entradas: 7 variables sin contar R. No se presenta un mapa gigante; las funciones se factorizan en los mapas de 3 y 2 variables mostrados aquí.',40,105,11.5,1111,color=MUTED)
text('Base del curso: clase 06, pp. 7 y 17; clase 07, p. 2; clase 08, pp. 3-4. Las ecuaciones se verificaron en las 256 combinaciones de estado, entradas y reinicio.',40,63,10,1111,color=MUTED)
end()

def gate(kind,x,y,n=2):
    w=80;h=54
    c.setStrokeColor(colors.HexColor(INK));c.setFillColor(colors.HexColor('#eff5f8'));c.setLineWidth(1.7)
    p=c.beginPath()
    if kind=='AND':
        p.moveTo(x,y-h/2);p.lineTo(x+w/2,y-h/2);p.curveTo(x+7*w/6,y-h/2,x+7*w/6,y+h/2,x+w/2,y+h/2);p.lineTo(x,y+h/2);p.close()
        inputs=[(x,y+12),(x,y-12)]
    else:
        p.moveTo(x,y-h/2);p.curveTo(x+w*.5,y-h/2,x+w*.85,y-h*.35,x+w,y);p.curveTo(x+w*.85,y+h*.35,x+w*.5,y+h/2,x,y+h/2);p.curveTo(x+22,y+10,x+22,y-10,x,y-h/2);p.close()
        # The rear curve reaches x+16.5 at the center and x+9 near y +/-18.
        inputs=[(x+9,y+18),(x+16.5,y),(x+9,y-18)] if n==3 else [(x+12,y+12),(x+12,y-12)]
    c.drawPath(p,fill=1,stroke=1)
    text(kind,x+43,y+6,10,60,'center',True)
    return inputs,(x+w,y)

def and_term(x,y,a,b):
    ins,out=gate('AND',x,y)
    for pt,label in zip(ins,[a,b]):wire([(x-135,pt[1]),pt]);text(label,x-150,pt[1]+8,13,100,'right',True)
    return out

def final_gate(y,raw,name):
    ins,out=gate('AND',830,y)
    wire([raw,(750,raw[1]),(750,ins[0][1]),ins[0]])
    wire([(780,ins[1][1]),ins[1]]);text('G',760,ins[1][1]+8,13,40,'center',True)
    arrow([out,(1080,y)]);text(name,1100,y+10,16,70,'center',True)

begin('5 / Circuito combinacional de D2, D1 y D0','AND = Y; OR = O. Señales auxiliares: A = F · V; B = !F + !V; C = !F; G = !R.')
# D2: L4 A + L5
out=and_term(270,650,'L4','A');ins,raw=gate('OR',540,650)
wire([out,(460,650),(460,ins[0][1]),ins[0]])
wire([(415,ins[1][1]),ins[1]]);text('L5',396,ins[1][1]+8,13,70,'right',True);final_gate(650,raw,'D2')
# D1: L2 + L3 + L4 B
out=and_term(270,405,'L4','B');ins,raw=gate('OR',540,455,3)
wire([out,(460,405),(460,ins[2][1]),ins[2]])
for pt,label in zip(ins[:2],['L2','L3']):wire([(415,pt[1]),pt]);text(label,396,pt[1]+8,13,70,'right',True)
final_gate(455,raw,'D1')
# D0: L1 S + L3 P + L4 C
outs=[and_term(270,y,a,b) for y,a,b in [(280,'L1','S'),(200,'L3','P'),(120,'L4','C')]]
ins,raw=gate('OR',540,200,3)
for out,pt in zip(outs,ins):wire([out,(460,out[1]),(460,pt[1]),pt])
final_gate(200,raw,'D0')
text('Cada D va a su flip-flop del mismo número. Las L se obtienen de los bits actuales mediante el decodificador de la página siguiente.',40,73,12,1111,color=MUTED)
end()

begin('6 / Memoria de estado y salidas L','Tres flip-flops D guardan q2, q1 y q0. Los cinco indicadores se obtienen del estado actual.')
for bit,y in [(2,650),(1,475),(0,300)]:
    c.setStrokeColor(colors.HexColor(INK));c.setFillColor(colors.HexColor('#edf4f9'));c.setLineWidth(1.5)
    c.rect(360,y-40,110,80,fill=1,stroke=1)
    text(f'FF-D {bit}',415,y+25,14,100,'center',True)
    text('D',373,y+5,12,25);text('Q',449,y+5,12,25)
    wire([(150,y),(360,y)]);text(f'D{bit}',115,y+9,16,60,'center',True)
    wire([(315,y-23),(360,y-23)]);text('CLK',284,y-15,11,50,'center')
    p=c.beginPath();p.moveTo(360,y-32);p.lineTo(371,y-23);p.lineTo(360,y-14);c.drawPath(p)
    wire([(470,y),(680,y)]);text(f'q{bit}',567,y+20,16,70,'center',True)
c.setFillColor(colors.HexColor('#eef6f3'));c.setStrokeColor(colors.HexColor(GREEN));c.rect(680,260,170,430,fill=1,stroke=1)
text('DECODIFICADOR',765,590,14,160,'center',True,color=GREEN)
text('q2 q1 q0\n\nLas 5 ecuaciones\nde la página 3',765,554,13,145,'center')
for i,y in enumerate([650,560,470,380,290]):
    wire([(850,y),(1044,y)],PHASES[i])
    c.setFillColor(colors.HexColor(FILLS[i]));c.setStrokeColor(colors.HexColor(PHASES[i]));c.circle(1062,y,18,fill=1,stroke=1)
    text(f'L{i+1}',1109,y+10,15,60,'center',True,color=PHASES[i])
    text(['Espera','Inicialización','Preparación','Evaluación','Final'][i],945,y+26,12,170,'center',color=PHASES[i])
text('CLK es la misma señal para los tres flip-flops. Los nombres iguales indican la misma conexión. R está incluido en las ecuaciones D: no se añade aquí un borrado asíncrono.',40,205,12,1111)
text('En 011 se enciende solo L4. Si la lógica calcula D = 100, el siguiente pulso cambia el estado a 100 y pasa a encenderse L5.',40,150,13,1111,bold=True)
text('Los q alimentan el decodificador; las L vuelven a la lógica de la página 5. Así el circuito recuerda la fase y calcula la siguiente. Este es el controlador general; el conteo, los números y el arbitraje interno son otros bloques.',40,105,11.5,1111,color=MUTED)
end()
c.save()
print(OUTPUT)
print('Verificadas 256 combinaciones de estado, entradas y reset.')

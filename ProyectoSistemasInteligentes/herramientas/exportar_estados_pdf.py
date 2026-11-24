"""Guía visual de autómatas de Judge; exportación vectorial en siete páginas."""
from pathlib import Path
from math import atan2, cos, sin, sqrt
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parent.parent
OUTPUT=ROOT/'output/pdf/Estados_y_automatas_Judge.pdf'
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial',boldItalic='Arial-Bold')
W,H=842,595
INK='#183346'; MUTED='#526775'; LINE='#dae3e9'
COLORS=['#2563a0','#7d4eb1','#087b78','#ba6320','#a33f60']
FILLS=['#eaf2fb','#f1ecf8','#e8f5f2','#fff1e6','#fbeef2']
c=canvas.Canvas(str(OUTPUT),pagesize=(W,H))
c.setTitle('Judge - Guía visual de estados y autómatas')
c.setAuthor('Equipo de proyecto')
page=0

def txt(s,x,y,size=11,width=160,align='left',color=INK,bold=False,background=False):
    style=ParagraphStyle('label',fontName='Arial-Bold' if bold else 'Arial',fontSize=size,leading=size*1.27,textColor=colors.HexColor(color),alignment={'left':0,'center':1,'right':2}[align])
    p=Paragraph(escape(s).replace('\n','<br/>'),style)
    _,h=p.wrap(width,500)
    xx=x-width/2 if align=='center' else x-width if align=='right' else x
    if background:
        c.setFillColor(colors.white); c.rect(xx-3,y-h-2,width+6,h+5,fill=1,stroke=0)
    p.drawOn(c,xx,y-h)
    return y-h

def arrow(points,color=INK,dashed=False):
    c.saveState(); c.setStrokeColor(colors.HexColor(color)); c.setFillColor(colors.HexColor(color)); c.setLineWidth(1.6)
    if dashed:c.setDash(4,3)
    p=c.beginPath();p.moveTo(*points[0])
    for xy in points[1:]:p.lineTo(*xy)
    c.drawPath(p)
    c.setDash()
    x,y=points[-1]; px,py=points[-2]; a=atan2(y-py,x-px)
    p=c.beginPath();p.moveTo(x,y);p.lineTo(x-8*cos(a-.43),y-8*sin(a-.43));p.lineTo(x-8*cos(a+.43),y-8*sin(a+.43));p.close()
    c.drawPath(p,fill=1,stroke=0);c.restoreState()

def state(code,name,x,y,phase,r=43):
    c.setFillColor(colors.HexColor(FILLS[phase]));c.setStrokeColor(colors.HexColor(COLORS[phase]));c.setLineWidth(2)
    c.circle(x,y,r,fill=1,stroke=1)
    txt(code,x,y+23,14,2*r-12,'center',COLORS[phase],True)
    txt(name,x,y+2,10.6,2*r-11,'center')

def loop(x,y,label,phase,side='top',r=43):
    d=1 if side=='top' else -1
    anchor=y+d*sqrt(r*r-20*20)
    control=y+d*(r+43)
    start=(x-20,anchor); finish=(x+20,anchor)
    c.saveState(); c.setStrokeColor(colors.HexColor(COLORS[phase])); c.setLineWidth(1.6)
    p=c.beginPath();p.moveTo(*start);p.curveTo(x-90,control,x+90,control,*finish);c.drawPath(p)
    a=atan2(finish[1]-control,finish[0]-(x+90))
    p=c.beginPath();p.moveTo(*finish);p.lineTo(finish[0]-8*cos(a-.43),finish[1]-8*sin(a-.43));p.lineTo(finish[0]-8*cos(a+.43),finish[1]-8*sin(a+.43));p.close()
    c.setFillColor(colors.HexColor(COLORS[phase]));c.drawPath(p,fill=1,stroke=0);c.restoreState()
    txt(label,x,y+(r+53 if d==1 else -r-40),10,195,'center')

def begin(title,subtitle,section):
    global page
    page+=1;c.setFillColor(colors.white);c.rect(0,0,W,H,fill=1,stroke=0)
    txt('GAME & WATCH / JUDGE / J1 VS. J2',40,568,9,400,color=MUTED,bold=True)
    txt(title,40,547,23,760,bold=True)
    txt(subtitle,40,515,11,760,color=MUTED)
    c.setStrokeColor(colors.HexColor(LINE));c.setLineWidth(.8);c.line(40,502,802,502)
    c.line(40,32,802,32)
    txt(section,40,25,8,690,color=MUTED)
    txt(str(page),802,25,8,30,'right',MUTED)

def sidebar(phase,meaning,action,example,extra=''):
    # Explanations sit below the graph so every main chain reads left to right.
    c.setStrokeColor(colors.HexColor(LINE));c.line(40,190,802,190)
    for x,title,body in [(40,'En palabras simples',meaning),(305,'Qué hace',action),(570,'Ejemplo',example)]:
        txt(title,x,173,12,225,color=COLORS[phase],bold=True)
        txt(body,x,148,11,225)

def entry(x,y,phase):
    txt('Entrada',x,y+24,10,85,'center',MUTED)
    arrow([(x,y+7),(x,y-20)],COLORS[phase])

def exit_to(q,x,y):
    txt('Ir a '+q,x,y,11,90,'center',bold=True)

def end():c.showPage()

# 1. Cadena horizontal de cinco fases, con retornos en carriles separados.
begin('El autómata completo','Jugador 1 contra jugador 2. Lectura principal: de izquierda a derecha.','01 / Diagrama general - dos jugadores')
xs=[90,245,400,555,710]; y=330; r=40
arrow([(40,y),(50,y)]);txt('Inicio',41,392,10,60,'center')
labels=['Game B','Siguiente\npulso','Números\nrevelados','Ronda resuelta:\nhay ganador']
for i,label in enumerate(labels):
    arrow([(xs[i]+r,y),(xs[i+1]-r,y)])
    txt(label,(xs[i]+xs[i+1])/2,306,10.5,130,'center')
arrow([(555,370),(555,464),(400,464),(400,370)])
txt('Ronda resuelta: sin ganador',477,491,10.5,225,'center')
arrow([(710,290),(710,205),(90,205),(90,290)],MUTED,dashed=True)
txt('Reiniciar',323,226,10.5,120,'center',MUTED)
loop(90,y,'Sin Game B',0,r=r);loop(400,y,'Preparación en curso',2,'bottom',r=r)
loop(555,y,'Evaluación en curso',3,'bottom',r=r);loop(710,y,'Sin reinicio',4,r=r)
for x,code,name,phase in zip(xs,['q0','q1','q2','q3','q4'],['Espera /\nreloj','Iniciar\npartida','Preparar\nronda','Resolver\nronda','Fin de\npartida'],range(5)):
    state(code,name,x,y,phase,r=r)
sidebar(0,'Círculo = estado. Flecha = cambio. Texto = condición. Bucle = permanecer. Pulso = señal del reloj.','Ambos participantes son personas. Game B inicia la partida. Reiniciar vuelve a q0 desde cualquier fase.','Presionas Game B: q0 pasa a q1 y luego a q2. Durante q3 se leen los botones de J1 y de J2.')
end()

# 2. q0
begin('q0 / Esperar a los jugadores','Estados internos E0 y E1, en horizontal.','02 / Detalle de q0 - dos jugadores')
arrow([(70,330),(177,330)],COLORS[0]);txt('Entrada',118,360,10.5,100,'center')
loop(220,330,'Sin Game B',0)
arrow([(263,330),(457,330)],COLORS[0]);txt('Game B',360,361,11,150,'center')
arrow([(543,330),(740,330)],COLORS[0]);txt('Inicio confirmado',640,361,10.5,165,'center');exit_to('q1',770,341)
state('E0','Mostrar\nreloj',220,330,0);state('E1','Confirmar\ninicio',500,330,0)
sidebar(0,'El juego espera a que los dos participantes quieran empezar.','Muestra la hora. Game B confirma el inicio de una partida para dos personas.','Sin pulsar Game B, permanece en E0. Al pulsarlo, pasa por E1 y sale hacia q1.')
end()

# 3. q1
begin('q1 / Iniciar una partida','Un estado interno: I0.','03 / Detalle de q1 - dos jugadores')
arrow([(80,330),(292,330)],COLORS[1]);txt('Entrada a q1',180,362,11,150,'center')
arrow([(408,330),(740,330)],COLORS[1]);txt('Siguiente pulso',571,362,11,175,'center');exit_to('q2',770,341)
state('I0','Poner\npuntajes a 0',350,330,1,r=58)
sidebar(1,'Prepara una partida nueva para J1 y J2.','Pone ambos puntajes en cero y limpia los datos anteriores. No se repite entre rondas.','Si los marcadores anteriores eran 24 y 18, al iniciar ambos quedan en 0.')
end()

# 4. q2
begin('q2 / Preparar una ronda','P0, P1, P2 y P3 avanzan de izquierda a derecha.','04 / Detalle de q2 - dos jugadores')
xs=[110,300,490,680];y=330;r=43
arrow([(40,y),(67,y)],COLORS[2]);txt('Entrada',45,361,10,85,'center')
for i,label in enumerate(['Siguiente pulso','Cuenta terminada','Números válidos']):
    arrow([(xs[i]+r,y),(xs[i+1]-r,y)],COLORS[2]);txt(label,(xs[i]+xs[i+1])/2,305,10.5,145,'center')
loop(300,y,'Cuenta en curso',2);loop(490,y,'Números aún no válidos',2)
arrow([(723,y),(780,y)],COLORS[2]);txt('Revelados',756,305,10,90,'center');txt('q3',800,341,12,35,'center',bold=True)
for x,code,name in zip(xs,['P0','P1','P2','P3'],['Iniciar\ncuenta','Esperar\ncuenta','Guardar\nnúmeros','Mostrar\nnúmeros']):state(code,name,x,y,2)
sidebar(2,'Organiza la siguiente ronda y conserva los puntos acumulados.','Hace la cuenta regresiva, guarda dos números del 1 al 9 y los muestra. Esos números se mantienen durante q3.','N1 = 8 y N2 = 3. Cuando los dos números están listos y visibles, comienza la reacción de ambos jugadores.')
end()

# 5. q3: los seis estados en una sola fila; las dos salidas abren ramas.
begin('q3 / Resolver la ronda','A0 a A5 en horizontal. A5 separa las dos salidas posibles.','05 / Detalle de q3 - dos jugadores')
xs=[80,205,330,455,580,705]; y=330;r=36
arrow([(22,y),(44,y)],COLORS[3]);txt('Entrada',42,390,10,80,'center')
labels=['Siguiente\npulso','Tiempo\nterminado','Comparación\nlista','Resultado\nlisto','Puntos\nactualizados']
for i,label in enumerate(labels):
    arrow([(xs[i]+r,y),(xs[i+1]-r,y)],COLORS[3]);txt(label,(xs[i]+xs[i+1])/2,285,10,110,'center')
loop(205,y,'Ventana abierta: registrar acciones',3,r=r);loop(455,y,'Evaluación pendiente',3,r=r)
arrow([(739,342),(792,401)],COLORS[3]);txt('Sin ganador',750,460,10,105,'center');txt('q2',800,424,12,35,'center',bold=True)
arrow([(739,318),(792,249)],COLORS[3]);txt('Hay ganador',751,232,10,105,'center');txt('q4',800,255,12,35,'center',bold=True)
for x,code,name in zip(xs,['A0','A1','A2','A3','A4','A5'],['Abrir\nventana','Registrar\nacciones','Comparar\nnúmeros','Evaluar\nacciones','Actualizar\npuntos','Comprobar\nvictoria']):state(code,name,x,y,3,r=r)
sidebar(3,'Lee las acciones de dos personas: los botones de ataque y esquiva de J1 y J2.','Registra los botones de J1 y J2 hasta que cierre el tiempo. Evalúa, actualiza una sola vez y comprueba si alguien llegó a 50.','Con N1 = 8 y N2 = 3, J1 debe atacar y J2 esquivar. Sin ganador vuelve a q2; con ganador pasa a q4.')
end()

# 6. q4
begin('q4 / Mostrar el resultado final','Un estado interno: G0.','06 / Detalle de q4 - dos jugadores')
arrow([(80,330),(292,330)],COLORS[4]);txt('Entrada a q4',180,362,11,150,'center')
loop(350,330,'Sin reinicio',4,r=58)
arrow([(408,330),(740,330)],COLORS[4]);txt('Reiniciar',571,362,11,175,'center');exit_to('q0',770,341)
state('G0','Mostrar\nganador',350,330,4,r=58)
sidebar(4,'La partida entre J1 y J2 terminó.','Muestra al ganador y conserva el marcador final hasta reiniciar. No prepara otra ronda.','J2 alcanza 50 puntos. Se muestra el resultado; al reiniciar se regresa a q0, esperando otra partida.')
end()

# 7. Significados y conexión breve con las clases revisadas.
begin('Qué significa cada estado','q0 a q4 son las fases. Las otras letras nombran estados dentro de cada fase.','07 / Significados y relación con el curso')

def group(x,y,title,phase,items,width=225):
    txt(title,x,y,13,width,color=COLORS[phase],bold=True); y-=27
    for code,description in items:
        txt(code,x,y,10.5,35,color=COLORS[phase],bold=True)
        bottom=txt(description,x+38,y,10.5,width-38)
        y=bottom-10
    return y

y=group(40,476,'q0 / Esperar',0,[('E0','Muestra el reloj y espera inicio.'),('E1','Confirma el inicio para dos personas.')])
y=group(40,y-16,'q1 / Inicializar',1,[('I0','Pone puntajes a cero y prepara la partida.')])
group(40,y-16,'q4 / Finalizar',4,[('G0','Muestra al ganador y espera reinicio.')])
group(305,476,'q2 / Preparar ronda',2,[('P0','Inicia la cuenta regresiva.'),('P1','Espera el fin de la cuenta.'),('P2','Guarda N1 y N2.'),('P3','Revela los números.')])
group(570,476,'q3 / Resolver ronda',3,[('A0','Abre el tiempo de reacción.'),('A1','Registra acciones y su orden.'),('A2','Compara N1 y N2.'),('A3','Evalúa las acciones registradas.'),('A4','Actualiza los puntos una vez.'),('A5','Comprueba si hay ganador.')],width=232)
c.setStrokeColor(colors.HexColor(LINE));c.line(40,210,802,210)
txt('Cómo se conecta con la materia',40,196,14,750,bold=True)
txt('Binario',40,166,10.5,100,bold=True)
txt('Los 5 estados pueden codificarse 000, 001, 010, 011 y 100: se necesitan 3 bits.',150,166,10.5,650)
txt('Lógica booleana',40,139,10.5,110,bold=True)
txt('Ejemplo: salir de q0 si Game B vale 1; si vale 0, permanecer en q0.',150,139,10.5,650)
txt('Karnaugh',40,112,10.5,100,bold=True)
txt('Primero se obtiene la tabla de transición; luego se simplifican sus funciones para el circuito.',150,112,10.5,650)
txt('Material revisado: clase 02, p. 4 (binario); clase 06, pp. 7 y 17 (funciones y tablas); clase 07, p. 2 (simplificación); clase 08, pp. 3-4 (Karnaugh). Los dibujos son el modelo del proyecto, no figuras extraídas de esas clases.',40,75,8.5,760,color=MUTED)
end()
c.save()
print(OUTPUT)

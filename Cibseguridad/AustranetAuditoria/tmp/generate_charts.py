import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("tmp/charts", exist_ok=True)
os.makedirs("output/pdf", exist_ok=True)

# Configuración estética general
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# GRÁFICO 1: Donut Chart - Semáforo General de Urgencia (495 cuentas)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
labels = ['Urgencia Crítica (Rojo)\n108 cuentas (21.8%)', 
          'Urgencia Media (Amarillo)\n235 cuentas (47.5%)', 
          'Conforme / Regular (Verde)\n152 cuentas (30.7%)']
sizes = [108, 235, 152]
colors = ['#E53E3E', '#DD6B20', '#38A169']
explode = (0.05, 0, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                                  autopct='%1.1f%%', pctdistance=0.75, startangle=140,
                                  textprops=dict(color="#1A202C", fontsize=9, weight="bold"),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.set_title("Distribución General por Nivel de Urgencia (495 Cuentas)\nEvaluación frente a ISO/IEC 27001:2022", 
             fontsize=12, weight='bold', color='#1A365D', pad=15)
plt.tight_layout()
fig1_path = "tmp/charts/chart1_donut_urgencia.png"
plt.savefig(fig1_path, dpi=300)
plt.close()

# -------------------------------------------------------------
# GRÁFICO 2: Bar Horizontal - Realidad de Colaboradores Internos (189 cuentas)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

categories = [
    'Inactivos > 60d (Habilitados)',
    'Bloqueados >= 60d (Offboarding)',
    'Especiales / Admin Inactivos',
    'Nuevos sin Login (Regla 5d)',
    'Alerta Preventiva (30-59d)',
    'Bloqueados Recientes (< 60d)',
    'Especiales / Admin Activos',
    'Activos Regulares (< 30d)'
]
counts = [53, 46, 9, 5, 3, 16, 9, 48]
bar_colors = ['#E53E3E', '#E53E3E', '#E53E3E', '#DD6B20', '#DD6B20', '#38A169', '#38A169', '#38A169']

y_pos = np.arange(len(categories))
bars = ax.barh(y_pos, counts, color=bar_colors, edgecolor='none', height=0.65, zorder=3)

# Grid
ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0', zorder=0)
ax.set_axisbelow(True)

# Invertir para leer de arriba a abajo
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=9, weight='bold', color='#2D3748')
ax.invert_yaxis()

# Anotaciones numéricas
for bar in bars:
    w = bar.get_width()
    pct = (w / 189) * 100
    ax.text(w + 1.2, bar.get_y() + bar.get_height()/2, f'{int(w)} ({pct:.1f}%)', 
            va='center', ha='left', fontsize=8.5, weight='bold', color='#4A5568')

ax.set_xlim(0, 62)
ax.set_xlabel("Número de Colaboradores Internos", fontsize=9, weight='bold', color='#4A5568')
ax.set_title("Diagnóstico de Colaboradores Internos (189 Miembros)\n57.1% en Zona Crítica de Incumplimiento SGSI", 
             fontsize=12, weight='bold', color='#1A365D', pad=15)

# Leyenda personalizada
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#E53E3E', label='[CRITICO] Acción Inmediata: 108 cuentas (57.1%)'),
    Patch(facecolor='#DD6B20', label='[MEDIO] Preventivo / Alerta: 8 cuentas (4.2%)'),
    Patch(facecolor='#38A169', label='[CONFORME] Operación Normal: 73 cuentas (38.6%)')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=8, framealpha=0.95)

plt.tight_layout()
fig2_path = "tmp/charts/chart2_internos_bar.png"
plt.savefig(fig2_path, dpi=300)
plt.close()

# -------------------------------------------------------------
# GRÁFICO 3: Comparativa Member vs Guest (Stacked Bar Chart)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4), dpi=300)

groups = ['Miembros Internos (189)', 'Invitados Externos (306)']
critico = [108, 0]      # 57.1% vs 0%
medio = [8, 227]        # 4.2% vs 74.2% (117 sin canje + 101 inactivos + 9 bloqueados)
conforme = [73, 79]     # 38.6% vs 25.8%

x = np.arange(len(groups))
width = 0.45

p1 = ax.bar(x, critico, width, label='[CRITICO] Acción Inmediata', color='#E53E3E', zorder=3)
p2 = ax.bar(x, medio, width, bottom=critico, label='[MEDIO] Preventivo / Depuración', color='#DD6B20', zorder=3)
p3 = ax.bar(x, conforme, width, bottom=np.array(critico)+np.array(medio), label='[CONFORME] Activo Regular', color='#38A169', zorder=3)

ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0', zorder=0)
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=10, weight='bold', color='#2D3748')
ax.set_ylabel("Cantidad de Cuentas", fontsize=9, weight='bold', color='#4A5568')
ax.set_title("Comparativa de Cumplimiento: Miembros Internos vs Invitados Externos", 
             fontsize=12, weight='bold', color='#1A365D', pad=15)

# Etiquetas dentro de barras
for i in range(len(groups)):
    # Critico
    if critico[i] > 15:
        ax.text(x[i], critico[i]/2, f'{critico[i]}\n({critico[i]/sum([critico[i], medio[i], conforme[i]])*100:.1f}%)', 
                ha='center', va='center', color='white', weight='bold', fontsize=9)
    # Medio
    if medio[i] > 15:
        ax.text(x[i], critico[i] + medio[i]/2, f'{medio[i]}\n({medio[i]/sum([critico[i], medio[i], conforme[i]])*100:.1f}%)', 
                ha='center', va='center', color='white', weight='bold', fontsize=9)
    # Conforme
    if conforme[i] > 15:
        ax.text(x[i], critico[i] + medio[i] + conforme[i]/2, f'{conforme[i]}\n({conforme[i]/sum([critico[i], medio[i], conforme[i]])*100:.1f}%)', 
                ha='center', va='center', color='white', weight='bold', fontsize=9)

ax.legend(loc='upper right', fontsize=8.5, framealpha=0.95)
plt.tight_layout()
fig3_path = "tmp/charts/chart3_comparativa.png"
plt.savefig(fig3_path, dpi=300)
plt.close()

print("Gráficos generados limpiamente sin warnings.")

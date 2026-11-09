"""
07. Proteómica estructural: comparar la estructura de una familia de proteínas
================================================================================
Autor: Dr. José Juan Torres Martínez
Docente de Ciencias Químicas / UASLP / México
Material académico para estudiantes
Serie AlphaFold — Script 07

Descripción: Compara las predicciones de AlphaFold/ColabFold de los cuatro
miembros de la familia ACCD (subunidad beta de la acetil-CoA carboxilasa,
EC 2.1.3.15) y muestra qué regiones de la estructura se conservan entre
especies y cuáles cambian. Lee los archivos JSON de puntajes que genera
ColabFold (uno por miembro), resume el pLDDT y el PAE de cada uno y genera
tres gráficas de comparación.

La pregunta
------------
Una familia de proteínas son proteínas con el mismo origen evolutivo y la
misma función básica en organismos distintos. Si la función se conserva, la
estructura del dominio que hace el trabajo también se conserva. Aquí se
comprueba eso con datos: se predice la misma enzima en cuatro organismos y
se comparan la confianza (pLDDT) y el error de posición relativa (PAE).

La familia: ACCD (gen accD)
----------------------------
Las cuatro entradas son revisadas (Reviewed) en UniProt, consultadas el
2026-11-09. Todas pertenecen a la familia AccD/PCCB, llevan el dominio
Pfam PF01039 (Carboxyl_trans), los InterPro IPR000438, IPR011762 e
IPR034733, el perfil PROSITE PS50980 y la regla HAMAP MF_01395. Todas
catalizan la misma reacción: transferir el grupo carboxilo desde la
biotina carboxilada al acetil-CoA para formar malonil-CoA, el primer paso
comprometido de la biosíntesis de ácidos grasos. Todas unen un ion Zn(2+)
en un dedo de zinc de tipo C4 dentro del dominio.

    Organismo                UniProt   Longitud   Dominio COA_CT_NTER   Dedo de zinc C4
    -----------------------  --------  ---------  --------------------  -----------------
    Chlorella vulgaris       P56293    411 aa     32..302               36..58 (Zn: 36, 39, 55, 58)
    Arabidopsis thaliana     P56765    488 aa     227..488              231..250 (Zn: 231, 234, 247, 250)
    Escherichia coli (K12)   P0A9Q5    304 aa     23..292               27..49
    Bacillus subtilis (168)  C0SP93    290 aa     28..290               32..54 (Zn: 32, 35, 51, 54)

Lectura de la tabla: en las dos bacterias el dominio catalítico ocupa casi
toda la cadena (E. coli 23..292 de 304; B. subtilis 28..290 de 290). En
cambio, Arabidopsis tiene una extensión larga de 226 aminoácidos antes del
dominio (residuos 1..226) y Chlorella tiene una extensión de 109
aminoácidos después del dominio (residuos 303..411). La gráfica 2 muestra
si esas extensiones se predicen con la misma confianza que el dominio.

Dos datos de UniProt que se usan en la interpretación: la ACCD de E. coli
tiene una región desordenada anotada en el extremo C-terminal (residuos
284..304) y existe una estructura experimental de esta proteína por
cristalografía de rayos X (PDB 2F9Y, resolución 3.20 Å), con la que se
puede comparar la predicción (paso 5). La ACCD de Arabidopsis tiene una
edición del RNA en la posición 265, dentro del dominio.

Paso 1. Obtener las secuencias
--------------------------------
Descarga cada secuencia en formato FASTA desde UniProt (abre el enlace en
el navegador y copia la secuencia, sin la línea que empieza con `>`):

    Chlorella vulgaris:      https://rest.uniprot.org/uniprotkb/P56293.fasta
    Arabidopsis thaliana:    https://rest.uniprot.org/uniprotkb/P56765.fasta
    Escherichia coli:        https://rest.uniprot.org/uniprotkb/P0A9Q5.fasta
    Bacillus subtilis:       https://rest.uniprot.org/uniprotkb/C0SP93.fasta

Paso 2. Predecir las cuatro en ColabFold
-----------------------------------------
Abre ColabFold:

    https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

Haz una corrida por miembro, con las MISMAS opciones en las cuatro para
que la comparación sea válida (las mismas del script 01: num_relax 0,
template_mode none, msa_mode mmseqs2_uniref_env). Usa estos nombres de
trabajo (jobname):

    ACCD_Chlorella, ACCD_Arabidopsis, ACCD_Ecoli, ACCD_Bacillus

Cada predicción tarda entre 5 y 20 minutos, según la longitud.

Paso 3. Descargar y renombrar los JSON de puntajes
---------------------------------------------------
De cada corrida descarga el archivo `.json` de puntajes del modelo rank_1
(el nombre es algo como
`ACCD_Chlorella_scores_rank_001_alphafold2_ptm_model_1_seed_000.json`) y
renómbralo así, en la misma carpeta que este script:

    ACCD_Chlorella.json
    ACCD_Arabidopsis.json
    ACCD_Ecoli.json
    ACCD_Bacillus.json

Descarga también los cuatro archivos `.pdb` (rank_1) para el paso 5.

Paso 4. Correr este script
---------------------------
Corre el script en Google Colab o en tu computadora con los cuatro JSON en
la misma carpeta. El script imprime una tabla resumen (longitud, pLDDT
promedio, porcentaje de residuos con pLDDT mayor que 70 y menor que 50, y
PAE promedio) y guarda tres gráficas en PNG:

    07_plddt_promedio_familia.png
    07_plddt_por_residuo_normalizado.png
    07_pae_promedio_familia.png

Si un JSON no trae la matriz PAE, la gráfica 3 usa solo los miembros que
sí la traen y el script lo indica en pantalla.

Paso 5 (opcional). Superponer las cuatro estructuras en un visor
-------------------------------------------------------------------
Abre los cuatro PDB en PyMOL o ChimeraX y superpónlos. El dominio
carboxiltransferasa se superpone en los cuatro miembros; las extensiones
N- y C-terminales de Arabidopsis y Chlorella quedan fuera del núcleo
conservado. Para E. coli, abre además la estructura experimental PDB 2F9Y
y superpónla con la predicción: es la comparación directa entre AlphaFold
y la cristalografía de rayos X para esta familia.

Uso: corre este script en Google Colab (o en tu computadora) con los
cuatro archivos JSON en la misma carpeta. Cambia los nombres de archivo
en la lista MIEMBROS si usaste otros nombres.

Requisitos: numpy, matplotlib.
En Colab ya están instalados. En tu computadora:
    pip install numpy matplotlib
================================================================================
"""

import json
import sys

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. La familia: datos verificados en UniProt (entradas revisadas, 2026-11-09)
# ---------------------------------------------------------------------------
# Cada miembro trae su acceso de UniProt, su longitud y los rangos del
# dominio COA_CT_NTER y del dedo de zinc C4, copiados de la tabla de
# características (FT) de su entrada. El script comprueba que la longitud
# del JSON coincida con la longitud de UniProt y avisa si no coincide.
MIEMBROS = [
    {
        "nombre": "Chlorella vulgaris",
        "corto": "C. vulgaris",
        "accession": "P56293",
        "archivo_json": "ACCD_Chlorella.json",
        "longitud_uniprot": 411,
        "dominio": (32, 302),
        "dedo_zinc": (36, 58),
    },
    {
        "nombre": "Arabidopsis thaliana",
        "corto": "A. thaliana",
        "accession": "P56765",
        "archivo_json": "ACCD_Arabidopsis.json",
        "longitud_uniprot": 488,
        "dominio": (227, 488),
        "dedo_zinc": (231, 250),
    },
    {
        "nombre": "Escherichia coli (K12)",
        "corto": "E. coli",
        "accession": "P0A9Q5",
        "archivo_json": "ACCD_Ecoli.json",
        "longitud_uniprot": 304,
        "dominio": (23, 292),
        "dedo_zinc": (27, 49),
    },
    {
        "nombre": "Bacillus subtilis (168)",
        "corto": "B. subtilis",
        "accession": "C0SP93",
        "archivo_json": "ACCD_Bacillus.json",
        "longitud_uniprot": 290,
        "dominio": (28, 290),
        "dedo_zinc": (32, 54),
    },
]

# Umbrales de pLDDT (los mismos del script 02).
# pLDDT > 90: muy confiable. 70-90: confiable. 50-70: baja. < 50: muy baja.


# ---------------------------------------------------------------------------
# 2. Leer los archivos JSON de ColabFold
# ---------------------------------------------------------------------------
def leer_miembro(miembro):
    """Lee el JSON de un miembro y devuelve su pLDDT y su matriz PAE."""
    with open(miembro["archivo_json"], "r") as f:
        datos = json.load(f)

    plddt = np.array(datos["plddt"], dtype=float)
    pae = np.array(datos["pae"], dtype=float) if "pae" in datos else None
    return plddt, pae


resultados = []

for miembro in MIEMBROS:
    try:
        plddt, pae = leer_miembro(miembro)
    except FileNotFoundError:
        print(f"AVISO: no se encontró {miembro['archivo_json']} "
              f"({miembro['nombre']}); se omite este miembro.")
        print("  Descarga el JSON de ColabFold y renómbralo como indica el paso 3.")
        continue

    # Comprobación: la longitud del JSON debe coincidir con UniProt.
    if len(plddt) != miembro["longitud_uniprot"]:
        print(f"AVISO: {miembro['nombre']} tiene {len(plddt)} residuos en el "
              f"JSON, pero UniProt anota {miembro['longitud_uniprot']} "
              f"para {miembro['accession']}. Revisa que la secuencia usada "
              f"en ColabFold sea la de esa entrada.")

    dom_ini, dom_fin = miembro["dominio"]
    n_dominio = dom_fin - dom_ini + 1
    resultados.append({
        "miembro": miembro,
        "plddt": plddt,
        "pae": pae,
        "n": len(plddt),
        "plddt_promedio": float(plddt.mean()),
        "plddt_desv": float(plddt.std()),
        "plddt_min": float(plddt.min()),
        "plddt_max": float(plddt.max()),
        "pct_mayor_70": 100.0 * float(np.sum(plddt > 70)) / len(plddt),
        "pct_menor_50": 100.0 * float(np.sum(plddt < 50)) / len(plddt),
        "pae_promedio": float(pae.mean()) if pae is not None else None,
        "plddt_dominio": float(plddt[dom_ini - 1:dom_fin].mean()),
        "cobertura_dominio": 100.0 * n_dominio / len(plddt),
    })

if len(resultados) < 2:
    print("\nSe necesitan al menos dos miembros con su JSON para comparar "
          "la familia. Revisa el paso 3 y vuelve a correr el script.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# 3. Tabla resumen de la familia
# ---------------------------------------------------------------------------
print("Familia ACCD (subunidad beta de la acetil-CoA carboxilasa, EC 2.1.3.15)")
print("=" * 78)
print(f"{'Miembro':<22} {'Long.':>6} {'pLDDT prom.':>11} {'%>70':>6} "
      f"{'%<50':>6} {'PAE prom. (Å)':>13}")
for r in resultados:
    pae_txt = f"{r['pae_promedio']:.1f}" if r["pae_promedio"] is not None else "sin dato"
    print(f"{r['miembro']['corto']:<22} {r['n']:>6} "
          f"{r['plddt_promedio']:>11.1f} {r['pct_mayor_70']:>6.1f} "
          f"{r['pct_menor_50']:>6.1f} {pae_txt:>13}")

print("\nDominio COA_CT_NTER (de UniProt) y pLDDT promedio dentro del dominio:")
for r in resultados:
    dom_ini, dom_fin = r["miembro"]["dominio"]
    print(f"  {r['miembro']['corto']:<14} dominio {dom_ini}..{dom_fin} "
          f"({r['cobertura_dominio']:.0f}% de la cadena), "
          f"pLDDT en el dominio: {r['plddt_dominio']:.1f}")

nombres = [r["miembro"]["corto"] for r in resultados]
promedios = [r["plddt_promedio"] for r in resultados]
desviaciones = [r["plddt_desv"] for r in resultados]
pct_mayor_70 = [r["pct_mayor_70"] for r in resultados]

# ---------------------------------------------------------------------------
# 4. Gráfica 1: pLDDT promedio por miembro de la familia
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(resultados))
ax.bar(x, promedios, yerr=desviaciones, capsize=6, color="#2166ac")
ax.axhline(90, color="#2166ac", linestyle="--", linewidth=1)
ax.axhline(70, color="#5ab4ac", linestyle="--", linewidth=1)
ax.axhline(50, color="#d73027", linestyle="--", linewidth=1)
for xi, prom, pct in zip(x, promedios, pct_mayor_70):
    ax.text(xi, prom + 4, f"{prom:.1f}\n({pct:.0f}% > 70)",
            ha="center", va="bottom", fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(nombres)
ax.set_ylabel("pLDDT promedio (adimensional, 0-100)")
ax.set_title("Confianza promedio de la predicción (pLDDT) por miembro\n"
             "Familia ACCD, acetil-CoA carboxilasa subunidad beta")
ax.set_ylim(0, 110)
ax.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("07_plddt_promedio_familia.png", dpi=300)
plt.show()

# ---------------------------------------------------------------------------
# 5. Gráfica 2: pLDDT por residuo con la posición normalizada (0-100%)
# ---------------------------------------------------------------------------
# Las cuatro proteínas tienen longitudes distintas (290 a 488
# aminoácidos), así que la posición se expresa como porcentaje de la
# cadena: 0% es el primer residuo y 100% es el último. La banda sombreada
# marca el dominio COA_CT_NTER de cada miembro (rangos de UniProt).
fig, axes = plt.subplots(len(resultados), 1, figsize=(12, 3 * len(resultados)),
                         sharex=True)
if len(resultados) == 1:
    axes = [axes]
for ax, r in zip(axes, resultados):
    plddt = r["plddt"]
    pos_pct = np.linspace(0, 100, len(plddt))
    dom_ini, dom_fin = r["miembro"]["dominio"]
    n = len(plddt)
    ax.axvspan(100 * dom_ini / n, 100 * dom_fin / n,
               color="#2166ac", alpha=0.12)
    ax.axhspan(90, 100, color="#2166ac", alpha=0.10)
    ax.axhspan(70, 90, color="#5ab4ac", alpha=0.10)
    ax.axhspan(50, 70, color="#fdae61", alpha=0.10)
    ax.axhspan(0, 50, color="#d73027", alpha=0.10)
    ax.plot(pos_pct, plddt, color="#1a1a1a", linewidth=0.8)
    ax.set_ylabel("pLDDT")
    ax.set_ylim(0, 100)
    ax.set_title(f"{r['miembro']['nombre']} ({r['miembro']['accession']}, "
                 f"{n} aa) — banda: dominio COA_CT_NTER "
                 f"{dom_ini}..{dom_fin}")
    ax.grid(True, alpha=0.3)
axes[-1].set_xlabel("Posición en la cadena (% de la longitud total)")
fig.suptitle("pLDDT por residuo, posición normalizada — familia ACCD",
             fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("07_plddt_por_residuo_normalizado.png", dpi=300)
plt.show()

# ---------------------------------------------------------------------------
# 6. Gráfica 3: PAE promedio por miembro (solo si el JSON trae la matriz PAE)
# ---------------------------------------------------------------------------
con_pae = [r for r in resultados if r["pae_promedio"] is not None]
if con_pae:
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(con_pae))
    ax.bar(x, [r["pae_promedio"] for r in con_pae], color="#5ab4ac")
    for xi, r in zip(x, con_pae):
        ax.text(xi, r["pae_promedio"] + 0.5, f"{r['pae_promedio']:.1f} Å",
                ha="center", va="bottom", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels([r["miembro"]["corto"] for r in con_pae])
    ax.set_ylabel("PAE promedio (Å)")
    ax.set_title("Error de posición relativa promedio (PAE) por miembro\n"
                 "Familia ACCD — valores bajos indican posición relativa "
                 "más confiable")
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("07_pae_promedio_familia.png", dpi=300)
    plt.show()
else:
    print("\nNingún JSON trae la matriz PAE: no se generó la gráfica 3.")
    print("Si ColabFold guardó la PAE en otro archivo, revisa el script 02, "
          "que explica dónde aparece la matriz PAE.")

# ---------------------------------------------------------------------------
# Interpretación
# ---------------------------------------------------------------------------
# Gráfica 1: pLDDT promedio por miembro
# - Eje X: cada miembro de la familia (C. vulgaris, A. thaliana, E. coli,
#   B. subtilis). Eje Y: pLDDT promedio, de 0 a 100, adimensional (no tiene
#   unidades: es un puntaje de confianza). La barra de error es la
#   desviación estándar del pLDDT entre residuos: una barra de error
#   grande indica que la confianza varía mucho a lo largo de la cadena
#   (por ejemplo, dominio bien predicho y extensiones con pLDDT bajo).
# - El número sobre cada barra es el porcentaje de residuos con pLDDT
#   mayor que 70 (región confiable). Las líneas punteadas marcan 90, 70 y
#   50, los umbrales del script 02.
# - Qué significa: si los cuatro promedios son parecidos, las cuatro
#   predicciones son comparables en confianza global. Un promedio más bajo
#   en un miembro no indica una proteína peor, sino una predicción menos
#   segura, muchas veces por las extensiones fuera del dominio.
#
# Gráfica 2: pLDDT por residuo, posición normalizada
# - Eje X: posición en la cadena, en porcentaje de la longitud total
#   (0% primer residuo, 100% último residuo). Se normaliza porque las
#   cuatro proteínas tienen longitudes distintas (290 a 488 aminoácidos)
#   y así se pueden superponer en la misma escala.
# - Eje Y: pLDDT, de 0 a 100, adimensional. La banda azul marca el
#   dominio COA_CT_NTER según UniProt.
# - Lo que se aprecia: dentro de la banda (el dominio catalítico) el
#   pLDDT se mantiene alto en los cuatro miembros, porque esa es la parte
#   que se conserva en la familia. Fuera de la banda (las extensiones
#   N-terminal de Arabidopsis y C-terminal de Chlorella) el pLDDT suele
#   ser más bajo y más variable: son regiones propias de cada organismo,
#   sin contraparte conservada en los demás miembros.
# - Qué significa: la estructura del dominio se conserva porque la
#   función se conserva (la misma reacción EC 2.1.3.15 en los cuatro).
#   Las regiones fuera del dominio cambian entre organismos y su
#   predicción es menos segura; su forma se interpreta con cautela.
#
# Gráfica 3: PAE promedio por miembro
# - Eje X: cada miembro de la familia. Eje Y: PAE promedio, en
#   Ångströms (Å). Un Å es 10^-10 metros, la escala de los átomos.
# - Lo que se aprecia: un PAE promedio bajo indica que las posiciones
#   relativas entre residuos están bien determinadas en ese miembro; un
#   PAE promedio alto indica más incertidumbre global.
# - Qué significa: el PAE promedio resume en un número la rigidez de la
#   predicción. Se lee junto con la gráfica 2: un miembro con extensiones
#   largas de pLDDT bajo suele tener también un PAE promedio mayor.
#
# ---------------------------------------------------------------------------
# Qué aprendimos
# ---------------------------------------------------------------------------
# - Una familia de proteínas se reconoce por compartir función, dominio y
#   motivo: los cuatro miembros de ACCD comparten la reacción EC 2.1.3.15,
#   el dominio COA_CT_NTER (Pfam PF01039) y el dedo de zinc C4 que une
#   Zn(2+), aunque sus longitudes van de 290 a 488 aminoácidos.
# - El pLDDT (0-100, adimensional) comparado entre miembros muestra qué
#   regiones se conservan: el dominio catalítico tiene pLDDT alto en los
#   cuatro, y las extensiones fuera del dominio tienen pLDDT más bajo.
# - El PAE (en Ångströms) comparado entre miembros muestra qué predicción
#   tiene mejor definidas las posiciones relativas entre sus residuos.
# - Normalizar la posición como porcentaje de la cadena permite comparar
#   proteínas de longitudes distintas en la misma escala.
# - La estructura conservada explica la función conservada: el mismo
#   dominio, la misma reacción. Las diferencias de estructura fuera del
#   dominio son diferencias propias de cada organismo.
# - AlphaFold predice estructura, no función: que dos miembros se vean
#   parecidos no prueba por sí solo que trabajen igual en la célula. Para
#   eso hacen falta experimentos.

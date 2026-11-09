"""
05. Preparar la estructura para docking molecular
================================================================
Autor: Dr. José Juan Torres Martínez
Docente de Ciencias Químicas, UASLP

Descripción: Toma el archivo PDB que genera ColabFold (rank_1) y lo
deja listo para docking: elimina aguas y heteroátomos, conserva solo
la cadena de la proteína, y recorta las regiones de pLDDT bajo (menos
de 50) que no son confiables. Guarda el PDB limpio para usarlo en
AutoDock Vina, SwissDock u otra herramienta de docking.

Uso: corre este script en Google Colab o en tu computadora con el
archivo .pdb de ColabFold en la misma carpeta. Cambia las variables
ARCHIVO_PDB y UMBRAL_PLDDT.

Requisitos: numpy. (No requiere Biopython: el PDB se procesa como texto.)
================================================================
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Parámetros
# ---------------------------------------------------------------------------
# Archivo PDB descargado de ColabFold (el modelo rank_1)
ARCHIVO_PDB = "ACCD_Chlorella_rank_001_alphafold2_ptm_model_1_seed_000.pdb"
# Archivo de salida
ARCHIVO_SALIDA = "ACCD_Chlorella_limpio.pdb"
# Residuos con pLDDT menor que este umbral se eliminan (no confiables)
UMBRAL_PLDDT = 50.0

# ---------------------------------------------------------------------------
# 2. Leer el PDB y el pLDDT por residuo
# ---------------------------------------------------------------------------
# En los PDB de AlphaFold, el pLDDT de cada residuo está en la columna
# del factor B (columnas 61-66 de cada línea ATOM).
residuos_buenos = set()
lineas_atom = []

with open(ARCHIVO_PDB, "r") as f:
    for linea in f:
        if linea.startswith("ATOM"):
            # Número de residuo (columnas 23-26) y pLDDT (columnas 61-66)
            num_res = int(linea[22:26])
            plddt = float(linea[60:66])
            lineas_atom.append((num_res, plddt, linea))
            if plddt >= UMBRAL_PLDDT:
                residuos_buenos.add(num_res)

print(f"Residuos totales: {len(set(n for n, _, _ in lineas_atom))}")
print(f"Residuos con pLDDT >= {UMBRAL_PLDDT}: {len(residuos_buenos)}")

# ---------------------------------------------------------------------------
# 3. Escribir el PDB limpio
# ---------------------------------------------------------------------------
# Se conservan solo los átomos de residuos confiables. Se eliminan aguas
# (HETATM) y heteroátomos. Se añade TER al final.
with open(ARCHIVO_SALIDA, "w") as out:
    for num_res, plddt, linea in lineas_atom:
        if num_res in residuos_buenos:
            out.write(linea)
    out.write("TER\n")
    out.write("END\n")

print(f"Archivo limpio guardado en: {ARCHIVO_SALIDA}")
print("Listo para docking (AutoDock Vina, SwissDock, etc.).")

# ---------------------------------------------------------------------------
# Notas
# ---------------------------------------------------------------------------
# - Si tu proteína tiene un ligando o cofactor conocido, añádelo después
#   con la herramienta de docking; AlphaFold no predice ligandos.
# - Si el sitio activo quedó recortado por pLDDT bajo, baja el umbral a 40
#   o revisa el script 02: puede ser una región flexible real.
# - Para docking con AutoDock Vina, convierte el PDB a PDBQT con
#   OpenBabel o MGLTools antes de correr el docking.

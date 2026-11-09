# 04. Predecir un complejo proteína-proteína

**Autor:** Dr. José Juan Torres Martínez — Docente de Ciencias Químicas, UASLP

## La pregunta

¿Dos proteínas interactúan? ColabFold (AlphaFold-Multimer) puede predecir
la estructura de un complejo a partir de las secuencias de sus componentes.

## El ejemplo

El complejo acetil-CoA carboxilasa tiene varias subunidades. Aquí
predeciremos dos de sus componentes juntos para ver si ColabFold los
coloca en contacto.

- **Componente A:** ACCD de *Chlorella vulgaris* (UniProt P56293).
- **Componente B:** biotina carboxilasa (BC) de *Chlorella vulgaris*.
  Búscala en UniProt: https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id:3077+AND+biotin+carboxylase&format=tsv&fields=accession,id,protein_name,length&size=5
  Toma el acceso de la entrada que corresponda y descarga su FASTA.

## Paso 1. Obtener ambas secuencias

Descarga el FASTA de cada una (como en el script 01) y copia las
secuencias de aminoácidos.

## Paso 2. Predecir el complejo en ColabFold

Abre ColabFold:

https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

En la celda `query_sequence`, pega las dos secuencias separadas por dos
puntos (`:`), así:

```
<secuencia_A>:<secuencia_B>
```

En la celda de opciones, asegúrate de que el modelo sea multímero
(ColabFold lo detecta automáticamente cuando hay `:` en la secuencia).

Ejecuta (Runtime > Run all).

## Paso 3. Interpretar el resultado

ColabFold genera, además del pLDDT, el puntaje **pTM** (predicted TM-score)
y el **ipTM** (interface pTM), que mide la confianza de la interfaz:

- **ipTM > 0.8:** interfaz muy confiable.
- **ipTM 0.6–0.8:** interfaz probablemente correcta.
- **ipTM < 0.6:** interfaz incierta.

Revisa también el mapa PAE entre cadenas: si hay bloques de PAE bajo
entre las dos cadenas, sus posiciones relativas están bien definidas.

## Interpretación

- Un ipTM alto sugiere que las proteínas interactúan y que el modelo del
  complejo es confiable.
- Un ipTM bajo NO prueba que no interactúen; solo dice que AlphaFold no
  está seguro. Hacen falta experimentos (co-inmunoprecipitación, doble
  híbrido, etc.) para confirmar.
- AlphaFold-Multimer funciona mejor cuando las proteínas interactúan de
  forma estable y tienen homólogos que co-evolucionan.

## Qué aprendimos

- Un complejo se predice con las dos secuencias separadas por `:` en
  ColabFold, que usa el modelo multímero.
- El ipTM mide la confianza de la interfaz: por encima de 0.8 es muy
  confiable, entre 0.6 y 0.8 es probablemente correcta y por debajo de
  0.6 es incierta.
- Un ipTM bajo no prueba que las proteínas no interactúen; solo dice
  que AlphaFold no está seguro y que hacen falta experimentos.

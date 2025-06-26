# tp_fund_informatica
Trabajo Práctico Final de la materia Fundamentos de Informática 

## Contexto del problema
Se desea desarrollar un sistema en Python que gestione las calificaciones de alumnos a partir de un archivo CSV y permita consultar, procesar y ordenar los datos.
Cada línea del archivo CSV tendrá el siguiente formato:
```
Nombre,Materia,Nota1,Nota2,Nota3,NotaFinal
```
- NotaFinal es el promedio de las tres notas.
- El sistema debe calcular esta nota automáticamente al cargar datos manuales.

---

## Requisitos del sistema
- Cargar datos desde un archivo CSV, guardándolos en una lista de listas o matriz.
- Permitir agregar alumnos manualmente por teclado, con cálculo automático de la nota final.
- Generar cinco informes, por ejemplo:
  - Listado completo de alumnos con sus notas y promedio.
  - Promedio general por materia.
  - Alumnos con nota final mayor a un valor dado.
  - Alumnos con al menos una nota menor a 4.
  - Cantidad de aprobados y desaprobados por materia.
- Implementar al menos dos métodos de ordenamiento sobre los datos:
  - Por nombre del alumno.
  - Por nota final (de mayor a menor).

---

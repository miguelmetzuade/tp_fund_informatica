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

## Organización del código
Usar funciones para cada operación (carga de CSV, carga manual, informes, ordenamiento).

Validar los datos ingresados (por ejemplo, que las notas estén entre 0 y 10).

Comentar el código explicando cada bloque funcional.

---

## Calificación:
Rúbrica de Calificación

Puntaje Total: 10 puntos

| Criterio                                    | Puntaje |
| ------------------------------------------- | ------- |
| Carga desde archivo CSV                     | 1.0     |
| Carga manual de datos                       | 1.0     |
| Implementación de 5 informes                | 2.0     |
| Aplicación de dos métodos de ordenamiento   | 2.0     |
| Organización del código en funciones        | 1.0     |
| Presentación clara y documentación          | 1.0     |
| Participación individual en la presentación | 1.0     |


### Bonificaciones
- Bonus 1 (0.5 pts): uso de archivos JSON para guardar configuraciones o resultados.
- Bonus 2 (0.5 pts): interfaz gráfica simple (puede ser con tkinter, PySimpleGUI, etc.).

---

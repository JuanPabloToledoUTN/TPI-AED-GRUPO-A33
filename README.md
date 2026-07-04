# Sistema de Gestión de Estacionamiento

## Trabajo Práctico Integrador

**Materia:** Algoritmos y Estructuras de Datos  
**Carrera:** Ingeniería en Sistemas de Información - UTN FRRe  
**Lenguaje:** Python  
**Grupo:** A33

---

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de estacionamiento utilizando Python.

El sistema permite administrar el ingreso y egreso de vehículos, calcular el importe a pagar según el tiempo de permanencia y mostrar estadísticas generales del funcionamiento del estacionamiento.

El desarrollo se realizó aplicando los conceptos vistos en la materia, como:

- Variables
- Constantes
- Funciones
- Estructuras de decisión
- Ciclos
- Listas
- Diccionarios
- Validación de datos
- Modularización del programa

---

## Funcionalidades

- Registrar ingreso de vehículos.
- Registrar egreso de vehículos.
- Calcular el importe según el tiempo de permanencia.
- Mostrar vehículos actualmente estacionados.
- Mostrar estadísticas generales.
- Controlar la capacidad máxima del estacionamiento.
- Validar el ingreso de datos incorrectos.

---

## Datos del sistema

- Capacidad máxima: **50 vehículos**
- Tarifa: **$1000 por hora**

---

## Requisitos

- Python 3.10 o superior.

---

## Ejecución

1. Descargar el proyecto.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python TPI_A33_ALGORITMOS_ESTACIONAMIENTO.py
```

---

## Estructura del programa

El sistema se encuentra dividido en módulos funcionales:

- Menú principal.
- Funciones auxiliares.
- Búsqueda de vehículos.
- Registro de ingreso.
- Registro de egreso.
- Cálculo de importes.
- Estadísticas.
- Programa principal.

---

## Ejemplo de uso

### Caso válido

1. Registrar ingreso.
2. Ingresar patente.
3. Ingresar hora.
4. Registrar egreso.
5. Mostrar ticket con el importe correspondiente.

### Caso con validaciones

El sistema detecta errores como:

- Patente vacía.
- Hora fuera del rango 0–23.
- Patente duplicada.
- Vehículo inexistente.
- Hora de salida menor que la hora de ingreso.
- Estacionamiento completo.

---

## Integrantes

- Toledo, Juan Pablo
- Alfonso Abatte, Valentina Milagros
- Delbon, Valentina
- Martin, Julieta

---

## Repositorio

Agregar aquí el enlace al repositorio de GitHub o GitLab.

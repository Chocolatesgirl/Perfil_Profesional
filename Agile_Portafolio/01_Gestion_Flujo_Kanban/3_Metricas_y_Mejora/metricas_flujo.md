# 📊 Métricas de Flujo en Kanban

## 🎯 Objetivo

Definir, analizar e interpretar métricas de flujo para optimizar el desarrollo de una:

👉 **App de aprendizaje de inglés para niños de 3 a 8 años**

El enfoque es:

* Medir el rendimiento del equipo
* Detectar cuellos de botella
* Tomar decisiones basadas en datos
* Mejorar la entrega continua de valor

---

## 🧱 Flujo de trabajo analizado

```text id="x9a3f6"
Backlog → Ready → Development → Code Review → Testing → QA → Release → Done
```

---

## 📊 Métricas clave

### 🔹 1. Lead Time

Tiempo total desde que una historia entra al backlog hasta que se entrega en producción.

👉 Ejemplo:

* Feature: Juego de vocabulario
* Lead Time: **10 días**

📌 Interpretación:

* Mide la velocidad total del sistema
* Impacta directamente en time-to-market

---

### 🔹 2. Cycle Time

Tiempo desde que el equipo comienza a trabajar hasta que la funcionalidad se entrega.

👉 Ejemplo:

* Desde Development hasta Release
* Cycle Time: **4 días**

📌 Interpretación:

* Mide eficiencia operativa
* Indicador clave de flujo interno

---

### 🔹 3. Throughput

Cantidad de historias completadas en un período.

👉 Ejemplo:

* 8 historias completadas por semana

📌 Interpretación:

* Mide capacidad de entrega
* Permite estimar predictibilidad

---

### 🔹 4. Work In Progress (WIP)

Cantidad de tareas en curso simultáneamente.

👉 Ejemplo:

* 7 tareas activas → riesgo de saturación

📌 Interpretación:

* Alto WIP → mayor multitarea
* Impacta negativamente en Cycle Time

---

## 🔍 Análisis aplicado (simulación real)

### 🚨 Problema detectado

Durante la simulación:

* Testing alcanza su límite WIP (2/2)
* Code Review también saturado
* Development continúa iniciando trabajo

👉 Resultado:

* Aumento del Cycle Time
* Disminución del Throughput
* Acumulación de tareas

---

## 🧠 Diagnóstico

| Métrica    | Comportamiento | Interpretación               |
| ---------- | -------------- | ---------------------------- |
| Cycle Time | Alto           | Cuello de botella en Testing |
| WIP        | Alto           | Sobrecarga del sistema       |
| Throughput | Bajo           | Flujo ineficiente            |

---

## 🛠️ Acciones tomadas

* Reducción del WIP en Development
* Apoyo del equipo en Testing
* Priorización de tareas bloqueadas
* Ajuste de políticas de flujo

---

## 📈 Resultados después de ajustes

| Métrica    | Antes    | Después      |
| ---------- | -------- | ------------ |
| Cycle Time | Alto     | ↓ Reducido   |
| Throughput | Bajo     | ↑ Estable    |
| WIP        | Saturado | ↓ Controlado |

---

## 📊 Métricas de producto (nivel senior)

Además del flujo técnico, se analizaron métricas de impacto:

* Tiempo de uso por sesión
* Interacciones por actividad
* Progreso de aprendizaje
* Retención de usuarios

👉 Esto permite alinear desarrollo con valor real de negocio.

---

## 🔄 Mejora continua

* Ajuste dinámico de WIP
* Reducción del tamaño de historias
* Automatización de pruebas
* Optimización del flujo end-to-end

---

## 💼 Enfoque profesional

Las métricas no son solo indicadores:

👉 Son herramientas para:

* Tomar decisiones estratégicas
* Optimizar el sistema de trabajo
* Mejorar la eficiencia del equipo
* Aumentar la calidad del producto

---

## 🔥 Insight clave

> No se trata de trabajar más rápido…
> sino de hacer que el trabajo fluya mejor.

---

## 🎯 Conclusión

El uso de métricas de flujo permite transformar un equipo:

👉 reactivo → en un sistema predecible, eficiente y orientado a resultados

Asegurando una entrega continua de valor al usuario final.


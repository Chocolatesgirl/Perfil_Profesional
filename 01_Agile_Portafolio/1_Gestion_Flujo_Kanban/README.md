## 🚀 Gestión de Flujo con Kanban en Entornos Reales

Este módulo demuestra cómo implementar Kanban como sistema de gestión de flujo en equipos de desarrollo de software, enfocado en la optimización de entrega continua, reducción de cuellos de botella y toma de decisiones basada en métricas.

Se basa en prácticas aplicadas en contextos reales de transformación ágil.

El enfoque está orientado a:

* Visualizar el trabajo end-to-end
* Optimizar el flujo de entrega
* Reducir tiempos de desarrollo
* Tomar decisiones basadas en métricas

---

## 📈 Impacto esperado

La implementación de Kanban como sistema de gestión de flujo permite generar impacto directo en el desempeño del equipo y en los resultados del producto:

- Reducción del Lead Time
- Disminución del Cycle Time
- Mejora en la predictibilidad de entrega
- Identificación temprana de cuellos de botella
- Incremento del throughput del equipo
- Optimización del uso de capacidad

👉 Este enfoque permite evolucionar desde la gestión de tareas hacia la optimización del sistema de trabajo.

---

## 🧩 Caso aplicado

Se desarrolla un caso práctico basado en una:

👉 **App de aprendizaje de inglés para niños de 3 a 8 años**

Objetivos del producto:

* Mejorar la experiencia de aprendizaje
* Incrementar el engagement mediante interacciones
* Aumentar la retención de usuarios

---

## 🧱 Flujo de Trabajo

## 🔄 Flujo de trabajo

El flujo se define con políticas explícitas en cada etapa:

| Etapa | Descripción | Política de entrada | Política de salida |
|------|------------|--------------------|-------------------|
| Ready | Trabajo refinado | Historia definida + criterios de aceptación | Pull a desarrollo |
| Development | Construcción | Capacidad disponible | Código completo |
| Code Review | Validación técnica | PR creado | Aprobación |
| Testing | Validación funcional | Build estable | Tests OK |
| QA | Validación final | Feature completa | Aprobación QA |
| Release | Despliegue | QA aprobado | Deploy |

---

## ⚙️ Componentes del sistema Kanban

Este módulo se compone de cuatro dimensiones principales:

---

### 🧩 1. Diseño del flujo

📄 `diseno_tablero_kanban.md`

* Definición de columnas del tablero
* Estructura del flujo de trabajo
* Ejemplos de historias y tareas reales
* Adaptación a herramientas como Jira / Azure DevOps

---

### 🔄 2. Operación del flujo

📄 `simulacion_flujo_trabajo_jira.md`
📄 `politicas_wip.md`

* Simulación de un tablero en operación real
* Gestión de tareas en distintas etapas
* Aplicación de límites WIP
* Identificación y resolución de bloqueos

👉 Se aplica el principio:
**“Stop starting, start finishing”**

---

### 📊 3. Métricas y mejora

- `metricas_flujo.md`
- `cumulative_flow_explicado.md`

* Medición de Lead Time, Cycle Time y Throughput
* Análisis del flujo mediante métricas
* Identificación de cuellos de botella
* Uso de CFD (Cumulative Flow Diagram)

---

## 📊 Cumulative Flow Diagram (CFD)

El Cumulative Flow Diagram permite visualizar el comportamiento del flujo de trabajo a lo largo del tiempo, mostrando la distribución de tareas en cada etapa del proceso.

<p align="center">
  <img src="03_Metricas_y_Mejora/cumulative_flow_diagram.png" width="700">
</p>

---

---

## ⏱️ Análisis de Lead Time

El Lead Time mide el tiempo total desde que una tarea es solicitada hasta que es entregada.

### 🔍 Distribución del Lead Time

<p align="center">
  <img src="03_Metricas_y_Mejora/lead_time_distribution.png" width="600">
</p>

---

### 📊 Interpretación

- Alta dispersión → flujo inestable  
- Valores extremos → cuellos de botella o bloqueos  
- Distribución concentrada → sistema predecible  

---

### 🚨 Hallazgos en el caso

- Variabilidad alta en tiempos de entrega  
- Tareas bloqueadas en Testing incrementan el Lead Time  
- Falta de control de WIP genera acumulación  

---

### 🛠️ Acciones tomadas

- Implementación de límites WIP  
- Priorización de tareas en progreso  
- Reducción de multitasking  

---

### 📈 Resultado

- Disminución de la variabilidad  
- Mayor predictibilidad  
- Reducción del Lead Time promedio

---

## 📉 Mejora del flujo (Before vs After)

Se comparó el comportamiento del sistema antes y después de implementar prácticas Kanban.

<p align="center">
  <img src="03_Metricas_y_Mejora/flujo_before_after.png" width="700">
</p>

---

### 🔍 Comparación

| Métrica | Antes | Después |
|--------|------|--------|
| Lead Time | Alto | Reducido |
| Cycle Time | Variable | Estable |
| WIP | Descontrolado | Limitado |
| Flujo | Inestable | Continuo |

---

### 🎯 Impacto

- Flujo más estable  
- Reducción de tiempos de entrega  
- Mayor capacidad de respuesta  
- Mejora en la eficiencia del equipo  

👉 Se pasa de un sistema reactivo a uno gestionado por flujo.

### 🔍 ¿Qué información entrega?

- Evolución del trabajo en curso (WIP)
- Velocidad de entrega del equipo
- Estabilidad del flujo
- Identificación de cuellos de botella

---

### ⚠️ Interpretación del gráfico

En el análisis del CFD se pueden identificar patrones clave:

- **Bandas que se expanden**  
  👉 Indican acumulación de trabajo → posible cuello de botella  

- **Bandas paralelas y estables**  
  👉 Flujo equilibrado → sistema estable  

- **Bandas irregulares o con variaciones bruscas**  
  👉 Flujo inestable → problemas en la gestión del trabajo  

---

### 🚨 Análisis aplicado al caso

En este caso se observa:

- Acumulación en la etapa de **Testing**  
  → Indica un cuello de botella en validación  

- Diferencias en el ancho de las bandas  
  → Reflejan variabilidad en la capacidad del equipo  

- Crecimiento no uniforme de “Done”  
  → Baja predictibilidad de entrega  

---

### 🛠️ Decisiones tomadas a partir del CFD

- Reducción de WIP en etapas previas  
- Redistribución de carga hacia Testing  
- Priorización de tareas bloqueadas  
- Ajuste del flujo para evitar sobrecarga  

---

### 📈 Resultado esperado

- Flujo más estable  
- Reducción del Lead Time  
- Mayor predictibilidad  
- Disminución de cuellos de botella  

👉 El CFD permite pasar de intuición a decisiones basadas en datos.

---

### 🚀 4. Caso práctico aplicado

📄 `caso_practico_kanban_app_ingles.md`

* Implementación completa del sistema Kanban
* Problemas reales del flujo
* Decisiones del equipo
* Resultados obtenidos

---

## 🔍 Ejemplo de situación real

Durante la operación del tablero:

* Testing alcanza su límite WIP
* Code Review se satura
* Development continúa iniciando trabajo

👉 Resultado:

* Aumento del Cycle Time
* Flujo inestable

---

## 🛠️ Acciones implementadas

* Reducción del WIP en Development
* Priorización de tareas bloqueadas
* Apoyo del equipo en Testing
* Ajuste del flujo de trabajo

---

## 📈 Resultados obtenidos

* Reducción de tiempos de entrega
* Flujo más estable y predecible
* Disminución de bloqueos
* Mejora en la calidad del producto

---

## 📊 Impacto en el producto

* Mayor velocidad de entrega de funcionalidades
* Mejor experiencia de usuario
* Incremento en uso de la aplicación
* Mayor satisfacción de usuarios (niños y padres)

---

## 💼 Enfoque profesional

Este módulo refleja prácticas utilizadas en entornos reales de desarrollo:

* Gestión de delivery end-to-end
* Optimización del flujo de trabajo
* Uso de métricas para toma de decisiones
* Alineación entre desarrollo y objetivos de negocio

---

## 🔥 Insight clave

> No se trata de gestionar tareas…
> sino de gestionar cómo fluye el trabajo.

---

## Conclusión

Kanban no solo permite visualizar tareas; permite gestionar el sistema de trabajo, estabilizar el flujo y mejorar la capacidad de entrega de valor.

En este módulo, el enfoque está puesto en cómo transformar la operación del equipo a través de decisiones basadas en flujo, límites WIP y métricas.

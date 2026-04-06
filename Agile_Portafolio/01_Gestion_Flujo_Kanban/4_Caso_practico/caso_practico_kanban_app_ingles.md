# 🧩 Caso Práctico: Implementación de Kanban en App de Inglés para Niños

## 🎯 Contexto

Se implementa un sistema Kanban para gestionar el desarrollo de una:

👉 **Aplicación de aprendizaje de inglés para niños de 3 a 8 años**

El producto busca mejorar:

* La **retención de usuarios**
* El **engagement mediante experiencias interactivas**
* El aprendizaje mediante **audio, juegos y recompensas**

---

## 🚨 Problema inicial

El equipo presentaba:

* Sobrecarga de trabajo en desarrollo
* Retrasos en fases de Testing y QA
* Falta de visibilidad del estado real de las tareas
* Entregas poco predecibles

👉 El flujo de trabajo era inconsistente y generaba cuellos de botella.

---

## 🧠 Objetivo de la implementación

Diseñar un sistema Kanban que permita:

* Visualizar el flujo de trabajo end-to-end
* Limitar el trabajo en curso (WIP)
* Reducir tiempos de entrega
* Detectar y resolver bloqueos rápidamente
* Mejorar la predictibilidad del equipo

---

## 🧱 Diseño del flujo Kanban

Se definió el siguiente flujo:

```text id="snfslb"
Backlog → Ready → Development → Code Review → Testing → QA → Release → Done
```

### Principios aplicados:

* Flujo continuo (sin dependencia de sprints rígidos)
* Trabajo en unidades pequeñas
* Políticas explícitas por columna
* Gestión activa del flujo

---

## 📌 Ejemplo de Feature

**Feature:** Juego de vocabulario con audio

**Historia de usuario:**

> Como niño, quiero escuchar la pronunciación de una palabra para aprender correctamente

### Criterios de aceptación:

* Reproducción de audio al interactuar con la palabra
* Feedback visual mediante animaciones
* Compatibilidad con dispositivos móviles

---

## ⚙️ Implementación de WIP

Se definieron límites de trabajo en curso:

| Columna     | Límite WIP |
| ----------- | ---------- |
| Development | 3          |
| Code Review | 2          |
| Testing     | 2          |
| QA          | 2          |

### Resultado:

* Reducción de multitarea
* Mayor foco del equipo
* Mejora en la calidad de entrega

---

## 📊 Métricas utilizadas

Se incorporaron métricas de flujo para tomar decisiones:

### Lead Time

Tiempo total desde la idea hasta producción
👉 Ejemplo: 10 días

### Cycle Time

Tiempo desde inicio de desarrollo hasta entrega
👉 Ejemplo: 4 días

### Throughput

Cantidad de historias entregadas por semana
👉 Ejemplo: 8 historias

### WIP

Cantidad de trabajo en curso
👉 Controlado para evitar saturación

---

## 🔍 Problema detectado (caso real)

Durante la implementación:

👉 Se detectó acumulación en la columna **Testing**

### Impacto:

* Aumento del Cycle Time
* Retrasos en entregas
* Cuellos de botella en QA

---

## 🛠️ Acciones tomadas

* Se restringió el ingreso de nuevas tareas en Development
* Se priorizó la resolución de Testing
* Se redistribuyó la carga de trabajo del equipo
* Se mejoraron prácticas de pruebas automatizadas

---

## 📈 Resultados obtenidos

* Reducción del Cycle Time en un ~30%
* Flujo de trabajo más estable
* Menor acumulación de tareas
* Mayor predictibilidad en entregas
* Mejora en la calidad del producto

---

## 📊 Impacto en el producto

* Aumento del tiempo de uso por sesión
* Mejora en la experiencia de aprendizaje
* Mayor interacción con funcionalidades clave
* Feedback positivo de usuarios (niños y padres)

---

## 🔄 Mejora continua

Se establecieron prácticas de optimización:

* Ajuste dinámico de WIP
* Reducción del tamaño de historias
* Identificación temprana de bloqueos
* Uso continuo de métricas para toma de decisiones

---

## 💼 Enfoque profesional

Este caso refleja una implementación real de Kanban orientada a:

* Gestión de delivery end-to-end
* Optimización del flujo de trabajo
* Toma de decisiones basada en datos
* Alineación entre desarrollo y objetivos de negocio

---

## 🎯 Conclusión

La implementación de Kanban permitió transformar un flujo de trabajo reactivo en un sistema:

👉 predecible, eficiente y orientado a la entrega continua de valor.

Este enfoque es clave en entornos donde la velocidad y la calidad impactan directamente en la experiencia del usuario.


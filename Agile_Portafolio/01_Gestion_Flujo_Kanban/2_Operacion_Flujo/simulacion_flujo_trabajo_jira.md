# 🧪 Simulación de Flujo de Trabajo en Jira — Kanban

## 🎯 Objetivo

Simular el funcionamiento real de un tablero Kanban en Jira / Azure DevOps para el desarrollo de una:

👉 **App de aprendizaje de inglés para niños de 3 a 8 años**

Este documento representa cómo el equipo gestiona el trabajo día a día.

---

## 🧱 Estructura del tablero

```text id="l7w42d"
Backlog → Ready → Development → Code Review → Testing → QA → Release → Done
```

---

## 📋 Estado inicial del tablero

### 🧩 Backlog

* [EPIC-01] Sistema de aprendizaje interactivo
* [EPIC-02] Reconocimiento de voz
* [EPIC-03] Sistema de recompensas

---

### 🟡 Ready

* [US-101] Reproducción de audio en palabras
* [US-102] Animaciones visuales interactivas
* [US-103] Integración básica de reconocimiento de voz

---

## 🔵 Development (WIP: 3/3)

* [US-101] Reproducción de audio
  👤 Backend Developer
  🔧 Integrando API de audio

* [US-102] Animaciones visuales
  👤 Frontend Developer
  🎨 Implementando animaciones

* [US-104] Persistencia de progreso
  👤 Fullstack Developer
  💾 Diseñando base de datos

---

## 🟣 Code Review (WIP: 2/2)

* [US-105] Sistema de login padres
* [US-106] Navegación UI principal

⚠️ Límite alcanzado → No se pueden ingresar nuevas tareas

---

## 🟠 Testing (WIP: 2/2)

* [US-107] Validación reproducción audio
* [US-108] Pruebas de animaciones

🚨 Problema detectado:

* Testing saturado
* Tareas acumulándose

---

## 🟢 QA (WIP: 1/2)

* [US-109] Validación experiencia usuario

---

## 🚀 Release

* [US-095] Pantalla inicio
* [US-096] Navegación básica

---

## ✅ Done

* [US-090] Configuración inicial proyecto
* [US-091] Estructura base frontend

---

# 🔍 Situación real del flujo

## 🚨 Problema identificado

* Columna **Testing** saturada
* Code Review también al límite
* Development sigue iniciando trabajo

👉 Resultado:

* Aumento del Cycle Time
* Cuello de botella en validación

---

# 🛠️ Decisiones del equipo (Daily Kanban)

Durante la daily se toman las siguientes acciones:

### 1. 🚫 Stop starting, start finishing

* Se detiene ingreso de nuevas tareas a Development

---

### 2. 🔄 Enfoque en desbloqueo

* Developers apoyan Testing
* Se priorizan tareas en QA

---

### 3. ⚙️ Ajuste de flujo

* Se revisa necesidad de automatizar pruebas
* Se evalúa reducir tamaño de historias

---

# 📈 Evolución del tablero (después de ajustes)

## 🟠 Testing (WIP: 1/2)

* Disminuye carga

## 🟣 Code Review (WIP: 1/2)

* Flujo más rápido

## 🔵 Development (WIP: 2/3)

* Menor sobrecarga

👉 Flujo vuelve a estabilizarse

---

# 📊 Impacto en métricas

| Métrica    | Antes    | Después    |
| ---------- | -------- | ---------- |
| Cycle Time | Alto     | Reducido   |
| WIP        | Saturado | Controlado |
| Throughput | Bajo     | Estable    |

---

# 💼 Prácticas observadas

* Gestión activa del flujo
* Uso de WIP como herramienta estratégica
* Enfoque en terminar trabajo antes de comenzar nuevo
* Colaboración cross-funcional

---

# 🎯 Conclusión

El tablero Kanban no es solo visualización:

👉 Es un sistema dinámico de gestión de trabajo

Donde el equipo:

* Detecta cuellos de botella
* Toma decisiones en tiempo real
* Optimiza continuamente el flujo

---

## 🚀 Valor profesional

Esta simulación demuestra:

* Experiencia en herramientas como Jira / Azure DevOps
* Capacidad de gestión de equipos ágiles
* Pensamiento orientado a flujo y métricas
* Toma de decisiones basada en datos

---

## 🔥 Insight clave

> El problema no es la cantidad de trabajo…
> es cómo fluye el trabajo dentro del sistema.

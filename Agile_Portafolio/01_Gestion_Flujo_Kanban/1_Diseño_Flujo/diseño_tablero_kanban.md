# 🧱 Diseño de Tablero Kanban — App de Inglés para Niños

## 🎯 Objetivo

Definir la estructura de un tablero Kanban para gestionar el desarrollo de una:

👉 **Aplicación de aprendizaje de inglés para niños de 3 a 8 años**

El tablero está diseñado para ser implementado en herramientas como:

* Jira
* Azure DevOps

---

## 🔄 Flujo del tablero

```text
Backlog → Ready → Development → Code Review → Testing → QA → Release → Done
```

---

## 📌 Definición de columnas

### 🧩 Backlog

* Contiene todas las iniciativas priorizadas
* Definidas a nivel de feature o épica

---

### 🟡 Ready

* Historias refinadas
* Cumplen Definition of Ready (DoR)
* Listas para ser tomadas por el equipo

---

### 🔵 Development

* Historias en desarrollo activo
* Código en construcción

---

### 🟣 Code Review

* Validación técnica
* Revisión de calidad de código

---

### 🟠 Testing

* Pruebas unitarias e integradas
* Validación funcional

---

### 🟢 QA

* Validación final
* Pruebas de usuario / negocio

---

### 🚀 Release

* Listo para despliegue
* Aprobado por QA

---

### ✅ Done

* Funcionalidad en producción
* Cumple Definition of Done

---

## 📋 Ejemplos de tareas (Jira / Azure DevOps)

---

### 🎮 Feature: Juego de vocabulario interactivo

**Epic:** Aprendizaje básico de vocabulario

---

#### 🧩 Historia 1

**Título:** Implementar reproducción de audio en palabras

**Descripción:**
Como niño, quiero escuchar la pronunciación de una palabra para aprender correctamente

**Criterios de aceptación:**

* Audio se reproduce al tocar la palabra
* Funciona en móvil y tablet
* No supera 1 segundo de latencia

**Tareas técnicas:**

* Integrar API de audio
* Crear componente de reproducción
* Manejar eventos táctiles

---

#### 🧩 Historia 2

**Título:** Crear animaciones visuales al interactuar

**Descripción:**
Como niño, quiero ver animaciones para hacer el aprendizaje más entretenido

**Criterios de aceptación:**

* Animación al tocar palabra
* Compatible con dispositivos móviles
* No afecta rendimiento

**Tareas técnicas:**

* Implementar animaciones (CSS/JS)
* Integrar con componente UI
* Pruebas de rendimiento

---

---

### 🎤 Feature: Reconocimiento de voz

---

#### 🧩 Historia 3

**Título:** Integrar reconocimiento de voz básico

**Descripción:**
Como niño, quiero pronunciar palabras y recibir feedback

**Criterios de aceptación:**

* Detecta pronunciación correcta
* Feedback visual inmediato
* Funciona en entorno móvil

**Tareas técnicas:**

* Integrar API de speech-to-text
* Validar pronunciación
* Manejar errores de audio

---

---

### 🎁 Feature: Sistema de recompensas

---

#### 🧩 Historia 4

**Título:** Implementar sistema de stickers

**Descripción:**
Como niño, quiero recibir recompensas al completar actividades

**Criterios de aceptación:**

* Asignación de stickers por logro
* Visualización en perfil
* Persistencia de datos

**Tareas técnicas:**

* Crear modelo de datos
* Implementar lógica de asignación
* Guardar progreso

---

---

### 👨‍👩‍👧 Feature: Dashboard para padres

---

#### 🧩 Historia 5

**Título:** Visualizar progreso del niño

**Descripción:**
Como padre, quiero ver el avance de aprendizaje

**Criterios de aceptación:**

* Progreso por nivel
* Tiempo de uso
* Actividades completadas

**Tareas técnicas:**

* Crear API de métricas
* Diseñar UI dashboard
* Integrar backend

---

---

## ⚙️ Configuración en Jira / Azure DevOps

### Tipos de ítems

* Epic
* Feature
* User Story
* Task
* Bug

---

### Campos recomendados

* Prioridad
* Story Points
* Responsable
* Fecha objetivo
* Estado
* Etiquetas (feature, frontend, backend, QA)

---

## 🔒 Políticas clave del tablero

* No iniciar nuevas tareas si WIP está lleno
* Priorizar tareas bloqueadas
* Toda historia debe cumplir DoR antes de entrar
* Toda historia debe cumplir DoD antes de cerrar

---

## 📊 Ejemplo de flujo real

1. Historia entra a **Ready**
2. Equipo la toma → pasa a **Development**
3. Se completa → pasa a **Code Review**
4. Validación técnica → pasa a **Testing**
5. QA valida → pasa a **Release**
6. Se despliega → pasa a **Done**

---

## 💼 Enfoque profesional

Este diseño refleja:

* Gestión de flujo end-to-end
* Separación clara de etapas de desarrollo
* Control de calidad en múltiples niveles
* Alineación con herramientas reales (Jira / Azure DevOps)

---

## 🎯 Resultado esperado

* Flujo de trabajo visible y controlado
* Reducción de cuellos de botella
* Mejora en la calidad del software
* Entrega continua de valor al usuario

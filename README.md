# Servicio de Pedidos 🚀

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Descripción
Proyecto de **servicio de pedidos** usando Python y FastAPI. Permite gestionar usuarios, platos y pedidos de forma modular, simulando un sistema real de restaurante o comercio electrónico.

---

## Tecnologías
- Python 3.10+
- FastAPI (API REST)
- Uvicorn (Servidor ASGI)
- Pydantic (Modelos de datos)
- SQLite (opcional)
- Git / GitHub

---

## Estructura del proyecto

```text
PedidoService/
 ├─ main.py          # API principal: define endpoints de usuarios, platos y pedidos
 ├─ models.py        # Modelos de datos (Pydantic)
 ├─ services/        # Lógica de negocio (funciones para usuarios, platos y pedidos)
 ├─ requirements.txt # Dependencias del proyecto
 ├─ README.md        # Documentación del proyecto
 └─ .gitignore       # Archivos a ignorar en GitHub (venv, logs, __pycache__)

 ---

## Funcionalidades
- Crear, listar y eliminar usuarios  
- Crear, listar y eliminar platos  
- Crear y consultar pedidos por usuario  
- Gestión de IDs únicas para usuarios y platos  
- Modularización por microservicios

---

## Instalación
Clonar el repositorio:
git clone https://github.com/Chocolatesgirl/PedidoService.git
cd PedidoService
Crear entorno virtual:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Instalar dependencias:
pip install -r requirements.txt

---

## Uso
Ejecutar el servicio:
uvicorn main:app --reload --port 8000
Probar endpoints con navegador, Postman o curl:
GET /usuarios → Listar usuarios
POST /usuarios → Crear usuario
GET /platos → Listar platos
POST /pedidos → Crear pedido
Ejemplo con curl:
curl -X POST "http://127.0.0.1:8000/usuarios" -H "Content-Type: application/json" -d '{"nombre":"Verónica"}'
Documentación automática de FastAPI:
http://127.0.0.1:8000/docs

---

## Contribuciones
Hacer fork del repositorio
Crear rama nueva: git checkout -b feature/nueva-funcionalidad
Commit de cambios: git commit -m "Agregar nueva funcionalidad"
Push a tu rama: git push origin feature/nueva-funcionalidad
Crear Pull Request en GitHub

---

## Licencia
Este proyecto está bajo MIT License.
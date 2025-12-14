# 📦 CLI Inventory Manager (Python + SQL)

Sistema de gestión de inventario ligero basado en consola (CLI), desarrollado en **Python** implementando **Programación Orientada a Objetos (POO)** y persistencia de datos con **SQLite**.

Este proyecto fue diseñado para demostrar la integración de lógica de negocio, manipulación de bases de datos relacionales y estructuras de código modulares sin dependencias externas pesadas.

# Características Técnicas

* **Arquitectura Modular:** Separación clara entre la lógica de base de datos (`DatabaseManager`) y la lógica de negocio (`InventorySystem`).
* **Persistencia de Datos:** Uso de SQLite para almacenamiento permanente local.
* **Seguridad SQL:** Implementación de *Parameterized Queries* para prevenir inyección SQL.
* **CRUD Completo:** Funcionalidades para Crear, Leer, Actualizar y Borrar productos.
* **Sin Dependencias:** Funciona con la librería estándar de Python (no requiere `pip install`).

# Tecnologías.

* ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
* ![SQLite](https://img.shields.io/badge/SQLite-Standard-green)

## Instalación y Uso.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/Inventory-Manager-Python.git](https://github.com/TU_USUARIO/Inventory-Manager-Python.git)
    cd Inventory-Manager-Python
    ```

2.  **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```
    *(El archivo de base de datos `inventory.db` se creará automáticamente en la primera ejecución).*

# Estructura del Código

El proyecto sigue principios de POO:

```mermaid
classDiagram
    class DatabaseManager {
        +connect()
        +execute_query()
        +close()
    }
    class Product {
        +name: str
        +category: str
        +price: float
        +stock: int
    }
    class InventorySystem {
        +add_product()
        +update_stock()
        +delete_product()
        +show_products()
    }
    InventorySystem --> DatabaseManager : Utiliza


Roadmap y Mejoras Futuras
Este proyecto es una implementación base. Las siguientes características están planificadas para futuras iteraciones:

[ ] Validaciones: Implementar manejo de excepciones para evitar precios negativos o caracteres inválidos.

[ ] Reportes: Exportación de inventario a formato CSV/Excel.

[ ] ORM: Migración de SQL crudo a SQLAlchemy para abstracción de base de datos.

[ ] Interfaz Gráfica: Implementación de GUI con Tkinter o PyQt.

[ ] Testing: Unit Testing con unittest o pytest.

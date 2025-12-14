import sqlite3
from datetime import datetime

# ==========================================
# PROYECTO: Simple Inventory Manager
# AUTOR: Gonzalo Leiva
# TECNOLOGÍAS: Python, SQLite, POO
# ==========================================

class DatabaseManager:
    # Esta Clase se encarga de la conexión y ejecución de consultas SQL
    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # SQL puro para crear la tabla si no existe
        sql_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            last_updated TEXT
        )
        """
        self.cursor.execute(sql_query)
        self.conn.commit()

    def execute_query(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        self.conn.commit()
        return self.cursor

    def close(self):
        self.conn.close()

class Product:
    """Clase que representa un producto"""
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

class InventorySystem:
    """Clase principal que maneja la lógica del negocio"""
    def __init__(self):
        self.db = DatabaseManager()

    def add_product(self):
        print("\n AGREGAR NUEVO PRODUCTO ")
        try:
            name = input("Nombre: ")
            category = input("Categoría: ")
            price = float(input("Precio: "))
            stock = int(input("Cantidad inicial: "))
            
            # Insertar en BD usando parámetros para evitar inyección SQL
            query = "INSERT INTO products (name, category, price, stock, last_updated) VALUES (?, ?, ?, ?, ?)"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.db.execute_query(query, (name, category, price, stock, timestamp))
            print(f"✅ ¡Producto '{name}' agregado exitosamente!")
        except ValueError:
            print("Error: Por favor ingrese números válidos para precio y stock.")

    def show_products(self):
        print("\n--- LISTA DE PRODUCTOS ---")
        query = "SELECT * FROM products"
        result = self.db.execute_query(query).fetchall()

        if not result:
            print("El inventario está vacío.")
            return

        print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'PRECIO':<10} {'STOCK':<10}")
        print("-" * 60)
        for row in result:
            # row es una tupla: (id, name, category, price, stock, last_updated)
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} ${row[3]:<9.2f} {row[4]:<10}")

    def update_stock(self):
        self.show_products()
        print("\n--- ACTUALIZAR STOCK ---")
        try:
            prod_id = int(input("ID del producto a actualizar: "))
            new_stock = int(input("Nuevo stock total: "))
            
            query = "UPDATE products SET stock = ?, last_updated = ? WHERE id = ?"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            cursor = self.db.execute_query(query, (new_stock, timestamp, prod_id))
            
            if cursor.rowcount > 0:
                print("✅ Stock actualizado correctamente.")
            else:
                print("⚠️ ID no encontrado.")
        except ValueError:
            print("Error: Ingrese un ID numérico válido.")

    def delete_product(self):
        print("\n ELIMINAR PRODUCTO ")
        try:
            prod_id = int(input("ID del producto a eliminar: "))
            query = "DELETE FROM products WHERE id = ?"
            cursor = self.db.execute_query(query, (prod_id,))
            
            if cursor.rowcount > 0:
                print(" Producto eliminado.")
            else:
                print(" ID no encontrado.")
        except ValueError:
            print("Error: Ingrese un ID numérico válido.")

def main():
    system = InventorySystem()
    
    while True:
        print("\n= SISTEMA DE GESTIÓN DE INVENTARIO (Python + SQL) =")
        print("1. Ver Productos")
        print("2. Agregar Producto")
        print("3. Actualizar Stock")
        print("4. Eliminar Producto")
        print("5. Salir")
        
        option = input("Seleccione una opción: ")

        if option == '1':
            system.show_products()
        elif option == '2':
            system.add_product()
        elif option == '3':
            system.update_stock()
        elif option == '4':
            system.delete_product()
        elif option == '5':
            print("Saliendo...")
            system.db.close()
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

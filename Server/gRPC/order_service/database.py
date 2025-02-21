import mysql.connector

class ProductDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='ecommerce'
        )
        
    def get_price(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT price FROM products WHERE product_id=%s", (product_id,))
        result = cursor.fetchone()
        return result[0] if result else None
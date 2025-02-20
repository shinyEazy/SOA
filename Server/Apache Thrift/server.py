from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import mysql.connector
from gen_py.OrderService import OrderService

class OrderServiceHandler:
    def calculateTotal(self, productId, quantity):
        price = 0.0
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yourpassword",
                database="ecommerce"
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT price FROM products WHERE productId = '{productId}'")
            result = cursor.fetchone()
            if result:
                price = result[0]
            cursor.close()
            db.close()
        except Exception as e:
            print(e)
        return price * quantity

handler = OrderServiceHandler()
processor = OrderService.Processor(handler)
transport = TSocket.TServerSocket(host='0.0.0.0', port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting Thrift server...")
server.serve()
import grpc
from concurrent import futures
import order_pb2
import order_pb2_grpc
import mysql.connector

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CalculateTotal(self, request, context):
        price = 0.0
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yourpassword",
                database="ecommerce"
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT price FROM products WHERE productId = '{request.productId}'")
            result = cursor.fetchone()
            if result:
                price = result[0]
            cursor.close()
            db.close()
        except Exception as e:
            print(e)
        return order_pb2.OrderResponse(total=price * request.quantity)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
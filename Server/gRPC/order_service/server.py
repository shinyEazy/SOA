from concurrent import futures
import grpc
import time

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

import orders_pb2
import orders_pb2_grpc
from database import ProductDB

class OrderServicer(orders_pb2_grpc.OrderServiceServicer):
    def __init__(self, delay=0):
        self.db = ProductDB()
        self.delay = delay

    def CalculateTotal(self, request, context):
        print(f"Received request for product_id: {request.product_id}, quantity: {request.quantity}")
        if self.delay > 0:
            time.sleep(self.delay)

        price = self.db.get_price(request.product_id)
        if not price:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return orders_pb2.OrderResponse()

        total = price * request.quantity
        return orders_pb2.OrderResponse(total=total, status="SUCCESS")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(delay=0.1), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server is running')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
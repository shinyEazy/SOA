from locust import User, task, between, events
import grpc
import sys
import os
import time
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "order_client/generated"))

import orders_pb2
import orders_pb2_grpc

class GrpcClient:
    def __init__(self, host, environment):
        self.environment = environment
        self.host = host
        self.channel = grpc.insecure_channel(host)
        self.stub = orders_pb2_grpc.OrderServiceStub(self.channel)

    def calculate_total(self, product_id, quantity):
        req = orders_pb2.OrderRequest(product_id=product_id, quantity=quantity)

        start_time = time.time()

        try:
            response = self.stub.CalculateTotal(req, timeout=5)
            total_time = (time.time() - start_time) * 1000 

            self.environment.events.request.fire(
                request_type="grpc",
                name="CalculateTotal",
                response_time=total_time,
                response_length=0,  
                exception=None if response.status == "SUCCESS" else "Request Failed",
            )

            return response

        except grpc.RpcError as e:
            total_time = (time.time() - start_time) * 1000  

            self.environment.events.request.fire(
                request_type="grpc",
                name="CalculateTotal",
                response_time=total_time,
                response_length=0,
                exception=e, 
            )

            print(f"gRPC Error: {e.code()}, {e.details()}")
            return None

class OrderUser(User):
    wait_time = between(0.1, 0.5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = GrpcClient(self.host, self.environment)  

    @task
    def calculate_total(self):
        product_id = f"prod_{random.randint(1, 1000)}"  
        quantity = random.randint(1, 50)  
        response = self.client.calculate_total(product_id, quantity)
        
        if response:
            formatted_total = f"{response.total:.2f}"  
            print(f"Order Response: Product: {product_id}, Quantity: {quantity}, Total: {formatted_total}, Status: {response.status}")

# locust -f locustfile.py --host=192.168.158.128:50051

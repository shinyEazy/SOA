from locust import HttpUser, task, between
import grpc
import order_pb2
import order_pb2_grpc

class GrpcUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def calculateTotal(self):
        with grpc.insecure_channel('server_vm_ip:50051') as channel:
            stub = order_pb2_grpc.OrderServiceStub(channel)
            stub.CalculateTotal(order_pb2.OrderRequest(productId="prod1", quantity=5))
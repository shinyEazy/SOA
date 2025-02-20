import grpc
import order_pb2
import order_pb2_grpc

def run():
    with grpc.insecure_channel('server_vm_ip:50051') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)
        response = stub.CalculateTotal(order_pb2.OrderRequest(productId="prod1", quantity=5))
        print("Total cost: ", response.total)

if __name__ == '__main__':
    run()
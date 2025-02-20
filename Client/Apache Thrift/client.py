from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen_py.OrderService import OrderService

transport = TSocket.TSocket('server_vm_ip', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = OrderService.Client(protocol)

transport.open()
total = client.calculateTotal("prod1", 5)
print("Total cost: ", total)
transport.close()
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("server_vm_ip", 1099);
            OrderService service = (OrderService) registry.lookup("OrderService");
            double total = service.calculateTotal("prod1", 5);
            System.out.println("Total cost: " + total);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) {
        try {
            OrderServiceImpl service = new OrderServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("OrderService", service);
            System.out.println("Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
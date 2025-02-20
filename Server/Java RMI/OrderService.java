import java.rmi.Remote;
import java.rmi.RemoteException;

public interface OrderService extends Remote {
    double calculateTotal(String productId, int quantity) throws RemoteException;
}
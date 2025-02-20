import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class OrderServiceImpl extends UnicastRemoteObject implements OrderService {
    protected OrderServiceImpl() throws RemoteException {
        super();
    }

    public double calculateTotal(String productId, int quantity) throws RemoteException {
        double price = 0.0;
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ecommerce", "root", "yourpassword")) {
            PreparedStatement stmt = conn.prepareStatement("SELECT price FROM products WHERE productId = ?");
            stmt.setString(1, productId);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                price = rs.getDouble("price");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return price * quantity;
    }
}
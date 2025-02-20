package com.example.rmi;
import java.rmi.*;
import java.rmi.server.*;
import java.sql.*;
public class OrderServiceImpl extends UnicastRemoteObject implements OrderService {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/ecommerce";
    private static final String DB_USER = "root"; // Replace with your user
    private static final String DB_PASSWORD = "123456"; // Replace with your password
    public OrderServiceImpl() throws RemoteException {}
    @Override
    public double calculateTotal(String productId, int quantity) throws RemoteException {
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement stmt = conn.prepareStatement("SELECT price FROM products WHERE product_id=?")) {
            stmt.setString(1, productId);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) return rs.getDouble("price") * quantity;
            else throw new RemoteException("Product not found");
        } catch (SQLException e) { throw new RemoteException("Database error", e); }
    }
}
package com.example.rmi;
import java.rmi.registry.*;
public class OrderServiceClient {
    public static void main(String[] args) throws Exception {
        String productId = args[0];
        int quantity = Integer.parseInt(args[1]);
        Registry registry = LocateRegistry.getRegistry("192.168.158.128", 1099);
        OrderService service = (OrderService) registry.lookup("OrderService");
        double total = service.calculateTotal(productId, quantity);
        System.out.println("Total: " + total);
    }
}

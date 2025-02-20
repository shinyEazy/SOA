package com.example.rmi;
import java.rmi.registry.*;
public class RMIServer {
    public static void main(String[] args) throws Exception {
        OrderService service = new OrderServiceImpl();
        Registry registry = LocateRegistry.createRegistry(1099);
        registry.rebind("OrderService", service);
        System.out.println("RMI Server running...");
    }
}
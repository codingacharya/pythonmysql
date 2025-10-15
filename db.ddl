CREATE DATABASE s1_sb;

USE s1_db;

CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales_data (product_name, category, quantity, price, sale_date) VALUES
('Laptop', 'Electronics', 10, 60000, '2025-01-10'),
('Mouse', 'Electronics', 50, 500, '2025-02-12'),
('Keyboard', 'Electronics', 40, 1200, '2025-02-18'),
('T-Shirt', 'Clothing', 20, 800, '2025-03-05'),
('Shoes', 'Clothing', 15, 2000, '2025-04-10'),
('Book', 'Stationery', 30, 300, '2025-05-22'),
('Pen','Stationery',10,100,'2025-10-20');


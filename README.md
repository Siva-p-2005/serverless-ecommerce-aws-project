# Serverless E-commerce Store Project (AWS)

## 👨‍🎓  Name
Siva

## ☁️ Project Type
AWS Serverless Project

## 🎯 Project Objective
To build a fully serverless e-commerce application where users can browse products, add items to a cart, and place orders using AWS managed services without maintaining servers.

---

## 🧰 Technology Stack
- AWS Lambda (Python)
- Amazon API Gateway (HTTP API)
- Amazon S3 (Static Website Hosting)
- Amazon DynamoDB
- AWS IAM

---

## 🏗️ Architecture Overview
User (Browser)  
→ S3 Static Website  
→ API Gateway  
→ AWS Lambda Functions  
→ DynamoDB Tables

---

## 🔧 AWS Services Used
- **Amazon S3**: Hosts frontend static website (HTML, CSS, JavaScript)
- **AWS Lambda**: Backend logic for product listing, cart management, and order processing
- **API Gateway**: Connects frontend with Lambda functions
- **DynamoDB**: Stores products, cart details, and orders
- **IAM**: Manages permissions securely between AWS services

---

## 📊 DynamoDB Tables

### 1️⃣ Products Table
- ProductID (Primary Key)
- Name
- Description
- Price
- ImageURL

### 2️⃣ Cart Table
- UserID (Partition Key)
- ProductID (Sort Key)
- Quantity
- Price

### 3️⃣ Orders Table
- OrderID (Primary Key)
- OrderDate
- Products
- TotalAmount
- UserID
- ## 🗄️ DynamoDB Sample Data

All DynamoDB table sample data is available in a single file:

- `dynamodb/all_tables_data.json`

This file contains Products, Cart, and Orders table data.


---

## ⚙️ Lambda Functions

### 🔹 GetProducts
- Fetches all products from DynamoDB
- Method: GET

### 🔹 AddToCart
- Adds selected products to user cart
- Method: POST

### 🔹 GetCart
- Retrieves cart items for a user
- Method: GET

### 🔹 PlaceOrder
- Creates order from cart items
- Clears cart after successful order
- Method: POST

---

## 🔐 IAM Role & Policy
- Role Name: LambdaEcommerceRole
- Permissions:
  - dynamodb:Scan
  - dynamodb:GetItem
  - dynamodb:PutItem
  - dynamodb:UpdateItem
  - dynamodb:DeleteItem
  - dynamodb:Query

---

## 🚀 Execution Steps
1. User opens frontend URL hosted in S3
2. Products loaded using GetProducts API
3. User adds items to cart using AddToCart API
4. Cart viewed using GetCart API
5. Order placed using PlaceOrder API
6. Order stored in DynamoDB and cart cleared

---

## ✅ Key Features
- Fully serverless architecture
- Cost-effective and scalable
- No EC2 or server management
- Secure access using IAM roles
- Fast response using AWS managed services

---

## 📌 Conclusion
This project demonstrates a real-world serverless application using AWS. It highlights how modern cloud-native applications can be built with high scalability, low cost, and minimal operational overhead.

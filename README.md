# 🧾 Invoice Management System

## About the Project  
The **Invoice Management System** is a desktop application developed using **Python** with **Tkinter** for the graphical user interface. It integrates **MySQL** for data storage and **ReportLab** for generating PDF invoices. This system allows users to manage invoices by inserting details into a database and generating professional tax invoices in PDF format.  

---

## ✨ Features  
- 📋 **Insert Invoice Details**  
  Record customer details, product information, and GST calculations into the MySQL database.

- 🖨️ **Generate Tax Invoice**  
  Create a professional invoice in **PDF format** using the **ReportLab** library, complete with itemized details, GST breakdowns, and totals.

- 🖥️ **User-Friendly Interface**  
  Simple and intuitive interface built with **Tkinter** for seamless interaction.

---

## 🛠️ Tools and Technologies Used  
- **Python** 🐍: For application logic and GUI.  
- **Tkinter** 🖼️: For building the desktop interface.  
- **MySQL** 🛢️: To store and retrieve invoice details.  
- **ReportLab** 📝: To create and style PDF invoices.  

---

## 🗄️ Database Structure  
The system uses a MySQL database named `sys` with a table `sales.Invoice` having the following columns:  

| 🏷️ **Column Name**  | 🔢 **Data Type** | 📝 **Description**           |  
|----------------------|-----------------|-----------------------------|  
| `inv_no`            | INT             | Invoice number (Primary Key).  |  
| `inv_date`          | DATE            | Invoice date.                  |  
| `cust_name`         | VARCHAR         | Customer name.                 |  
| `cust_mobile`       | VARCHAR         | Customer phone number.         |  
| `prod_name`         | VARCHAR         | Product name.                  |  
| `prod_qty`          | INT             | Quantity of the product.       |  
| `prod_rate`         | FLOAT           | Rate of the product.           |  
| `price`             | FLOAT           | Total price before GST.        |  
| `CGST_Amount`       | FLOAT           | Central GST amount.            |  
| `SGST_Amount`       | FLOAT           | State GST amount.              |  
| `IGST_Amount`       | FLOAT           | Integrated GST amount.         |  

---

## 🧑‍💻 How the Application Works  

### 1️⃣ Insert Invoice Details  
- Enter invoice details through the GUI or input fields.  
- Data includes product name, quantity, rate, customer details, and GST percentage.  
- The system automatically calculates:  
  - 🛒 **Price** (Quantity × Rate).  
  - 🏦 **SGST, CGST, or IGST** based on GST type and percentage.  

### 2️⃣ Generate Invoice PDF  
- Enter the invoice number and click **Print**.  
- The system fetches invoice data from the MySQL database and generates a professional PDF invoice with:  
  - Itemized product details.  
  - GST breakdown.  
  - Total cost.  

---

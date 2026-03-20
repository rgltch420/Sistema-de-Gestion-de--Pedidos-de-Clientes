# Order Management System

A console-based Order Management System developed in Python.  
This program allows users to register clients, register products, create orders, and generate reports.

---

## Features

- Register clients with name and email validation  
- Register products using tuples (ID, name, price)  
- Create orders linking clients and products  
- Generate reports including:
  - Total orders
  - Total income
  - Orders grouped by client
  - Products sold  

---

## Project Structure
-src/
-│── main.py
-│── modules/
-│ ├── clientes.py
-│ ├── productos.py
-│ ├── pedidos.py
-│ ├── reportes.py



## How to Run

1. Navigate to the project folder:

 -src

2. Run the program 

- python main.py

## Supported Operating Systems

This program is compatible with:

-Linux (tested on Arch Linux)

-Windows

-macOS

## OS-Specific Behavior

The program uses a function to clear the console screen:

-os.system("cls" if os.name == "nt" else "clear")

-On Linux / macOS

Uses the clear command

-On Windows

Uses the cls command

## If Issues Occur

If the screen does not clear correctly:

- Option 1: Check terminal support

Linux/macOS → ensure clear works in your terminal

Windows → use CMD or PowerShell

- Option 2: Disable screen clearing

You can comment out the clear function:
- #clear()

## Notes

- The program uses dictionaries for data storage

- Products are stored as tuples

- No lists are used (as required by the assignment)

- Input validation is implemented to prevent errors

## Example Workflow

1. Register clients

2. Register products

3. Create orders

4. View report
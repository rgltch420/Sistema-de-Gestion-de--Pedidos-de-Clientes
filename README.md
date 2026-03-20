# Order Management System

A console-based **Order Management System** developed in Python.  
This application allows users to manage clients, products, orders, and reports in a simple and structured way.

---

## Features

- Client registration with name and email validation  
- Product registration using tuples (`ID`, `name`, `price`)  
- Order creation linking clients and products  
- Report generation including:
  - Total number of orders  
  - Total income  
  - Orders grouped by client  
  - Sold products summary  

---

## Project Structure

```bash
src/
│
├── main.py
└── modules/
    ├── clientes.py
    ├── productos.py
    ├── pedidos.py
    └── reportes.py
````

---

## How to Run

1. Navigate to the project directory:

```bash
cd src
```

2. Run the program:

```bash
python main.py
```

---

## Supported Operating Systems

This program is compatible with:

* Linux (tested on Arch Linux)
* Windows
* macOS

---

## OS-Specific Behavior

The application clears the console screen using:

```python
os.system("cls" if os.name == "nt" else "clear")
```

### Behavior by OS

* **Linux / macOS:** uses the `clear` command
* **Windows:** uses the `cls` command

---

## Troubleshooting

If the screen does not clear correctly:

### Option 1: Verify terminal support

* Linux/macOS: ensure the `clear` command works in your terminal
* Windows: use CMD or PowerShell

### Option 2: Disable screen clearing

You can comment out the clear function in the code:

```python
# clear()
```

---

## Notes

* The program uses dictionaries for data storage
* Products are stored as tuples
* Lists are not used (as required by the assignment)
* Input validation is implemented to prevent errors

---

## Example Workflow

1. Register clients
2. Register products
3. Create orders
4. View reports

```

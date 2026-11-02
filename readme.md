# Hardware Store Inventory Management System (Sistema de Gestión de Inventario para Ferretería)

An interactive, real-time inventory management software designed for a local hardware store. This system optimizes staff operations, tracks stock levels instantaneously, and prevents commodity losses by replacing manual paper-based logs with a robust, validated in-memory database.

Developed as the Final Practical Assignment for **Programación 1** (Distance Learning Programming Degree) at the **Universidad Tecnológica Nacional (UTN)**.

## 👤 Author & Commission

* **Author:** Victor
* **Commission:** A26 C1-13
* **Institution:** Universidad Tecnológica Nacional (UTN)

---

## 📌 Problem Context & Solution Overview

### The Manual Challenge
The local store originally operated via manual annotation or direct visual inspection of shelves. This caused delays in customer service, undetected material leakage, and human errors in counting stock.

### The Digital Solution
This application runs entirely in memory (RAM). It features a strictly validated CLI interface that handles real-time stock updates, prevents negative values, ensures clean entries, and frees up system memory safely upon exit.

### Scope Limitations (Out of Scope)
To comply with academic constraints, this system strictly excludes:
* Financial operations, cash register tracking, or commercial invoicing.
* Object-Oriented Programming (OOP) principles (no classes or objects).
* Advanced data structures (such as sets, deques, etc.).
* Global variables (data integrity relies purely on parameter passing by reference).

---

## 🛠️ Technical Stack & Environment

* **Language:** Python 3.14.5 (Academic standard requirement).
* **Paradigm:** Procedural, Modular programming.
* **IDE:** Visual Studio Code (Terminal integrated for manual testing and debugging).
* **Source Structure:** Monolithic architecture concentrated in a single source file: `Reta_Victor_P1.py`.

---

## 📐 Architecture & Data Mapping

The solution enforces a clear three-layer procedural separation:

1. **Central Control Layer (main):** Orchestrates the loop, prints the interactive menu, maps options, and centralizes exception capturing.
2. **Business Logic Layer:** Specialized modules (`def`) that manipulate inventory data and evaluate constraint metrics.
3. **Data Layer:** A localized, mutable sequence mapping structured catalog parameters in real-time.

```text
┌──────────────────────────────────────────────────┐
│              Central Control (main() Loop)       |
│      - Persistent Menu - System Exception Catcher| 
└────────────────────────────┬─────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────┐
│                Business Logic Functions                 │
│     - Validation Filters - Rule Violations(Raises)     
└────────────────────────────┬─────────────────────┘
                             │ (Pass-by-reference)
                             ▼
┌─────────────────────────────────────────────────────────┐
│             Data Layer (In-Memory Storage)             │
│    - Primary Sequence (list) -> Row Schemas(dicts)     │
└─────────────────────────────────────────────────────────┘
```

### Core Data Concept Applied
* **Main Sequence (`list`):** Acts as the primary warehouse ledger, holding multiple map schemas sequentially.
* **Row Schemas (`dict`):** Houses literal structural keys matching strict data classifications: `{'herramienta': str, 'cantidad': int}`.

---

## 🔌 Modules and Function Specifications

### `main() -> None`
The primary system runtime core. Initiates an empty storage matrix and hooks an ongoing interactive menu cycle. Evaluates inputs (redirecting routes from options 1 to 6), manages user-exits (option 7), and applies a smart terminal cursor reset via escape sequences (`\033[7D`). It encapsulates all traveling errors through an overarching `try...except` trap.

### `buscar_herramienta_inventario(inventario: list, nombre: str) -> int`
A specialized look-up routine. Normalizes strings via `.upper()` and `.strip()` filters to eliminate casing disparities or trailing spaces. Returns the index position if located, or `-1` if absent.

### `imprimir_menu() -> None`
Renders the CLI management dashboard options on standard output.

### `cargar_herramientas(inventario: list) -> None`
Handles batch-initialization routines. Employs dedicated `try...except` control blocks to force accurate item integers. Includes a quick escape listener (`SALIR`) to safely disrupt batch loads. Prevents duplicates or empty labels through local evaluation loops.

### `mostrar_inventario(inventario: list) -> None`
Parses the active warehouse records sequentially. Safely identifies empty records using a `len()` validation filter.

### `consultar_stock(inventario: list) -> None`
Enables custom single-item availability searches. Propagates standard `ValueError` anomalies to the main orchestrator if inputs are empty.

### `consultar_agotados(inventario: list) -> None`
An analytical reporter module. Scans the warehouse and filters entities where stock equals zero, summarizing the precise quantity of depleted products.

### `registrar_producto(inventario: list) -> None`
Enables ad-hoc single-item entry. Conducts validation filters against blank titles, duplicate item tags, or negative stock quantities.

### `actualizar_stock(inventario: list) -> None`
Handles point-of-sale reductions or supplier stock intakes. Requires choices between sales (1) or restock operations (2). Validates supply parameters and raises strict warnings if sales quantities exceed current shelf availability.

---

## 🛡️ Exception Design (Error Handling)

This application uses Python's execution termination model via two distinct strategic patterns:

* **Local Interception (Retry Pattern):** Implemented inside `cargar_herramientas`. Numerical conversions are wrapped inside an internal `while True` loop. If a user provides faulty data, the local block catches it, shows an error message, and prompts for input again without disrupting the ongoing session.
* **Traveling Exceptions (Bubbling Pattern):** Handled across options 3, 5, and 6. When business constraints fail (e.g., selling more stock than available, empty names, negative amounts), the functions trigger a `raise ValueError("Error Message")`. Since no local `except` block catches it inside these modules, the exception bubbles up directly to `main()`. The orchestrator logs the context error safely and returns the clerk back to the principal menu dashboard.

---

## Video Link

https://www.youtube.com/watch?v=nfF_3H7a6aQ&t=382s

---


## 🚀 Execution Instructions

1. Ensure you have Python installed (Version 3.10+ recommended, developed on 3.14.5).
2. Clone this repository:
   ```bash
   git clone https://github.com
   cd your-repository-name
   ```
3. Run the monolithic script file:
   ```bash
   python Reta_Victor_P1.py
   ```
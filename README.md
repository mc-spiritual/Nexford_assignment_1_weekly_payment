# Nexford_assignment_1_weekly_payment

# Highridge Construction - Worker Payment Processing System

This project was developed as a software engineering task for Highridge Construction Company. It facilitates the weekly payment process for 400 workers by generating dynamic payment slips using Python and R.

## 📌 Project Overview

The objective of this assignment is to automate the creation of payment slips based on each worker’s salary and gender, and assign them an appropriate employee level based on specific business rules.

---

## Features

- Dynamically generates a list of 400 workers.
- Assigns random gender and salary to each worker.
- Applies conditional logic to determine employee levels:
  - `A1` if salary is between $10,001 and $19,999.
  - `A5-F` if salary is between $7,501 and $29,999 and the worker is female.
  - Default level is `B2` otherwise.
- Includes error handling in the Python script.
- Saves payment slip data to a CSV file.
- Provides both Python and R versions of the solution.

---

## 🧠 Technologies Used

- **Python 3.x** (for initial development)
- **R** (for replicated functionality)
- **CSV** (as the output format)

---

## 📂 Files in this Repository

| Filename                 | Description                                         |
|--------------------------|-----------------------------------------------------|
| `weekly_payments.py`     | Main Python script for generating payment slips     |
| `weekly_payments.R`      | Equivalent R script for the same task               |
| `highridge_payment_slips.csv` | Output file with the generated payment data        |
| `README.md`              | Project overview and usage instructions             |

--- 

## 🧑‍💻 How to Run the Code

### ✅ Python

1. Make sure Python is installed.
2. Open terminal or PowerShell in the project directory.
3. Run the script:

```bash
python weekly_payments.py

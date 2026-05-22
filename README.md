# Nurath Hospital Management System

Welcome to the **Nurath Hospital Management System** — a comprehensive, interactive, and easy-to-use hospital data management and analytics platform designed for hospital staff and students.

---

## Project Overview

This project aims to streamline hospital record management and empower users with insightful analytics. Whether you are hospital staff registering patients or students analyzing hospital data, this system provides a seamless experience with a modern web interface and powerful backend.

---

## Tech Stack

- **Python**: Core programming language
- **Streamlit**: Web app framework for UI and interactivity
- **PostgreSQL (via Supabase)**: Cloud-hosted database for patient records and user management
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization (bar charts, line graphs, etc.)
- **psycopg2**: PostgreSQL database adapter for Python

---

## Features Built

- **User Authentication:**  
  Secure login and signup system with role-based access (Staff or Student).

- **Patient Record Management (Staff Only):**  
  - Add new patient records with detailed info (name, age, illness, bill, status, height, weight).  
  - Update patient status or billing information.  
  - Delete patient records securely.

- **Data Analytics (Students and Staff):**  
  - Statistical summaries such as mean age and billing.  
  - View patient admission and discharge stats.  
  - Identify patients with maximum bills, oldest and youngest patients.  
  - Daily patient counts and billing trends.

- **Visual Dashboards:**  
  Interactive bar charts and line graphs showing status-wise bills, admissions, discharges, and billing trends over time.

- **Body Mass Index (BMI) Calculator:**  
  Built-in BMI calculator with WHO categories, including custom inputs.

---

## Project Structure

/root
│
├── hospitalapp.py # Main Streamlit application code
├── sqlitepac.py # Database connection and patient record operations
├── analytics.py # Data analytics functions using Pandas
├── plotings.py # Data visualization and plotting functions
├── requirements.txt # Python dependencies list
└── README.md # Project overview and instructions (this file)

markdown
Copy
Edit

- `hospitalapp.py`: Handles the UI and user interactions. Implements login, patient data management, analytics dashboard, and BMI calculator.  
- `sqlitepac.py`: Connects to PostgreSQL database and handles CRUD operations on patient records.  
- `analytics.py`: Extracts and processes data for insights like max bill, oldest/youngest patients, and discharge status.  
- `plotings.py`: Prepares data frames for visualizations and provides aggregated stats by date, status, etc.

---

## How to Run

  1. Clone this repository.
  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
  3. Run the Streamlit app:
    ```bash
     streamlit run hospitalapp.py
  4. Open the provided localhost URL in your browser.
 

Author

Tharun Reddy

Open to collaboration and feedback to improve this project further.

Feel free to reach out or contribute!



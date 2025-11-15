#  Data Validation & Cleaning API  
A simple FastAPI service that validates, cleans, and standardizes sales data.  
It ensures correct data types, fixes formatting, removes invalid rows, and generates a detailed data-quality report.

##  Features

### ✔ Validate incoming JSON records  
- Ensures correct data types  
- Validates date formats  
- Enforces positive quantity  
- Ensures numeric price  

### ✔ Clean & Standardize  
- Trims strings  
- Converts product names to Title Case  
- Converts price → float  
- Converts dates → proper ISO format  
- Drops invalid rows

### ✔ Quality Report  
The API returns:  
- rows_received  
- rows_cleaned  
- invalid_rows  
- missing_values count  

### ✔ Supports:  
- **POST** user JSON  
- **GET** sample data (`sample.json`) located in `sample_data/`


##  Project Structure

fastapi-data-cleaning/
│
├── app/
│ ├── main.py # API routes
│ ├── schemas.py # Pydantic models
│ ├── cleaners.py # Data cleaning logic
│ ├── quality.py # Quality report generator
│
├── sample_data/
│ └── sample.json # Example input data
│
├── requirements.txt
└── README.md

##  Installation & Local Setup

### 1. Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/fastapi-data-cleaning.git

cd fastapi-data-cleaning

### 2. Create a virtual environment

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run FastAPI

uvicorn app.main:app --reload


Go to:  
http://127.0.0.1:8000/docs to use the API.


##  API Endpoints

### **POST /clean_json**  
Send your raw JSON data:

[
{
"product": "  iphone ",
"quantity": "2",
"price": "55000",
"order_date": "2024/01/10"
}
]


### Response example:

{
"cleaned_data": [...],
"quality_report": {
"rows_received": 3,
"rows_cleaned": 1,
"invalid_rows": 2,
"missing_values": {...}
}
}


### **GET /sample**  
Cleans and returns the contents of `sample_data/sample.json`.


### Build command:

pip install -r requirements.txt


### Start command:

uvicorn app.main:app --host=0.0.0.0 --port=8000


##  Author
**Anuja Ingale**  
GitHub: https://github.com/anujaingale41-lab






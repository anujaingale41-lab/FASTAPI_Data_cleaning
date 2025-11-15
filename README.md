# **Data Validation & Cleaning API**

A simple **FastAPI** service to validate and clean sales data.
Designed for **data engineers** to demonstrate data validation, cleaning, and reporting in Python.


## **Features**

* Validate user-submitted JSON data
* Clean and standardize product data (`product`, `quantity`, `price`, `order_date`)
* Generate a **quality report** showing rows cleaned and invalid rows
* Preloaded sample JSON for testing (`sample_data/sample.json`)
* Fully **deployed on Render**, accessible via public URL


## **Endpoints**

| Method | Endpoint      | Description                                                        |
| ------ | ------------- | ------------------------------------------------------------------ |
| GET    | `/sample`     | Returns cleaned data from `sample_data/sample.json`                |
| POST   | `/clean_json` | Submit your JSON data and get cleaned results and a quality report |


## **Live API**

You can test the API live:

* Swagger Docs: [https://fastapi-data-cleaning.onrender.com/docs](https://fastapi-data-cleaning.onrender.com/docs)
* Sample data: [https://fastapi-data-cleaning.onrender.com/sample](https://fastapi-data-cleaning.onrender.com/sample)


## **Usage**

### **1️. Run locally**

1. Clone the repository:

```bash
git clone https://github.com/anujaingale41-lab/fastapi-data-cleaning.git
cd fastapi-data-cleaning
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run FastAPI:

```bash
uvicorn app.main:app --reload
```

5. Open Swagger docs:

```
http://127.0.0.1:8000/docs
```


### **2️. Using the API**

#### GET `/sample`

Returns cleaned sample data from `sample_data/sample.json`.

#### POST `/clean_json`

Send a JSON body like:

```json
[
  {"product": "  iphone ", "quantity": "2", "price": "55000", "order_date": "2024-01-10"},
  {"product": "MOTOROLA", "quantity": 1, "price": 22000, "order_date": "2024-01-12"}
]
```

Response includes:

* `cleaned_data`: cleaned & validated rows
* `quality_report`: summary of rows received, cleaned, and invalid rows

---

## **Project Structure**

```
fastapi-data-cleaning/
│
├─ app/
│   ├─ main.py          # FastAPI app
│   ├─ schemas.py       # Pydantic models
│   ├─ cleaners.py      # Data cleaning functions
│   └─ quality.py       # Quality report functions
│
├─ sample_data/
│   └─ sample.json      # Sample dataset
│
├─ requirements.txt     # Python dependencies
└─ README.md
```


## **Technologies**

* Python 3.x
* FastAPI
* Pydantic
* Pandas
* Uvicorn
* Render (for deployment)


## **Author**

**Anuja Ingale**
[GitHub](https://github.com/anujaingale41-lab)


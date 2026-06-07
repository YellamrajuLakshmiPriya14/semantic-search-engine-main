# Semantic Search Engine

A simple Semantic Search Engine built with **FastAPI**, **Sentence Transformers**, **FAISS**, **DuckDB**, and **Pandas**.

This project lets you search text by **meaning** instead of only matching exact keywords.

For example, if you search:

```text
payment failed
```

the system can return similar customer support messages such as:

```text
transaction did not go through
card was charged twice
unable to complete payment
```

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Folder Structure](#project-folder-structure)
- [Prerequisites](#prerequisites)
- [Dataset Setup](#dataset-setup)
- [Local Installation](#local-installation)
- [How to Run the Project](#how-to-run-the-project)
- [How to Test the API](#how-to-test-the-api)
- [Common Errors and Fixes](#common-errors-and-fixes)
- [How the Project Works](#how-the-project-works)
- [Future Improvements](#future-improvements)

---

## Project Overview

This project performs **semantic search** on customer support text data.

Traditional search checks whether the exact search word exists in the data.

Semantic search checks the **meaning** of the query.

Example:

```text
User query: payment failed
```

The engine may return:

```text
card charged twice
transaction unsuccessful
refund not received
```

even if the exact words are different.

---

## Features

- Load customer support data from CSV
- Clean and prepare text data
- Generate text embeddings using Sentence Transformers
- Store and query data using DuckDB
- Create a FAISS vector index
- Search similar text using vector similarity
- Expose search through FastAPI
- Test APIs using Swagger UI

---

## Tech Stack

- Python
- Pandas
- DuckDB
- Sentence Transformers
- FAISS
- FastAPI
- Uvicorn

---

## Project Folder Structure

After setup, the folder should look like this:

```text
semantic-search-engine-main/
│
├── app.py
├── load_data.py
├── clean_data.py
├── generate_embeddings.py
├── create_index.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── twcs.csv ( Not able to upload as it is bigger in size )
│   ├── embeddings.npy
│   ├── faiss.index
│   └── support.duckdb ( Not able to upload as it is bigger in size )
│
└── __pycache__/
```

Important files:

| File | Purpose |
|---|---|
| `load_data.py` | Loads the CSV dataset into DuckDB |
| `clean_data.py` | Cleans and prepares the text data |
| `generate_embeddings.py` | Converts text into numerical embeddings |
| `create_index.py` | Creates the FAISS search index |
| `app.py` | Runs the FastAPI search API |
| `requirements.txt` | Contains required Python packages |

---

## Prerequisites

Install these before running the project:

- Python 3.10 or above
- Git, optional
- pip
- Internet connection for downloading Python packages and the embedding model

Check Python version:

```bash
python --version
```

Check pip version:

```bash
pip --version
```

---

## Dataset Setup

This project expects a dataset file at:

```text
data/twcs.csv
```

### Step 1: Create the `data` folder

Inside the project folder, create a folder named:

```text
data
```

Your folder should look like:

```text
semantic-search-engine-main/data/
```

### Step 2: Download the dataset

Download the **Customer Support on Twitter** dataset from Kaggle:

```text
https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter
```

### Step 3: Rename the CSV file

After downloading and extracting the dataset, rename the CSV file to:

```text
twcs.csv
```

### Step 4: Move the CSV file

Place it inside the `data` folder:

```text
semantic-search-engine-main/data/twcs.csv
```

---

## Local Installation

### Step 1: Open CMD or Terminal

Go to the project folder.

Example on Windows:

```bash
cd "C:\Users\bittu\OneDrive\Desktop\Dhibrahim\semantic-search-engine-main"
```

### Step 2: Install all dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs the required packages such as:

```text
fastapi
uvicorn
duckdb
faiss-cpu
sentence-transformers
pandas
numpy
```

---

## How to Run the Project

Run the project files in this exact order.

### Step 1: Load the data

```bash
python load_data.py
```

This reads `data/twcs.csv` and stores the data in DuckDB.

---

### Step 2: Clean the data

```bash
python clean_data.py
```

This cleans the text data and prepares it for embedding generation.

---

### Step 3: Generate embeddings

```bash
python generate_embeddings.py
```

This converts text into vector embeddings using Sentence Transformers.

Example:

```text
"payment failed"
```

becomes something like:

```text
[0.23, -0.15, 0.88, ...]
```

---

### Step 4: Create the FAISS index

```bash
python create_index.py
```

This creates the file:

```text
data/faiss.index
```

This file is required for fast semantic search.

---

### Step 5: Start the FastAPI server

```bash
uvicorn app:app --reload
```

If successful, you should see:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## How to Test the API

Open this URL in your browser:

```text
http://127.0.0.1:8000
```

You should see:

```json
{"message":"Semantic Search API Running"}
```

Now open the Swagger API page:

```text
http://127.0.0.1:8000/docs
```

### Test the `/search` endpoint

1. Click `GET /search`
2. Click `Try it out`
3. Enter a query:

```text
payment failed
```

4. Set `k` as:

```text
5
```

5. Click `Execute`

You should get semantically similar results from the dataset.

Example output:

```json
{
  "query": "payment failed",
  "results": [
    "card was charged twice",
    "transaction did not go through",
    "unable to complete payment"
  ]
}
```

---

## Common Errors and Fixes

### Error 1: `ModuleNotFoundError: No module named 'fastapi'`

Fix:

```bash
pip install fastapi uvicorn
```

Better fix:

```bash
pip install -r requirements.txt
```

---

### Error 2: `ModuleNotFoundError: No module named 'duckdb'`

Fix:

```bash
pip install duckdb
```

---

### Error 3: `ModuleNotFoundError: No module named 'faiss'`

Fix:

```bash
pip install faiss-cpu
```

---

### Error 4: `ModuleNotFoundError: No module named 'sentence_transformers'`

Fix:

```bash
pip install sentence-transformers
```

---

### Error 5: `FileNotFoundError: data/twcs.csv`

Reason:

The dataset file is missing.

Fix:

Create a `data` folder and place the dataset here:

```text
data/twcs.csv
```

---

### Error 6: `could not open data/faiss.index`

Reason:

The FAISS index was not created yet.

Fix:

Run:

```bash
python generate_embeddings.py
python create_index.py
```

Then start the server again:

```bash
uvicorn app:app --reload
```

---

### Error 7: `404 Not Found` for `favicon.ico`

This is not a real issue.

It only means the browser tried to load a website icon, but the project does not have one.

You can ignore it.

---

## How the Project Works

The full project flow is:

```text
CSV Dataset
    ↓
load_data.py
    ↓
DuckDB Database
    ↓
clean_data.py
    ↓
Clean Text
    ↓
generate_embeddings.py
    ↓
Text Embeddings
    ↓
create_index.py
    ↓
FAISS Index
    ↓
app.py
    ↓
FastAPI Search API
```

When a user searches:

```text
payment failed
```

the query is converted into an embedding.

Then FAISS compares that embedding with stored embeddings and returns the closest matches.

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Returns:

```json
{"message":"Semantic Search API Running"}
```

---

### Search Endpoint

```http
GET /search
```

Example request:

```text
http://127.0.0.1:8000/search?query=payment%20failed&k=5
```

Parameters:

| Parameter | Description | Example |
|---|---|---|
| `query` | Search text entered by user | `payment failed` |
| `k` | Number of results to return | `5` |

---

## Future Improvements

Possible improvements:

- Add a frontend using React, Streamlit, or Flask templates
- Show similarity scores with results
- Add filters by company, category, or date
- Use ChromaDB, Pinecone, or Weaviate instead of local FAISS
- Add authentication
- Deploy the API on Render, Railway, AWS, or Azure
- Add Docker support
- Add unit tests
- Improve cleaning and preprocessing pipeline

---


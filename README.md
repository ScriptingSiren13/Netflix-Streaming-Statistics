# **STREAMING STATISTICS**

<p align="center">
  <img src="https://img.shields.io/badge/Netflix%20Analytics-Streamlit%20Dashboard-E50914?style=for-the-badge&logo=netflix&logoColor=white" />
</p>

<h1 align="center"> Netflix Streaming Statistics Dashboard</h1>
<p align="center">An interactive Streamlit dashboard to explore patterns, trends, and insights from the Netflix titles dataset.</p>

---

##  Tech & Tools Used

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black"/>
<img src="https://img.shields.io/badge/Seaborn-4C8CB5?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>

---

##  Dataset

<img src="https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/>

**Source:** *Netflix Movies and TV Shows Dataset*

---

##  Project Overview

A fully interactive Streamlit dashboard designed to explore Netflix content using:

- Dynamic visuals  
- Clean tab-based navigation  
- Netflix-themed UI  
- Light/Dark mode switching  

It answers key analytical questions about global Netflix trends and provides rich insights into genres, ratings, durations, countries, and more.

---

##  Features

### 🔹 About Section  
Explains the purpose and scope of the dashboard.

### 🔹 Raw Data Exploration  
Includes:
- Dataset shape  
- Column info  
- Missing value summary  
- Data type overview  

### 🔹 Insightful Analytics  
Answers important questions like:
- What dominates Netflix: Movies or TV Shows?  
- How has the platform grown?  
- Which countries contribute the most content?  
- Who are the top actors/directors?  
- How are ratings distributed globally?  

### 🔹 Advanced Visualizations  
A complete suite of visual charts:
- Heatmaps (correlation, ratings, type vs. rating)  
- Violin plots  
- Boxplots  
- Stacked bar charts  
- Word clouds  
- Sankey flows  
- Choropleth maps  
- Histograms and distribution plots

  ---

##  Project Structure
```
streaming-statistics/
│── data/
│ └── netflix_titles.csv
│
│── notebooks/
│ └── eda_notebook.ipynb
│
│── streamlit_app/
│ └── app.py
│
│── images/
│── requirements.txt
│── README.md
│── .gitignore
```
---

## Installation

Follow these steps to set up the project on your machine:

### 1 Clone the repository
```bash
git clone https://github.com/ScriptingSiren13/streaming-statistics.git
cd streaming-statistics

2 Install dependencies
pip install -r requirements.txt


Usage
After installation, launch the Streamlit dashboard using:

1️⃣ Run the Streamlit App
bash
Copy code
streamlit run streamlit_app/app.py
2️⃣ Open the Dashboard
Once the app starts, your browser will automatically open:

arduino
Copy code
http://localhost:8501
If it doesn't open automatically, you can manually paste the URL into your browser.




---


## Connect With Me
<p align="center">Made with passion, data, and Netflix vibes by <b>Zarnain</b></p> <p align="center"> <a href="https://www.linkedin.com/in/zarnain-723a31325"> <img src="https://img.shields.io/badge/LinkedIn-Zarnain-blue?style=for-the-badge&logo=linkedin&logoColor=white"/> </a> <a href="https://github.com/ScriptingSiren13"> <img src="https://img.shields.io/badge/GitHub-ScriptingSiren13-black?style=for-the-badge&logo=github"/> </a> </p>

##  Project Overview

A fully interactive Streamlit dashboard designed to explore Netflix content using:

- Dynamic visuals  
- Clean tab-based navigation  
- Netflix-themed UI  
- Light/Dark mode switching  

It answers key analytical questions about global Netflix trends and provides rich insights into genres, ratings, durations, countries, and more.

---



#  Text Cleaner Agent


A hybrid text-cleaning tool that uses **rule-based preprocessing** + **LLM polishing** to clean messy text while preserving meaning.  
Built with FastAPI (backend) + Streamlit (UI).


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/FastAPI-Ready-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4.1-6A5ACD?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-1.0.0-yellow?style=for-the-badge">
</p>



A lightweight Text Cleaning Agent built using FastAPI, Streamlit, and OpenAI.  
It takes messy or unstructured text and cleans it using a hybrid approach:  
rule-based preprocessing followed by LLM-powered polishing.  
Perfect for quickly converting rough text into clean, readable output.


---



##  Features

-  Cleans messy text using a hybrid system (Rule-Based + LLM)
-  Fixes spacing, punctuation, casing, and unnecessary symbols
-  Uses GPT-4.1 for final polishing while preserving original meaning
-  FastAPI backend for text processing
-  Streamlit frontend for a clean and easy UI
-  Shows character count before and after cleaning
-  Clean and modern UI with custom styling
-  Real-time text cleaning with a single click


---



##  Project Structure
```
text-cleaner-agent/
│
├── backend/
│   └── app/
│       ├── cleaner/
│       │   ├── llm_polish.py
│       │   ├── pipeline.py
│       │   ├── rule_based.py
│       │   └── __init__.py
│       │
│       ├── schemas/
│       │   ├── text_schema.py
│       │   └── __init__.py
│       │
│       ├── system_prompt/
│       │   ├── text_cleaner_prompt.txt
│       │   └── __init__.py
│       │
│       ├── routes.py
│       ├── main.py
│       └── __init__.py
│
├── requirements/
│   ├── text_cleaner_Specifications.md
│   └── requirements.txt
│
├── streamlit_app/
│   ├── app.py
│   └── README.md
│
└── README.md
```


---



## Tech Stack Used
**Backend**
 • FastAPI — for building the REST API
 • Pydantic — for validating incoming text
 • Uvicorn — ASGI server to run FastAPI
 • Python 3.10+

**Text Processing**
 • Custom Rule-Based Pipeline
   •spacing cleanup
   •punctuation normalization
   •casing correction
   •symbol cleanup

**LLM Integration**
 • OpenAI API (GPT-4.1) — used for final polishing of cleaned text

**Frontend**
 • Streamlit — simple, fast UI framework
 • Requests — used by Streamlit to call the FastAPI backend


---


 
## How to Run the Project
Follow these steps to run the Text Cleaner Agent locally.

**1️. Clone the Repository**
git clone https://github.com/your-username/text-cleaner-agent.git
cd text-cleaner-agent

**2️. Install Dependencies**
Make sure you are inside the project folder:

pip install -r requirements.txt

**3️. Run the FastAPI Backend**
Navigate to the backend folder:

cd backend
uvicorn app.main:app --reload



If port 8000 is busy, you can run:

uvicorn app.main:app --reload --port 8001


**Backend will run at:**

 http://127.0.0.1:8000/docs
or
 http://127.0.0.1:8001/docs

**4️. Run the Streamlit Frontend**

Open a new terminal window and run:

cd frontend_streamlit
streamlit run app.py


The Streamlit app will open automatically.

---



## How It Works
The Text Cleaner Agent follows a **hybrid pipeline** combining rule-based preprocessing with a final LLM polish.

**1️. Rule-Based Cleaning**
The backend first applies a deterministic pipeline to clean raw messy text.

Includes:
• Extra spacing cleanup
• Symbol and punctuation normalization
• Sentence casing correction
• Removal of repeated characters

**2. LLM Polishing**
After rule-based cleaning, the cleaned text is sent to GPT-4.1 with a custom system prompt to:
• improve clarity
• fix grammar
• ensure natural flow
• remove noise while keeping meaning

**3.  Final Output**
Streamlit displays:
• cleaned text
• before/after character counts
• polished formatting inside a beautiful rounded UI box


---



## Output Preview

### Before Cleaning
![Before Screenshot](images/screenshot1.png)

### After Cleaning
![After Screenshot](images/screenshot2.png)


---

##  Connect With Me

If you liked this project or found it helpful, feel free to connect with me!

<p align="center">
  <a href="https://github.com/ScriptingSiren13">
    <img src="https://img.shields.io/badge/GitHub-ScriptingSiren13-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/in/zarnain-723a31325">
    <img src="https://img.shields.io/badge/LinkedIn-Zarnain-blue?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>

<p align="center">
  Made by Zarnain
</p>


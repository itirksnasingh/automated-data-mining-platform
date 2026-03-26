# 🚀 Automated Data Mining & Insight Generation Platform

🔗 **Live App:** https://automated-data-mining-platform.streamlit.app  
🔗 **GitHub Repository:** https://github.com/itirksnasingh/automated-data-mining-platform

---

## 📌 Overview

The **Automated Data Mining & Insight Generation Platform** is an intelligent analytics system that allows users to upload datasets and automatically discover patterns, insights, and relationships within the data.

The platform integrates concepts from **Data Warehousing & Data Mining** and **Advanced Python** to build a real-world mini analytics platform capable of:

- analyzing datasets
- discovering hidden patterns
- generating insights automatically
- visualizing relationships
- producing analytical reports

This project demonstrates how **data mining algorithms and Python-based data engineering** can be combined to transform raw data into actionable knowledge.

---

# ✨ Key Features

### 📂 Dataset Upload & Automatic Analysis
Users can upload any dataset and the platform automatically begins analyzing the structure and contents.

### 🧠 Dataset Intelligence Engine
Automatically detects:

- number of rows and columns
- numerical vs categorical attributes
- dataset structure

### 📊 Data Quality Analyzer
Generates a dataset quality report including:

- missing values
- duplicate records
- potential data issues
- data cleaning suggestions

### 🔍 Exploratory Data Analysis (EDA)
Performs statistical exploration using:

- descriptive statistics
- distribution analysis
- correlation insights
- interactive charts

### 🤖 Pattern Discovery Engine

Implements important **data mining algorithms**:

**Clustering (K-Means)**  
Groups similar data points to identify hidden patterns.

**Association Rule Mining**  
Discovers relationships between items or features in datasets.

Example:


Laptop → Mouse
Confidence: 0.74


### 🧾 Automated Insight Generation

The system automatically generates human-readable insights such as:

- high-value customer segments
- common feature relationships
- important statistical observations

### 🌐 Relationship Network Visualization

Displays discovered relationships using a **network graph**, helping users visually understand connections within the data.

### 📑 Analytics Report Generation

The platform can generate a **downloadable PDF analytics report** including:

- dataset overview
- discovered patterns
- clustering results
- generated insights
- recommendations

---

# 🏗 System Architecture


User Dataset Upload
│
▼
Dataset Intelligence Engine
│
▼
Data Quality Analysis
│
▼
Exploratory Data Analysis
│
▼
Pattern Discovery Engine
(Clustering + Association Rules)
│
▼
Insight Generator
│
▼
Visualization Dashboard
│
▼
Analytics Report Generation


---

# 🛠 Tech Stack

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- MLxtend

### Visualization
- Matplotlib
- Seaborn
- Plotly
- NetworkX

### Web Dashboard
- Streamlit
- Streamlit Option Menu

### Reporting
- FPDF

---

# 📊 Dashboard Features

The interactive dashboard provides the following modules:

- Dataset Intelligence
- Data Quality Analysis
- Exploratory Analysis
- Pattern Discovery
- Relationship Graph Visualization
- Generated Insights
- Report Export

---

# 📸 Example Outputs

*(Add screenshots here)*

### Dashboard Overview
![Dashboard](images/dashboard.png)

### Pattern Relationship Network
![Network Graph](images/network.png)

### Generated Insights Panel
![Insights](images/insights.png)

---

# 📚 Concepts Demonstrated

This project integrates topics from:

### Data Warehousing & Data Mining

- Data preprocessing
- Data profiling
- Exploratory data analysis
- Clustering algorithms
- Association rule mining
- Pattern discovery
- Insight generation

### Advanced Python

- Pandas data wrangling
- NumPy numerical computation
- modular project architecture
- decorators for performance tracking
- logging systems
- data pipelines
- visualization using Python libraries

---

# 💡 What I Learned

While building this project, I learned:

- how to design a **modular Python analytics system**
- implementing **machine learning algorithms for pattern discovery**
- performing **large-scale data preprocessing using Pandas**
- building **interactive dashboards using Streamlit**
- generating **automated insights from datasets**
- deploying a **live analytics platform using Streamlit Cloud**
- managing code using **Git and GitHub**

---

# 🚀 How to Run Locally

Clone the repository:

```bash
git clone https://github.com/itirksnasingh/automated-data-mining-platform.git
cd automated-data-mining-platform

Create virtual environment:

python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run src/dashboard/intelligence_console.py
🌍 Live Deployment

The project is deployed using Streamlit Cloud.

🔗 Live Application:
https://automated-data-mining-platform.streamlit.app

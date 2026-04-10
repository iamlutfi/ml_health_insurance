# Machine Learning Health Insurance

> End-to-end machine learning projects — from data exploration to deployment with Streamlit.

---

## Project Objectives

This project was created as a personal learning tool to understand the end-to-end ML workflow, including:

- Exploratory Data Analysis (EDA)
- Preprocessing & feature engineering
- Model training and evaluation
- Implementing clean code within the context of an ML project
- A clean and organized ML project structure
- Model deployment using Streamlit *(final stage)*

---

## Project Structure

```
ml_health_insurance/
├── notebooks/
│ ├── 00_EDA.ipynb # Exploratory Data Analysis
│ └── 01_Split_Preprocessing.ipynb # Split data & preprocessing
├── main.py # Application entry point
├── pyproject.toml # Project configuration & dependencies
├── uv.lock # Lock file (uv package manager)
├── .python-version # Python version used
├── .gitignore
└── README.md
```

> **Note:** The structure will evolve as the project progresses. Folders such as `src/`, `models/`, and `app/` will be added in later phases.

---

## Setup & Running the Project

This project uses [`uv`](https://github.com/astral-sh/uv) as its package manager.

```bash
# Clone repository
git clone https://github.com/username/ml_health_insurance.git
cd ml_health_insurance

# Install dependencies
uv sync
```
---

## Dataset

The dataset used is health insurance data containing demographic information and insurance premium costs.

**Key features:**

| Feature | Type | Description |
|---|---|---|
| `age` | Numeric | Policyholder age |
| `sex` | Categorical | Gender |
| `bmi` | Numeric | Body Mass Index |
| `children` | Numeric | Number of dependents |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Region of residence |
| `charges` | Numeric | Insurance cost *(target)* |

---

## Tech Stack

| Components | Tools |
|---|---|
| Package Manager | `uv` |
| Exploration & Modeling | `pandas`, `numpy`, `scikit-learn` |
| Visualization | `matplotlib`, `seaborn` |
| Deployment *(planned)* | `streamlit` |
| Notebook | `jupyter` |

---

## License

MIT License — feel free to use for educational purposes.
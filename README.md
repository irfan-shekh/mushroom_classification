<div align="center">

# 🍄 MycoSense AI — Mushroom Classification System

**A production-ready Django & Machine Learning web application that accurately classifies wild mushrooms as Edible or Deadly Poisonous based on 22 morphological & sensory characteristics.**

[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Accuracy](https://img.shields.io/badge/Test_Accuracy-99.75%25-10B981?style=for-the-badge&logo=target&logoColor=white)](#-machine-learning-architecture)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

[Quick Start](#-quick-start) • [Features](#-features) • [ML Architecture](#-machine-learning-architecture) • [Project Structure](#-project-structure) • [Running the App](#-running-the-application) • [Testing](#-testing--validation)

</div>

---

## 🌟 Overview

Identifying wild mushrooms is historically difficult and dangerous; many poisonous species closely mimic edible varieties. **MycoSense AI** bridges morphological taxonomy and machine learning by applying **Principal Component Analysis (PCA)** dimensionality reduction coupled with an ensemble **Random Forest Classifier (300 estimators)** to evaluate physical mushroom traits with **99.75% accuracy**.

The accompanying web interface provides an immersive, bioluminescent glassmorphic dark interface with real-time field validation, progress indicators, 1-click test specimen presets, and asynchronous classification with confidence scores.

---

## ✨ Features

- **🎯 High-Precision Classification**: Trained on the Audubon Society Field Guide mushroom database, achieving 100% training accuracy and 99.75% holdout test accuracy.
- **🧬 PCA Dimensionality Reduction**: Compresses 22 categorical features into 7 orthogonal principal components, eliminating collinearity and optimizing inference latency (<10ms).
- **🎨 Modern Glassmorphic Dark UI**: Designed with a bioluminescent mycology aesthetic, custom dropdown wrappers, glowing status indicators, and responsive flex/grid layouts.
- **⚡ Instant AJAX Inference**: Asynchronous form submission providing immediate in-place classification without full page reload flickers.
- **📊 Real-time Confidence Scoring**: Returns model certainty percentage for both edible and poisonous predictions.
- **🪄 1-Click Specimen Presets**: Pre-configured sample presets (`Sample Edible` and `Sample Poisonous`) for instantaneous testing and demonstration.
- **📁 Multi-Path Execution**: Run seamlessly directly from the project root (`python app.py`, `python manage.py runserver`, or `run.bat`) or from within the inner Django app folder.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.8+** (Compatible with Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13)
- **pip** package installer

### 2. Clone the Repository
```bash
git clone https://github.com/irfan-shekh/mushroom_classification.git
cd mushroom_classification
```

### 3. Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS / Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Running the Application

You can start the application using any of the following convenient entry points:

### Option A: Quick Application Runner (Recommended)
```bash
python app.py
```
*Optional custom port:* `python app.py 8080`

### Option B: Standard Django Management Command
```bash
python manage.py runserver
```

### Option C: 1-Click Windows Launcher
Double-click [`run.bat`](file:///c:/D%20drive/ML_Projects/mushroom_classification/run.bat) or run from Command Prompt:
```cmd
run.bat
```

### Option D: From the Django Subdirectory
```bash
cd Code/mysite
python manage.py runserver
```

Once started, open your web browser and navigate to:
👉 **`http://127.0.0.1:8000`**

---

## 📊 Machine Learning Architecture

```
┌─────────────────────────────────┐
│  22 Categorical Characteristics  │
│  (Cap, Odor, Gills, Stalk, etc) │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│     Categorical LabelEncoder    │
│    (Standardized Numerical Map) │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│      PCA Dimensionality         │
│  (Reduces 22 dims -> 7 Comps)   │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│     Random Forest Classifier    │
│  (300 Estimators, Ensemble ML)  │
└────────────────┬────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
   [ 0 = Edible ]    [ 1 = Poisonous ]
```

### Evaluated Morphological Traits (22 Dimensions)

| Category | Characteristics Evaluated |
| :--- | :--- |
| **Cap Morphology** | Cap Shape, Cap Surface, Cap Color, Bruises Status |
| **Sensory & Gills** | Odor, Gill Attachment, Gill Spacing, Gill Size, Gill Color |
| **Stalk Anatomy** | Stalk Shape, Stalk Root, Surface Above/Below Ring, Color Above/Below Ring |
| **Veil & Spores** | Veil Type, Veil Color, Ring Number, Ring Type, Spore Print Color |
| **Ecology** | Population Distribution, Natural Habitat |

### Performance Metrics
- **Dataset Size**: 8,124 mushroom specimens
- **Target Distribution**: 4,208 Edible (51.8%) / 3,916 Poisonous (48.2%)
- **Training Accuracy**: `100.00%`
- **Testing Accuracy (20% holdout)**: `99.75%`
- **Inference Time**: `< 10ms`

---

## 📁 Project Structure

```
mushroom_classification/
│
├── manage.py                    # Root Django management entry point
├── app.py                       # Root launcher & CLI test runner
├── test_models.py               # Root ML model validation suite
├── run.bat                      # 1-click Windows batch launcher
├── requirements.txt             # Python project dependencies
├── README.md                    # Project documentation
│
└── Code/
    ├── mushrooms.csv            # Original Audubon Society dataset
    ├── Mushrooms.ipynb          # Exploratory Data Analysis & Model Training
    └── mysite/                  # Django project application root
        ├── manage.py            # Inner Django management script
        ├── requirements.txt     # Pinned legacy dependencies
        ├── db.sqlite3           # Local development SQLite database
        ├── mysite/              # Core Django project config
        │   ├── settings.py      # App settings & static configs
        │   ├── urls.py          # Master routing configuration
        │   ├── wsgi.py          # WSGI deployment hook
        │   └── asgi.py          # ASGI asynchronous entry point
        └── polls/               # Main mushroom classification app
            ├── views.py         # Prediction handler & AJAX endpoint
            ├── urls.py          # Polls routing
            ├── Mushs.pickle     # Trained Random Forest classifier
            ├── MushsPCA.pickle  # Trained PCA transformation model
            ├── static/          # Static assets directory
            └── templates/
                └── index.html   # Glassmorphic responsive frontend
```

---

## 🧪 Testing & Validation

The project includes an automated test suite verifying pickle model integrity, PCA transformation matrices, and both edible and poisonous classification pathways.

### Run Tests via Root Test Runner
```bash
python test_models.py
```

### Or Run via `app.py`
```bash
python app.py test
```

**Expected Output:**
```text
🍄 Testing Mushroom Classification Models
==================================================
✅ Model files found
📦 Loading models...
✅ Models loaded successfully

🧪 Testing with sample data...
📊 Input shape: (1, 22)
🔄 PCA transformed shape: (1, 7)
🔮 Raw prediction: [0]
✅ Prediction: EDIBLE

🧪 Testing with poisonous characteristics...
☠️ Prediction: POISONOUS

✅ All tests completed successfully!
```

---

## 🛠 Tech Stack

- **Backend Framework**: [Django 4.2+ / 5.x](https://www.djangoproject.com/)
- **Machine Learning**: [scikit-learn](https://scikit-learn.org/), [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/), [joblib](https://joblib.readthedocs.io/)
- **Frontend**: Vanilla HTML5, CSS3 Glassmorphism, Modern JavaScript (ES6+ Fetch API)
- **Typography & Icons**: [Google Fonts (Outfit & Plus Jakarta Sans)](https://fonts.google.com/), [Font Awesome 6](https://fontawesome.com/)
- **Production Server**: [Gunicorn](https://gunicorn.org/) / WSGI

---

## 🔒 Security & Best Practices

- **CSRF Protection**: Integrated Django Cross-Site Request Forgery tokens on all POST requests and AJAX headers.
- **Model Deserialization**: Pre-compiled and verified model pickles compatible with modern scikit-learn architectures.
- **UTF-8 Console Resiliency**: Auto-reconfigured standard outputs on Windows terminals (`cp1252` fallback protection).

---

## ⚠️ Disclaimer

> [!CAUTION]
> **Important Safety Notice**: This application is developed for educational, exploratory, and scientific research purposes only. **Never consume wild mushrooms based on automated machine learning predictions.** Many poisonous mushroom species are lethal and can be indistinguishable from edible varieties without microscopic spore analysis or professional mycological expertise.

---

## 👤 Author

**Irfan Shekh**
- GitHub: [@irfan-shekh](https://github.com/irfan-shekh)
- Repository: [mushroom_classification](https://github.com/irfan-shekh/mushroom_classification)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

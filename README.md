# Student Performance Indicator - End-to-End Machine Learning Project

## Project Overview

The **Student Performance Indicator** is an end-to-end Machine Learning project developed to predict a student's **Math Score** based on different demographic, educational, and academic factors.

The project demonstrates the complete Machine Learning lifecycle, starting from data ingestion and preprocessing to model training, model evaluation, model saving, and deployment using a **Flask web application**.

The project follows a modular and reusable structure with separate components for data ingestion, data transformation, model training, prediction, logging, exception handling, and utility functions.

## Problem Statement

Student performance can be influenced by several factors such as gender, ethnicity, parental level of education, lunch type, test preparation, reading score, and writing score.

The objective of this project is to build a Machine Learning model that can predict a student's **Math Score** using these available features.

The project also compares multiple regression algorithms and selects the best-performing model based on the **R² score**.

## Dataset

The project uses a student performance dataset containing information related to students' demographic and academic characteristics.

### Features Used

* **Gender**
* **Race/Ethnicity**
* **Parental Level of Education**
* **Lunch**
* **Test Preparation Course**
* **Reading Score**
* **Writing Score**

### Target Variable

* **Math Score**

The dataset is divided into training and testing datasets using an **80:20 train-test split** with a fixed random state for reproducibility.

## Technologies Used

### Programming Language

* Python

### Libraries

* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* XGBoost
* CatBoost
* Dill

### Web Framework

* Flask

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

## Machine Learning Models

Multiple regression algorithms are trained and evaluated to identify the best-performing model.

The project currently includes:

1. Random Forest Regressor
2. Decision Tree Regressor
3. Gradient Boosting Regressor
4. Linear Regression
5. K-Neighbors Regressor
6. XGBoost Regressor
7. CatBoost Regressor
8. AdaBoost Regressor

The models are evaluated using the **R² (R-squared) score**.

The model with the highest R² score is selected as the best model and saved for future predictions.

## Data Preprocessing

The project uses a Scikit-learn preprocessing pipeline.

### Numerical Features

The numerical features are:

* Reading Score
* Writing Score

The numerical preprocessing pipeline performs:

1. Missing value handling using **median imputation**
2. Feature scaling using **StandardScaler**

### Categorical Features

The categorical features are:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course

The categorical preprocessing pipeline performs:

1. Missing value handling using **most-frequent imputation**
2. Categorical encoding using **OneHotEncoder**
3. Unknown categories are handled using `handle_unknown="ignore"`

A `ColumnTransformer` is used to combine the numerical and categorical preprocessing pipelines.

The fitted preprocessor is saved as:

```text
artifacts/preprocessor.pkl
```

## Machine Learning Workflow

The complete workflow of the project is:

```text
Dataset
   ↓
Data Ingestion
   ↓
Train-Test Split
   ↓
Data Transformation
   ↓
Handling Missing Values
   ↓
Categorical Encoding
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Saving
   ↓
Prediction Pipeline
   ↓
Flask Web Application
   ↓
Student Math Score Prediction
```

## Model Evaluation

The project compares the performance of different regression algorithms using the **R² score**.

The training process evaluates all configured models and identifies the model with the highest R² score.

Example format for the final results:

| Model                       |       R² Score |
| --------------------------- | -------------: |
| Random Forest Regressor     | Add your score |
| Decision Tree Regressor     | Add your score |
| Gradient Boosting Regressor | Add your score |
| Linear Regression           | Add your score |
| K-Neighbors Regressor       | Add your score |
| XGBoost Regressor           | Add your score |
| CatBoost Regressor          | Add your score |
| AdaBoost Regressor          | Add your score |

The best-performing model is selected automatically based on the highest R² score.

## Project Structure

```text
ML-projects/
│
├── .ebextensions/
│
├── Note book/
│   └── data/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   └── __init__.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── application.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

The repository uses separate `src/components` and `src/pipeline` directories for the ML workflow and prediction functionality.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lokeshnagasaitungala79-creator/ML-projects.git
```

### 2. Navigate to the Project Directory

```bash
cd ML-projects
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

The repository currently includes NumPy, Pandas, Seaborn, Matplotlib, Scikit-learn, CatBoost, Dill, XGBoost, Flask, and the local package installation.

## How to Run

### Step 1: Prepare the Dataset

Place the student dataset in the appropriate project data directory.

The training pipeline expects the student dataset containing the required columns such as:

```text
gender
race_ethnicity
parental_level_of_education
lunch
test_preparation_course
math_score
reading_score
writing_score
```

### Step 2: Run the Training Pipeline

The project performs:

```text
Data Ingestion
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Best Model Selection
```

The trained model and preprocessing object are stored in the `artifacts` directory.

```text
artifacts/model.pkl
artifacts/preprocessor.pkl
```

### Step 3: Start the Flask Application

Run:

```bash
python app.py
```

The Flask application starts the web server.

Open the URL displayed in the terminal, normally:

```text
http://127.0.0.1:5000/
```

## Flask Web Application

The trained Machine Learning model is integrated with a **Flask web application**.

The application provides a web interface where users can enter student information and receive a predicted Math Score.

### Input Features

The web application accepts:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Reading Score
* Writing Score

The Flask application passes these inputs through the prediction pipeline, which loads the saved preprocessing object and trained model before generating the prediction.

The application contains routes for the home page and prediction functionality.

### Prediction Process

```text
User Input
    ↓
Flask Application
    ↓
CustomData
    ↓
Prediction Pipeline
    ↓
Preprocessor
    ↓
Trained ML Model
    ↓
Predicted Math Score
    ↓
Display Result
```

## Results

The project successfully implements an end-to-end Machine Learning workflow for predicting student Math Scores.

The system:

* Processes raw student data
* Performs train-test splitting
* Handles missing values
* Encodes categorical features
* Scales numerical features
* Trains multiple regression models
* Compares model performance
* Selects the best-performing model
* Saves the trained model
* Provides predictions through a Flask web application

### Final Model Performance

Add your actual result here after running the project:

```text
Best Model:
R² Score:
```

For example:

```text
Best Model: __________________
R² Score: __________________
```

The model selection logic in the project automatically chooses the model with the highest R² score.

## Screenshots

Add screenshots of your working application here.

### Home Page

```text
![Home Page](screenshots/home.png)
```

### Prediction Page

```text
![Prediction Page](screenshots/prediction.png)
```

### Prediction Result

```text
![Prediction Result](screenshots/result.png)
```

> Create a `screenshots` folder in the repository and place your actual screenshots inside it.

Recommended screenshots:

1. Home page
2. Student input form
3. Prediction result
4. Model evaluation/output

## Future Improvements

The following improvements can be added in future versions:

* Deploy the application to a cloud platform.
* Add a more interactive dashboard for student performance analysis.
* Add additional Machine Learning and ensemble models.
* Perform advanced hyperparameter tuning.
* Add cross-validation for more reliable model evaluation.
* Improve the user interface and responsiveness.
* Add prediction confidence or uncertainty information where appropriate.
* Add automated testing.
* Add CI/CD using GitHub Actions.
* Containerize the application using Docker.
* Improve data validation and input error handling.
* Add monitoring for the deployed Machine Learning model.

## Conclusion

The **Student Performance Indicator** project demonstrates how Machine Learning can be developed and deployed as a complete application rather than being limited to a Jupyter Notebook.

The project covers the complete workflow from **data ingestion and preprocessing to model training, evaluation, model persistence, and Flask-based deployment**.

This project helped demonstrate practical skills in Python, Pandas, NumPy, Scikit-learn, ensemble learning, XGBoost, CatBoost, Flask, Git, and GitHub.

## Author

**Lokesh Naga Sai Tungala**

GitHub:
https://github.com/lokeshnagasaitungala79-creator

## License

This project is created for educational and learning purposes.

# Credit Scoring Model

**CodeAlpha Machine Learning Internship — Project 1**

## About the Project
This beginner machine learning project demonstrates binary classification using sample customer financial data. It uses Logistic Regression to predict a customer's creditworthiness.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Logistic Regression

## Dataset Features
- `income` — sample customer income
- `debt` — sample customer debt
- `payment_history` — illustrative payment-history indicator
- `credit_history_years` — years of credit history
- `creditworthy` — target label (1 or 0)

## Project Files
- `create_dataset.py` — creates and saves the sample dataset.
- `credit_data.csv` — sample customer data.
- `train_model.py` — loads the data, trains the model, evaluates training accuracy, and predicts a sample customer's class.
- `.gitignore` — excludes files that should not be tracked, such as the local virtual environment.

## How to Run

Install the required libraries:

`pip install pandas scikit-learn`

Run the scripts from the project directory:

`python create_dataset.py`

`python train_model.py`

## Current Results
The model successfully trains and generates a prediction. The reported training accuracy was 100% on five sample rows.

**Important:** This is training accuracy, not test accuracy. The dataset is too small to establish reliable performance on unseen customers.

## Limitations
This is an educational prototype with illustrative data. It is not suitable for real credit decisions. A larger dataset, proper testing, and fairness and privacy checks would be required for real-world use.

## Author
AI Software Engineering Student

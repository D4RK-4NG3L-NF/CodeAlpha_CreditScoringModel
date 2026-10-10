
# Credit Scoring Model

## Overview
This project was developed as part of my CodeAlpha Machine Learning Internship. It uses Logistic Regression to classify fictional customer records into two creditworthiness categories.

## Features
- Income
- Debt
- Payment history
- Credit history duration

## Technologies Used
- Python
- Pandas
- Scikit-learn
- VS Code
- Git and GitHub

## Dataset
The dataset contains 30 fictional customer records and four input features. The target column, `creditworthy`, contains binary labels:
- `1`: Creditworthy class
- `0`: Not-creditworthy class

## Model
Logistic Regression is trained using an 80/20 train-test split.

- Training records: 24
- Testing records: 6
- Test accuracy: 83.33% on this small test split

## How to Run
Install the required libraries:

```bash
pip install pandas scikit-learn
```

Create the dataset:

```bash
python create_dataset.py
```

Train and evaluate the model:

```bash
python train_model.py
```

## Limitations
This is an educational project using a small, synthetic dataset. The test result is not a reliable estimate of real-world performance. This model must not be used to make actual lending or credit decisions.

## Learning Outcomes
- Creating a dataset with Pandas
- Preparing input features and target labels
- Training a Logistic Regression model
- Splitting data into training and testing sets
- Evaluating predictions with accuracy, a confusion matrix, and a classification report

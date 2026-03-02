#About this dataset
*Telcom Customer Churn*<br>

Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The raw data contains 7043 rows (customers) and 21 columns (features).

import libraries
"""

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

"""## read & understand data"""

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.shape

pd.set_option('display.max_columns', None) # to display all columns
df.head()

df.isna().sum()

df.duplicated().sum()

df.info

# check data types and validation
df.dtypes

"""## Data preprocessing & Cleaning"""

# change datatypes of specific columns to fit our purpose

# Fix TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)


# Convert Yes / No columns to Boolean
yes_no_cols = [
    'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Churn'
]

df[yes_no_cols] = df[yes_no_cols].replace({
    'Yes': True,
    'No': False
})


# Handle "No internet service" / "No phone service"
df['MultipleLines'] = df['MultipleLines'].replace({
    'Yes': True,
    'No': False,
    'No phone service': False
})

internet_cols = [
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

df[internet_cols] = df[internet_cols].replace({
    'No internet service': False
})


# Gender as category (keep text OR optional Boolean)
df['gender'] = df['gender'].astype('category')

# map 0 , 1 for SeniorCitizen column into "Senior" and "Non-Senior"
df['SeniorCitizen'] = df['SeniorCitizen'].map({
    1: 'Senior',
    0: 'Non-Senior'
})


# Keep multi-category columns as text
cat_cols = ['InternetService', 'Contract', 'PaymentMethod']
df[cat_cols] = df[cat_cols].astype('category')

for col in df.columns:
    if df[col].dtype != 'int64' and df[col].dtype != 'float64':
        print(f'{col} : {df[col].unique()}')

# check outliers

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

for col in num_cols:
    plt.figure(figsize=(4,3))
    plt.boxplot(df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

"""the upper boxplot shows that Pricing structure and customer usage are stable"""

df.describe()

"""##Data visualization"""

# this shows if the churn is balanced or not.
sns.countplot(x='Churn', data=df)
plt.title('Customer Churn Distribution')
plt.show()

# this shows High charges leads to higher churn risk
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges by Churn')
plt.show()

df.to_csv(
    "churn_cleaned.csv",
    index=False,
    encoding="utf-8"
)

"""## Classification Machine Learning model
### Churn Prediction Model
using logistic regression




"""

# prepare data to fit with ML
df_ml= df.copy()
# Binary categorical columns (Yes / No)
binary_cols = [
    'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Churn'
]

df_ml[binary_cols] = df_ml[binary_cols].replace({'Yes': 1, 'No': 0})


# Gender (Male / Female)
df_ml['gender'] = df_ml['gender'].map({'Male': 1, 'Female': 0})


# Columns with "No internet service" / "No phone service"
service_cols = ['MultipleLines']

df_ml[service_cols] = df_ml[service_cols].replace({
    'Yes': 1,
    'No': 0,
    'No phone service': 0
})


internet_related_cols = [
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

df_ml[internet_related_cols] = df_ml[internet_related_cols].replace({
    'No internet service': 0
})


# One-Hot Encoding (multi-category)
multi_cat_cols = ['InternetService', 'Contract', 'PaymentMethod']

df_ml = pd.get_dummies(df_ml, columns=multi_cat_cols, drop_first=True)


# Drop customerID (not useful for ML)
df_ml.drop(columns=['customerID', "SeniorCitizen"], inplace=True)

X = df_ml.drop('Churn', axis=1)
y = df_ml['Churn']
print('shape after preprocessing: ',df_ml.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # keeps churn ratio balanced
)

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

scaler = StandardScaler()
X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

cm = confusion_matrix(y_test, y_pred)

cm_table = pd.DataFrame(
    cm,
    index=['Actual Stay', 'Actual Churn'],
    columns=['Predicted Stay', 'Predicted Churn']
)

print(cm_table)
print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
from sklearn.metrics import confusion_matrix

"""model accuracy is : 84.42% , this means that the model has a strong ability to distinguish between customers who churn and those who stay."""

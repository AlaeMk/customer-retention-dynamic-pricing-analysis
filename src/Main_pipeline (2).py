import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_curve, roc_auc_score

# =========================================================================
# ----- WEEK 1: DATA PREPROCESSING -----
# =========================================================================
print("--- Starting Week 1: Data Preprocessing ---")

# 1. Loading the Excel file 
path = r"C:\Users\alaem\Downloads\churn-hotel-infotact\raw\hotel_bookings.xlsx"
df = pd.read_excel(path)

# 2. Handling Missing Values
df['agent'] = df['agent'].fillna(0)
df['company'] = df['company'].fillna(0)
print("Missing values in 'agent' and 'company' successfully handled.")

# 3. Outlier Treatment: Average Daily Rate (ADR)
q_high = df['adr'].quantile(0.999)
df = df[(df['adr'] >= 0) & (df['adr'] < q_high)]
print(f"Outliers treated. Data shape after filtering ADR: {df.shape}")

# 4. Feature Engineering: Total Duration of Stay
df['total_stay'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
print("Feature Engineering completed: 'total_stay' column added.")

# 5. Saving the cleaned dataset
output_path = r"C:\Users\alaem\Downloads\churn-hotel-infotact\clean_data\week1\cleaned_hotel_bookings.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved at: {output_path}\n")


# =========================================================================
# ----- WEEK 2: EXPLORATORY DATA ANALYSIS (EDA) -----
# =========================================================================
print("--- Starting Week 2: Exploratory Data Analysis ---")

# 1. Select numeric variables to find correlations with cancellations (is_canceled)
numeric_cols = [
    'is_canceled', 'lead_time', 'total_stay', 'adr', 
    'is_repeated_guest', 'previous_cancellations', 
    'previous_bookings_not_canceled', 'booking_changes'
]
corr_matrix = df[numeric_cols].corr()

# 2. Visualizing the Correlation Matrix using Seaborn and Matplotlib
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix: Identifying Key Churn Drivers", fontsize=14, pad=15)
plt.tight_layout()

# 3. Saving the plot 
plot_path = r"C:\Users\alaem\Downloads\churn-hotel-infotact\clean_data\week2\cancellation_correlation_matrix.png"
os.makedirs(os.path.dirname(plot_path), exist_ok=True)
plt.savefig(plot_path)
print(f"Week 2 Visualization generated and saved at: {plot_path}\n")


# =========================================================================
# ----- WEEK 3: BASELINE PREDICTIVE MODELING (Scikit-Learn) -----
# =========================================================================
print("--- Starting Week 3: Baseline Predictive Modeling ---")

# 1. Selecting numerical features
features_cols = [
    'lead_time', 'total_stay', 'adr', 'is_repeated_guest', 
    'previous_cancellations', 'previous_bookings_not_canceled', 'booking_changes'
]

X = df[features_cols]
y = df['is_canceled']

# 2. Split data: 80% Train and 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- Data Splitting Done ---")
print(f"Train data size: {X_train.shape[0]} rows")
print(f"Test data size: {X_test.shape[0]} rows\n")

# 3. Model Initialization (Logistic Regression)
model = LogisticRegression(max_iter=1000)

# 4. Model Training (Fit)
print("Training the model... Please wait...")
model.fit(X_train, y_train)

# 5. Making Predictions on the test data
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]
# 6. Model Accuracy & Evaluation Report
accuracy = accuracy_score(y_test, y_pred)
print("\n================ EVALUATION REPORT ================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Performance Metrics:")
print(classification_report(y_test, y_pred))
# 1. Calcul ROC-AUC Score
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC Score: {roc_auc * 100:.2f}%")
print("===================================================\n")

# 2. Drawing the ROC-AUC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.tight_layout()

# 3. Saving the Plot Image
roc_plot_path = r"C:\Users\alaem\Downloads\churn-hotel-infotact\clean_data\week3\roc_auc_curve.png"
os.makedirs(os.path.dirname(roc_plot_path), exist_ok=True)
plt.savefig(roc_plot_path)
print(f"ROC-AUC Plot generated and saved at: {roc_plot_path}")
print("===================================================\n")

# -------------------------------------------------------------------------
# 🌟 [الزيادة الجديدة]: حفظ بيانات الـ Machine Learning في CSV للـ Dashboard
# -------------------------------------------------------------------------
print("--- Saving ML Predictions for Power BI ---")

# n-sn3ou DataFrame jdid fih l-klyonat mta3 l-imti7an (X_test)
df_predictions = X_test.copy()
df_predictions['Churn_Probability'] = y_pred_proba

# n-zydou el-column mta3 el-79i9a (Actual Churn)
df_predictions['Actual_Is_Canceled'] = y_test

# n-zydou el-column mta3 t-wa99o3at el-Model (Predicted Churn)
df_predictions['Predicted_Is_Canceled'] = y_pred

# n-sayvohom fi folder esmou week3
ml_output_path = r"C:\Users\alaem\Downloads\churn-hotel-infotact\clean_data\week3\week3_model_predictions.csv"
os.makedirs(os.path.dirname(ml_output_path), exist_ok=True)
df_predictions.to_csv(ml_output_path, index=False)

print(f"ML Predictions successfully saved at: {ml_output_path}")
print("Project Pipeline Executed Successfully from Week 1 to Week 3!\n")

# =========================================================================
# ----- DISPLAY ALL VISUALIZATIONS AT THE VERY END -----
# =========================================================================
print("Opening the visualization window...")
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score, roc_curve,
    precision_recall_curve, average_precision_score, ConfusionMatrixDisplay
)

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

pd.set_option("display.max_columns", 100)





df = pd.read_csv("sample_data.csv")
df




NUMERICAL_FEATURES = [

]

CATEGORICAL_FEATURES = [

]

TARGET = "is_fraud"

ALL_FEATURES = NUMERICAL_FEATURES + CATEGORICAL_FEATURES
print(f"{len(NUMERICAL_FEATURES)} numerical features, {len(CATEGORICAL_FEATURES)} categorical features")



print("Missing values per column:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

fraud_rate = df[TARGET].mean()
print(f"\nOverall fraud rate: {fraud_rate:.3%}")

fig, ax = plt.subplots()
df[TARGET].value_counts().plot(kind="bar", ax=ax, color=["#4C72B0", "#C44E52"])
ax.set_xticklabels(["Non Fraud (0)", "Fraud (1)"], rotation=0)
ax.set_title("Class Balance")
ax.set_ylabel("Count")
plt.show()


fig, axes = plt.subplots(2, 3, figsize=(16, 8))
num_subset = ["postal_code_distance", "velocity_total_txn_48h", "velocity_amount_24h",
              "auth_count_24h", "minutes_since_last_auth", "mobile_zip_distance_6m"]

for ax, col in zip(axes.ravel(), num_subset):
    sns.histplot(data=df, x=col, hue=TARGET, bins=40, stat="density",
                 common_norm=False, ax=ax, palette=["#4C72B0", "#C44E52"])
    ax.set_title(col)

plt.tight_layout()
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(14, 10))
cat_subset = ["region_indicator", "cvv_outcome_code", "ecommerce_outcome_code", "arqc_result_code"]

for ax, col in zip(axes.ravel(), cat_subset):
    rate_by_cat = df.groupby(col)[TARGET].mean().sort_values(ascending=False)
    rate_by_cat.plot(kind="bar", ax=ax, color="#C44E52")
    ax.axhline(fraud_rate, color="black", linestyle="--", linewidth=1, label="overall rate")
    ax.set_title(f"Fraud rate by {col}")
    ax.set_ylabel("Fraud rate")
    ax.legend()

plt.tight_layout()
plt.show()



corr = df[NUMERICAL_FEATURES + [TARGET]].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
ax.set_title("Correlation matrix — numerical features & target")
plt.show()


import xgboost as xgb
print(xgb.__version__)


df_model = df.copy()

# Categorical features: convert to pandas 'category' dtype, NOT string + one-hot
df_model[CATEGORICAL_FEATURES] = df_model[CATEGORICAL_FEATURES].astype("category")
df_model.info()


X = df_model[NUMERICAL_FEATURES + CATEGORICAL_FEATURES]
y = df_model[TARGET]


from sklearn.model_selection import StratifiedGroupKFold

# Baseline: group-safe, but NOT time-safe
sgkf = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)

for train_idx, test_idx in sgkf.split(df_model, y, groups=df_model["account_identifier"]):
    df_train, df_test = df_model.iloc[train_idx], df_model.iloc[test_idx]
    break



model = xgb.XGBClassifier(   
    tree_method="hist",
    enable_categorical=True,
    n_estimators=2000,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    early_stopping_rounds=50,
    eval_metric="logloss",   # or "rmse"/"mae" for regression
)

print(df_model[CATEGORICAL_FEATURES].dtypes)  # should show 'category' for each

model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
print(model.get_booster().feature_types)      # should show 'c' for categorical columns, 'q'/'float' for numeric


results = {
    "Logistic Regression": (y_proba_lr, roc_auc_score(y_test, y_proba_lr), average_precision_score(y_test, y_proba_lr)),
    "Random Forest": (y_proba_rf, roc_auc_score(y_test, y_proba_rf), average_precision_score(y_test, y_proba_rf)),
    "Gradient Boosting": (y_proba_gb, roc_auc_score(y_test, y_proba_gb), average_precision_score(y_test, y_proba_gb)),
}

summary = pd.DataFrame(
    {name: {"ROC-AUC": vals[1], "PR-AUC": vals[2]} for name, vals in results.items()}
).T.sort_values("PR-AUC", ascending=False)
summary


fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for name, (proba, roc_auc, pr_auc) in results.items():
    fpr, tpr, _ = roc_curve(y_test, proba)
    axes[0].plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")

    precision, recall, _ = precision_recall_curve(y_test, proba)
    axes[1].plot(recall, precision, label=f"{name} (AP={pr_auc:.3f})")

axes[0].plot([0, 1], [0, 1], "k--", linewidth=1)
axes[0].set_xlabel("False Positive Rate")
axes[0].set_ylabel("True Positive Rate")
axes[0].set_title("ROC Curves")
axes[0].legend()

axes[1].axhline(y_test.mean(), color="k", linestyle="--", linewidth=1, label="baseline (fraud rate)")
axes[1].set_xlabel("Recall")
axes[1].set_ylabel("Precision")
axes[1].set_title("Precision-Recall Curves")
axes[1].legend()

plt.tight_layout()
plt.show()


best_name = summary.index[0]
best_proba = results[best_name][0]
best_pred = (best_proba >= 0.5).astype(int)

cm = confusion_matrix(y_test, best_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legitimate", "Fraud"])
disp.plot(cmap="Blues", values_format="d")
plt.title(f"Confusion Matrix — {best_name} (threshold=0.5)")
plt.show()

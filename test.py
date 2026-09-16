from sklearn.model_selection import train_test_split

X_tr, X_val, y_tr, y_val = train_test_split(
    X_train, y_train, test_size=0.15, stratify=y_train, random_state=42
)

scale_pos_weight = (y_tr == 0).sum() / (y_tr == 1).sum()
print("scale_pos_weight:", scale_pos_weight)

model = xgb.XGBClassifier(
    tree_method="hist",
    enable_categorical=True,
    n_estimators=2000,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    early_stopping_rounds=50,
    eval_metric="aucpr",       # PR-AUC — more informative than logloss for imbalanced fraud
    scale_pos_weight=scale_pos_weight,
    random_state=42,
)

model.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    verbose=False,
)

print("Best iteration:", model.best_iteration)

y_proba_xgb = model.predict_proba(X_test)[:, 1]

results["XGBoost"] = (
    y_proba_xgb,
    roc_auc_score(y_test, y_proba_xgb),
    average_precision_score(y_test, y_proba_xgb),
)
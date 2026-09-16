from sklearn.metrics import roc_curve, precision_recall_curve, roc_auc_score, average_precision_score

roc_auc = roc_auc_score(y_test, y_proba_xgb)
pr_auc  = average_precision_score(y_test, y_proba_xgb)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

fpr, tpr, _ = roc_curve(y_test, y_proba_xgb)
axes[0].plot(fpr, tpr, label=f"XGBoost (AUC={roc_auc:.3f})")
axes[0].plot([0, 1], [0, 1], "k--", linewidth=1)
axes[0].set_xlabel("False Positive Rate")
axes[0].set_ylabel("True Positive Rate")
axes[0].set_title("ROC Curve")
axes[0].legend()

precision, recall, _ = precision_recall_curve(y_test, y_proba_xgb)
axes[1].plot(recall, precision, label=f"XGBoost (AP={pr_auc:.3f})")
axes[1].axhline(y_test.mean(), color="k", linestyle="--", linewidth=1, label="baseline (fraud rate)")
axes[1].set_xlabel("Recall")
axes[1].set_ylabel("Precision")
axes[1].set_title("Precision-Recall Curve")
axes[1].legend()

plt.tight_layout()
plt.show()
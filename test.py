from sklearn.metrics import roc_auc_score, average_precision_score, classification_report

# 1. Compare metrics across train/val/test
for name, X_, y_ in [("Train", X_tr, y_tr), ("Val", X_val, y_val), ("Test", X_test, y_test)]:
    proba = model.predict_proba(X_)[:, 1]
    auc = roc_auc_score(y_, proba)
    ap  = average_precision_score(y_, proba)
    print(f"{name:5s} | ROC-AUC: {auc:.4f} | PR-AUC: {ap:.4f}")



results_eval = model.evals_result()

epochs = len(results_eval["validation_0"]["aucpr"])
x_axis = range(epochs)

plt.figure(figsize=(10, 5))
plt.plot(x_axis, results_eval["validation_0"]["aucpr"], label="Val")
plt.legend()
plt.ylabel("PR-AUC")
plt.xlabel("Boosting Round")
plt.title("Validation PR-AUC over Training")
plt.axvline(model.best_iteration, linestyle="--", color="gray", label=f"Best iter: {model.best_iteration}")
plt.legend()
plt.show()
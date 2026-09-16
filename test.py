def topk_by_fraction(y_true, y_proba, fraction):
    k = int(len(y_true) * fraction)
    top_k_idx = np.argsort(y_proba)[-k:]
    y_true = np.array(y_true)
    top_k_labels = y_true[top_k_idx]
    precision = top_k_labels.sum() / k
    recall = top_k_labels.sum() / y_true.sum()
    return precision, recall, k

for frac in [0.001, 0.005, 0.01, 0.02]:
    p, r, k = topk_by_fraction(y_test, y_proba_test, frac)
    print(f"Top {frac:.1%} (k={k}): Precision={p:.3f}, Recall={r:.3f}")


    import matplotlib.pyplot as plt
import pandas as pd

# XGBoost supports several importance types: "weight", "gain", "cover"
importance_dict = model.get_booster().get_score(importance_type="gain")

importance_df = pd.DataFrame({
    "feature": list(importance_dict.keys()),
    "importance": list(importance_dict.values())
}).sort_values("importance", ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(importance_df["feature"][:15][::-1], importance_df["importance"][:15][::-1])
plt.xlabel("Gain")
plt.title("Top 15 Feature Importances (Gain)")
plt.tight_layout()
plt.show()

import numpy as np

def topk_precision_recall(y_true, y_proba, k):
    # Get indices of top-k highest probability predictions
    top_k_idx = np.argsort(y_proba)[-k:]
    
    y_true = np.array(y_true)
    top_k_labels = y_true[top_k_idx]
    
    precision_at_k = top_k_labels.sum() / k
    recall_at_k = top_k_labels.sum() / y_true.sum()
    
    return precision_at_k, recall_at_k

# Example: top 500 riskiest test transactions
k = 500
prec_k, rec_k = topk_precision_recall(y_test, y_proba_test, k)
print(f"Top-{k}: Precision = {prec_k:.3f}, Recall = {rec_k:.3f}")

for k in [100, 500, 1000, 2000]:
    prec_k, rec_k = topk_precision_recall(y_test, y_proba_test, k)
    print(f"Top-{k:5d}: Precision = {prec_k:.3f} | Recall = {rec_k:.3f}")
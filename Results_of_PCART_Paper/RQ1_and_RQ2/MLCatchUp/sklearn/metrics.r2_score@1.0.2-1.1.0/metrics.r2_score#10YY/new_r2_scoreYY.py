from sklearn.metrics import r2_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2_score(sample_weight=None, y_pred=y_pred, y_true=y_true, force_finite=True)
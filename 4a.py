# pip install scikit-learn pandas
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 1. Supervised learning
svm = SVC(probability=True, random_state=42)
svm.fit(X_train, y_train)
supervised = svm.predict(X_test)

# 2. Semi-supervised learning
# Hide labels for 70% of training samples
import numpy as np
rng = np.random.RandomState(42)
y_semi = y_train.copy()
hidden = rng.choice(len(y_semi), int(0.7 * len(y_semi)), replace=False)
y_semi[hidden] = -1

semi = SelfTrainingClassifier(SVC(probability=True, random_state=42))
semi.fit(X_train, y_semi)
semi_pred = semi.predict(X_test)

# 3. Ensemble learning
ensemble = VotingClassifier([
    ("svm", SVC(probability=True, random_state=42)),
    ("rf", RandomForestClassifier(n_estimators=100, random_state=42))
], voting="soft")

ensemble.fit(X_train, y_train)
ensemble_pred = ensemble.predict(X_test)

# Compare results
print("Model Performance")
print("Supervised SVM:", round(accuracy_score(y_test, supervised) * 100, 2), "%")
print("Semi-supervised:", round(accuracy_score(y_test, semi_pred) * 100, 2), "%")
print("Ensemble:", round(accuracy_score(y_test, ensemble_pred) * 100, 2), "%")

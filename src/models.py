from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

def get_model(name: str):
    name = name.lower()
    if name == "random forest":
        return RandomForestClassifier(n_estimators=200, random_state=42)
    if name == "svm":
        return SVC(probability=True, random_state=42)
    if name == "knn":
        return KNeighborsClassifier(n_neighbors=5)
    if name == "mlp":
        return MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42)
    if name == "logistic regression":
        return LogisticRegression(max_iter=500, n_jobs=None)
    if name == "gradient boosting":
        return GradientBoostingClassifier(random_state=42)
    raise ValueError(f"Unknown model: {name}")

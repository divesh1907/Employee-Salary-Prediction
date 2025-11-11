import matplotlib.pyplot as plt

def plot_metrics(metrics: dict):
    names = list(metrics.keys())
    values = [metrics[k] for k in names]

    plt.figure(figsize=(6,4))
    plt.bar(names, values)
    plt.ylim(0, 1.0)
    plt.title("Model Performance")
    plt.xlabel("Metric")
    plt.ylabel("Score")
    plt.tight_layout()
    return plt.gcf()

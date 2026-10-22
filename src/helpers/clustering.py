import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import cut_tree, dendrogram, linkage
from scipy.spatial.distance import squareform

# Turn simillarities into matrixes
def distance_matrix(S: np.ndarray) -> np.ndarray:
    D = 1 - S 
    np.fill_diagonal(D, 0.0)
    return np.clip(D,0, None)

# Flattens N x N matrix to an array consisting of unique (pair) values and removes redundant values
# Output: N(N-1)/2 length array
def single_link(S: np.ndarray) -> np.ndarray:
    return linkage(squareform(distance_matrix(S)), method="single")

# Turns Z into readable merge lines
def merge_lines(Z: np.ndarray, names: list[str]) -> list[str]:
    members = {i: [name] for i, name in enumerate(names)}
    lines = []
    for step, (a, b, dist, _size) in enumerate(Z, start=1):
        left, right = members[int(a)], members[int(b)]
        members[len(names) + step - 1] = left + right
        lines.append(f"merge {step}: {left} + {right} at similarity {1 - dist:.4f}")
    return lines

# Custs tree into K=2 groups and returns the file names of each
def two_clusters(Z: np.ndarray, names: list[str]) -> dict[int, list[str]]:
    clusters: dict[int, list[str]] = {}
    for name, label in zip(names, cut_tree(Z, n_clusters=2).ravel()):
        clusters.setdefault(int(label) + 1, []).append(name)
    return clusters

# Visualizer
def save_dendrogram(Z: np.ndarray, names: list[str], path: str) -> None:
    fig, ax = plt.subplots(figsize=(12,6))
    k2_cut = (Z[-2, 2] + Z[-1, 2]) / 2
    dendrogram(Z, labels=names, ax=ax, leaf_rotation=90,
               color_threshold=k2_cut, above_threshold_color="grey")
    ax.axhline(k2_cut, linestyle="--", color="black", linewidth=0.8)
    ax.set_ylabel("Distance (1 - cosine similarity)")
    ax.set_title("Single-linkage dendrogram")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
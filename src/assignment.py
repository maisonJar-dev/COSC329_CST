import csv
from pathlib import Path
import numpy as np

from preprocessing.preprocess import preprocess
from helpers.clustering import merge_lines, save_dendrogram, single_link, two_clusters
from vectorization.similarity import cosine_matrix
from vectorization.tfidf import tfidf_matrix

OUTPUTS = Path("src/outputs")
        
def load_docs(folder: Path, stop_words: set[str]) -> tuple[list[str], list[list[str]]]:
    files = sorted(folder.glob("*.txt"))
    names = [f.name for f in files]
    docs = [preprocess(f.read_text(encoding="utf-8"), stop_words) for f in files]
    return names, docs

def write_matrix_csv(path: Path, row_names: list[str], col_names: list[str], matrix: np.ndarray) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["file", *col_names])
        for name, row in zip(row_names, matrix):
            writer.writerow([name, *(f"{v:.4f}" for v in row)])

def main() -> None:
    stop_words = set(Path("src/stoppers/stop_words.txt").read_text(encoding="utf-8").split())
    names, docs = load_docs(Path("src/data/alldocs"), stop_words)
    
    X, vocab = tfidf_matrix(docs=docs)
    S = cosine_matrix(X)
    Z = single_link(S)

    OUTPUTS.mkdir(exist_ok=True)
    write_matrix_csv(OUTPUTS / "document_vector.csv", names, vocab, X)
    write_matrix_csv(OUTPUTS / "cosine_similarity.csv", names, names, S)
    (OUTPUTS / "merges.txt").write_text("\n".join(merge_lines(Z, names)) + "\n")
    clusters = two_clusters(Z, names)
    (OUTPUTS / "clusters_k2.txt").write_text(
        "".join(f"cluster {label} ({len(files)} files): {', '.join(files)}\n" for label, files in clusters.items())
    )
    save_dendrogram(Z, names, str(OUTPUTS / "dendrogram.png"))

if __name__ == "__main__":
    main()

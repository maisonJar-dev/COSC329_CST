import math 
from collections import Counter
import numpy as np

def term_frequency(tokens: list[str]) -> dict[str, float]:
    counts = Counter(tokens)
    return {term: n / len(tokens) for term, n in counts.items()}

def inverse_document_frequency(docs: list[list[str]]) -> dict[str, float]:
    doc_freq = Counter(term for doc in docs for term in set(doc))
    return {term: math.log(len(docs) / df) for term, df in doc_freq.items()}

def tfidf_matrix(docs: list[list[str]]) -> tuple[np.ndarray, list[str]]:
    idf = inverse_document_frequency(docs)
    # Sorting here makes output deterministic so output is replicatable in tests
    vocab = sorted(idf)
    rows = []
    for doc in docs:
        tf = term_frequency(doc)
        rows.append([tf.get(term, 0.0) *idf[term] for term in vocab])
    return np.array(rows), vocab

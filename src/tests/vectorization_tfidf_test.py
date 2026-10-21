import pytest

import numpy as np
import math
from vectorization.tfidf import term_frequency, inverse_document_frequency, tfidf_matrix

# MARK: Term Frq

def test_tf_known_values():
    tf = term_frequency(["a", "b", "a", "c"])
    assert tf == pytest.approx({"a": 0.5, "b": 0.25, "c": 0.25})
 
 
def test_tf_sums_to_one():
    tf = term_frequency(["x", "y", "y", "z", "z", "z"])
    assert sum(tf.values()) == pytest.approx(1.0)
 
 
def test_tf_single_token():
    assert term_frequency(["only"]) == {"only": 1.0}

# MARK: Inverse Frq
 
def test_idf_known_values():
    docs = [["a", "b"], ["a", "c"], ["a"]]
    idf = inverse_document_frequency(docs)
    assert idf["a"] == pytest.approx(0.0)              # in all 3 docs: log(3/3)
    assert idf["b"] == pytest.approx(math.log(3 / 1))
    assert idf["c"] == pytest.approx(math.log(3 / 1))
 
 
def test_idf_counts_a_term_once_per_document():
    # "a" appears three times in one doc, but its document frequency is still 1
    docs = [["a", "a", "a"], ["b"]]
    assert inverse_document_frequency(docs)["a"] == pytest.approx(math.log(2))
 
 
def test_idf_rarer_terms_score_higher():
    docs = [["common", "rare"], ["common"], ["common"]]
    idf = inverse_document_frequency(docs)
    assert idf["rare"] > idf["common"]
 
# MARK: TFIDF Mtrx
 
def test_matrix_shape_and_sorted_vocab():
    docs = [["the", "cat"], ["the", "dog", "barked"]]
    matrix, vocab = tfidf_matrix(docs)
    assert vocab == ["barked", "cat", "dog", "the"]
    assert matrix.shape == (2, 4)
 
 
def test_matrix_matches_hand_computation():
    docs = [["a", "b", "b"], ["a", "c"]]
    matrix, vocab = tfidf_matrix(docs)
    assert vocab == ["a", "b", "c"]
    ln2 = math.log(2)
    expected = np.array([
        [0.0, (2 / 3) * ln2, 0.0],   # doc 0: a is everywhere -> 0, b = tf 2/3 * log 2
        [0.0, 0.0, (1 / 2) * ln2],   # doc 1: c = tf 1/2 * log 2
    ])
    np.testing.assert_allclose(matrix, expected)
 
 
def test_term_in_every_document_gets_zero_column():
    docs = [["x", "y"], ["x", "z"], ["x"]]
    matrix, vocab = tfidf_matrix(docs)
    np.testing.assert_array_equal(matrix[:, vocab.index("x")], 0.0)
 
 
def test_absent_terms_are_zero():
    docs = [["a"], ["b"]]
    matrix, vocab = tfidf_matrix(docs)
    assert matrix[0, vocab.index("b")] == 0.0
    assert matrix[1, vocab.index("a")] == 0.0
 
 
def test_values_are_non_negative():
    docs = [["a", "b", "c"], ["b", "c", "d"], ["c", "d", "e", "e"]]
    matrix, _ = tfidf_matrix(docs)
    assert (matrix >= 0).all()
 
 
def test_token_order_within_a_doc_does_not_matter():
    m1, _ = tfidf_matrix([["a", "b", "b"], ["c"]])
    m2, _ = tfidf_matrix([["b", "a", "b"], ["c"]])
    np.testing.assert_allclose(m1, m2)
 


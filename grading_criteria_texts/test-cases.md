# `src/tests/preprocessing_preprocess_test.py`

```Python
def test_clean_text():
    _text = "So, on that trip I went on this cool adventure with my firends!"
    assert preprocess.preprocess(_text, stop_words) == expected
```
Tests that the preprocess function behaives as expected and drops stop words, suffixes, and punctuation.

# `src/tests/vectorization_tfidf_test.py`

```Python
def test_tf_known_values():
    tf = term_frequency(["a", "b", "a", "c"])
    assert tf == pytest.approx({"a": 0.5, "b": 0.25, "c": 0.25})
```
- Tests TF is as expected, count / number of tokens, so a = 2 / 4 = 1/2 = 0.5

```Python
def test_tf_sums_to_one():
    tf = term_frequency(["x", "y", "y", "z", "z", "z"])
    assert sum(tf.values()) == pytest.approx(1.0)
```
- The sum of all TF values should always sum to one.

```Python
def test_tf_single_token():
    assert term_frequency(["only"]) == {"only": 1.0}
```
- TF of 1 token with token count of 1 should return 1. 

```Python
def test_idf_known_values():
    docs = [["a", "b"], ["a", "c"], ["a"]]
    idf = inverse_document_frequency(docs)
    assert idf["a"] == pytest.approx(0.0)              # in all 3 docs: log(3/3)
    assert idf["b"] == pytest.approx(math.log(3 / 1))
    assert idf["c"] == pytest.approx(math.log(3 / 1))
```
- IDF works with looking uniqueness of a token, so if it shows in all documents: log(3/3) = log(1) = 0 for 'a' vs log(3/1) for 'b'

```Python
def test_idf_counts_a_term_once_per_document():
    # "a" appears three times in one doc, but its document frequency is still 1
    docs = [["a", "a", "a"], ["b"]]
    assert inverse_document_frequency(docs)["a"] == pytest.approx(math.log(2))
```
- Repeating a token inside a document should not raise its df for df(t)

```Python
def test_idf_rarer_terms_score_higher():
    docs = [["common", "rare"], ["common"], ["common"]]
    idf = inverse_document_frequency(docs)
    assert idf["rare"] > idf["common"]
```
- Term in fewer documents should gain higher IDF score

```Python
def test_matrix_shape_and_sorted_vocab():
    docs = [["the", "cat"], ["the", "dog", "barked"]]
    matrix, vocab = tfidf_matrix(docs)
    assert vocab == ["barked", "cat", "dog", "the"]
    assert matrix.shape == (2, 4)
```
- Asserts words sorted alphabetically, and asserts shape of matrix, 1 row per document, 1 column per unique word.  

```Python
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
```
- The matrix matches expected values of IDF * TF

```Python
def test_term_in_every_document_gets_zero_column():
    docs = [["x", "y"], ["x", "z"], ["x"]]
    matrix, vocab = tfidf_matrix(docs)
    np.testing.assert_array_equal(matrix[:, vocab.index("x")], 0.0)
```
- Terms that show in every document should be 0

```Python
def test_absent_terms_are_zero():
    docs = [["a"], ["b"]]
    matrix, vocab = tfidf_matrix(docs)
    assert matrix[0, vocab.index("b")] == 0.0
    assert matrix[1, vocab.index("a")] == 0.0
```
- A term that isn't in a document should be 0 in that row. 

```Python
def test_values_are_non_negative():
    docs = [["a", "b", "c"], ["b", "c", "d"], ["c", "d", "e", "e"]]
    matrix, _ = tfidf_matrix(docs)
    assert (matrix >= 0).all()
```
- No entry in the matrix is negative

```Python
def test_token_order_within_a_doc_does_not_matter():
    m1, _ = tfidf_matrix([["a", "b", "b"], ["c"]])
    m2, _ = tfidf_matrix([["b", "a", "b"], ["c"]])
    np.testing.assert_allclose(m1, m2)
```
- Shuffling tokens inside a document does not change its row. 

# `src/tests/vectorization_similarity_test.py`

```Python
def test_cosine_matrix_diagonal_is_one() -> None:
    X = np.array([[3.0, 4.0, 0.0], [1.0, 2.0, 2.0]])
    assert np.diag(cosine_matrix(X)) == pytest.approx([1.0, 1.0])
```
- Every document scores 1 against itself

```Python
def test_cosine_matrix_is_symmetric() -> None:
    X = np.array([[1.0, 2.0], [3.0, 1.0], [0.5, 4.0]])
    S = cosine_matrix(X)
    assert S == pytest.approx(S.T)
```
- Tests cosine matrix is symmetric, meaning the transpose is equal to the original

```Python
def test_cosine_matrix_ignores_vector_length() -> None:
    # Same direction, different magnitude → identical
    X = np.array([[1.0, 2.0], [10.0, 20.0]])
    assert cosine_matrix(X)[0, 1] == pytest.approx(1.0)
```
- Tests that the normalization aspect of cosine matrixes works

```Python
def test_cosine_matrix_single_doc() -> None:
    assert cosine_matrix(np.array([[2.0, 5.0]])) == pytest.approx(np.array([[1.0]]))
```
- Documents should be similar to theirself, returning a 1. 

```Python
def test_cosine_matrix_zero_vector_is_zero_not_nan() -> None:
    # Empty doc after preprocessing → zero vector; must not produce nan
    S = cosine_matrix(np.array([[1.0, 2.0], [0.0, 0.0]]))
    assert not np.isnan(S).any()
    assert S[0, 1] == pytest.approx(0.0)
```
- A document left empty should score 0 against others instead of producing a NaN

# `src/tests/helpers_clustering_test.py`

```Python
def test_distance_matrix_known_values() -> None:
    D = distance_matrix(np.array([[1.0, 0.25], [0.25, 1.0]]))
    assert D == pytest.approx(np.array([[0.0, 0.75], [0.75, 0.0]]))
```
- Distance is 1 - Similarity, so 0.25 sim becomes 0.75, and the diagonal becomes 0.0

```Python
def test_distance_matrix_clips_float_noise_to_zero() -> None:
    # cosine can come out as 1.0000000002 → distance must not go negative
    D = distance_matrix(np.array([[1.0, 1.0 + 1e-10], [1.0 + 1e-10, 1.0]]))
    assert (D >= 0).all()
    assert np.diag(D) == pytest.approx([0.0, 0.0])
```
- Makes sure the floats don't create negative distances

```Python
def test_single_link_uses_closest_cross_pair() -> None:
    # Max cross-pair similarity is A–D = 0.2, so the final merge is at distance 0.8
    assert single_link(S)[-1, 2] == pytest.approx(0.8)
```
- Assert that the final merge uses the smallest remaining distance between two clusters. 

```Python
def test_merge_lines_readable_output() -> None:
    assert merge_lines(single_link(S), NAMES) == [
        "merge 1: ['A'] + ['B'] at similarity 0.9000",
        "merge 2: ['C'] + ['D'] at similarity 0.8000",
        "merge 3: ['A', 'B'] + ['C', 'D'] at similarity 0.2000",
    ]
```
- Each merge prints as a readable line

```Python
def test_merge_lines_one_line_per_merge() -> None:
    assert len(merge_lines(single_link(S), NAMES)) == len(NAMES) - 1
```
- n documents produce n - 1 merges

```Python
def test_two_clusters_splits_pairs() -> None:
    groups = sorted(sorted(g) for g in two_clusters(single_link(S), NAMES).values())
    assert groups == [["A", "B"], ["C", "D"]]
```
- Cutting tree into two clusters gives {A,B} & {C,D}

```Python
def test_two_clusters_ties_still_gives_two_groups() -> None:
    # Every pair equally similar: the split is arbitrary, but must be K=2 and cover all docs
    S_tie = np.full((3, 3), 0.5)
    np.fill_diagonal(S_tie, 1.0)
    clusters = two_clusters(single_link(S_tie), ["A", "B", "C"])
    assert len(clusters) == 2
```
- Checks that through a tie two clusters are still found 
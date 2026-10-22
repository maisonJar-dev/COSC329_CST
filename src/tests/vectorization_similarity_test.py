import numpy as np
import pytest

from vectorization.similarity import cosine_matrix


def test_cosine_matrix_diagonal_is_one() -> None:
    X = np.array([[3.0, 4.0, 0.0], [1.0, 2.0, 2.0]])
    assert np.diag(cosine_matrix(X)) == pytest.approx([1.0, 1.0])


def test_cosine_matrix_is_symmetric() -> None:
    X = np.array([[1.0, 2.0], [3.0, 1.0], [0.5, 4.0]])
    S = cosine_matrix(X)
    assert S == pytest.approx(S.T)


def test_cosine_matrix_ignores_vector_length() -> None:
    # Same direction, different magnitude → identical
    X = np.array([[1.0, 2.0], [10.0, 20.0]])
    assert cosine_matrix(X)[0, 1] == pytest.approx(1.0)


def test_cosine_matrix_single_doc() -> None:
    assert cosine_matrix(np.array([[2.0, 5.0]])) == pytest.approx(np.array([[1.0]]))


def test_cosine_matrix_zero_vector_is_zero_not_nan() -> None:
    # Empty doc after preprocessing → zero vector; must not produce nan
    S = cosine_matrix(np.array([[1.0, 2.0], [0.0, 0.0]]))
    assert not np.isnan(S).any()
    assert S[0, 1] == pytest.approx(0.0)

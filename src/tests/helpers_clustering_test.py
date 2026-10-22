import numpy as np
import pytest

from helpers.clustering import (
    distance_matrix,
    merge_lines,
    single_link,
    two_clusters,
)

# A, B very similar; C, D very similar; the two pairs barely similar
NAMES = ["A", "B", "C", "D"]
S = np.array(
    [
        [1.0, 0.9, 0.1, 0.2],
        [0.9, 1.0, 0.15, 0.1],
        [0.1, 0.15, 1.0, 0.8],
        [0.2, 0.1, 0.8, 1.0],
    ]
)

# MARK: Distance


def test_distance_matrix_known_values() -> None:
    D = distance_matrix(np.array([[1.0, 0.25], [0.25, 1.0]]))
    assert D == pytest.approx(np.array([[0.0, 0.75], [0.75, 0.0]]))


def test_distance_matrix_clips_float_noise_to_zero() -> None:
    # cosine can come out as 1.0000000002 → distance must not go negative
    D = distance_matrix(np.array([[1.0, 1.0 + 1e-10], [1.0 + 1e-10, 1.0]]))
    assert (D >= 0).all()
    assert np.diag(D) == pytest.approx([0.0, 0.0])


# MARK: Single link

def test_single_link_uses_closest_cross_pair() -> None:
    # Max cross-pair similarity is A–D = 0.2, so the final merge is at distance 0.8
    assert single_link(S)[-1, 2] == pytest.approx(0.8)


# MARK: Merge lines


def test_merge_lines_readable_output() -> None:
    assert merge_lines(single_link(S), NAMES) == [
        "merge 1: ['A'] + ['B'] at similarity 0.9000",
        "merge 2: ['C'] + ['D'] at similarity 0.8000",
        "merge 3: ['A', 'B'] + ['C', 'D'] at similarity 0.2000",
    ]


def test_merge_lines_one_line_per_merge() -> None:
    assert len(merge_lines(single_link(S), NAMES)) == len(NAMES) - 1


# MARK: Two clusters

def test_two_clusters_splits_pairs() -> None:
    groups = sorted(sorted(g) for g in two_clusters(single_link(S), NAMES).values())
    assert groups == [["A", "B"], ["C", "D"]]


def test_two_clusters_ties_still_gives_two_groups() -> None:
    # Every pair equally similar: the split is arbitrary, but must be K=2 and cover all docs
    S_tie = np.full((3, 3), 0.5)
    np.fill_diagonal(S_tie, 1.0)
    clusters = two_clusters(single_link(S_tie), ["A", "B", "C"])
    assert len(clusters) == 2
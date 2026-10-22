import pytest
from preprocessing import preprocess

stop_words = {"i", "me", "my", "myself"}

expected = [
    "that",
    "trip",
    "went",
    "thi",
    "cool",
    "adventur",
    "with",
    "firend",
]


def test_clean_text():
    _text = "So, on that trip I went on this cool adventure with my firends!"
    assert preprocess.preprocess(_text, stop_words) == expected
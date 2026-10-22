import re
from nltk.stem import PorterStemmer

STEMMER = PorterStemmer()

def preprocess(text: str, stop_words: set[str]) -> list[str]:
    words = re.findall(r"[a-z]+", text.lower())
    words = [w for w in words if w not in stop_words]
    stems = [STEMMER.stem(w) for w in words]
    return [s for s in stems if len(s) >= 3]
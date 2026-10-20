# COSC329_CST
Clustering Story Texts Learning Analytics Assignment 2.

Maison Gulyas
-------------

### Architecture 
src/
  |- helpers/ 		# Computing document similarity, applying clustering, other helpful functionalities.
  |- preprocessing/ 	# Text sanitization
  |- vectorization/ 	# TFIDF, TF, IDF
  |- tests/		# Python tests
  |- data/ 		# Text data
  |- outputs/		# Useful Outputs

### Interpretation

My interpretation for this project is stored and updated here: [link](interpretation.md)


# Running

**Setup Venv:**
```
python -m venv .venv
```

**Install Dependencies:**
```
pip install -r requirements.txt
```

**Run assingment.py:**
```
python src/assingment.py
```

## Tests

**Run tests:**
```
python -m pytest -q
```


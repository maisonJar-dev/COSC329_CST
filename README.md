# COSC329_CST
Clustering Story Texts Learning Analytics Assignment 2.

Maison Gulyas
-------------

### Architecture 

```
src/
├── helpers/          # Document similarity, clustering, utilities
├── preprocessing/    # Text sanitization
├── vectorization/    # TF, IDF, TF-IDF
├── tests/            # Pytest suite
├── data/             # Story text corpus
└── outputs/          # Generated results
```

### Interpretation

My interpretation for this project is stored and updated here: [link](interpretation.md)


# Running

**Setup Venv:**
```
python -m venv .venv
source .venv/bin/activate 
```

**Install Dependencies:**
```
pip install -r requirements.txt
```

**Run assingment.py:**
```
python src/assignment.py
```

## Tests

**Run tests:**
```
python -m pytest -q
```


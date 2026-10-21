from pathlib import Path
from preprocessing.preprocess import preprocess


class AssignmentA2:
    def __init__(self, _encoding="utf-8", *, alldocs: Path | str, stop_words: Path | str) -> None:
        self.words: list[str]
        _stop_words = set(stop_words.read_text(encoding=_encoding).splitlines())
        for file in alldocs.rglob("*.txt"):
            if file.is_file():
                self.words = preprocess(
                    text=file.read_text(encoding=_encoding),
                    stop_words=_stop_words
                )
              
def main() -> None:
    a2 = AssignmentA2(
        alldocs=Path("src/data/alldocs"), 
        stop_words=Path("src/stoppers/stop_words.txt")
    )
    

if __name__ == "__main__":
    main()

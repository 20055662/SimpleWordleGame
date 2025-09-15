# src/utils.py
def load_words(file_path):
    """Load words from a text file and return a list."""
    with open(file_path, 'r') as f:
        return [word.strip() for word in f]

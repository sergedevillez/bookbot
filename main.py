from stats import get_words_amount
from stats import get_characters_occurrences
from stats import get_sorted_occurrences
import sys

def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, content, sorted_occurrences):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}")
    print(f"----------- Word Count ----------")
    print(f"Found {len(content.split())} total words")
    print("--------- Character Count -------")
    for key, value in sorted_occurrences:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_books_text(filepath)
    occurrences = get_characters_occurrences(content)
    sorted_occurrences = get_sorted_occurrences(occurrences)
    print_report(filepath, content, sorted_occurrences)

main()
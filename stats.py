
def get_words_amount(text):
    """
    Returns the number of words in the given text.
    :param text: The text to analyze.
    :return: A string indicating the number of words found.
    """
    return len(text.split())

def get_characters_occurrences(text):
    """
    Return a dictionary with each distinct characters present in the text and their occurrence as value
    :param text: The text to analyze.
    :param character: The character to count occurrences of.
    :return: A dictionary with characters as keys and their occurrences as values.
    """
    uniques = set(text.lower())
    occurrences = {}
    for char in uniques:
        occurrences[char] = text.lower().count(char)
    return occurrences

def get_sorted_occurrences(occurrences):
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)
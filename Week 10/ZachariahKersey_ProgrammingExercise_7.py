import re

def find_sentences(paragraph):
    """
    Compares the paragraph to regex pattern to find sentences within it

    Parameters:
        paragraph (str): Paragraph to compare against

    Variables:
        pattern (regex): Regex pattern to compare against
        matches (list): List of matches from comparing paragraph against regex

    Logic:
        1. Find all sentences in paragraph
        2. Returns matches

    Returns:
        matches (list): List of matches from comparing paragraph against regex
    """
    pattern = r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)"
    # Find all matches to the sentence pattern regex within the paragraph
    matches = re.findall(pattern, paragraph, flags=re.DOTALL)
    return matches


def display_sentences(matches):
    """
    Validate a phone based on its format

    Parameters:
        matches (list): List of matches from comparing paragraph against regex

    Variables:
        None

    Logic:
        1. Loop over the matches, numbering and printing each sentence
        2. Prints the total number of sentences found within the paragraph

    Returns:
        None
    """

    # Iterate over found matches, numbering and printing each
    for i in range(len(matches)):
        print(f"Sentence {i + 1}: {matches[i]}")
    # Print the total number of sentences for the user
    print(f"Total count of sentences: {len(matches)}")


if __name__ == "__main__":
    # Takes the user's inputted paragraph
    user_input = input("Enter a paragraph: ")
    # Determine all matches from user input
    found_matches = find_sentences(user_input)
    # Display findings to user
    display_sentences(found_matches)
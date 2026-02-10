def analyzeEmail():
    """
    Analyzes the words found in the email and generates a spam score.

    Parameters:
        None

    Variables:
        score (int): The spam score.
        wordsFound (list): A list of spam keywords words found in the email.
        SPAM_KEYWORDS (list): A list of commonly used spam keywords.
        email (str): The email's contents inputted by the user.

    Logic:
        1. Receive email's contents from user input.
        2. Loop over every spam keyword in SPAM_KEYWORDS.
        3. Increase spam score if current spam keyword is found in the email.
        4. Append the current spam keyword to the list of found words.
        5. Return the spam score and list of keywords words found in the email.

    Returns:
        tuple:
            spamScore (int): The spam score.
            wordsFound (list): A list of words found in the email.
    """

    # Initialize spam score and list of found keywords variables
    score = 0
    wordsFound = []

    # Create list of commonly used words in spam emails for reference
    SPAM_KEYWORDS = [
        "Free money", "Cash bonus", "Get paid", "Make money",
        "Earn extra cash", "Act now", "Urgent", "Limited time",
        "Don't miss out", "Hurry", "Risk-free", "No hidden fees",
        "Buy direct", "Cancel at any time", "Check or money order",
        "Congratulations", "Confidentiality", "Cures",
        "Dear friend", "Get rich quick", "Winner", "Do it today",
        "Money back", "Dollars", "Pure profit", "No obligation",
        "Free gift", "Last chance", "Don't hesitate", "Important"
    ]

    # Take user input for the content of their email
    email = input("Enter the email's contents: ").lower()

    for keyword in SPAM_KEYWORDS:
        # Check if the lowercased version of the keyword is found in the email
        if keyword.lower() in email:
            score += 1
            # Add the keyword to the list of keywords found in the email
            wordsFound.append(keyword)

    # Return the spam score and list of spam keywords found as a tuple
    return score, wordsFound


def analyzeScore(score, found_keywords):
    """
    Analyzes the spam score and displays the risk of the email.

    Parameters:
        score (int): The spam score.
        found_keywords (list): A list of spam keywords found in the email.

    Variables:
        risk (str): The calculated risk based on the spam score.

    Logic:
        1. Print the calculated spam score.
        2. Set the risk value based on the spam score.
        3. Print the risk value.
        4. Print any spam keywords found in the email or none if none found.

    Returns:
        None
    """
    print(f"\nSpam Score: {score}/30")

    if score >= 10:
        risk = "High likelihood"
    elif score >= 5:
        risk = "Medium likelihood"
    elif score >= 1:
        risk = "Low likelihood"
    else:
        risk = "Very low likelihood"

    print(f"Likelihood that message is spam: {risk}")

    if found_keywords:
        print("\nSuspicious words/phrases found:")
        for keyword in found_keywords:
            print(f"- {keyword}")
    else:
        print("\nNo spam keywords detected.")


if __name__ == "__main__":
    # Analyze email contents
    spamScore, wordsFound = analyzeEmail()
    # Analyze risk based on spam score
    analyzeScore(spamScore, wordsFound)
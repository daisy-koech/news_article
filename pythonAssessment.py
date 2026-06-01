def count_specific_word(text, word):
    words = text.split()
    count = 0

    for w in words:
        if w == word:
            count += 1
    return count

def identify_most_common_word(text):
    if text == "":
        return None
    words = text.split()
    most_common = ""
    highest_count = 0

    for w in words:
        current_count = count_specific_word(text, w)
        if current_count > highest_count:
            highest_count = current_count
            most_common = w
    return most_common

def calculate_average_word_length(text):
    if text == "":
        return 0
    words = text.split()
    total = 0

    for w in words:
        for char in w:
            if char.isalnum():
                total += 1
    return total / len(words)

def count_paragraphs(text):
    if text == "":
        return 1
    paragraphs = text.split("\n\n")
    return len(paragraphs)

def count_sentences(text):
    if text == "":
        return 1
    count = 0
    index = 0

    while index < len(text):
        if text[index] == "." or text[index] == "!" or text[index] == "?":
            count += 1
        index += 1
    return count

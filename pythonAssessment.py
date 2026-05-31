my_article = open("news_article.txt", "r")
article_text = my_article.read()
my_article.close()

def count_specific_word(article_words, search_word):
    words = article_words.split()
    count = 0

    for word in words:
        if word == search_word:
            count = count + 1
    return count

def identify_most_common_word(article_words):
    if article_words == "":
        return None
    words = article_words.split()
    most_common = ""
    highest_count = 0

    for word in words:
        current_count = count_specific_word(article_words, word)
        if current_count > highest_count:
            highest_count = current_count
            most_common = word
    return most_common

def calculate_average_word_length(article_words):
    if article_words == "":
        return 0
    words = article_words.split()
    letters = 0
    word_length = len(words)

    for word in words:
        for char in word:
            if char.isalnum():
                letters = letters + 1
    average_length = letters / word_length
    return average_length

def count_paragraphs(article_words):
    if article_words == "":
        return 1
    paragraphs = article_words.split("\n\n")
    return len(paragraphs)

def count_sentences(article_words):
    if article_words == "":
        return 1
    count = 0
    index = 0

    while index < len(article_words):
        if article_words[index] == "." or article_words[index] == "!" or article_words[index] == "?":
            count = count + 1
        index = index + 1
    return count

search_word = input("Enter a word to count in the text: ")
if search_word == "":
    print("Please enter a word")
else:
    print("Word count:", count_specific_word(article_text, search_word))

print("The most common word is:", identify_most_common_word(article_text))
print("The average word length is:", calculate_average_word_length(article_text))
print("The number of paragraphs is:", count_paragraphs(article_text))
print("The number of sentences in the text is:", count_sentences(article_text))

# TODO
from cs50 import get_string


def count_letters(text):
    letters = 0
    for letter in text.lower():
        if letter.islower():
            letters += 1

    return letters


def count_words(text):
    words = 0
    for letter in text:
        if (letter == ' '):
            words += 1

    return words + 1


def count_sentences(text):
    sentences = 0
    for letter in text:
        if letter == '!' or letter == '?' or letter == '.':
            sentences += 1

    return sentences


def main():

    text = get_string("Text: ")
    words = count_words(text)
    sentences = count_sentences(text)
    letters = count_letters(text)

    # gets number of letters, sentences, words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index >= 16:
        print("Grade 16+\n")
    elif index < 1:
        print("Before Grade 1\n")
    else:
        print(f"Grade {index}\n")


main()

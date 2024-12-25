#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// declaring functions
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Enter Text: ");

    float words = count_words(text);
    float sentences = count_sentences(text);
    float letters = count_letters(text);

    printf("Words: %f, sentences: %f, letters: %f\n", words, sentences, letters);

    // gets number of letters, sentences, words

    float L = (letters / (float)words) * 100;
    float S = (sentences / (float)words) * 100;
    printf("L: %f, S: %f\n", L, S);

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    // count letters in for loop
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (islower(text[i]) | isupper(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    // count words in for loop
    int words = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }
    return words + 1;
}

int count_sentences(string text)
{
    // count sentences in for loop
    int sentences = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '!' || text[i] == '?' || text[i] == '.')
        {
            sentences++;
        }
    }
    return sentences;
}
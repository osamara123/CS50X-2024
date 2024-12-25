// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <cs50.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 456976;

// Hash table
node *table[N];

// number of words
int count_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *cursor = table[hash(word)];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // check two letters
    if (word[1] != '\0')
    {
        return ((toupper(word[0]) - 'A') * 26 + toupper(word[1]) - 'A');
    }

    // one letter word
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("File couldn't open.\n");
        return false;
    }
    //read words from dic
    char *word = malloc(LENGTH + 1);
    if (word == NULL)
    {
        // fclose(file);
        return false;
    }
    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        // index inside hash table to insert word
        int index = hash(word);
        // first word in the curret node
        if (table [index] == NULL)
        {
            n->next = NULL;
        }
        else
        {
            n->next = table[index];
        }
        table [index] = n;
        count_words++;
    }
    // free memory
    fclose(file);
    free(word);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count_words;
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table [i];
        node *tmp = table [i];
        // traverse a node
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}

// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>



#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 7500;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int length = strlen(word);
    char copy[length +1];
    for (int i = 0; i != '\0' ; i++)
    {
        copy[i] = tolower(word[i]);
    }
    int ind = hash(copy);
    if (table[ind] == NULL)
    {
        return 0;
    }
    node *tmp = table[ind];
    while (tmp != NULL)
    {
        if (strcmp(tmp ->word, copy) == 0)
        {
            return 1;
        }
        tmp = tmp -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int value = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        value += tolower(word[i]);
    }
    return (value / N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Dictionary does not exist.\n");
        return false;
    }
    char str[LENGTH +1];
    while(fscanf(file, "%s", str) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n ->word, str);
        int hashh = hash(str);

        if (hash)
    }

        return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int counter = 0;
    for (int i = 0; i < N; i++)
    {
        node *tmp = table[i];
        while (tmp -> next != NULL)
        {
            counter++;
            tmp = tmp -> next;
        }
    }
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *tmp = malloc(sizeof(node));
        node *current = table[i];
        while (current -> next != NULL)
        {
            tmp = current;
            current = current -> next;
            free(tmp);
        }
    }
    return false;
}

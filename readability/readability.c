#include <cs50.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text;
    int letters, words, sentences;


    text = get_string("Text: ");


    letters = count_letters(text);
    printf("letters: %d\n",letters);
    words = count_words(text);
    printf("words: %d\n",words);
    sentences = count_sentences(text);
    printf("sentences: %d\n",sentences);


int L, S, index;


    L = (letters / words) * (float)100;
    S = (sentences / words) * (float)100;
    index = (0.0588 * L ) - (0.296 * S ) - 15.8;


    printf("Text: %s\n",text);
    printf("Grade: %d\n",index);
}

int count_letters(string text)
{
    int counter = 0;
    for( int i = 0; i < strlen(text); i++ )
    {
        if( (text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122 )  )
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text)
{
    int counter = 1;
    for( int i = 0; i < strlen(text); i++ )
    {
        if( text[i] == 32 )
        counter++;
    }
    return counter;
}

int count_sentences(string text)
{
    int counter = 0;
    for( int i = 0; i < strlen(text); i++ )
    {
        if( text[i] == 33 || text[i] == 46 || text[i] == 63 )
        {
            counter++;
        }
    }
    return counter;
}
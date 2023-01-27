#include <cs50.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text;
    int letters, words;


    text = get_string("Text: ");


    letters = count_letters(text);
    printf("letters: %d\n",letters);
    words = count_words(text);
    printf("words: %d\n",words);




    printf("Text: %s\n",text);

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
    int counter;
    for( int i = 0; i < strlen(text); i++ )
    {
        
    }
}
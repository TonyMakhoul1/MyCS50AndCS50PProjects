#include <cs50.h>
#include <stdio.h>
#include <

int count_letters(string Text);

int main(void)
{
    string text;
    int letters;
    text = get_string("Text: ");
    letters = count_letters(text);
    printf("letters: %d",letters);

    printf("Text: %s\n",text);

}

int count_letters(string text)
{
    int counter = 0;
    for( int i = 0; i < strlen(text); i++ )
    {
        counter += counter;
    }
    return counter;
}

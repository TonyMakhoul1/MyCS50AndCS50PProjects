#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


    for( int i = 0; i < strlen(argv[1]); i++)
    {
        only_digits(argv[1][i]);

        int k;
        k = atoi(argv[1]);

        string plaintext = get_string("Plaintext: ");
        printf("Ciphertext: ");

        for( int j = 0; j < strlen(plaintext); j++ )
        {
            rotate(plaintext[j],k);

        }
     }
        printf("\n");
        return 0;
    }





bool only_digits(string s[])
{
    for( int i = 0; i < strlen(s); i++)
    {
        if((!isdigit(s[i])) && (s[i] >= 0 && s[i] <= 9))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }

    }
    return 0;
}

char rotate(char c, int n)
{


            if(islower(c))
            {
                printf("%c", (c - 97 + n) % 26 + 97);
            }
            else if(isupper(c))
            {
                printf("%c", (c - 65 + n) % 26 + 65);
            }
            else
            {
                printf("%c",c);
            }
            return c;
}

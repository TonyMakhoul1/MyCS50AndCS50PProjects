#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height,stored,i,j,k ;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    stored = height;
    printf("Stored: %i\n",stored);

    for(i = 1 ; i <= height ; i++)
    {
        for(j = 1 ; j <= (height-i) ; j++)
        printf(" ");
        for(k = 1 ; k <= i ; k++)
        printf("#");
        printf("\n");
    }
}
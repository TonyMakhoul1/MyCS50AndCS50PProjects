#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file;
    if (argc != 2)
    {
        printf("Usage recover\n");
        return 1;
    }
    else
    {
        if (file = fopen(argv[1], "r") == NULL)
           {
               printf("Can't open %s", argv[1]);
           }
    }
    int count = 0;
    unint8_t BYTE;
    




}
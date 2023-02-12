#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(arbv[1], "r");
    if (argc != 2)
    {
        printf("Usage recover\n");
        return 1;
    }
    else
    {
        if (file == NULL)
           {
               printf("Can't open %s", argv[1]);
           }
    }
    int count = 0;
    unint8_t BYTE;





}
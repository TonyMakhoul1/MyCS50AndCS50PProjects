#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage recover\n");
        return 1;
    }
    if (FILE *file = fopen(argv[1], "r") == NULL)
    {
        printf("Can't open %s", argv[1])
    }
    

}
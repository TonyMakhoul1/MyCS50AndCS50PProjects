#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start ;

    do
    {
        start = get_int("Start: ");
    } while(start<9);

    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("End: ");
    } while(end<start);

    // TODO: Calculate number of years until we reach threshold
    int born , pass , stay , llamas , n=0;
    born = start/3;
    pass = start/4;
    stay = born - pass;
    llamas = start;

    while(llamas<end)
    {
        llamas = llamas + stay;
        n++;
        born = llamas/3;
        pass = llamas/4;
        stay = born -pass;
    }
    // TODO: Print number of years
    printf("Number Of Years: %i \n", n);
}

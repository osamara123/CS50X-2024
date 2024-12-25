#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int start_size, end_size, Years = 0, new_size, Gain, Lose;
    // TODO: Prompt for start size
    do
    {
        start_size = get_int("Start_size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    do
    {
        end_size = get_int ("End Size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold

    while (start_size < end_size)
    {
        Gain = start_size / 3;
        Lose = start_size / 4;
        new_size = start_size + Gain - Lose;
        start_size = new_size;
        Years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", Years);
}

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int Height;
    do
    {
        Height = get_int("Enter height: ");
    }
    while (Height < 1 | Height > 8);

    for (int i = 1; i <= Height; i++)
    {
        for (int j = Height; j >= 1; j--)
        {
            if (j <= i)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}

#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("Enter message: ");
    for (int i = 0; i < strlen(message); i++)
    {
        int Remainder[BITS_IN_BYTE];
        int num = (int)message[i];

        // convert decimal to binary
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            Remainder [BITS_IN_BYTE - j - 1] = num % 2;
            num /= 2;
        }

        // print char in binary by calling print_bulb func
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            //call funct
            print_bulb(Remainder [j]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

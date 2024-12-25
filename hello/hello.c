#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // ask user for name
    string name = get_string("Enter name: ");
    // print a hello message to user
    printf("hello, %s\n", name);
}
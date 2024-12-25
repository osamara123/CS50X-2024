#include <stdio.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t BYTE;
const int block_size = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Number of arguments should be at least one!\n");
        return 1;
    }
    // open card.raw file
    FILE *file = fopen(argv[1], "r");
    // output file
    FILE *img = NULL;
    if (file == NULL)
    {
        printf("file can't open.\n");
        return 2;
    }
    // recover images
    int count_image = 0;
    BYTE buffer [512];
    char filename [8];
    bool found = false;
    while (fread(buffer, 1, block_size, file))
    {
        // check start of JPEG file
        if (buffer [0] == 0xff && buffer [1] == 0xd8 && buffer [2] == 0xff && (buffer [3] & 0xf0) == 0xe0)
        {
            // first JPEG file
            if (count_image == 0)
            {
                // open file to write data into
                //write JPEG file name
                found = true;
                sprintf(filename, "%03i.jpg", count_image++);
                img = fopen(filename, "w");
                fwrite(buffer, 1, block_size, img);
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", count_image++);
                img = fopen(filename, "w");
                fwrite(buffer, 1, block_size, img);
            }
        }
        else
        {
            // writing the previous file
            if (found)
            {
                fwrite(buffer, 1, block_size, img);
            }
        }
    }
    fclose(file);
    fclose(img);
}
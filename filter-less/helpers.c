#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average;
            average = (image [i][j].rgbtBlue + image [i][j].rgbtRed + image [i][j].rgbtGreen) / (float)3;
            image [i][j].rgbtBlue = round(average);
            image [i][j].rgbtRed = round(average);
            image [i][j].rgbtGreen = round(average);
            if (image [i][j].rgbtBlue > 255)
            {
                image [i][j].rgbtBlue = 255;
            }
            if (image [i][j].rgbtRed > 255)
            {
                image [i][j].rgbtRed = 255;
            }
            if (image [i][j].rgbtGreen > 255)
            {
                image [i][j].rgbtGreen = 255;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // speia formulas
            float sepiaRed = (.393 * image [i][j].rgbtRed) + (.769 * image [i][j].rgbtGreen) + (.189 * image [i][j].rgbtBlue);
            float sepiaGreen = (.349 * image [i][j].rgbtRed) + (.686 * image [i][j].rgbtGreen) + (.168 * image [i][j].rgbtBlue);
            float sepiaBlue = (.272 * image [i][j].rgbtRed) + (.534 * image [i][j].rgbtGreen) + (.131 * image [i][j].rgbtBlue);
            int b = round(sepiaBlue);
            int r = round(sepiaRed);
            int g = round(sepiaGreen);
            if (b > 255)
            {
                b = 255;
            }
            if (r > 255)
            {
                r = 255;
            }
            if (g > 255)
            {
                g = 255;
            }
            image [i][j].rgbtRed = r;
            image [i][j].rgbtBlue = b;
            image [i][j].rgbtGreen = g;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int temp1 = image [i][j].rgbtBlue;
            int temp2 = image [i][j].rgbtRed;
            int temp3 = image [i][j].rgbtGreen;
            image [i][j].rgbtBlue = image [i][width - j - 1].rgbtBlue;
            image [i][j].rgbtRed = image [i][width - j - 1].rgbtRed;
            image [i][j].rgbtGreen = image [i][width - j - 1].rgbtGreen;
            image [i][width - j - 1].rgbtBlue = temp1;
            image [i][width - j - 1].rgbtRed = temp2;
            image [i][width - j - 1].rgbtGreen = temp3;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy [height][width];

    // create copy of image array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy [i][j].rgbtRed = image [i][j].rgbtRed;
            copy [i][j].rgbtGreen = image [i][j].rgbtGreen;
            copy [i][j].rgbtBlue = image [i][j].rgbtBlue;
        }
    }

    // change image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_red = 0, sum_green = 0, sum_blue = 0;
            int num = 0;
            // update single pixel
            for (int ii = i - 1; ii < i + 2; ii++)
            {
                for (int jj = j - 1; jj < j + 2; jj++)
                {
                    if (ii >= 0 && ii <= height - 1 && jj >= 0 && jj <= width - 1)
                    {
                        int r = copy [ii][jj].rgbtRed;
                        int b = copy [ii][jj].rgbtBlue;
                        int g = copy [ii][jj].rgbtGreen;
                        sum_red += r;
                        sum_green += g;
                        sum_blue += b;
                        num++;
                    }
                }
            }
            float avg_red = sum_red / (float)num;
            float avg_green = sum_green / (float)num;
            float avg_blue = sum_blue / (float)num;
            image [i][j].rgbtRed = round(avg_red);
            image [i][j].rgbtGreen = round(avg_green);
            image [i][j].rgbtBlue = round(avg_blue);
        }
    }
    return;
}
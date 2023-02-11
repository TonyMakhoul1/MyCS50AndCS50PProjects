#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            original[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, swapcol = width-1; j < width; j++)
        {
            image[i][j] = original[i][swapcol];
            swapcol--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            int rowx[] = {i-1; i; i+1};
            int colx[] = {j-1; j; j+1};
            for (int row = 0; row < 3; row++)
            {
                for(int col = 0; col < 3; col++)
                {
                    
                }
            }
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE previous[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            previous[i][j] = image[i][j];
        }
    }
    gx[3][3] =
    {
        {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}
    }
    gy[3][3] =
    {
        {-1, -2, -1}, {0, 0, 0}, {1, 2, 1}
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_row[3] = {row-1; row; row+1};
            new_col[3] = {col-1; col; col+1};
        }
    }
    return;
}

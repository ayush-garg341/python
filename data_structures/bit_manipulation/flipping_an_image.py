"""
Given that an image is represented by an (n×n) matrix containing
flip and invert the image, and return the resultant image.

Horizontally flipping an image means that the mirror image
of the matrix should be returned.
Flipping [1, 0, 0] horizontally results in [0, 0, 1]
"""


def flip_and_invert_image(image):
    # Replace this placeholder return statement with your code
    rows = len(image)
    cols = len(image[0])
    row = 0
    while row < rows:
        i = 0
        j = cols - 1
        while i <= j:
            if i == j:
                image[row][i] = image[row][i] ^ 1
            else:
                image[row][i], image[row][j] = image[row][j], image[row][i]

                image[row][i] = image[row][i] ^ 1
                image[row][j] = image[row][j] ^ 1

            i += 1
            j -= 1
        row += 1
    return image


print(flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(flip_and_invert_image([[1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0]]))

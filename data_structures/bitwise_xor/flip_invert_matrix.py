"""
Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [1, 1, 0] results in [0, 0, 1].
"""


def flip_and_invert_image(matrix):
    for i in range(len(matrix)):
        row_len = len(matrix[i])
        j = 0
        while j <= (row_len - 1) // 2:
            matrix[i][j], matrix[i][row_len - 1 - j] = (
                matrix[i][row_len - 1 - j] ^ 1,
                matrix[i][j] ^ 1,
            )
            j += 1

    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(
        flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
    )


main()

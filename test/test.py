"""
Create 3D array for given dimensions - (x, y, z)

@author: Naimish Agarwal
"""


def three_d_array(value, *dim):
    """
    Create 3D-array
    :param dim: a tuple of dimensions - (x, y, z)
    :param value: value with which 3D-array is to be filled
    :return: 3D-array
    """

    return [[[value for _ in range(dim[2])] for _ in range(dim[1])] for _ in range(dim[0])]

if __name__ == "__main__":
    array = three_d_array(False, *(2, 3, 1))
    x = len(array)
    y = len(array[0])
    z = len(array[0][0])
    print(x, y, z)

    array[0][0][0] = True
    array[1][1][0] = True

    print(array)

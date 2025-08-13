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

    return [[[value for _ in range(dim[0])] for _ in range(dim[1])] for _ in range(dim[2])]

if __name__ == "__main__":

    default_value = 0
    num_x = 3
    num_y = 4
    num_z = 2
    
    array = three_d_array(default_value, *(num_x, num_y, num_z))
    
    x = len(array[0][0])
    y = len(array[0])
    z = len(array)
        
    print(x, y, z)

    array[0][0][0] = 1
    array[0][0][1] = 2
    array[0][0][2] = 3

    array[0][1][0] = 4
    array[0][1][1] = 5
    array[0][1][2] = 6

    for x in range(len(array)):
        print(array[x])
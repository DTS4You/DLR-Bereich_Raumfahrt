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
    # [Z][Y][0]   -> Stripe PIN Value
    # [Z][Y][1]   -> Start Position Start from 0
    # [Z][Y][2]   -> Number of LED in this Segment

    return [[[value for _ in range(dim[0])] for _ in range(dim[1])] for _ in range(dim[2])]

#------------------------------------------------------------------------------

def set_stripe_value(array):

    array[0][0][0] = 1      # 1. Stripe PIN
    array[0][0][2] = 3      # 1. Stripe ; 1. Segment  -> Teil 1.1
    array[0][1][2] = 6      # 1. Stripe ; 2. Segment  -> Teil 1.2
    array[0][2][2] = 9      # 1. Stripe ; 3. Segment  -> Teil 1.3
    array[0][3][2] = 9      # 1. Stripe ; 4. Segment  -> Teil 1.4

    array[1][0][0] = 2      # 2. Stripe PIN
    array[1][0][2] = 8      # 2. Stripe ; 1. Segment  -> Teil 2.1 
    array[1][1][2] = 8      # 2. Stripe ; 2. Segment  -> Teil 2.2 
    array[1][2][2] = 8      # 2. Stripe ; 3. Segment  -> Teil 2.3 
    array[1][3][2] = 8      # 2. Stripe ; 4. Segment  -> Teil 2.4 

    array[2][0][0] = 3      # 2. Stripe PIN
    array[2][0][2] = 4      # 3. Stripe ; 1. Segment  -> Teil 3.1 
    array[2][1][2] = 4      # 3. Stripe ; 2. Segment  -> Teil 3.2 
    array[2][2][2] = 0      # 3. Stripe ; 3. Segment  -> Teil 3.3 
    array[2][3][2] = 0      # 3. Stripe ; 4. Segment  -> Teil 3.4 

#------------------------------------------------------------------------------

def make_stripe_array(array):
    num_segment = len(array[0])
    num_stripes = len(array)
    #print(num_segment)
    #print(num_stripes)
    for z in range(num_stripes):
        for y in range(num_segment):
            if array[z][y][2] > 0 :     # Anzahl Pixel > 0
                if y > 0:               # Ab dem 2. Segment wird der Startwert berechnet
                    array[z][y][1] = array[z][y - 1][2] + array[z][y - 1][1]
                    array[z][y][0] = array[z][0][0]     # Stripe PIN set to first item

# =============================================================================

if __name__ == "__main__":

    default_value = 0
    num_values = 3
    num_segments = 4
    num_stripes = 3

    array = three_d_array(default_value, *(num_values, num_segments, num_stripes))
    
    x = len(array[0][0])
    y = len(array[0])
    z = len(array)
        
    print(x, y, z)

    set_stripe_value(array)

    for x in range(len(array)):
        print(array[x])

    print("Build Array")
    make_stripe_array(array)

    for x in range(len(array)):
        print(array[x])
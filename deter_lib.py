def deter2x2(matrix):
    """
    function to calculate the determinant of
    the 2x2 matrix.
    The determinant of a matrix is defined as
    the upper-left element times the lower right element
    minus
    the upper-right element times the lower left element
    """
    result = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])

    # TODO: calculate the determinant of the 2x2 matrix

    return result



def deter3x3(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    result = (a*e*i) - (a*f*h) - (b*d*i) + (b*f*g) + (c*d*h) - (c*e*g)
    return result


matrix_test = [[4,1,3],[5,3,1],[8,4,2]]
print(deter3x3(matrix_test))

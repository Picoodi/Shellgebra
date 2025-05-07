from Functions import *


#This function calculates the new row of a matrix with the given number
def calculate_new_rows(row, number):
    new_row = []
    for element in row:
        new_row.append(element * number)

    return new_row


#This function take two matrix rows and subtracts them from each other and returns one new row
def subtract_rows(row0, row1):
    new_row = []
    for i in range(len(row0)):
        new_row.append(row0[i] - row1[i])

    return new_row


#This function creates the upper triangular matrix and from the given matrix and returns the new one
def matrix_zeros(matrix):
    #find the max row number
    max_row_number = 0
    for row in matrix:
        max_row_number += 1

    # find the max colum number
    max_colum_number = 0
    for colum in matrix[0]:
        max_colum_number += 1

    #going through the matrix with 2 for loops one for columns and one for rows of the matrix
    # -2 because one less of the IT counting from 0 and one because the function changes the numbers in the row one below
    for colum in range(max_colum_number -1):

        # first row always stays the same so we start at index 1
        for row in range(1, max_row_number):

            # we have the first colum always calculated with the row at index 0
            if colum == 0:
                matrix[row] = subtract_rows(calculate_new_rows(matrix[0], matrix[row][colum]),
                                            calculate_new_rows(matrix[row], matrix[0][colum]))

            # if it is the last row we break because we already changed it.
            elif row == max_row_number - 1:
                break

            #for all the other rows we just do the algorithm
            else:
                row = colum + 1  #the row where the number needs to be changed to 0, is the colum index+1.
                matrix[row] = subtract_rows(calculate_new_rows(matrix[row - 1], matrix[row][colum]),
                                            calculate_new_rows(matrix[row], matrix[row - 1][colum]))

    return matrix


Matrix = [[2, 1, -1],
          [-3,-1,2 ],
          [-1,1,2 ]
          ]

Changed_Matrix = matrix_zeros(Matrix)
print(f"Creates a new matrix of the form:")
for Row in Changed_Matrix:
    print(Row)
print("")

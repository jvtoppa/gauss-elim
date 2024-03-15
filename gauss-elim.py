### element == a11, a22, etc.

def line_multiplication_a11(augmented_matrix, element):
    total_treatment = []
   
    tt2 = []
    #while element != len(augmented_matrix):
    for rows in range(element, len(augmented_matrix) - 1):
        after_constant_treatment = []
        if augmented_matrix[rows][element] != 0:
            constant = augmented_matrix[rows + 1][element]/int(augmented_matrix[element][element])
        else:
            constant = 0

        for iterator in augmented_matrix[element]:
            
            after_constant_treatment.append(int(int(iterator)*constant))
        total_treatment.append(after_constant_treatment)
        ######
        print('tt', total_treatment)
    for l in range(0, len(total_treatment)):
        tt = []
        for f in range(0, len(total_treatment[l])):
            tt.append(augmented_matrix[l + element + 1][f] - total_treatment[l][f])
        tt2.append(tt)

       # element+= 1
    a = 0
    while a != element + 1:
        tt2.insert(0, augmented_matrix[a])
        a+= 1
    return tt2


def line_multiplication_a22(augmented_matrix):
    return line_multiplication_a11(augmented_matrix, 1)



def matrix_inputting(i, j):

    matrix_input = []
        #matrix input


    for columns in range(0, j):
        matrix_columns = []
        for rows in range(0, i):
            matrix_values = int(input('Input a' + str(rows + 1) + str(columns + 1) + ':\n'))
            matrix_columns.append(matrix_values)

        matrix_input.append(matrix_columns)

    return(matrix_input)


def main():

    print('STEP 1: Input matrix A and B to create (A|B)')
    print('NOW INPUTTING: MATRIX A')

    i = int(input('Input no. of rows:\n'))
    j = int(input('Input no. of columns:\n'))

    original_matrix = matrix_inputting(i, j)

    print('NOW INPUTTING: MATRIX B\nps: Matrix b is 1 by j in size')

    answers_matrix = matrix_inputting(1, j)
    
    for x in range(0, len(answers_matrix)):
        #TODO: Change [0] to [n] for different applications of gauss elimination

        original_matrix[x].append(answers_matrix[x][0])

    augmented_matrix = original_matrix

    constant_treatment = line_multiplication_a11(augmented_matrix, 0)
    constant_treatment_2 = line_multiplication_a22(constant_treatment)
    print(constant_treatment_2)
            

if __name__ == "__main__":
    main()

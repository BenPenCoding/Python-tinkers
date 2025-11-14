#Import the NumPy library
import numpy as np

#Define the matrix multiplication function
def matrixMult(array1, array2):

    #Initialize and fill the variables that store the shape/dimensions of the multiplication arrays
    shape1 = array1.shape
    shape2 = array2.shape

    #Initialize the product array
    array3 = np.zeros((shape1[1], shape2[0]))

    #If the matrices are conformable (multiplicand has the same number of columns as the multiplier's number of rows)
    if shape1[1] == shape2[0]:

        #Iterate through the rows of the multiplicand array
        for i in range(shape1[0]):

            #Iterate through the columns of the multiplier array
            for j in range(shape2[1]):

                #Initialize and fill the multiplicand array
                tempArray1 = array1[i]

                #Initialize the multiplier array
                tempArray2 = np.zeros(len(tempArray1))

                #Initalize a variable to store the length of the multiplicand array row length
                tempArray1Length = len(tempArray1)
                
                #Fill the multiplier array
                for k in range(tempArray1Length):

                    #Add the element to the multiplier array
                    tempArray2[k] = array2[k][j]

                #Initialize an array for the temporary products of single-array multiplication to be summed
                tempProductArray = np.zeros(tempArray1Length)
                
                #Multiply the elements of the multiplicand and multiplier arrays and add them to the product array
                for k in range(tempArray1Length):

                    #Initialize the variables from both arrays to be multiplied
                    multiplicand = tempArray1[k]
                    multiplier = tempArray2[k]

                    #Add the product of the variables to the temporary product array to sum and add to the product array
                    tempProductArray[k] = multiplicand * multiplier

                #Initalize a variable to store the sum the products of individual multiplication 
                tempSum = np.sum(tempProductArray)

                #Add the total product to the product array
                array3[i][j] = tempSum

        #Return the product array
        return array3
                
    #If the matrices are non-conformable, return an error message.             
    else:

        #Returns an error message
        return "ERROR - the matrices are not conformable."

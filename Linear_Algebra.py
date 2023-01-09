from numpy import *
import time
#This function takes linear equation Ax = b and determines if there is a unique solution set, where input A is a matrix and b is a vector
def problem1(A, b):
    if A.ndim == 2 and b.ndim == 2 and A.shape[0] == A.shape[1]: #Checking that the dimensions and shapes of the Matrix, A, and the vector, b, are the same
        if linalg.matrix_rank(A) == b.shape[0] and linalg.det(A) != 0: #If the rank of the matrix is equal to the length of the vector, returns True as there exists a solution
            return True
        else:
            return False
    else:
        return False #The function returns False if either the first or second conditions are not met

#A follow-up function that first checks if the matrix is solvable using problem1, then returns the time it takes to actually solve the system using one of two methods of the users choice. Input A again represents a matrix and b a vector
def problem2(A, b, method):
    if problem1(A, b) == False: #First checks if a solution exists and returns None if there isn't
        return None
    else:
        if method == "ge": #'ge' here stands for Gaussian elimination, which reduces the matrix to row-echelon form and then performs backwards substitution to solve the system
            start = time.perf_counter() #Marking the start time
            linalg.solve(A, b) #Solving the system
            return (time.perf_counter() - start) #Returning the time it takes the program to run by subtracting the start time from the end time
        elif method == "inv": #'inv' here stands for inverse, take the inverse of the matrix and multiply it by the vector to get the solution
            start = time.perf_counter() #Marking the start time again
            sol = (linalg.inv(A)) * b #Solving the system with the inverse method
            return (time.perf_counter() - start) #And again returning the difference in the times once the program has run to completion

#The third function that now calls the second function and returns an `array` of the coefficients of the best-fit polynomial for the runtime of Gaussian elimination or the inverse matrix method depending on the value of `method` (`"ge"` or `"inv"`). The runtime is fit to a third order polynomial
def problem3(n_array, method): #n_array represents the dimension of the matrix you want to use, and method again is either 'ge' or 'inv'
    list1 = [] #Initializing an empty list
    for i in n_array:
        A = random.random((i, i)) #Generates a random shape matrix
        b = random.random((i, 1)) #Generates a random column vector, which needs to have just 1 column
        problem2(A, b, method) #calls the second function to determine if the system has a solution, and returns its runtime for later use
        list1.append((problem2(A, b, method))) #Adds the runtimes of each iteration of the randomly generated matrices
    return polyfit(n_array, list1, 3) #Returns a polynomial of degree 3 
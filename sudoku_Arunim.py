def find_square(i,j):
    if i%3==0:
        a =i//3 -1
    else:
        a = i//3
    if j%3==0:
        b = j//3 - 1
    else:
        b = j//3
    x = 3*a+1
    y = 3*b+1
    return x,y
def check_validity(sudoku,i,j,val):
    square_list = []
    [a,b] = find_square(i,j)
    for p in range(a,a+3):
        for q in range(b,b+3):
            if sudoku[p][q] != 0:
                square_list.append(sudoku[p][q])
    row_list = sudoku[i]
    column_list = []
    for row in range(1,10):
        column_list.append(sudoku[row][j])
    if (val not in square_list and val not in row_list and val not in column_list):
        return True
    else:
        return False
def solve(sudoku,i,j):
    #print("came next")
    if i==10:
        """for c in range(1,10):
                print(sudoku[c][1:])
                print("")"""
        return True
    current_i = 0
    current_j = 0
    #print("i j",i,j)
    if (j==9):
        #print("j==9")
        current_i = i+1
        current_j = 1
    else:
        #print("else j==9")
        current_j = j+1
        current_i = i
    if sudoku[i][j]!=0:
        #print("sudoku[i][j]")
        return solve(sudoku,current_i,current_j)
    else:
        """print("val")
        print("SUDOKU")
        for i in range(1,10):
                print(sudoku[i][1:])
                print("")"""

        for val in range(1,10):
            #print("outside val",val)
            if (check_validity(sudoku,i,j,val) == True):
                #print("inside valid")
                #print("inside val",val)
                sudoku[i][j] = val
                #print("inside i j",i,j)
                """for x in range(1,10):
                        print(sudoku[x][1:])
                        print("")"""
                if solve(sudoku,current_i,current_j)==True:
                    return True
                sudoku[i][j] = 0

    return False
sudoku = [[0]]
#sudoku.append([0])
#print(sudoku)
for i in range(1,10):
    a = list(map(int,input().split()))
    sudoku.append([0])
    for j in a:
        sudoku[i].append(j)
#print(sudoku)
#print(check_validity(sudoku,1,8,3))
solve(sudoku,1,1)
print("SUDOKU SOLVER")
for i in range(1,10):
    for j in range(1,10):
        print(sudoku[i][j],end = " ")
    print(" ")

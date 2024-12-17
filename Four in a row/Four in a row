array = [[['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ],
        [ ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ],
        [ ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ],
        [ ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ],
        [ ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ],
        [ ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] , ['    '] ]]

#that is a big 2D array'! 7X6 to be exact



    
def checkH(): #checks all rows for a win 
    win = 0
    for i in range(6): #for every row 
        
        for j in range(4): #for every first 4 grids (dont need the start on the last 3)
            
            n = array[i][j] 
            
            if n == array[i][j+1] == array[i][j+2] == array[i][j+3] != ['    '] : #if the starting point and the next 3 grids are equal, someone's won
                array[i][j] = ['    ']
                array[i][j+1] = ['    ']
                array[i][j+2] = ['    ']
                array[i][j+3] = ['    '] #these empty all grids where the four in a row occured, allowing the game to continue
                win= 1
                
    return win

def checkV(): #checks all columns for a win 
    win = 0
    for i in range(7): #for every column
        
        for j in range(3): #for the first 3 grids (don't need to start on the other 3)
            
            n = array[j][i]
                
            if n == array[j+1][i] == array[j+2][i] == array[j+3][i] != ['    ']: #if the starting point and the next 3 grids are equal, someone's won
                array[j][i] = ['    ']
                array[j+1][i] = ['    ']
                array[j+2][i] = ['    ']
                array[j+3][i] = ['    '] #these empty all grids where the four in a row occured, allowing the game to continue
                win = 1
   
    return win

def checkD1(): #checks all right to left diagonals for a win
    win = 0 
    x,y,i = 5,0,0  #x is the row number, y is the column number, and i is the increment number
    while True: #used 'while True' loops and 'break commands' instead of a for loop to make it more automated 
        i = 0
        while True:
            try:  #attempt to check if the starting grid, and the three following grids are equal
                if array[x+i][y+i] == array[x+i+1][y+i+1] == array[x+i+2][y+i+2] == array[x+i+3][y+i+3] != ['    ']: #if the starting point and the next 3 grids are equal, someone's won
                    array[x+i][y+i] = ['    ']
                    array[x+i+1][y+i+1] = ['    ']
                    array[x+i+2][y+i+2] = ['    ']
                    array[x+i+3][y+i+3] = ['    '] #these empty all grids where the four in a row occured, allowing the game to continue
                    win = 1 #if equal, inform the program someone has won
                
                i +=1 #increment i
            
            except:
                break #if the program checks a grid that doesn't exist, stop checking that diagonal.     
    
        if y > 5: #if y>5 (basically if y is 6) then stop checking all right to left diagonals (stops our starting point (x,y) falling on a non-existent grid)
            break
        if x < 1:
            y +=1 #if we have reached the top row, now only increment the column number
        else:
            x -=1 #if we haven't reached the top row, increment the row number
    
    
    return win #informs the program if a win was found 

def checkD2(): #I did not comment this function as it's almost identical to the above function
    win = 0 
    x,y,i = 5,6,0  
    
    while True: 
        i = 0
        while True:
            try:  
                if array[x+i][y-i] == array[x+i+1][y-i-1] == array[x+i+2][y-i-2] == array[x+i+3][y-i-3] !=  ['    ']:
                    array[x+i][y-i] = ['    ']
                    array[x+i+1][y-i-1] = ['    ']
                    array[x+i+2][y-i-2] = ['    ']
                    array[x+i+3][y-i-3] = ['    '] #these empty all grids where the four in a row occured, allowing the game to continue
                    win = 1
                i +=1 
            
            except:
                break  
    
        if y < 1: 
            break
        if x < 1:
            y -=1 
        else:
            x -=1 
    return win

def place(array,column,counter):
    columnIndex = column -1 #finds the actual index of the column the user has chosen
    for i in range(5,-1,-1): #iterates from 5 to 0 by an increment of -1. This will find the first empty grid from the bottom
         if array[i][columnIndex][0] == '    ': #upon finding the first empty grid
             array[i][columnIndex][0] = counter #fill it
             break

def drop(pArray): #this function drops all counters down if there is a space below them
    for b in range(3): #does it thrice just to be super duper sure that nothing is left floating
        for i in range(7): #for every column
            for j in range(5): #for the first 5 rows (nothing below the 6th row)
                temp = ''
                below = ''
                if pArray[j][i][0] != '    ': #if the current grid is not empty
                    temp = pArray[j][i][0] #save the counter type (X or O) to a temporary variable 
                    below = pArray[j+1][i][0] #the grid below our current grid
                    if below == '    ': #if the below grid is empty
                        pArray[j][i][0] = '    '
                        pArray[j+1][i][0] = temp #we move down the counter
    return pArray


def check():
    if checkH() == checkV() == checkD1() == checkD2() == 0: #if all check functions return no wins, do nothing.
        pass
    else:
        return 1 #inform the program that a win has been identified

def display(array,p1score,p2score): #this function will show the user what the grid looks like
    for j in range(5):
        print(f" {array[j][0][0]} | {array[j][1][0]} | {array[j][2][0]} | {array[j][3][0]} | {array[j][4][0]} | {array[j][5][0]} | {array[j][6][0]}")
        print("-----------------------------------------------")
    print(f" {array[5][0][0]} | {array[5][1][0]} | {array[5][2][0]} | {array[5][3][0]} | {array[5][4][0]} | {array[5][5][0]} | {array[5][6][0]}")
    print("  ^      ^      ^      ^      ^      ^     ^")
    print("  1     2     3     4     5     6     7")
    print(f"\nPlayer 1's score: {p1score}, and Player 2's score: {p2score}\n")


#main
player = 1
p1score =0
p2score =0
counter = ''
print("Welcome to Connect 4 (Ben's version!)\n")
print("Player 1 will be 'O' and Player 2 will be 'X'\n") #this is just some UI business
while True:
    display(array,p1score,p2score) 
    if player == 1: counter = ' O '
    else: counter = ' X '
    print(f"\nPlayer {player}'s go. Which column would you like your '{counter}' in?")
    while True: #here I use a while loop to ensure I get correct input data, so the program doesn't request a grid that does not exist
        try: #I use error checking to first check that it is an integer
            playerChoice = int(input())
            if playerChoice > 0 and playerChoice < 8: #then I also check that the integer is between 1 and 7 inclusive
                break
            else: print(f"\nThat's not a column! Must be between 1 and 7 inclusive. Try again Player {player}")
        except: print(f"\nThat's not a column! Must be between 1 and 7 inclusive. Try again Player {player}") #error messages in case erroneous data is input
    
    place(array,playerChoice,counter) #calls the place function which places the current player's counter into the requested grid
    
    if check() == 1:
        print(f"\nPlayer {player} gets Four in a row! +1 score!\n") #if a win is identified, increase score of player
        if player == 1: #this determines which player to give the score to
            p1score +=1
        else:
            p2score +=1
    array = drop(array) #by calling the drop function, all counters are dropped if there was no counter below it
    
    if p1score > 2 or p2score> 2: #if either player has enough score to win
        print(f"\nPlayer {player} reached 3 points! GAME OVER")
        break #end the game entirely
        
    if player == 1: #this just swaps the players
        player = 2
    else:
        player = 1


    
    
    
    
    
    
    
    
    
    
    
    
            


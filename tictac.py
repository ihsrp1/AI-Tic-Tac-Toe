import sys
import os
import time
import random

def show_board(board):
    for i in range(0, 9):
            if((i % 3) == 2):
                print(board[i])
            else:
                print(board[i], end='|')

def check_winner(board):
    if(board[0] == board[1] == board[2] == 'X'):
        return 'X'
    elif(board[3] == board[4] == board[5] == 'X'):
        return 'X'
    elif(board[6] == board[7] == board[8] == 'X'):
        return 'X'
    elif(board[0] == board[4] == board[8] == 'X'):
        return 'X'
    elif(board[2] == board[4] == board[6] == 'X'):
        return 'X'
    elif(board[1] == board[4] == board[7] == 'X'):
        return 'X'
    elif(board[0] == board[3] == board[6] == 'X'):
        return 'X'
    elif(board[2] == board[5] == board[8] == 'X'):
        return 'X'
    
    if(board[0] == board[1] == board[2] == 'O'):
        return 'O'
    elif(board[3] == board[4] == board[5] == 'O'):
        return 'O'
    elif(board[6] == board[7] == board[8] == 'O'):
        return 'O'
    elif(board[0] == board[4] == board[8] == 'O'):
        return 'O'
    elif(board[2] == board[4] == board[6] == 'O'):
        return 'O'
    elif(board[1] == board[4] == board[7] == 'O'):
        return 'O'
    elif(board[0] == board[3] == board[6] == 'O'):
        return 'O'
    elif(board[2] == board[5] == board[8] == 'O'):
        return 'O'
    
    if '_' in board: 
        return '_'
    else:
        return 'tie'
    
def minimax(board, i):
    result = check_winner(board)
    if(result == 'X'):
        return -10
    elif(result == 'O'):
        return 10
    elif(result == 'tie'):
        return 0
    
    
    if(i):
        bestScore = -9999
        for j in range(0, 9):
            if(board[j] == '_'):
                board[j] = 'O'
                score = minimax(board, abs(i-1))
                board[j] = '_'
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 9999
        for j in range(0, 9):
            if(board[j] == '_'):
                board[j] = 'X'
                score = minimax(board, abs(i-1))
                board[j] = '_'
                bestScore = min(score, bestScore)
        return bestScore

    
def main():
    board = [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
    ]
    xPoints = 0
    oPoints = 0
    tiePoints = 0
    i = 0
    flagWin = False
    # 0 = X
    # 1 = O
    while 1:
        os.system('clear')
        print('Player: {}    |    Computer: {}    |    Tie: {}' .format(xPoints, oPoints, tiePoints))
        
        if(i):
            print('O\'s turn')
        else:
            print('X\'s turn')

        show_board(board)

        if(check_winner(board) == 'X'):
            print('X won!')
            xPoints+=1
            flagWin = True
            time.sleep(1)
            board = [
                '_', '_', '_',
                '_', '_', '_',
                '_', '_', '_'
            ]
        elif(check_winner(board) == 'O'):
            print('O won!')
            oPoints+=1
            flagWin = True
            time.sleep(1)
            board = [
                '_', '_', '_',
                '_', '_', '_',
                '_', '_', '_'
            ]
        elif(check_winner(board) == 'tie'):
            print('It\'s a tie!')
            tiePoints+=1
            flagWin = True
            time.sleep(1)
            board = [
                '_', '_', '_',
                '_', '_', '_',
                '_', '_', '_'
            ]


        if not flagWin:
            if(i):
                bestScore = -9999
                bestMove = 0
                print('Hmmm...')
                time.sleep(random.random())
                for j in range(0, 9):
                    if(board[j] == '_'):
                        board[j] = 'O'
                        score = minimax(board, abs(i-1))
                        board[j] = '_'
                        if score > bestScore:
                            bestScore = score
                            bestMove = j
                board[bestMove] = 'O'
                i = abs(i-1)
            else:    
                pos = int(input('Where would you like to play next: '))
                if(board[pos-1] == '_'):
                    board[pos-1] = 'X'
                    i = abs(i-1)
                else:
                    print('Invalid move... :(')
                    time.sleep(1)
        else:
            flagWin = False

        
        

main()

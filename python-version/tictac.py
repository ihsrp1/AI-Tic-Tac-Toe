import sys
import os
import time
import random
import pygame

width = 640
height = 480
screen_coords = {
    0: (156, 55),
    1: (286, 55),
    2: (416, 55),
    3: (156, 185),
    4: (286, 185),
    5: (416, 185),
    6: (156, 315),
    7: (286, 315),
    8: (416, 315)
}
white = (255, 255, 255)
red = (255, 0, 0)
pygame.init()
playFont = pygame.font.SysFont('Helvetica', 100)
textFont = pygame.font.SysFont('Helvetica', 25)
screen = pygame.display.set_mode((width, height))
total = 0

def start_game():
    pygame.display.set_caption('Tic-Tac-Toe')
    pygame.draw.line(screen, white, (255, 45), (255, 435), 3)
    pygame.draw.line(screen, white, (385, 45), (385, 435), 3)
    pygame.draw.line(screen, white, (125, 175), (515, 175), 3)
    pygame.draw.line(screen, white, (125, 305), (515, 305), 3)
    pygame.display.flip()

def show_text(text, x, y, font, color):
    text = str(text)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    
def show_board(font, board):
    for i in range(9):
        if(board[i] != '_'):
            x, y = screen_coords[i]
            show_text(board[i], x, y, font, white)
           
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

def printBoard(board):
    for i in range(0, 9):
        if((i % 3) == 2):
            print(board[i])
        else:
            print(board[i], end='|')

def minimax(board, i, alpha, beta, it):
    global total
    total += 1
    result = check_winner(board)
    if(result == 'X'):
        return -1
    elif(result == 'O'):
        return 1
    elif(result == 'tie'):
        return 0
    
    # print(i)
    
    if(i): # MAX
        bestScore = -9999
        for j in range(0, 9):
            if(board[j] == '_'):
                board[j] = 'O'
                if it < 7:
                    os.system('clear')
                    printBoard(board)
                    time.sleep(1/(it**2))
                score = minimax(board, abs(i-1), alpha, beta, it)
                if it < 7:
                    os.system('clear')
                    printBoard(board)
                    time.sleep(1/(it**2))
                board[j] = '_'
                bestScore = max(score, bestScore)
                alpha = max(score, alpha)
                if beta <= alpha:
                    break
        return bestScore
    else: # MIN
        bestScore = 9999
        for j in range(0, 9):
            if(board[j] == '_'):
                board[j] = 'X'
                if it < 7:
                    os.system('clear')
                    printBoard(board)
                    time.sleep(1/(it**2))
                score = minimax(board, abs(i-1), alpha, beta, it)
                board[j] = '_'
                if it < 7:
                    os.system('clear')
                    printBoard(board)
                    time.sleep(1/(it**2))
                bestScore = min(score, bestScore)
                beta = min(score, beta)
                if beta <= alpha:
                    break
        return bestScore

def getBox(x, y):
    if(x >= 125 and x < 254):
        if(y >= 45 and y < 174):
            return 0
        elif(y > 176 and y < 304):
            return 3
        elif(y > 306 and y <= 435):
            return 6
    elif(x > 256 and x < 384):
        if(y >= 45 and y < 174):
            return 1
        elif(y > 176 and y < 304):
            return 4
        elif(y > 306 and y <= 435):
            return 7
    elif(x > 386 and x <= 515):
        if(y >= 45 and y < 174):
            return 2
        elif(y > 176 and y < 304):
            return 5
        elif(y > 306 and y <= 435):
            return 8

    return -1

def wait_for_play():
    x, y = 0, 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                return x, y

def main():
    global total
    total = 0
    start_game()

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
        text_points = 'Player: {}    |    Computer: {}    |    Tie: {}'.format(xPoints, oPoints, tiePoints)
        screen = pygame.display.set_mode((width, height))
        start_game()
        show_board(playFont, board)
        show_text(text_points, 125, 0, textFont, white)
        

        if(check_winner(board) == 'X'):
            print('X won!')
            show_text('X won!', 280, 436, textFont, white)
            pygame.display.flip()
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
            show_text('O won!', 280, 436, textFont, white)
            pygame.display.flip()
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
            show_text('It\'s a tie!', 270, 436, textFont, white)
            pygame.display.flip()
            tiePoints+=1
            flagWin = True
            time.sleep(1)
            board = [
                '_', '_', '_',
                '_', '_', '_',
                '_', '_', '_'
            ]
        else:
            show_text(('O\'s turn' if i == 1 else 'X\'s turn'), 280, 436, textFont, white)
            pygame.display.flip()


        if not flagWin:
            if(i):
                bestScore = -9999
                bestMove = 0
                # print('Hmmm...')
                time.sleep(random.random())
                it = board.count('_')
                for j in range(0, 9):
                    if(board[j] == '_'):
                        board[j] = 'O'
                        score = minimax(board, abs(i-1), -9999, 9999, it)
                        board[j] = '_'
                        if score > bestScore:
                            bestScore = score
                            bestMove = j
                board[bestMove] = 'O'
                i = abs(i-1)
            else:
                x, y = wait_for_play()
                move = getBox(x, y)
                #move = int(input('Where would you like to play next: '))
                if(move != -1):
                    if(board[move] == '_'):
                        board[move] = 'X'
                        i = abs(i-1)
                    else:
                        print('Invalid move... :(')
                        time.sleep(1)
        else:
            flagWin = False
        print(total)
        # time.sleep(1)
        total = 0
        
        

main()

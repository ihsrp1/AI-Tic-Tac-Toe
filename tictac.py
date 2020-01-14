import sys
import os
import time
import random
import pygame


width = 640
height = 480

white = (255, 255, 255)

def start_game(screen):
    pygame.display.set_caption('Tic-Tac-Toe')
    pygame.draw.line(screen, white, (255, 45), (255, 435), 3)
    pygame.draw.line(screen, white, (385, 45), (385, 435), 3)
    pygame.draw.line(screen, white, (125, 175), (515, 175), 3)
    pygame.draw.line(screen, white, (125, 305), (515, 305), 3)
    pygame.display.flip()

def show_text(screen, text, x, y, font):
    text = str(text)
    text = font.render(text, True, white)
    screen.blit(text, (x, y))

def show_board(screen, font, board):
    for i in range(0, 9):
            if((i % 3) == 2):
                print(board[i])
            else:
                print(board[i], end='|')

    if(board[0] != '_'):
        show_text(screen, board[0], 157, 55, font)
    if(board[1] != '_'):
        show_text(screen, board[1], 287, 55, font)
    if(board[2] != '_'):
        show_text(screen, board[2], 417, 55, font)
    if(board[3] != '_'):
        show_text(screen, board[3], 157, 185, font)
    if(board[4] != '_'):
        show_text(screen, board[4], 287, 185, font)
    if(board[5] != '_'):
        show_text(screen, board[5], 417, 185, font)
    if(board[6] != '_'):
        show_text(screen, board[6], 157, 315, font)
    if(board[7] != '_'):
        show_text(screen, board[7], 287, 315, font)
    if(board[8] != '_'):
        show_text(screen, board[8], 417, 315, font)
        
        

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
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    playFont = pygame.font.SysFont('Helvetica', 100)
    textFont = pygame.font.SysFont('Helvetica', 25)


    start_game(screen)

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
            text_turn = 'O\'s turn'
        else:
            print('X\'s turn')
            text_turn = 'X\'s turn'


        text_points = 'Player: {}    |    Computer: {}    |    Tie: {}'.format(xPoints, oPoints, tiePoints)
        screen = pygame.display.set_mode((width, height))
        start_game(screen)
        show_board(screen, playFont, board)
        show_text(screen, text_points, 125, 0, textFont)
        

        if(check_winner(board) == 'X'):
            print('X won!')
            show_text(screen, 'X won!', 280, 436, textFont)
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
            show_text(screen, 'O won!', 280, 436, textFont)
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
            show_text(screen, 'It\'s a tie!', 270, 436, textFont)
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
            show_text(screen, text_turn, 280, 436, textFont)
            pygame.display.flip()


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
                x, y = wait_for_play()
                move = getBox(x, y)
                #move = int(input('Where would you like to play next: '))
                if(board[move] == '_'):
                    board[move] = 'X'
                    i = abs(i-1)
                else:
                    print('Invalid move... :(')
                    time.sleep(1)
        else:
            flagWin = False

        
        

main()

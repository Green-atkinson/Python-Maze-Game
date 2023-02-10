import curses 
import time 
import sys

import continueQuit

def two():
    print("LEVEL THREE")
    print("FINAL ROUND")
    print("")
    print("Collect all 9 letters to win the game!")
    print("4/9 of the letters are lower-case 'x'. 3/9 are punctuation marks.")
    print("Ready? GO!")
    print("")
    continueQuit.contQuit()

    #initializes a screen, stored in variable
    stdscr = curses.initscr()

    #prompts that put curses into the appropriate operating settings 
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    #initializes a variable to count the number of letters collected
    letter_counter = 0
    stdscr.refresh()

    #add an x to the screen
    stdscr.addstr(1, 1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    stdscr.addstr(2, 1, "Xo   X   Xx X XXX      XX   X        XX   XX")
    stdscr.addstr(3, 1, "XX X    X X    X X.XX XX  X   X  X X X  X XX")
    stdscr.addstr(4, 1, "X X XX X X XX X   X X  X X  XX X X  X  X   X")
    stdscr.addstr(5, 1, "X      X    X    X    X X  XX X  XX/XsXX X X")
    stdscr.addstr(6, 1, "X XX XX X X   X   X  X     X      XX X   X X")
    stdscr.addstr(7, 1, "X   X  X   XXX XxX X   X X XX  X  X  X  X  X")
    stdscr.addstr(8, 1, "X X   X   XX   XX X   XxX       X      X  XX")
    stdscr.addstr(9, 1, "XX  XX   X  XX  X X  X  XX   XX  X   XX  X~X")
    stdscr.addstr(10,1, "X  X   X      X     X  X X X  X X  XX X X  X")
    stdscr.addstr(11,1, "X    X X X XX   X X   Xx   XX  Xr XX  X    X")
    stdscr.addstr(12,1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    stdscr.refresh()

    #x- and y- coordinates of o & y
    ox = 2
    oy = 2
    stdscr.addch(oy, ox, 'o')

    #x- and y- coordinates of each letter
    x1x = 11
    x1y = 2
    stdscr.addch(x1y, x1x, 'x') 
    stdscr.refresh()
    
    punc1x = 19
    punc1y = 3
    stdscr.addch(punc1y, punc1x, '.') 
    stdscr.refresh()
    
    punc2x = 36
    punc2y = 5
    stdscr.addch(punc2y, punc2x, '/') 
    stdscr.refresh()

    sx = 38
    sy = 5
    stdscr.addch(sy, sx, 's')
    stdscr.refresh()

    x2x = 17
    x2y = 7
    stdscr.addch(x2y, x2x, 'x') 
    stdscr.refresh()
    
    x3x = 24
    x3y = 8
    stdscr.addch(x3y, x3x, 'x') 
    stdscr.refresh()

    punc3x = 43
    punc3y = 9
    stdscr.addch(punc3y, punc3x, '~') 
    stdscr.refresh()

    x4x = 24
    x4y = 11
    stdscr.addch(x4y, x4x, 'x') 
    stdscr.refresh()

    rx = 33
    ry = 11
    stdscr.addch(ry, rx, 'r')
    stdscr.refresh()

    #start the maze
    user_input = stdscr.getch()

    if user_input == ord('q'):
        sys.exit()
        curses.endwin()

    while user_input != ord('q'):

        #move down
        if user_input == ord('s') and chr(stdscr.inch(oy + 1, ox)) != 'X' and oy + 1 < 45:
            stdscr.addch(oy, ox, ' ')
            oy += 1 
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()

        #move up
        if user_input == ord('w') and chr(stdscr.inch(oy - 1, ox)) != 'X' and oy - 1 < 45:
            stdscr.addch(oy, ox, ' ')
            oy -= 1 
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()

        #move left
        if user_input == ord('a') and chr(stdscr.inch(oy, ox - 1)) != 'X' and ox - 1 < 45:
            stdscr.addch(oy, ox, ' ')
            ox -= 1
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()
        
        #move right
        if user_input == ord('d') and chr(stdscr.inch(oy, ox + 1)) != 'X' and ox + 1 < 45:
            stdscr.addch(oy, ox, ' ')
            ox += 1 
            stdscr .addch(oy, ox, 'o')
            stdscr.refresh()

        #To win the game, get o to touch all other letters 
        if oy == x1y and ox == x1x: 
            stdscr.addch(x1y, x1x, ' ')

            #count the number of letters collected 
            letter_counter += 1 
            stdscr.refresh()

            #reset the x and y coordinates of letter so it doesn't over count
            x1x = 0
            x1y = 0
            
        if oy == punc1y and ox == punc1x: 
            stdscr.addch(punc1y, punc1x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            punc1x = 0
            punc1y = 0

        if oy == punc2y and ox == punc2x:
            stdscr.addch(punc2y, punc2x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            punc2x = 0
            punc2y = 0
        
        if oy == sy and ox == sx: 
            stdscr.addch(sy, sx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            sx = 0
            sy = 0
        
        if oy == x2y and ox == x2x: 
            stdscr.addch(x2y, x2x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            x2x = 0
            x2y = 0
        
        if oy == x3y and ox == x3x: 
            stdscr.addch(x3y, x3x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            x3x = 0
            x3y = 0
        
        if oy == punc3y and ox == punc3x: 
            stdscr.addch(punc3y, punc3x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            punc3x = 0
            punc3y = 0
        
        if oy == x4y and ox == x4x: 
            stdscr.addch(x4y, x4x, ' ')
            letter_counter += 1 
            stdscr.refresh()
            x4x = 0
            x4y = 0
        
        if oy == ry and ox == rx: 
            stdscr.addch(ry, rx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            rx = 0
            ry = 0

        if letter_counter >= 9:
            #Passed level three
            stdscr.clear()
            stdscr.refresh()
            break

        #asks for the next move from user
        stdscr.refresh()
        user_input = stdscr.getch()

    #ends program
    curses.endwin()
        
import curses 
import time 
import sys

import continueQuit

def two():
    print("LEVEL TWO")
    print("")
    print("Collect all 6 letters to move on to the next level.")
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
    stdscr.addstr(1, 1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") 
    stdscr.addstr(2, 1, "Xo X X      X XXX     XX     mX wX")
    stdscr.addstr(3, 1, "XX  XXcXX X  XXX  XX  XXX XXXX  XX")
    stdscr.addstr(4, 1, "XiX  XX X X XXXX X hX XXX  X   X X")
    stdscr.addstr(5, 1, "X   X     X    X X X  XX  XXXX  XX")
    stdscr.addstr(6, 1, "XX XXX X XXXXX      X X  XX   X  X")
    stdscr.addstr(7, 1, "X   bX X X  X XXXXXXX   XX  X  X X")
    stdscr.addstr(8, 1, "X XXXX X XX X   XX   XXX   XXX   X")
    stdscr.addstr(9, 1, "X      X      X    X      XXXXXXXX")
    stdscr.addstr(10, 1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    stdscr.refresh()

    #x- and y- coordinates of o & y
    ox = 2
    oy = 2
    stdscr.addch(oy, ox, 'o')

    #x- and y- coordinates of each letter
    ix = 2
    iy = 4
    stdscr.addch(iy, ix, 'i') 
    stdscr.refresh()
    
    bx = 5
    by = 7
    stdscr.addch(by, bx, 'b') 
    stdscr.refresh()
    
    cx = 7
    су = 3
    stdscr.addch(cy, cx, 'c') 
    stdscr.refresh()

    hx = 20
    hy = 4
    stdscr.addch(hy, hx, 'h')
    stdscr.refresh()

    mx = 30
    my = 2
    stdscr.addch(my, mx, 'm')
    stdscr.refresh()

    wx = 33
    wy = 2
    stdscr.addch(hy, hx, 'w')
    stdscr.refresh()

    #start the maze
    user_input = stdscr.getch()

    if user_input == ord('q'):
        sys.exit()
        curses.endwin()

    while user_input != ord('q'):

        #move down
        if user_input == ord('s') and chr(stdscr.inch(oy + 1, ox)) != 'X' and oy + 1 < 35:
            stdscr.addch(oy, ox, ' ')
            oy += 1 
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()

        #move up
        if user_input == ord('w') and chr(stdscr.inch(oy - 1, ox)) != 'X' and oy - 1 < 35:
            stdscr.addch(oy, ox, ' ')
            oy -= 1 
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()

        #move left
        if user_input == ord('a') and chr(stdscr.inch(oy, ox - 1)) != 'X' and ox - 1 < 35:
            stdscr.addch(oy, ox, ' ')
            ox -= 1
            stdscr.addch(oy, ox, 'o') 
            stdscr.refresh()
        
        #move right
        if user_input == ord('d') and chr(stdscr.inch(oy, ox + 1)) != 'X' and ox + 1 < 35:
            stdscr.addch(oy, ox, ' ')
            ox += 1 
            stdscr .addch(oy, ox, 'o')
            stdscr.refresh()

        #To win the game, get o to touch all other letters 
        if oy == iy and ox == ix: 
            stdscr.addch(iy, ix, ' ')

            #count the number of letters collected 
            letter_counter += 1 
            stdscr.refresh()

            #reset the x and y coordinates of letter so it doesn't over count
            ix = 0
            iy = 0
            
        if oy == by and ox == bx: 
            stdscr.addch(by, bx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            bx = 0
            by = 0

        if oy == cy and ox == cx:
            stdscr.addch(cy, cx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            cx = 0
            cy = 0
        
        if oy == hy and ox == hx: 
            stdscr.addch(hy, hx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            hx = 0
            hy = 0
        
        if oy == my and ox == mx: 
            stdscr.addch(my, mx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            mx = 0
            my = 0
        
        if oy == wy and ox == wx: 
            stdscr.addch(wy, wx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            wx = 0
            wy = 0

        if letter_counter >= 6:
            #Passed level two
            stdscr.clear()
            stdscr.refresh()
            break

        #asks for the next move from user
        stdscr.refresh()
        user_input = stdscr.getch()

    #ends program
    curses.endwin()
        
#lets me use the curses module & sleep 
import curses 
import time 
import sys

import continueQuit

def one():
    print("LEVEL ONE")
    print ("")
    print("Collect all 4 letters to move on to the next level.")
    print("Ready? GO!")
    print("")
    continueQuit.contQuit()

    #initializes a screen, stored in variable stdscr 
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
    stdscr.addstr(2, 1, "X  X       XXXX X    X X XX X    X")
    stdscr.addstr(3, 1, "XX  X X XX         XX X X XX  XXXX")
    stdscr.addstr(4, 1, "XX  X X XXXXXXX XX  X   X XXX    X")
    stdscr.addstr(5, 1, "XXX XXX  XXXXX  XXX   X   XX  X XX")
    stdscr.addstr(6, 1, "XXX XXXX      X    XXX XX  X XXX X")
    stdscr.addstr(7, 1, "X   X    XXXX X XX XX  XX      X X")
    stdscr.addstr(8, 1, "X XXX X    XX X XX   XX X XXXX X X")
    stdscr.addstr(9, 1, "X     XXXX    X    X XXXX    X   X")
    stdscr.addstr(10, 1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    stdscr.refresh()

    #x- and y- coordinates of o & y
    ox = 2
    oу = 2
    stdscr.addch(oy, ox, 'o')

    #x- and y- coordinates of each letter
    yx = 21
    yy = 9
    stdscr.addch(yy, yx, 'y') 
    stdscr.refresh()

    gx = 24
    gy = 3
    stdscr.addch(gy, gx, 'g') 
    stdscr.refresh()

    tx = 14
    ty = 8 
    stdscr.addch(ty, tx, 't')
    stdscr.refresh()
    
    px = 33
    ру = 6
    stdscr.addch(py, px, 'p') 
    stdscr.refresh()

    #start the maze 
    user_input = stdscr.getch()
    
    if user_input == ord('q'):
        curses.endwin()
        sys.exit()
    while user_input != ord('q'):

        #move down
        if user_input == ord('s') and chr(stdscr.inch(oy + 1, ox)) != 'X' and oy + 1 < 35:
            stdscr.addch(oy, ox, ' ')
            оу += 1
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
        if user_input - ord('d') and chr(stdscr.inch(oy, ox + 1)) != 'X' and ox + 1 < 35:
            stdscr.addch(oy, ox, ' ')
            ox += 1
            stdscr.addch(oy, ox, 'o')
            stdscr.refresh()

        #To win the game, get o to touch all other letters 
        if oy == yy and ox == yx: 
            stdscr. addch(yy, yx, ' ')

            #count the number of letters collected
            letter_counter += 1 
            stdscr.refresh()
                
            #reset the x and y coordinates of letter so it doesn't over count
            yx = 0    
            yy = 0

        if oy == gy and ox == gx: 
            stdscr.addch(gy, gx, ' ')
            letter_counter += 1 
            stdscr.refresh()
            gx = 0
            gy = 0

        if ov == ty and ox == tx: 
            stdscr.addch(ty, tx, ' ')
            letter_counter += 1
            stdscr.refresh()
            tx = 0
            ty = 0

        if oy == py and ox == px: 
            stdscr.addch(py, px, ' ')
            letter_counter += 1 
            stdscr.refresh()
            px = 0
            ру = 0

        if letter_counter >= 4:
            #Passed level one
            stdscr.clear()
            stdscr.refresh()
            break

        #asks for the next move from user 
        stdscr.refresh()
        user_input = stdscr.getcho=()
    
    #end program  
    curses.endwin()
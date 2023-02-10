import sys

def contQuit():
    continue_quit = input("Press SPACE_BAR to continue or 'q' to quit.\n")
    while continue_quit != ' ':
        if continue_quit == 'q':
            sys.exit()
        else:
            print("Please enter a valid character\n")
            continue_quit = input("Press SPACE_BAR to continue or 'q' to quit.\n")
    print("\n")
    return continue_quit
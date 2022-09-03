import sys
import time
import random
import keyboard
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# To run and test in cmd "C:/Users/Meina Jia/AppData/Local/Programs/Python/Python310/python.exe" "c:/Users/Meina Jia/Google Drive/Downloads/Jasosc/python.py"
user = input("Please enter your name_>>> ")
print(Back.BLUE + Fore.RED + "JasoPC copyright 2022")
print(Back.BLUE + Fore.RED + "Current Version V.1.4.9")
time.sleep(0.5)
print(Back.BLUE + Fore.RED + "BOOTING UP 0%")
time.sleep(1)
print(Back.BLUE + Fore.RED + "BOOTING UP 25%")
time.sleep(1)
print(Back.BLUE + Fore.RED + "BOOTING UP 75%")
time.sleep(0.5)
print(Back.BLUE + Fore.RED + "BOOTING UP 100%")
print(Back.BLUE + Fore.RED + "ALL DONE")
time.sleep(0.3)
print(Back.BLUE + Fore.RED + "configuring[...]")
time.sleep(0.5)

st = 1
while st < 501:
    print(st)
    st = st + 1
print(Back.BLUE + Fore.RED + "ALL DONE")
print(Back.BLUE + Fore.RED + "LOGIN")
is_running_login = True
while is_running_login:
    l_user = input("Please enter your name_>>> ")
    if l_user != user:
        print(Back.RED + Fore.LIGHTYELLOW_EX + "FAILED INCORECCT NAME")
    elif l_user == user:
        print("Thanks")
        print("Hello, Welcome to JasoPC 1.0")
        print("Type help for commands you can do on your new JasoPC 1.0")
        j = True
        while j:
            cmd = input(Fore.LIGHTGREEN_EX + ">>> ")
            cmd = cmd.upper()
            if cmd == "HELP":
                print(Fore.YELLOW + f'''
                Hi {user} welcome to the help menu
                To do a command just type what is after the = sign in the guide
                Commands :
                    PC info = pc_info
                    Local time = time
                    Random number genorator = random_num_gen
                    2 number multiplacation calculator = mult_calc
                    Typing game = type_game
                    Snake game = snake_game
                    Shutdown = shutdown
                    Draw any box or rectangle = box_draw
                    ''')
            elif cmd == "SNAKE_GAME":
                import pygame
                ask_for_speed = int(input("Choose a speed (program will crash if you do not put in a number or if you put 0 or a nehgitive it will also crash): "))
                snake_speed = ask_for_speed
                print("Game running in sepreate window...")
                # Window size
                window_x = 700
                window_y = 600
                
                # defining colors
                black = pygame.Color(0, 0, 0)
                white = pygame.Color(255, 255, 255)
                red = pygame.Color(255, 0, 0)
                green = pygame.Color(0, 255, 0)
                blue = pygame.Color(0, 0, 255)
                
                # Initialising pygame
                pygame.init()
                
                # Initialise game window
                pygame.display.set_caption('JasoPC Snake Game')
                game_window = pygame.display.set_mode((window_x, window_y))
                
                # FPS (frames per second) controller
                fps = pygame.time.Clock()
                
                # defining snake default position
                snake_position = [100, 50]
                
                # defining first 4 blocks of snake body
                snake_body = [[100, 50],
                            [90, 50],
                            [80, 50],
                            [70, 50]
                            ]
                # fruit position
                fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                random.randrange(1, (window_y//10)) * 10]
                
                fruit_spawn = True
                
                # setting default snake direction towards
                # right
                direction = 'RIGHT'
                change_to = direction
                
                # initial score
                score = 0
                
                # displaying Score function
                def show_score(choice, color, font, size):
                
                    # creating font object score_font
                    score_font = pygame.font.SysFont(font, size)
                    
                    # create the display surface object
                    # score_surface
                    score_surface = score_font.render('Score : ' + str(score), True, color)
                    
                    # create a rectangular object for the text
                    # surface object
                    score_rect = score_surface.get_rect()
                    
                    # displaying text
                    game_window.blit(score_surface, score_rect)
                
                # game over function
                def game_over():
                
                    # creating font object my_font
                    my_font = pygame.font.SysFont('Arial', 30)
                    
                    # creating a text surface on which text
                    # will be drawn
                    game_over_surface = my_font.render(
                        'GAME OVER ): Your Score is : ' + str(score), True, red)
                    
                    # create a rectangular object for the text
                    # surface object
                    game_over_rect = game_over_surface.get_rect()
                    
                    # setting position of the text
                    game_over_rect.midtop = (window_x/2, window_y/4)
                    
                    # blit will draw the text on screen
                    game_window.blit(game_over_surface, game_over_rect)
                    pygame.display.flip()
                    
                    # after 2 seconds we will quit the program
                    time.sleep(3)
                    
                    # deactivating pygame library
                    pygame.quit()
                    
                    # quit the program
                    quit()
                
                
                # Main Function
                while True:
                    
                    # handling key events
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                change_to = 'UP'
                            if event.key == pygame.K_DOWN:
                                change_to = 'DOWN'
                            if event.key == pygame.K_LEFT:
                                change_to = 'LEFT'
                            if event.key == pygame.K_RIGHT:
                                change_to = 'RIGHT'
                
                    # If two keys pressed simultaneously
                    # we don't want snake to move into two
                    # directions simultaneously
                    if change_to == 'UP' and direction != 'DOWN':
                        direction = 'UP'
                    if change_to == 'DOWN' and direction != 'UP':
                        direction = 'DOWN'
                    if change_to == 'LEFT' and direction != 'RIGHT':
                        direction = 'LEFT'
                    if change_to == 'RIGHT' and direction != 'LEFT':
                        direction = 'RIGHT'
                
                    # Moving the snake
                    if direction == 'UP':
                        snake_position[1] -= 10
                    if direction == 'DOWN':
                        snake_position[1] += 10
                    if direction == 'LEFT':
                        snake_position[0] -= 10
                    if direction == 'RIGHT':
                        snake_position[0] += 10
                
                    # Snake body growing mechanism
                    # if fruits and snakes collide then scores
                    # will be incremented by 10
                    snake_body.insert(0, list(snake_position))
                    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                        score += 1
                        fruit_spawn = False
                    else:
                        snake_body.pop()
                        
                    if not fruit_spawn:
                        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                        random.randrange(1, (window_y//10)) * 10]
                        
                    fruit_spawn = True
                    game_window.fill(black)
                    
                    for pos in snake_body:
                        pygame.draw.rect(game_window, green,
                                        pygame.Rect(pos[0], pos[1], 10, 10))
                    pygame.draw.rect(game_window, red, pygame.Rect(
                        fruit_position[0], fruit_position[1], 10, 10))
                
                    # Game Over conditions
                    if snake_position[0] < 0 or snake_position[0] > window_x-10:
                        game_over()
                    if snake_position[1] < 0 or snake_position[1] > window_y-10:
                        game_over()
                
                    # Touching the snake body
                    for block in snake_body[1:]:
                        if snake_position[0] == block[0] and snake_position[1] == block[1]:
                            game_over()
                
                    # displaying score countinuously
                    show_score(1, white, 'times new roman', 20)
                
                    # Refresh game screen
                    pygame.display.update()
                
                    # Frame Per Second /Refresh Rate
                    fps.tick(snake_speed)

            elif cmd == "BOX_DRAW":
                running = True
                while running:
                    try:
                        rows = int(input("How many rows: "))
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "WARNING! You typed a decimal or a letter!")
                    try:
                        columns = int(input("How many columns: "))
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "WARNING! You typed a decimal or a letter!")
                    try:
                        if rows >= 1000:
                            print(Fore.YELLOW + Back.RED + "WARNING THIS WILL TAKE A LONG TIME DUE TO A LARGE AMT OF ROWS!")
                    except NameError:
                        print(Fore.YELLOW + Back.RED + "WARNING! You typed a decimal or a letter!")
                    symbol = input("Enter a symbol to use: ")
                    try:
                        for i in range(rows):
                            for j in range(columns):
                                print(symbol, end="")
                            print()
                    except NameError:
                        print(Fore.YELLOW + Back.RED + "WARNING! You typed in a decimal or a letter!")
                    runorno = input("Keep Drawing more boxes? (y) (n): ").upper()
                    if runorno == "Y":
                        running = True
                    elif runorno == "N":
                        running = False
                        print("Done! Type Help for more commands!")
                    else:
                        print("I do not understand")
            elif cmd == "RACING_GAME":
                print("Racing game is comming out in V.1.5")
            elif cmd == "SHUTDOWN":
                print(Back.BLUE + Fore.RED + "configuring shutdown[...]")
                time.sleep(1.5)
                bt = 1
                while bt < 201:
                    print(Fore.RED + f"{bt}")
                    bt = bt + 1
                print(Back.BLUE + Fore.RED + "ALL DONE")
                sys.exit()
            elif cmd == "TIME":
                w_time = time.time()
                print(time.ctime(w_time))
            elif cmd == "PC_INFO":
                pc_version = Fore.CYAN + "V.1.4.9"
                print(f"Current Version {pc_version}")
                print(Fore.CYAN + f'''
                What does the numbers in {pc_version} mean? 
                  - The first number means overall version 
                  - The second number is the version of that overall version 
                  - The 3rd number repesents the amount of the 2nd numbers version is completed
                ''')
            elif cmd == "RANDOM_NUM_GEN":
                rngen_is_running = True
                while rngen_is_running:
                    print("Welcome to random number Genorator!")
                    try:
                        ran_num1 = int(input("Please select your first number: "))
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "Oops!  Decimals are not supported! Support comming in V.1.5, OR You Put in Nothing, OR you put in a letter!")
                    try:
                        ran_num2 = int(input("please select your second number: "))
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "Oops!  Decimals are not supported! Support comming in V.1.5, OR You Put in Nothing!, OR you put in a letter!")
                    try:
                        print(Fore.YELLOW + Back.RED + f"Your random number between {ran_num1} and {ran_num2} is {random.randint(ran_num1,ran_num2)}")
                    except NameError:
                        print(Fore.YELLOW + Back.RED + "Oops! Your numbers were either decimals or fractions, or something else, OR You Put in Nothing, OR you put in a letter!! we will try to fix this before update 2.0!")
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "Oops! Your First number was smaller than the second! try flipping them and try again!")
                    more_gen = input("Do you want to generate another number? (y) (n): ").upper()
                    if more_gen == "Y":
                        rngen_is_running = True
                    elif more_gen == "N":
                        rngen_is_running = False
                        print("You Quit Random Number Genorator Type Help For More Commands.")
                    else:
                        print("I did not understand")

            elif cmd == "MULT_CALC":
                is_running_mult = True
                while is_running_mult:
                    mcalcnum1 = input("Choose a number: ")
                    mcalcnum2 = input("Choose your second number: ")
                    if mcalcnum1 == "":
                        mcalcnum1 = 0
                    if mcalcnum2 == "":
                        mcalcnum2 = 0
                    try:
                        calc_mult_res = int(mcalcnum1) * int(mcalcnum2)
                        print(f"You got {calc_mult_res}")
                    except ValueError:
                        print(Fore.YELLOW + Back.RED + "Oops!  Decimals are not supported! Or You Put In A letter! Support comming in V.1.5")
                    do_more_mult = input("Do you want to do more? (y) (n): ")
                    do_more_mult = do_more_mult.upper()
                    if do_more_mult == "Y":
                        is_running_mult = True
                    else: 
                        print("Done! Hope you wern't cheating on your math exam ):< , Type help for more commands")
                        is_running_mult = False
            elif cmd == "TYPE_GAME":
                TG_is_Running= True
                while TG_is_Running:
                    difficulty = input("How hard? E, M or, H (to quit press Q): ")
                    difficulty = difficulty.upper()
                    if difficulty == "E":
                        print("Easy mode")
                        print("Type, Hello, this is me and this is me, I walked to the store and saw an elephant and I was happy. The end")
                        E_1sent = input("Type. > ")
                        if E_1sent == "Hello, this is me and this is me, I walked to the store and saw an elephant and I was happy. The end":
                            print(Fore.GREEN + "You passed")
                        else:
                            print(Fore.LIGHTRED_EX + "FAIL")
                    elif difficulty == "M":
                        print("Moderate mode")
                        print("Type, The smart Teach went to McDonalds and stepped on a crack the pack she was holding cracked. While the manager saw her he also had a cracked cracker pack, and then the moo cow said hi. So the bob went shy.")
                        E_2sent = input("Type. > ")
                        if E_2sent == "The smart Teach went to McDonalds and stepped on a crack the pack she was holding cracked. While the manager saw her he also had a cracked cracker pack, and then the moo cow said hi. So the bob went shy.":
                            print("You passed")
                        else:
                            print(Fore.LIGHTRED_EX + "FAIL")
                    elif difficulty == "H":
                        print("Hard Mode.")
                        print("Type, One morning I met an elephant in my pajamas. How he got into my pajamas I'll never know. The horse raced past the barn fell.  The complex houses married and single soldiers and their families. Anyone who feels that if so many more students whom we haven’t actually admitted are sitting in on the course than ones we have that the room had to be changed, then probably auditors will have to be excluded, is likely to agree that the curriculum needs revision.")
                        E_3sent = input("Type. > ")
                        if E_3sent == "One morning I met an elephant in my pajamas. How he got into my pajamas I'll never know. The horse raced past the barn fell.  The complex houses married and single soldiers and their families. Anyone who feels that if so many more students whom we haven’t actually admitted are sitting in on the course than ones we have that the room had to be changed, then probably auditors will have to be excluded, is likely to agree that the curriculum needs revision.":
                            print("You passed")
                        else:
                            print(Fore.LIGHTRED_EX + "FAIL")
                    elif difficulty == "Q":
                        print("QUIT, please type help for more commands.")
                        break
                    else:
                        print("I did not understand")
            else:
                print(Fore.LIGHTRED_EX + Back.YELLOW + "Invilad input, please type something I can understand, if you do not know what to type please type help.")
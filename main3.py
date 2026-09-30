import pygame,sys,time,random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Alice In Borderland")

clock = pygame.time.Clock()

State = "MENU"

#Buttons
Play_button = pygame.Rect((300,250,200,50))
Quit_button_Menu = pygame.Rect((300,350,200,50))
Back_Game = pygame.Rect((300,450,200,50))
Single_Player = pygame.Rect((300,250,200,50))
Multi_Player = pygame.Rect((300,350,200,50))
input = pygame.Rect((300,350,200,50))
Play_Again = pygame.Rect((300,500,200,50))

#variables
input_text = ""
player_number = 0
machine_number = 0
AI_number1 = 0
AI_number2 = 0
AI_number3 = 0

#wins
player1_life = 0
AI_life1 = 0
AI_life2 = 0
AI_life3 = 0


#Font
font = pygame.font.SysFont("Arial",40)

last_click_time = -100
running = True
while running:
    current_time = pygame.time.get_ticks()

    # Finding mouse position and detecting quit event
    mouse_pos = pygame.mouse.get_pos()   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_time - last_click_time > 100:
            # event logic for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if State == "MENU":
                    if Play_button.collidepoint(mouse_pos):
                        State = "GAME"
                        last_click_time = current_time
                    elif Quit_button_Menu.collidepoint(mouse_pos):
                        running = False
                elif State == "GAME":
                    if Single_Player.collidepoint(mouse_pos):
                        State = "SINGLE_PLAYER"
                        last_click_time = current_time
                    elif Multi_Player.collidepoint(mouse_pos):
                        State = "MULTIPLAYER"
                        last_click_time = current_time
                    elif Back_Game.collidepoint(mouse_pos):
                        State = "MENU"
                elif State == "SINGLE_PLAYER":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Back_Game.collidepoint(mouse_pos):
                            State = "GAME"
                elif State == "RESULT":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Play_Again.collidepoint(mouse_pos):
                            State = "SINGLE_PLAYER"
                            input_text = ""
                elif State == "MULTIPLAYER":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Back_Game.collidepoint(mouse_pos):
                            State = "GAME"
        # event logic for inputting numbers    
        if event.type == pygame.KEYDOWN:
            if State == "SINGLE_PLAYER":
                if event.unicode.isdigit():
                    # text is appended to input text
                    input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]                    
                elif event.key == pygame.K_RETURN:
                    if input_text != "" and int(input_text) <= 100:
                        print("Stored number =", input_text)
                        player_number = int(input_text)
                        AI_numbers = [random.randint(0,100), random.randint(0,50), random.randint(0,30)]
                        All_numbers = AI_numbers + [player_number]

                        players = {
                            "You": player_number,
                            "AI 1": AI_numbers[0],
                            "AI 2": AI_numbers[1],
                            "AI 3": AI_numbers[2]
                        }

                        player_lives = {
                            "You": player1_life,
                            "AI 1": AI_life1,
                            "AI 2": AI_life2,
                            "AI 3": AI_life3                            
                        }

                        all_numbers = list(players.values())
                        average = sum(All_numbers) / len(All_numbers)
                        target = 2/3 * average

                        closest_player = min(players, key=lambda name: abs(players[name] - target))
                        closest_number = players[closest_player]

                        for name in players:
                            if players[name] == closest_number:
                                player_lives[name] = player_lives[name] + 1

                        player1_life = player_lives["You"]
                        AI_life1 = player_lives["AI 1"]
                        AI_life2 = player_lives["AI 2"]
                        AI_life3 = player_lives["AI 3"]           
                        print(player_lives.values())

                        # shows numbers for testing
                        print("--------------------------------------------------------------")
                        print (target)
                        print(All_numbers)
                        print(closest_number)
                        print("--------------------------------------------------------------")
                        State = "RESULT"
                        



    if State == "MENU":
        screen.fill((10,20,30))
        Title_surf = font.render("Alice In Borderland", True, (255,100,255))
        Title_surf_rect = Title_surf.get_rect(centerx = 400, top = 150)
        screen.blit(Title_surf,Title_surf_rect)

        pygame.draw.rect(screen,(0,0,255),Play_button)
        pygame.draw.rect(screen,(0,0,255),Quit_button_Menu)

        # buttons for main menu
        Play_surf = font.render("PLAY GAME", True, (255,255,255)) 
        Quit_surf = font.render("QUIT GAME", True, (255,255,255))



        if Play_button.collidepoint(mouse_pos):
            Play_surf = font.render("PLAY GAME", True, (250,20,100))
        elif Quit_button_Menu.collidepoint(mouse_pos):
            Quit_surf = font.render("QUIT GAME", True, (250,20,100))

        screen.blit(Play_surf, Play_surf.get_rect(center=Play_button.center))  
        screen.blit(Quit_surf, Quit_surf.get_rect(center=Quit_button_Menu.center))     

    elif State == "GAME":
        screen.fill((25,25,25))
        Select_Game_Surf = font.render("SELECT GAME TYPE", True, (255, 255, 255))
        Select_Game_Surf_Rect = Select_Game_Surf.get_rect(centerx=400, top = 150)
        screen.blit(Select_Game_Surf,Select_Game_Surf_Rect)

        pygame.draw.rect(screen,(0,0,255),Single_Player)
        pygame.draw.rect(screen,(0,0,255),Multi_Player)
        pygame.draw.rect(screen,(0,0,255),Back_Game)
        # buttons for game (make sure that the buttons are printed BEFORE the text)
        Single_Player_Surf = font.render("Single Player", True, (255,255,255))
        Multi_Player_Surf = font.render("Multi Player", True, (255,255,255))
        Back_Game_Surf = font.render("Go back", True, (255,255,255))

        if Back_Game.collidepoint(mouse_pos):
            Back_Game_Surf = font.render("Go back", True, (250,20,100))
        elif Single_Player.collidepoint(mouse_pos):
            Single_Player_Surf = font.render("Single Player", True, (255,20,100))
        elif Multi_Player.collidepoint(mouse_pos):
                Multi_Player_Surf = font.render("Multi Player", True, (255,20,100))

        screen.blit(Single_Player_Surf, Single_Player_Surf.get_rect(center=Single_Player.center))
        screen.blit(Multi_Player_Surf, Multi_Player_Surf.get_rect(center=Multi_Player.center))
        screen.blit(Back_Game_Surf, Back_Game_Surf.get_rect(center=Back_Game.center))

    elif State == "SINGLE_PLAYER":
        screen.fill((50,50,50))
        # title
        Game_Title_Surf = font.render("Enter a number between 1 and 100", True, (255,100,255))
        Game_Title_Surf_Rect = Game_Title_Surf.get_rect(centerx = 400, top = 150)
        
        #input button
        pygame.draw.rect(screen,(255,255,255), input, 2)
        screen.blit(Game_Title_Surf,Game_Title_Surf_Rect)

        # input text
        
        input_surf = font.render(input_text, True, (255,255,255))
        screen.blit(input_surf, input_surf.get_rect(center = input.center))

        #back button
        pygame.draw.rect(screen,(0,0,255),Back_Game)
        screen.blit(Back_Game_Surf, Back_Game_Surf.get_rect(center=Back_Game.center))
        

    elif State == "MULTIPLAYER":
        screen.fill((100,100,200))   
        pygame.draw.rect(screen,(0,0,255),Back_Game)
        screen.blit(Back_Game_Surf, Back_Game_Surf.get_rect(center=Back_Game.center))

    elif State == "RESULT":

        screen.fill((20,20,20))
        Player_number_surf = font.render(f"You chose {input_text}", True, (255,255,255))
        screen.blit(Player_number_surf, Player_number_surf.get_rect(centerx = 400, top = 100))
        
        #AI 1
        AI_1_Surf = font.render(f"AI 1 chose {AI_numbers[0]}", True, (255,255,255))
        screen.blit(AI_1_Surf,AI_1_Surf.get_rect(centerx= 400,top = 150))
        
        #AI 2
        AI_2_Surf = font.render(f"AI 2 chose {AI_numbers[1]}", True, (255,255,255))
        screen.blit(AI_2_Surf,AI_2_Surf.get_rect(centerx= 400,top = 200))  

        AI_3_Surf = font.render(f"AI 3 chose {AI_numbers[2]}", True, (255,255,255))
        screen.blit(AI_3_Surf,AI_3_Surf.get_rect(centerx= 400,top = 250))  
        
        target_surf1 = font.render(f"Average was {round(average,2)}",True, (255,255,255))
        target_surf2 = font.render(f"Target was {round(target,2)}", True, (255,255,255))
        closest_surf = font.render(f"Closest person was {closest_player}: {closest_number}", True, (255,255,255))
        # splitting the lines up to be better seen in a smaller screen
        screen.blit(target_surf1,target_surf1.get_rect(centerx= 400, top = 300))
        screen.blit(target_surf2,target_surf2.get_rect(centerx= 400, top = 350))
        screen.blit(closest_surf,closest_surf.get_rect(centerx = 400, top = 400))

        # lives
        Player_life_surf = font.render(f"Player has {player_lives["You"]} win(s)",True, (255,20,255))
        AI_life1_surf = font.render(f"AI 1 has {player_lives["AI 1"]} win(s)",True, (255,20,255))
        AI_life2_surf = font.render(f"AI 2 has {player_lives["AI 2"]} win(s)",True, (255,20,255))
        AI_life3_surf = font.render(f"AI 3 has {player_lives["AI 3"]} win(s)",True, (255,20,255))        

        # displaying the lives
        screen.blit(Player_life_surf,Player_life_surf.get_rect(centerx= 150, top = 40))
        screen.blit(AI_life1_surf,AI_life1_surf.get_rect(centerx= 150, top = 80))
        screen.blit(AI_life2_surf,AI_life2_surf.get_rect(centerx= 150, top = 120))
        screen.blit(AI_life3_surf,AI_life3_surf.get_rect(centerx = 150, top = 160))        


        Play_Again_Surf = font.render("Play Again?", True, (255,255,255))
        pygame.draw.rect(screen,(0,0,255),Play_Again)
        screen.blit(Play_Again_Surf,Play_Again_Surf.get_rect(center=Play_Again.center))
    pygame.display.flip()
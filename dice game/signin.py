import pygame

dis_width = 800
dis_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 253, 213)
 
display = pygame.display.set_mode((dis_width, dis_height))
signedin1 = False
signedin2 = False
def signin():
    pygame.font.init()
    pygame.init()
    
    FONT = pygame.font.SysFont('Comic Sans MS', 42)
    myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    usertext = ''

    def checkpass(usertext, pass1, pass2, user):
        global signedin1, signedin2
        if usertext == pass2 and user == 2 and signedin1 == True:
            signedin2 = True
        elif usertext == pass1 and user == 1:
            signedin1 = True
   
    def checkuser(usertext, pass1, pass2, user1, user2):
        global signedin1, signedin2
        user = 1
        if user == 1 and signedin1 == True:
            user = 2
        if signedin2 == 2 and signedin1 == True:
            checkpass(usertext, pass1, pass2, user)
        elif signedin1 == 2:
            checkpass(usertext, pass1, pass2, user)
        if str(usertext) == str(user1) and signedin1 != True:
            signedin1 = 2
        elif str(usertext) == str(user2) and signedin1 == True:
            signedin2 = 2
            
    def main(usertext):
        global signedin1, signedin2
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        user1 = "will"
        pass1 = "emojimovie"
        user2 = "jeff"
        pass2 = "lovecats"
        imageOld = pygame.image.load('background.jpg')
        image = pygame.transform.scale(imageOld, (800, 600))
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if usertext == "no":
                            signedin1 = True
                            signedin2 = True
                            break
                        checkuser(usertext, pass1, pass2, user1, user2)
                        usertext = ''
                    if event.key == pygame.K_BACKSPACE:
                        usertext = usertext[:-1]
                    elif not event.key == pygame.K_RETURN:
                        usertext += event.unicode
            '''screen.fill((255, 69, 30))
            '''
            screen.blit(image, (0, 0))
            usernum = 1
            if signedin1 == True:
                usernum = 2
            if signedin1 == 2 or signedin2 == 2:
                textsurface = myfont1.render('User {}s Password: '.format(usernum), True, black)
                textsurfaceRect = textsurface.get_rect(center=(400, 200))
                display.blit(textsurface, textsurfaceRect)
            else:
                textsurface = myfont1.render('User {}s Username: '.format(usernum), True, black)
                textsurfaceRect = textsurface.get_rect(center=(400, 200))
                display.blit(textsurface, textsurfaceRect)
            if signedin1 == True and signedin2 == True:
                break
            password_surface = FONT.render(usertext, True, (0, 0, 0))
            password_surface_rect = password_surface.get_rect(center=(400, 325))
            screen.blit(password_surface, password_surface_rect)
            pygame.display.update()

    main(usertext)

signin()


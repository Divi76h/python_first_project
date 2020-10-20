import pygame
from pygame.locals import *
import sys
import os
import json
import inputbox_pygame
import time


# complete login and add other options like change password and delete account
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill((157, 193, 131))

        draw_text('Authentication', font, (0, 0, 0), screen, 150, 25)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 200, 200, 50)
        button_3 = pygame.Rect(150, 300, 200, 50)

        pygame.draw.rect(screen, (0, 153, 204), button_1)
        pygame.draw.rect(screen, (0, 153, 204), button_2)
        pygame.draw.rect(screen, (0, 153, 204), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_1)
            if click:
                signup_username()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_2)
            if click:
                login_username()

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_3)
            if click:
                quit()

        draw_text('Signup', font, (0, 0, 0), screen, 200, 107)
        draw_text('Login', font, (0, 0, 0), screen, 210, 207)
        draw_text('Quit', font, (0, 0, 0), screen, 217, 307)

        pygame.display.update()
        mainClock.tick(60)


def signup_username():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global username_main
    global password_main

    username_main = ''
    password_main = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Signup username', font, (0, 0, 0), screen, 20, 20)
        draw_text('username:', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        signup_password()
                    elif event.key == pygame.K_BACKSPACE:
                        username_main = username_main[:-1]
                    else:
                        username_main += event.unicode

        txt_surface = font.render(username_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def signup_password():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global password_main

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Signup password', font, (0, 0, 0), screen, 20, 20)
        draw_text('password:', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        register(username_main, password_main)
                    elif event.key == pygame.K_BACKSPACE:
                        password_main = password_main[:-1]
                    else:
                        password_main += event.unicode

        txt_surface = font.render(password_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def register(username_main, password_main):
    if len(password_main) < 5:
        password_less_than_five()
    else:
        readFile = open("database.json", "r")
        data = {}
        data['users'] = []

        if os.stat("database.json").st_size != 0:
            data = json.loads(readFile.read())

            for user in data["users"]:
                if user['username'] == username_main:
                    username_is_taken()

            writeFile = open("database.json", 'w')

            data["users"].append({
                'username': username_main,
                'password': password_main
            })

            writeFile.write(json.dumps(data))

            writeFile.close()
            user_registered()
        else:
            writeFile = open("database.json", 'w')

            data['users'].append({
                'username': username_main,
                'password': password_main
            })
            writeFile.write(json.dumps(data))
            writeFile.close()
            user_registered()


def username_is_taken():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Username is taken', font, (0, 0, 0), screen, 123, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def password_less_than_five():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Passwords min length allowed is 5', font, (0, 0, 0), screen, 13, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def user_registered():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('User Registered', font, (0, 0, 0), screen, 138, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def login_username():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global username_main
    global password_main

    username_main = ''
    password_main = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Login username', font, (0, 0, 0), screen, 20, 20)
        draw_text('username:', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        login_password()
                    elif event.key == pygame.K_BACKSPACE:
                        username_main = username_main[:-1]
                    else:
                        username_main += event.unicode

        txt_surface = font.render(username_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def login_password():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global password_main
    password_main = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Login password', font, (0, 0, 0), screen, 20, 20)
        draw_text('password:', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        login_checker(username_main, password_main)
                    elif event.key == pygame.K_BACKSPACE:
                        password_main = password_main[:-1]
                    else:
                        password_main += event.unicode

        txt_surface = font.render(password_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def login_checker(username_main, password_main):
    readFile = open("database.json", "r")

    if os.stat("database.json").st_size == 0:
        signup_first()
    else:
        data = json.loads(readFile.read())

        isLoggedin = False

        global loggedInUser
        loggedInUser = {}

        for user in data["users"]:
            if user["username"] == username_main and user["password"] == password_main:
                isLoggedin = True
                loggedInUser = user

        if isLoggedin == True:
            success_login()

        else:
            wrong_comb()


def signup_first():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Signup First', font, (0, 0, 0), screen, 160, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def wrong_comb():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Wrong combination', font, (0, 0, 0), screen, 115, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def success_login():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('User successfully logged in', font, (0, 0, 0), screen, 65, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    logged_in_options()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    logged_in_options()

        pygame.display.update()
        mainClock.tick(60)


def logged_in_options():
    while True:
        screen.fill((157, 193, 131))

        draw_text('Logged in', font, (0, 0, 0), screen, 185, 25)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 100, 300, 50)
        button_2 = pygame.Rect(100, 200, 300, 50)
        button_3 = pygame.Rect(100, 300, 300, 50)

        pygame.draw.rect(screen, (0, 153, 204), button_1)
        pygame.draw.rect(screen, (0, 153, 204), button_2)
        pygame.draw.rect(screen, (0, 153, 204), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_1)
            if click:
                change_password_enter_old()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_2)
            if click:
                delete_account_menu()

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_3)
            if click:
                logged_out_successfully()

        draw_text('Change password', font, (0, 0, 0), screen, 125, 107)
        draw_text('Delete account', font, (0, 0, 0), screen, 147, 207)
        draw_text('Log out', font, (0, 0, 0), screen, 200, 307)

        pygame.display.update()
        mainClock.tick(60)


def change_password_enter_old():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global password_main
    password_main = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Password change', font, (0, 0, 0), screen, 20, 20)
        draw_text('enter old password: ', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        old_password_checker()
                    elif event.key == pygame.K_BACKSPACE:
                        password_main = password_main[:-1]
                    else:
                        password_main += event.unicode

        txt_surface = font.render(password_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def old_password_checker():
    if loggedInUser["password"] == password_main:
        change_password_enter_new()
    else:
        wrong_password()


def change_password_enter_new():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global newpassword
    newpassword = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Password change', font, (0, 0, 0), screen, 20, 20)
        draw_text('enter new password: ', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        change_password()
                    elif event.key == pygame.K_BACKSPACE:
                        newpassword = newpassword[:-1]
                    else:
                        newpassword += event.unicode

        txt_surface = font.render(newpassword, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def change_password():
    if len(newpassword) < 5:
        newpassword_less_than_five()
    else:
        readFile = open("database.json", "r")
        data = json.loads(readFile.read())
        position = -1

        for index, usr in enumerate(data["users"]):

            if usr['username'] == loggedInUser["username"]:
                position = index
                loggedInUser["password"] = newpassword
                break

        data['users'].pop(position)
        data['users'].insert(position, loggedInUser)
        writeFile = open("database.json", "w")
        writeFile.write(json.dumps(data))


def password_changed_successfully():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Password changed successfully', font, (0, 0, 0), screen, 35, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def logged_out_successfully():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Logged out successfully', font, (0, 0, 0), screen, 83, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False

                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False

                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def wrong_password():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Wrong password', font, (0, 0, 0), screen, 125, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    logged_in_options()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    logged_in_options()

        pygame.display.update()
        mainClock.tick(60)


def newpassword_less_than_five():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Passwords min length allowed is 5', font, (0, 0, 0), screen, 13, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    logged_in_options()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    logged_in_options()

        pygame.display.update()
        mainClock.tick(60)


def delete_account_menu():
    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Delete account', font, (0, 0, 0), screen, 150, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(65, 150, 150, 50)
        button_2 = pygame.Rect(285, 150, 150, 50)

        pygame.draw.rect(screen, (0, 153, 204), button_1)
        pygame.draw.rect(screen, (0, 153, 204), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    logged_in_options()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_1)
            if click:
                account_deletion_password_input()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (102, 204, 255), button_2)
            if click:
                logged_in_options()

        draw_text('Yes', font, (0, 0, 0), screen, 115, 160)
        draw_text('No', font, (0, 0, 0), screen, 340, 160)

        pygame.display.update()
        mainClock.tick(60)


def account_deletion_password_input():
    input_box = pygame.Rect(20, 140, 200, 50)

    color_inactive = pygame.Color(0, 153, 204)
    color_active = pygame.Color(0, 0, 0)
    color = color_inactive

    active = False

    global password_main
    password_main = ''

    running = True
    while running:
        screen.fill((157, 193, 131))

        draw_text('Delete account', font, (0, 0, 0), screen, 20, 20)
        draw_text('enter password: ', font, (0, 0, 0), screen, 20, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                        account_deletion_password_check()
                    elif event.key == pygame.K_BACKSPACE:
                        password_main = password_main[:-1]
                    else:
                        password_main += event.unicode

        txt_surface = font.render(password_main, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.update()
        mainClock.tick(60)


def account_deletion_password_check():
    if loggedInUser["password"] == password_main:
        delete_account()
    else:
        wrong_password()


def delete_account():
    readFile = open("database.json", "r")
    data = json.loads(readFile.read())

    data["users"].remove(loggedInUser)

    writeFile = open("database.json", "w")
    writeFile.write(json.dumps(data))
    writeFile.close()

    password_main = ''
    username_main = ''
    newpassword = ''

    user_account_successfully_deleted()


def user_account_successfully_deleted():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('Your account has been successfully deleted', font, (0, 0, 0), screen, 10, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def being_imported():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('This program is being imported', font, (0, 0, 0), screen, 30, 230)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    made_by()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    made_by()

        pygame.display.update()
        mainClock.tick(60)


def made_by():
    running = True
    while running:
        screen.fill((157, 193, 131))
        draw_text('This program is made by:', font, (0, 0, 0), screen, 75, 215)
        draw_text('Divij Kapoor', font, (0, 0, 0), screen, 160, 250)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_RETURN:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500), 0, 32)

    pygame.display.set_caption("Authentication")
    icon = pygame.image.load("lock.png")
    pygame.display.set_icon(icon)

    mainClock = pygame.time.Clock()

    font = pygame.font.SysFont('Corbel', 35)

    username_main = ''
    password_main = ''
    newpassword = ''

    loggedInUser = {}

    click = False

    main_menu()
else:
    print("This file is being imported")

    pygame.init()
    screen = pygame.display.set_mode((500, 500), 0, 32)

    pygame.display.set_caption("Authentication")
    icon = pygame.image.load("lock.png")
    pygame.display.set_icon(icon)

    mainClock = pygame.time.Clock()

    font = pygame.font.SysFont('Corbel', 35)

    username_main = ''
    password_main = ''
    newpassword = ''

    loggedInUser = {}

    click = False

    main_menu()

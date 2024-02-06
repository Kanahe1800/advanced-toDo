import pygame
import tkinter
from tkinter import ttk
from tkcalendar import *
from sys import exit

from gui import Button
from gui import Toolbar
from gui import InputBox
from gui import DropDown
from gui import create_label

from main_function import register
from main_function import login
from main_function import create_2d_list
from main_function import add_to_do
from main_function import select_priority
from main_function import selected_date
from main_function import delete_to_do


def start_window():
    """
    This window will open when the users start the program and allow users to either log in or register
    :return:
    """
    global input_username
    global flag
    pygame.init()
    button_check = False
    start_screen = pygame.display.set_mode([600, 337])
    input_username = InputBox(250, 50, 300, 30, (255, 255, 255), (0, 0, 0),
                              "Please enter your username", 2, (0, 0, 0), "", 20, start_screen)
    input_password = InputBox(250, 125, 300, 30, (255, 255, 255), (0, 0, 0),
                              "Please enter your password", 2, (0, 0, 0), "", 20, start_screen)
    login_button = Button(255, 200, 90, 30, (255, 255, 255), (0, 0, 0), "Log in", 20, 2, (0, 0, 0), start_screen)
    register_button = Button(255, 250, 90, 30, (255, 255, 255), (0, 0, 0), "Register", 20, 2, (0, 0, 0), start_screen)
    run = True
    while run:
        start_screen.fill((90, 90, 90))
        create_label("User Name", 100, 55, (0, 0, 0), 20, start_screen)
        create_label("Password", 100, 130, (0, 0, 0), 20, start_screen)
        input_username.draw(start_screen)
        input_password.draw(start_screen)
        login_button.display(start_screen)
        register_button.display(start_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            input_username.handle_event(event)
            input_password.handle_event(event)
            button_pressed = pygame.mouse.get_pressed()[0]

            if login_button.pressed() and button_pressed == 1 and not button_check and \
                    login(input_username.get_text(), input_password.get_text()):
                flag = "start"
                to_do_window()
            elif register_button.pressed() and button_pressed == 1 and not button_check:
                register_window()
            if button_pressed == 0:
                button_check = False


def register_window():
    """
    This window will open when the users click register button in start_window and allow users to register thorough GUI
    :return:
    """
    global new_username
    global flag
    pygame.init()
    button_check = False
    register_screen = pygame.display.set_mode([600, 337])
    new_username = InputBox(250, 50, 300, 30, (255, 255, 255), (0, 0, 0),
                            "Please decide your username", 2, (0, 0, 0), "", 20, register_screen)
    new_password = InputBox(250, 125, 300, 30, (255, 255, 255), (0, 0, 0),
                            "Please decide your password", 2, (0, 0, 0), "", 20, register_screen)
    reenter_password = InputBox(250, 200, 300, 30, (255, 255, 255), (0, 0, 0),
                                "Please enter your password again", 2, (0, 0, 0), "", 16, register_screen)
    register_button = Button(255, 280, 90, 30, (255, 255, 255), (0, 0, 0), "Register", 20, 2, (0, 0, 0),
                             register_screen)
    run = True
    while run:
        register_screen.fill((90, 90, 90))
        create_label("User Name", 100, 55, (0, 0, 0), 20, register_screen)
        create_label("Password", 100, 130, (0, 0, 0), 20, register_screen)
        create_label("Re-enter Password", 55, 205, (0, 0, 0), 20, register_screen)
        new_username.draw(register_screen)
        new_password.draw(register_screen)
        reenter_password.draw(register_screen)
        register_button.display(register_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            new_username.handle_event(event)
            new_password.handle_event(event)
            reenter_password.handle_event(event)
            button_pressed = pygame.mouse.get_pressed()[0]
            if register_button.pressed() and button_pressed == 1 and not button_check:
                status = register(new_username.get_text(), new_password.get_text(), reenter_password.get_text())
                if status:
                    flag = "register"
                    to_do_window()
            if button_pressed == 0:
                button_check = False


def to_do_window():
    """
    This window opens when users either log in or register to the account. This window includes every to-do that users
    have made
    :return:
    """
    global input_username
    global new_username
    global flag
    global edit_button_name
    pygame.init()
    button_check = False
    to_do_screen = pygame.display.set_mode([800, 450])
    change_tab = Toolbar(600, 50, to_do_screen)
    input_add_to_do = InputBox(50, 55, 400, 30, (255, 255, 255), (0, 0, 0), "What do you want to add?",
                               2, (0, 0, 0), "", 20, to_do_screen)
    select_due_date = Button(500, 55, 90, 30, (255, 255, 255), (0, 0, 0), "Date", 20, 2, (0, 0, 0),
                             to_do_screen)
    add_button = Button(700, 55, 90, 30, (255, 255, 255), (0, 0, 0), "Add", 20, 2, (0, 0, 0),
                        to_do_screen)
    color_inactive = (255, 255, 255)
    color_active = (204, 204, 204)
    select_priority_dropdown = DropDown([color_inactive, color_active], [color_inactive, color_active], 600, 55, 90, 30,
                                        pygame.font.SysFont(None, 20), "Select priority", ["Highest", "High", "Normal"]
                                        , 2, (0, 0, 0), (255, 255, 255))

    edit_button_name = {}
    done_button_name = {}
    user_name = "a"

    if flag == "start":
        element_list = create_2d_list(input_username.get_text())
        user_name = input_username.get_text()
    if flag == "register":
        element_list = create_2d_list(new_username.get_text())
        user_name = input_username.get_text()
    scroll_y = 90

    def create_edit_button():
        # print(element_list)
        for k in range(len(element_list)):
            individual_button_name = format(k)
            # print(individual_button_name)
            if k <= 9:
                edit_button = Button(550, 90 + k * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Edit", 20, 2, (0, 0, 0),
                                     to_do_screen)
            elif 10 <= k <= 19:
                edit_button = Button(550, 90 + (k - 10) * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Edit", 20, 2,
                                     (0, 0, 0), to_do_screen)
            else:
                edit_button = Button(550, 90 + (k - 20) * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Edit", 20, 2,
                                     (0, 0, 0), to_do_screen)
            edit_button_name[individual_button_name] = edit_button
        #　print(edit_button_name)

    def create_done_button():
        # print(element_list)
        for k in range(len(element_list)):
            individual_button_name = format(k)
            # print(individual_button_name)
            if k <= 9:
                done_button = Button(650, 90 + k * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Done", 20, 2, (0, 0, 0),
                                     to_do_screen)
            elif 10 <= k <= 19:
                done_button = Button(650, 90 + (k - 10) * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Done", 20, 2,
                                     (0, 0, 0), to_do_screen)
            else:
                done_button = Button(650, 90 + (k - 20) * 35, 90, 30, (255, 255, 255), (0, 0, 0), "Done", 20, 2,
                                     (0, 0, 0), to_do_screen)
            done_button_name[individual_button_name] = done_button

    def show_label():
        for j in range(len(element_list)):
            # print(scroll_y)
            if j <= 9:
                if scroll_y >= 90:
                    edit_button_name[str(j)].display(to_do_screen)
                    done_button_name[str(j)].display(to_do_screen)
                    create_label(element_list[j][0], 80, 90 + j * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][1], 300, 90 + j * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][2], 400, 90 + j * 35, (0, 0, 0), 25, to_do_screen)
            elif 10 <= j <= 19:
                if 73 <= scroll_y < 90:
                    create_label(element_list[j][0], 80, 90 + (j - 10) * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][1], 300, 90 + (j - 10) * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][2], 400, 90 + (j - 10) * 35, (0, 0, 0), 25, to_do_screen)
                    edit_button_name[str(j)].display(to_do_screen)
                    done_button_name[str(j)].display(to_do_screen)
            else:
                if 58 <= scroll_y < 73:
                    create_label(element_list[j][0], 80, 90 + (j - 20) * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][1], 300, 90 + (j - 20) * 35, (0, 0, 0), 25, to_do_screen)
                    create_label(element_list[j][2], 400, 90 + (j - 20) * 35, (0, 0, 0), 25, to_do_screen)
                    edit_button_name[str(j)].display(to_do_screen)
                    done_button_name[str(j)].display(to_do_screen)

    run = True
    while run:
        to_do_screen.fill((90, 90, 90))
        change_tab.draw(to_do_screen)
        input_add_to_do.draw(to_do_screen)
        add_button.display(to_do_screen)
        select_due_date.display(to_do_screen)
        select_priority_dropdown.draw(to_do_screen)
        list_of_to_do = pygame.Rect(50, 90, 480, 345)
        pygame.draw.rect(to_do_screen, "white", list_of_to_do)
        create_edit_button()
        create_done_button()
        show_label()
        button_pressed = pygame.mouse.get_pressed()[0]
        create_edit_button()
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_y = scroll_y + 15
                    show_label()
                if event.button == 5:
                    scroll_y = scroll_y - 15
                    show_label()
            input_add_to_do.handle_event(event)
            selected_option = select_priority_dropdown.update(event_list)
            if selected_option >= 0:
                select_priority_dropdown.main = select_priority_dropdown.options[selected_option]
            if input_add_to_do.get_text() != "":
                selected_to_do = input_add_to_do.get_text()

            def getting_date_from_calendar(file_name):
                window = tkinter.Tk()
                window.geometry("380x200")
                window.configure(background="white")

                style = ttk.Style(window)
                style.theme_use('clam')  # change theme, you can use style.theme_names() to list themes

                cal = Calendar(window, background="black", disabledbackground="black", bordercolor="black",
                               headersbackground="black", normalbackground="black", foreground='white',
                               normalforeground='white', headersforeground='white')

                # cal.config(background="black")
                def close():
                    window.destroy()

                # print(selected_to_do)
                read = tkinter.Button(window, text="read", command=lambda: [selected_date(cal, file_name,
                                                                                          selected_to_do), close()])
                read.grid(row=2, column=1)
                read.pack()
                cal.pack()
                window.mainloop()

            if add_button.pressed() and button_pressed == 1 and not button_check:
                if input_add_to_do.get_text() != "" and select_priority_dropdown.main != "Select priority":
                    select_priority(user_name, input_add_to_do.get_text(), select_priority_dropdown.main)
                    element_list = create_2d_list(user_name)
                    show_label()
            if select_due_date.pressed() and button_pressed == 1 and not button_check and input_add_to_do.get_text() \
                    != "" and add_to_do(user_name, input_add_to_do.get_text()):
                element_list = create_2d_list(user_name)
                getting_date_from_calendar(user_name)
            for i in edit_button_name:
                button_name = edit_button_name[i]
                if button_name.pressed() and button_pressed == 1 and not button_check:
                    if scroll_y >= 90:
                        edit_window(int(i), user_name)
                    if 73 <= scroll_y < 90:
                        int_i = int(i)
                        edit_window(int_i + 10, user_name)
                    if 58 <= scroll_y < 73:
                        int_i = int(i)
                        edit_window(int_i + 20, user_name)
            for i in done_button_name:
                button_name = done_button_name[i]
                if button_name.pressed() and button_pressed == 1 and not button_check:
                    if scroll_y >= 90:
                        print(element_list[int(i)][0])
                        delete_to_do(user_name, element_list[int(i)][0])
                        element_list = create_2d_list(user_name)
                        show_label()
                    if 73 <= scroll_y < 90:
                        int_i = int(i)
                        delete_to_do(user_name, element_list[int_i + 10][0])
                        element_list = create_2d_list(user_name)
                        show_label()
                    if 58 <= scroll_y < 73:
                        int_i = int(i)
                        delete_to_do(user_name, element_list[int_i + 20][0])
                        element_list = create_2d_list(user_name)
                        show_label()
            if button_pressed == 0:
                button_check = False

        pygame.display.update()


def edit_window(place, file_name):
    """
    This function will open when users click edit button in to_do_screen and allow users to edit their to-do thorough
    GUI
    :param place: The place where the to-do is located in the element_list created in to_do_window
    :param file_name: the txt file that has to-do that users want to edit
    :return:
    """
    color_inactive = (255, 255, 255)
    color_active = (204, 204, 204)
    pygame.init()
    button_check = False
    add = False
    to_do_list = create_2d_list(file_name)
    edit_screen = pygame.display.set_mode([400, 280])
    edit_input = InputBox(30, 60, 350, 30, (255, 255, 255), (0, 0, 0), to_do_list[place][0],
                          2, (0, 0, 0), "", 20, edit_screen)
    change_date_button = Button(30, 150, 170, 30, (255, 255, 255), (0, 0, 0), "Change date", 20, 2, (0, 0, 0),
                                edit_screen)
    change_priority_dropdown = DropDown([color_inactive, color_active], [color_inactive, color_active], 205, 150, 170,
                                        30, pygame.font.SysFont(None, 20), "Select priority",
                                        ["Highest", "High", "Normal"], 2, (0, 0, 0), (255, 255, 255))
    change_button = Button(30, 100, 170, 30, (255, 255, 255), (0, 0, 0), "Change", 20, 2, (0, 0, 0),
                           edit_screen)
    return_button = Button(205, 100, 170, 30, (255, 255, 255), (0, 0, 0), "Return", 20, 2, (0, 0, 0),
                           edit_screen)

    run = True
    while run:
        button_pressed = pygame.mouse.get_pressed()[0]
        edit_screen.fill((90, 90, 90))
        edit_input.draw(edit_screen)
        change_date_button.display(edit_screen)
        change_button.display(edit_screen)
        return_button.display(edit_screen)
        change_priority_dropdown.draw(edit_screen)
        event_list = pygame.event.get()
        delete_element_name = edit_input.get_original_text()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            edit_input.handle_event(event)
            selected_option = change_priority_dropdown.update(event_list)
            if selected_option >= 0:
                change_priority_dropdown.main = change_priority_dropdown.options[selected_option]

            def getting_date_from_calendar(date_file_name):
                window = tkinter.Tk()
                window.geometry("380x200")
                window.configure(background="white")

                style = ttk.Style(window)
                style.theme_use('clam')  # change theme, you can use style.theme_names() to list themes

                cal = Calendar(window, background="black", disabledbackground="black", bordercolor="black",
                               headersbackground="black", normalbackground="black", foreground='white',
                               normalforeground='white', headersforeground='white')

                # cal.config(background="black")
                def close():
                    window.destroy()

                if edit_input.get_text() == "":
                    read = tkinter.Button(window, text="read", command=lambda: [selected_date(cal, date_file_name,
                                                                                              edit_input.get_original_text()),
                                                                                close()])
                else:
                    read = tkinter.Button(window, text="read", command=lambda: [selected_date(cal, date_file_name,
                                                                                              edit_input.get_text()),
                                                                                close()])
                read.grid(row=2, column=1)
                read.pack()
                cal.pack()
                window.mainloop()

        if change_button.pressed() and button_pressed == 1 and not button_check:
            if change_priority_dropdown.main != "Select priority":
                if edit_input.get_text() == "":
                    select_priority(file_name, edit_input.get_original_text(), change_priority_dropdown.main)
                    to_do_window()
                else:
                    if not add:
                        delete_to_do(file_name, edit_input.get_original_text())
                        add_to_do(file_name, edit_input.get_text())
                        select_priority(file_name, edit_input.get_text(), change_priority_dropdown.main)
                        to_do_window()
                    else:
                        select_priority(file_name, edit_input.get_text(), change_priority_dropdown.main)
        if change_date_button.pressed() and button_pressed == 1 and not button_check:
            if edit_input.get_text() == "":
                getting_date_from_calendar(file_name)
            else:
                delete_to_do(file_name, edit_input.get_original_text())
                add_to_do(file_name, edit_input.get_text())
                getting_date_from_calendar(file_name)
        if return_button.pressed() and button_pressed == 1 and not button_check:
            to_do_window()

        if button_pressed == 0:
            button_check = False

        pygame.display.update()


start_window()

import pygame


class Button:
    # The code for this class was found in previous IA assessment
    def __init__(self, x, y, w, h, color, text_color, text, text_size, boarder_width, boarder_color, screen):
        self.x = x  # x-coordinate on the GUI of the button
        self.y = y  # y-coordinate on the GUI of the button
        self.w = w  # width of the button in pixels
        self.h = h  # height of the button in pixels
        self.color = color  # the color of the button in rgb format
        self.text_color = text_color  # the color of the text of the button in rgb format
        self.text = text  # the text of the button as a string
        self.text_size = text_size  # the font size of the text
        self.boarder_width = boarder_width  # the width in pixels of the buttons boarder
        self.boarder_color = boarder_color  # the color of the buttons border in rgb format
        self.screen = screen
        self.lock = False  # True if the button should not highlight if the cursor is over it
        # returns true if the cursor is over the button and False if it is not

    def pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.x + self.w > mouse_pos[0] > self.x and self.y + self.h > mouse_pos[1] > self.y:
            return True
        return False

    # displays the button
    def display(self, window):
        # if the button is under the cursor, change the color to highlight it
        if self.pressed() and not self.lock:
            color = (self.color[0] * 0.8, self.color[1] * 0.8, self.color[2] * 0.8)

        else:
            color = self.color
        # draw the boarder, the button, and the text in that order
        pygame.draw.rect(window, self.boarder_color, (self.x, self.y, self.w, self.h))
        x_pos = self.x + self.boarder_width
        y_pos = self.y + self.boarder_width
        pygame.draw.rect(window, color,
                         (x_pos, y_pos, self.w - 2 * self.boarder_width, self.h - 2 * self.boarder_width))

        if self.text != "":
            display_text(self.text, self.x + self.w / 2, self.y + self.h / 2, self.text_color,
                         self.text_size, self.screen)


class Toolbar:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.left_button = Button(0, 0, 200, 50, (0, 220, 100), (0, 0, 0), "To Do", 20, 2, (0, 0, 0), self.screen)
        self.left_middle_button = Button(200, 0, 200, 50, (0, 220, 100), (0, 0, 0), "Highest Priority", 20, 2,
                                         (0, 0, 0), self.screen)
        self.right_middle_button = Button(400, 0, 200, 50, (0, 220, 70), (0, 0, 0), "Timer", 20, 2, (0, 0, 0),
                                          self.screen)
        self.right_button = Button(600, 0, 200, 50, (0, 220, 70), (0, 0, 0), "Change Limit", 20, 2, (0, 0, 0),
                                   self.screen)

    # display the tool bar to the window
    def draw(self, window):
        window.blit(self.image, self.rect)
        self.left_button.display(window)
        self.left_middle_button.display(window)
        self.right_middle_button.display(window)
        self.right_button.display(window)

    # check whether the mouse cursor is clicked and which one is clicked
    def click(self):
        button_pressed = pygame.mouse.get_pressed()[0]
        if self.left_button.pressed() and button_pressed == 1:
            return "left"
        elif self.left_middle_button.pressed() and button_pressed == 1:
            return "mid_left"
        elif self.right_middle_button.pressed():
            return "mid_right"
        elif self.right_button.pressed():
            return "mid_left"
        else:
            return False


class InputBox:
    # source: https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
    def __init__(self, x, y, w, h, color, text_color, text, boarder_width, boarder_color, input_text, text_size,
                 screen):
        self.x = x  # x-coordinate on the GUI of the button
        self.y = y  # y-coordinate on the GUI of the button
        self.w = w  # width of the button in pixels
        self.h = h  # height of the button in pixels
        self.color = color
        self.text_color = text_color
        self.text = text
        self.instruction_text = text
        self.boarder_width = boarder_width
        self.boarder_color = boarder_color
        self.input_text = input_text
        self.text_size = text_size
        self.screen = screen
        self.active = False

    def pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.x + self.w > mouse_pos[0] > self.x and self.y + self.h > mouse_pos[1] > self.y:
            return True
        return False

    def handle_event(self, event):
        if self.pressed() and pygame.mouse.get_pressed()[0]:
            self.active = not self.active
            self.text = ""
        elif self.pressed():
            if self.active is True:
                self.text = ""
                self.active = self.active
            elif not self.input_text == "":
                self.text = ""
            else:
                self.text = self.instruction_text
        elif not self.input_text == "":
            self.active = False
            self.text = ""
        else:
            self.text = self.instruction_text

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode

    # return what is in the input box after the user's input
    def get_text(self):
        return self.input_text

    # get instruction text of the input box
    def get_original_text(self):
        return self.instruction_text

    # display the input box
    def draw(self, window):
        pygame.draw.rect(window, self.boarder_color, (self.x, self.y, self.w, self.h))
        x_pos = self.x + self.boarder_width
        y_pos = self.y + self.boarder_width
        pygame.draw.rect(window, self.color,
                         (x_pos, y_pos, self.w - 2 * self.boarder_width, self.h - 2 * self.boarder_width))
        display_text(self.text, self.x + self.w / 2, self.y + self.h / 2, self.text_color, self.text_size, self.screen)
        display_text(self.input_text, self.x + self.w / 2, self.y + self.h / 2, self.text_color, self.text_size,
                     self.screen)


class DropDown:
    # source: https://stackoverflow.com/questions/59236523/trying-creating-dropdown-menu-pygame-but-got-stuck
    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options, boarder_width, boarder_color, color):
        self.color_menu = color_menu
        self.color_option = color_option
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.boarder_width = boarder_width
        self.boarder_color = boarder_color
        self.color = color
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.boarder_color, (self.x, self.y, self.w, self.h))
        x_pos = self.x + self.boarder_width
        y_pos = self.y + self.boarder_width
        pygame.draw.rect(screen, self.color,
                         (x_pos, y_pos, self.w - 2 * self.boarder_width, self.h - 2 * self.boarder_width))
        message = self.font.render(self.main, 1, (0, 0, 0))
        screen.blit(message, message.get_rect(center=self.rect.center))
        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(screen, self.color_option[1 if i == self.active_option else 0], rect, 0)
                message = self.font.render(text, 1, (0, 0, 0))
                screen.blit(message, message.get_rect(center=rect.center))

    def update(self, event_list):
        mouse_position = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mouse_position)

        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mouse_position):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1


def display_text(text, x, y, color, size, screen):
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


def create_label(text, x, y, color, size, screen):
    font = pygame.font.Font("freesansbold.ttf", size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

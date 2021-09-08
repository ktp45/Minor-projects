import arcade
import sys
sys.path.append('Modules/')
from Modules import Slots

SCREEN_WIDTH = 1280  # declaration of used constants "magic numbers"
SCREEN_HEIGHT = 720  # resolution is 16 : 9
SPRITE_SCALING = SCREEN_WIDTH / 1920
SPRITE_SCALING_SYMBOL = SPRITE_SCALING * 0.8  # buttons and symbols scale depending on the resolution
MIN_BET = 0.2
STARTING_BET = 1.0
MAX_BET = 512
START_MONEY = 1000  # money constants can be made to be take from database
button_X = SCREEN_WIDTH * 0.95  # position of refresh button
button_Y = SCREEN_HEIGHT * 0.08
bet_X = SCREEN_WIDTH / 2.02  # position of the bet buttons
bet_Y = SCREEN_HEIGHT / 28
Line1_start_x = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2  # winning lines position
Line1_end_x = Line1_start_x + 600 * SPRITE_SCALING
Line1_end_x2 = Line1_end_x + 600 * SPRITE_SCALING
Line1_start_y = SCREEN_HEIGHT - 450 * SPRITE_SCALING / 2
Line1_end_y = Line1_start_y - 600 * SPRITE_SCALING
Line2_start_y = Line1_start_y - 300 * SPRITE_SCALING
Line2_end_y = Line1_start_y - 300 * SPRITE_SCALING


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.sauce_list = None  # declaration of all things that will change during the game
        self.bet = STARTING_BET
        self.money = START_MONEY
        self.line1 = 0
        self.line2 = 0
        self.line3 = 0
        self.spin_sound = arcade.load_sound("Resources/sound.wav")

    def fill_board(self, line=None):  # helper func that setups the screen

        self.sauce_list = arcade.SpriteList()
        count = 0
        posX = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2  # symbols starting position
        posY = SCREEN_HEIGHT - 450 * SPRITE_SCALING / 2
        background = arcade.Sprite("Resources/background.jpg", SPRITE_SCALING)  # background image and position
        background.center_x = SCREEN_WIDTH / 2
        background.center_y = SCREEN_HEIGHT / 2
        refresh = arcade.Sprite("Resources/refreshbut.png", SPRITE_SCALING * 1.25)  # refresh button image and position
        refresh.center_x = button_X
        refresh.center_y = button_Y
        arrow_up = arcade.Sprite("Resources/arrow.png", SPRITE_SCALING / 2)  # arrow buttons image and position
        arrow_up.center_x = bet_X * 1.12
        arrow_up.center_y = bet_Y * 1.5
        arrow_down = arcade.Sprite("Resources/arrow.png", SPRITE_SCALING / 2, flipped_vertically=True)
        arrow_down.center_x = bet_X * 0.88
        arrow_down.center_y = bet_Y * 1.5
        self.sauce_list.append(background)   # appending to the print list
        self.sauce_list.append(refresh)
        self.sauce_list.append(arrow_up)
        self.sauce_list.append(arrow_down)

        temp = None
        for i in line:  # ugly declaration of how symbols look ,they could duplicate so dictionaries are not useful
            if i == "k":
                temp = arcade.Sprite("Resources/ktp4.png", SPRITE_SCALING_SYMBOL)
            if i == "m":
                temp = arcade.Sprite("Resources/maio.png", SPRITE_SCALING_SYMBOL)
            if i == "v":
                temp = arcade.Sprite("Resources/vinegar.png", SPRITE_SCALING_SYMBOL)
            if i == "g":
                temp = arcade.Sprite("Resources/gorch.png", SPRITE_SCALING_SYMBOL)
            if i == "b":
                temp = arcade.Sprite("Resources/bbq.png", SPRITE_SCALING_SYMBOL)
            if i == "r":
                temp = arcade.Sprite("Resources/ranch.png", SPRITE_SCALING_SYMBOL)
            if i == "t":
                temp = arcade.Sprite("Resources/tabasco.png", SPRITE_SCALING_SYMBOL)
            if i == "s":
                temp = arcade.Sprite("Resources/garlic.png", SPRITE_SCALING_SYMBOL)
            if i == "o":
                temp = arcade.Sprite("Resources/olive.png", SPRITE_SCALING_SYMBOL)
            if i == "c":
                temp = arcade.Sprite("Resources/sour.png", SPRITE_SCALING_SYMBOL)

            temp.center_x = posX
            temp.center_y = posY
            self.sauce_list.append(temp)

            count += 1
            if not count % 5 == 0:  # each symbol is 300x300 and that way they are positioned like a matrix
                posX += 300 * SPRITE_SCALING
            else:
                posX = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2
                posY -= 300 * SPRITE_SCALING

    def setup(self):  # setup function
        result = Slots.main_game(1, 1)  # demo start the game
        line = result.get_board()  # put the board in a line
        self.fill_board(line) # call the helper func to fill the screen

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.sauce_list.draw() # All things that change go here
        arcade.draw_text(f"{self.bet}", bet_X, bet_Y, arcade.color.GREEN_YELLOW, 32, align="center", anchor_x="center")
        arcade.draw_text(f"{round(self.money, 1)}", bet_X - SCREEN_WIDTH / 2.8, bet_Y, arcade.color.GREEN_YELLOW, 32)
        # the bet and the money status text
        if self.line1 != 0:  # if there are winnings on line 1 they should be displayed
            arcade.draw_text(f"Line 1:{round(self.line1, 1)}", bet_X * 1.5, bet_Y * 2.1, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line1_start_y, Line1_end_x, Line1_end_y, arcade.color.GREEN, 10)
            arcade.draw_line(Line1_end_x, Line1_end_y, Line1_end_x2, Line1_start_y, arcade.color.GREEN, 10)
        if self.line2 != 0:  # same as line 1
            arcade.draw_text(f"Line 2:{round(self.line2, 1)}", bet_X * 1.5, bet_Y * 1.4, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line2_start_y, Line1_end_x2, Line2_end_y, arcade.color.GREEN, 10)
        if self.line3 != 0:  # same as line 1
            arcade.draw_text(f"Line 3:{round(self.line3, 1)}", bet_X * 1.5, bet_Y * 0.6, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line1_end_y, Line1_end_x, Line1_start_y, arcade.color.GREEN, 10)
            arcade.draw_line(Line1_end_x, Line1_start_y, Line1_end_x2, Line1_end_y, arcade.color.GREEN, 10)
        # Your drawing code goes here

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.spin_sound, 0.5, 0, False)  # the machine sound

        button_size = 240 * SPRITE_SCALING / 3  # the button is 240 x 240 so there is a calculation of his size
        inside_the_rbutton = False  # boolean indicating that click is inside the refresh button
        if button_X - button_size < x < button_X + button_size and button_Y - button_size < y < button_Y + button_size:
            inside_the_rbutton = True

        if inside_the_rbutton and self.money > self.bet:
            self.money = self.money - self.bet  # things that should happen every spin
            result = Slots.main_game(self.bet, self.money)
            board = result.get_board()
            lines = result.get_lines()  # updating all the values that change
            self.line1 = lines[0]
            self.line2 = lines[1]
            self.line3 = lines[2]
            self.money = self.money + result.get_wins()
            self.fill_board(board)

        inside_the_rbetbutton = False  # same as refresh button
        if bet_X * 1.12 - 20 < x < bet_X * 1.12 + 20 and bet_Y - 15 < y < bet_Y + 45:
            inside_the_rbetbutton = True

        if inside_the_rbetbutton and self.bet < MAX_BET:
            self.bet = self.bet * 2  # updating the bet

        inside_the_lbetbutton = False # same as refresh button
        if bet_X * 0.88 - 20 < x < bet_X * 0.88 + 20 and bet_Y - 15 < y < bet_Y + 45:
            inside_the_lbetbutton = True

        if inside_the_lbetbutton and self.bet > MIN_BET:
            self.bet = self.bet / 2

    def update(self, delta_time, line=None):

        self.sauce_list.draw()  # game update


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()  # the arcade main


if __name__ == "__main__":
    main()

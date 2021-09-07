import arcade
import Slots

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPRITE_SCALING = SCREEN_WIDTH / 1920
SPRITE_SCALING_SYMBOL = SPRITE_SCALING * 0.8
MIN_BET = 0.2
STARTING_BET = 1.0
MAX_BET = 512
START_MONEY = 1000
button_X = SCREEN_WIDTH * 0.95
button_Y = SCREEN_HEIGHT * 0.08
bet_X = SCREEN_WIDTH / 2.02
bet_Y = SCREEN_HEIGHT / 28
Line1_start_x = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2
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
        self.sauce_list = None
        self.bet = STARTING_BET
        self.money = START_MONEY
        self.line1 = 0
        self.line2 = 0
        self.line3 = 0
        self.spin_sound = arcade.load_sound("sound.wav")

    def fill_board(self, line=None):

        self.sauce_list = arcade.SpriteList()
        count = 0
        posX = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2
        posY = SCREEN_HEIGHT - 450 * SPRITE_SCALING / 2
        background = arcade.Sprite("background.jpg", SPRITE_SCALING)
        background.center_x = SCREEN_WIDTH / 2
        background.center_y = SCREEN_HEIGHT / 2
        refresh = arcade.Sprite("refreshbut.png", 1)
        refresh.center_x = button_X
        refresh.center_y = button_Y
        arrow_up = arcade.Sprite("arrow.png", SPRITE_SCALING / 2)
        arrow_up.center_x = bet_X * 1.12
        arrow_up.center_y = bet_Y * 1.5
        arrow_down = arcade.Sprite("arrow.png", SPRITE_SCALING / 2, flipped_vertically=True)
        arrow_down.center_x = bet_X * 0.88
        arrow_down.center_y = bet_Y * 1.5
        self.sauce_list.append(background)
        self.sauce_list.append(refresh)
        self.sauce_list.append(arrow_up)
        self.sauce_list.append(arrow_down)

        temp = None
        for i in line:
            if i == "k": temp = arcade.Sprite("ktp4.png", SPRITE_SCALING_SYMBOL)
            if i == "m": temp = arcade.Sprite("maio.png", SPRITE_SCALING_SYMBOL)
            if i == "v": temp = arcade.Sprite("vinegar.png", SPRITE_SCALING_SYMBOL)
            if i == "g": temp = arcade.Sprite("gorch.png", SPRITE_SCALING_SYMBOL)
            if i == "b": temp = arcade.Sprite("bbq.png", SPRITE_SCALING_SYMBOL)
            if i == "r": temp = arcade.Sprite("ranch.png", SPRITE_SCALING_SYMBOL)
            if i == "t": temp = arcade.Sprite("tabasco.png", SPRITE_SCALING_SYMBOL)
            if i == "s": temp = arcade.Sprite("garlic.png", SPRITE_SCALING_SYMBOL)
            if i == "o": temp = arcade.Sprite("olive.png", SPRITE_SCALING_SYMBOL)
            if i == "c": temp = arcade.Sprite("sour.png", SPRITE_SCALING_SYMBOL)

            temp.center_x = posX
            temp.center_y = posY
            self.sauce_list.append(temp)

            count += 1
            if not count % 5 == 0:
                posX += 300 * SPRITE_SCALING
            else:
                posX = (SCREEN_WIDTH - 4 * 300 * SPRITE_SCALING) / 2
                posY -= 300 * SPRITE_SCALING

    def setup(self):
        result = Slots.main_game(1, 1)
        line = result.get_board()
        self.fill_board(line)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.sauce_list.draw()
        arcade.draw_text(f"{self.bet}", bet_X, bet_Y, arcade.color.GREEN_YELLOW, 32, align="center", anchor_x="center")
        arcade.draw_text(f"{round(self.money, 1)}", bet_X - 450, bet_Y, arcade.color.GREEN_YELLOW, 32)
        if self.line1 != 0:
            arcade.draw_text(f"Line 1:{round(self.line1, 1)}", bet_X * 1.5, bet_Y * 2.1, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line1_start_y, Line1_end_x, Line1_end_y, arcade.color.GREEN, 10)
            arcade.draw_line(Line1_end_x, Line1_end_y, Line1_end_x2, Line1_start_y, arcade.color.GREEN, 10)
        if self.line2 != 0:
            arcade.draw_text(f"Line 2:{round(self.line2, 1)}", bet_X * 1.5, bet_Y * 1.4, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line2_start_y, Line1_end_x2, Line2_end_y, arcade.color.GREEN, 10)
        if self.line3 != 0:
            arcade.draw_text(f"Line 3:{round(self.line3, 1)}", bet_X * 1.5, bet_Y * 0.6, arcade.color.GREEN_YELLOW, 16)
            arcade.draw_line(Line1_start_x, Line1_end_y, Line1_end_x, Line1_start_y, arcade.color.GREEN, 10)
            arcade.draw_line(Line1_start_x, Line1_start_y, Line1_end_x, Line1_end_y, arcade.color.GREEN, 10)
        # Your drawing code goes here

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.spin_sound, 0.5, 0, False)
        if button_X - 60 < x < button_X + 60 and button_Y - 60 < y < button_Y + 60 and self.money > self.bet:
            self.money = self.money - self.bet
            result = Slots.main_game(self.bet, self.money)
            board = result.get_board()
            lines = result.get_lines()
            self.line1 = lines[0]
            self.line2 = lines[1]
            self.line3 = lines[2]
            self.money = self.money + result.get_wins()
            self.fill_board(board)

        if bet_X * 1.12 - 20 < x < bet_X * 1.12 + 20 and bet_Y - 15 < y < bet_Y + 45 and self.bet < MAX_BET:
            self.bet = self.bet * 2

        if bet_X * 0.88 - 20 < x < bet_X * 0.88 + 20 and bet_Y - 15 < y < bet_Y + 45 and self.bet > MIN_BET:
            self.bet = self.bet / 2

    def update(self, delta_time, line=None):
        """ All the logic to move, and the game logic goes here. """
        self.sauce_list.draw()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

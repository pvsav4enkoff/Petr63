# в пактах pycharm arcade
# если не получиться
# pip install arcade в CMD
# pip install --upgrade python в терминале pycharm  обновить Python
 # python.exe -m pip install --upgrade pip  если не получится обновить
 # pip install arcade
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "import module"


class MyImport(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
       arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

   def setup(self):
       pass

   def on_draw(self):
       self.clear()


def main():
   window = MyImport()
   window.setup()
   arcade.run()


if __name__ == "__main__":
   main()

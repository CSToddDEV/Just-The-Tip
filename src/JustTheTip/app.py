"""
Tip, hourly, paycheck, and tipout tracking application!
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class JustTheTip(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))

        name_label = toga.Label(
            'JUST THE TIP',
            style=Pack(padding=(5, 5),alignment=CENTER)
        )
        #self.name_input = toga.TextInput(style=Pack(flex=0))

        name_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER, flex=10, padding=5))
        name_box.add(name_label)
        #name_box.add(self.name_input)

        button = toga.Button(
            'Calvin Todd Test',
            style=Pack(padding=(5,5), flex=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

   ## def say_hello(self, widget):
     #   print("Hello", self.name_input.value)


def main():
    return JustTheTip()

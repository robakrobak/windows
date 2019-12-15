import tkinter as tk
import tkinter.colorchooser

from random import randint


# root - main window : tk.Tk()
class MainWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.geometry = main_window.minsize(width=500, height=1)
        self.title = main_window.wm_title('Main Window Title')
        self.frame = tk.Frame(self.main_window)

        self.new_label('Default text', MainWindow)
        self.new_button(MainWindow)

        self.frame.pack()

    def new_label(self, text, _class):
        l_other01 = tk.Label(self.frame, text='Hi. If you want to', width=25, bg='darkgrey')
        l_other02 = tk.Label(self.frame, text='guess right number..', width=25)

        l_other01.grid(column=0, row=1)
        l_other02.grid(column=0, row=2)

    def new_button(self, _class):
        b_start_game = tk.Button(self.frame, text='Start Game', command=lambda: self.new_window(GameWindow))
        b_start_game.grid(column=0, row=3)

        b_end_game = tk.Button(self.frame, text='Quit Game', command=self.quit_game)
        b_end_game.grid(column=0, row=4)

    def new_window(self, _class):
        self.new = tk.Toplevel(self.main_window)
        _class(self.new)

    def quit_game(self):
        self.main_window.destroy()


class GameWindow:
    def __init__(self, game_window):
        self.game_window = game_window
        # self.geometry = game_window.minsize(width=1, height=1)
        self.title = game_window.wm_title('Game Window')
        self.frame = tk.Frame(self.game_window)

        self.new_label_game('Chose right number', GameWindow)
        self.new_button_game(GameWindow)

        self.frame.pack()

    def new_label_game(self, text, _class):
        l_game = tk.Label(self.frame, text=text, pady=12)
        l_game.grid(column=0, row=0, columnspan=3)

    def new_button_game(self, _class):
        random = randint(1, 9)

        # Numbers
        b_no1 = tkinter.Button(self.frame, text=1, command=lambda: b_no1.configure(
            background='green') if random == 1 else b_no1.configure(background='red'))
        b_no1.grid(row=1, column=0, sticky='e', )
        b_no2 = tkinter.Button(self.frame, text=2, command=lambda: b_no2.configure(
            background='green') if random == 2 else b_no2.configure(background='red'))
        b_no2.grid(row=1, column=1, sticky='ns')
        b_no3 = tkinter.Button(self.frame, text=3, command=lambda: b_no3.configure(
            background='green') if random == 3 else b_no3.configure(background='red'))
        b_no3.grid(row=1, column=2, sticky='w')
        b_no4 = tkinter.Button(self.frame, text=4, command=lambda: b_no4.configure(
            background='green') if random == 4 else b_no4.configure(background='red'))
        b_no4.grid(row=2, column=0, sticky='e')
        b_no5 = tkinter.Button(self.frame, text=5, command=lambda: b_no5.configure(
            background='green') if random == 5 else b_no5.configure(background='red'))
        b_no5.grid(row=2, column=1, sticky='ns')
        b_no6 = tkinter.Button(self.frame, text=6, command=lambda: b_no6.configure(
            background='green') if random == 6 else b_no6.configure(background='red'))
        b_no6.grid(row=2, column=2, sticky='w')
        b_no7 = tkinter.Button(self.frame, text=7, command=lambda: b_no7.configure(
            background='green') if random == 7 else b_no7.configure(background='red'))
        b_no7.grid(row=3, column=0, sticky='e')
        b_no8 = tkinter.Button(self.frame, text=8, command=lambda: b_no8.configure(
            background='green') if random == 8 else b_no8.configure(background='red'))
        b_no8.grid(row=3, column=1, sticky='ns')
        b_no9 = tkinter.Button(self.frame, text=9, command=lambda: b_no9.configure(
            background='green') if random == 9 else b_no9.configure(background='red'))
        b_no9.grid(row=3, column=2, sticky='w')

        b_end_game = tk.Button(self.frame, text='To main window', command=self.quit_game)
        b_end_game.grid(column=0, row=4, columnspan=3)

    def quit_game(self):
        self.game_window.destroy()


def app():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    app()

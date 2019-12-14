import tkinter
import tkinter.colorchooser

from random import randint


def answer(answer_random, random_number):
    if answer_random == random_number:
        print("Here we go!")
    else:
        print("No hell no! Again!")

def game():
    random = randint(1, 9)
    window2 = tkinter.Tk()
    window2.wm_title('Choose your number')

    # question
    frame_question = tkinter.Text(window2, borderwidth=1, relief='ridge')
    frame_question.grid(row=1, column=0, sticky='ns')
    label_question = tkinter.Label(frame_question, text="Guess Number:")
    label_question.pack()

    # Frame numbers
    frame_numbers = tkinter.Frame(window2, borderwidth=0, relief='ridge')
    frame_numbers.grid(row=3, column=0, sticky='ns')

    # Numbers
    label_no1 = tkinter.Button(frame_numbers, text=1, command=lambda: label_no1.configure(
        background='green') if random == 1 else label_no1.configure(background='red'))
    label_no1.grid(row=3, column=1, sticky='ns')
    label_no2 = tkinter.Button(frame_numbers, text=2, command=lambda: label_no2.configure(
        background='green') if random == 2 else label_no2.configure(background='red'))
    label_no2.grid(row=3, column=2, sticky='ns')
    label_no3 = tkinter.Button(frame_numbers, text=3, command=lambda: label_no3.configure(
        background='green') if random == 3 else label_no3.configure(background='red'))
    label_no3.grid(row=3, column=3, sticky='ns')
    label_no4 = tkinter.Button(frame_numbers, text=4, command=lambda: label_no4.configure(
        background='green') if random == 4 else label_no4.configure(background='red'))
    label_no4.grid(row=4, column=1, sticky='ns')
    label_no5 = tkinter.Button(frame_numbers, text=5, command=lambda: label_no5.configure(
        background='green') if random == 5 else label_no5.configure(background='red'))
    label_no5.grid(row=4, column=2, sticky='ns')
    label_no6 = tkinter.Button(frame_numbers, text=6, command=lambda: label_no6.configure(
        background='green') if random == 6 else label_no6.configure(background='red'))
    label_no6.grid(row=4, column=3, sticky='ns')
    label_no7 = tkinter.Button(frame_numbers, text=7, command=lambda: label_no7.configure(
        background='green') if random == 7 else label_no7.configure(background='red'))
    label_no7.grid(row=5, column=1, sticky='ns')
    label_no8 = tkinter.Button(frame_numbers, text=8, command=lambda: label_no8.configure(
        background='green') if random == 8 else label_no8.configure(background='red'))
    label_no8.grid(row=5, column=2, sticky='ns')
    label_no9 = tkinter.Button(frame_numbers, text=9, command=lambda: label_no9.configure(
        background='green') if random == 9 else label_no9.configure(background='red'))
    label_no9.grid(row=5, column=3, sticky='ns')


def start_button():
    frame_start_game = tkinter.Frame(window, borderwidth=1, relief='ridge')
    frame_start_game.grid(row=0, column=0, sticky='ns')

    b_start_game = tkinter.Button(frame_start_game, text="Press here to start", command=game)
    b_start_game.pack(fill='x')


def end_button():
    frame_end_game = tkinter.Frame(window, borderwidth=1, relief='ridge')
    frame_end_game.grid(row=6, column=0, sticky='ns')

    # b_end_game = tkinter.Button(frame_end_game, text="Press here to finish", command=window.destroy)
    b_end_game = tkinter.Button(frame_end_game, text="Press here to finish", command=window.destroy)
    b_end_game.pack()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.wm_title('Start window')
    start_button()
    end_button()
    window.mainloop()

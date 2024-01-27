from tkinter import *
from functools import partial
from calc import calculate


def change_screen(screen_text: StringVar, char: str):
    screen_text.set(screen_text.get() + char)

def clear_screen(screen_text: StringVar):
    screen_text.set('')

def del_screen(screen_text: StringVar):
    screen_text.set(screen_text.get()[:-1])


def keep_flat(event): 
    event.widget.config(relief=FLAT) 

def output_result(text):
    result = calculate(text.get())
    text.set(str(result))


def create_calc(root):
    UNIT = 30
    my_font = 'Courier 18 bold'

    root.title("Calculette")
    root.resizable(False, False)


    frame = Canvas(root, bg="#2b2d42", width=15*UNIT, height=22*UNIT)
    frame.grid(sticky='nsew', columnspan=15, rowspan=22)


    text = StringVar()
    screen = Label(root, textvariable=text, bg="#edf2f4", relief=FLAT, anchor=W, padx=UNIT, font=my_font, width=1)
    screen.grid(column=1, row=1, columnspan=13, rowspan=3, sticky="nsew")



    # adding number keys
    nums = [Button(
        root, text=str(9-i), bg="#8d99ae", activebackground='#79869c', relief=FLAT, command=partial(change_screen, text, str(9-i)), font=my_font
        ) for i in range(10)]
    for i in range(9):
        nums[i].grid(row=9+(i//3)*3, column=8-(i%3)*3,columnspan=2, rowspan=2, sticky="nsew")
    nums[-1].grid(row=18, column=2,columnspan=5, rowspan=2, sticky="nsew")

    # operator keys
    operators = [Button(
        root, text=op, bg="#edf2f4", activebackground='#ced4da', relief=FLAT, command=partial(change_screen, text, op), font=my_font
        ) for op in '/*-+']
    positions = [(6, 8), (6, 11), (9, 11), (12, 11)]
    for i in range(4):
        row, col = positions[i]
        operators[i].grid(row=row, column=col,columnspan=2, rowspan=2, sticky="nsew")

    # point, equal, del, clear keys
    point = Button(root, text=".", bg="#8d99ae", activebackground='#79869c', relief=FLAT, command=partial(change_screen, text, "."), font=my_font)
    point.grid(row=18, column=8,columnspan=2, rowspan=2, sticky="nsew")

    equal = Button(root, text="=", bg="#ef233c", activebackground='#d90429', relief=FLAT, command=partial(output_result, text), font=my_font)
    equal.grid(row=15, column=11,columnspan=2, rowspan=5, sticky="nsew")

    del_btn = Button(root, text="del", bg="#ef233c", activebackground='#d90429', relief=FLAT, command=partial(del_screen, text), font=my_font)
    del_btn.grid(row=6, column=5,columnspan=2, rowspan=2, sticky="nsew")

    clear = Button(root, text="C", bg="#ef233c", activebackground='#d90429', relief=FLAT, command=partial(clear_screen, text), font=my_font)
    clear.grid(row=6, column=2,columnspan=2, rowspan=2, sticky="nsew")

    root.bind('<Button-1>', keep_flat)

def main():
    root = Tk()
    create_calc(root)
    root.mainloop()

if __name__ == "__main__":
    main()

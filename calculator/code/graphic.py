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

def output_result(text: StringVar):
    result = calculate(text.get())
    text.set(str(result))


def create_calc() -> tuple[Tk, StringVar]:
    UNIT = 30
    my_font = 'Courier 18 bold'

    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)


    frame = Canvas(root, bg="#2b2d42", width=15*UNIT, height=22*UNIT)
    frame.grid(sticky='nsew', columnspan=15, rowspan=22)

    text = StringVar()
    screen = Label(root, textvariable=text, bg="#edf2f4", relief=FLAT, padx=UNIT, anchor=W, font=my_font, width=1, name="screen")
    screen.grid(column=1, row=1, columnspan=13, rowspan=3, sticky="nsew")


    # adding number keys
    nums = [Button(
        root, text=str(9-i), bg="#8d99ae", activebackground='#79869c', relief=FLAT, name=f"btn-{9-i}", font=my_font
        ) for i in range(10)]
    for i in range(9):
        row, col, = 9+(i//3)*3, 8-(i%3)*3
        nums[i].grid(row=row, column=col, columnspan=2, rowspan=2, sticky="nsew")
    nums[-1].grid(row=18, column=2,columnspan=5, rowspan=2, sticky="nsew")

    # operator keys
    operators = [Button(
        root, text=op, bg="#edf2f4", activebackground='#ced4da', relief=FLAT, name=f"btn-{name}", font=my_font
        ) for op, name in zip('/*-+', ['div', 'mult', 'sub', 'add'])]
    positions = [(6, 8), (6, 11), (9, 11), (12, 11)]
    for i in range(4):
        row, col = positions[i]
        operators[i].grid(row=row, column=col,columnspan=2, rowspan=2, sticky="nsew")

    # point, equal, del, clear keys
    point = Button(root, text=".", bg="#8d99ae", activebackground='#79869c', relief=FLAT, name=f"btn-point", font=my_font)
    point.grid(row=18, column=8,columnspan=2, rowspan=2, sticky="nsew")

    equal = Button(root, text="=", bg="#ef233c", activebackground='#d90429', relief=FLAT, name=f"btn-equal", font=my_font)
    equal.grid(row=15, column=11,columnspan=2, rowspan=5, sticky="nsew")

    del_btn = Button(root, text="del", bg="#ef233c", activebackground='#d90429', relief=FLAT, name=f"btn-del", font=my_font)
    del_btn.grid(row=6, column=5,columnspan=2, rowspan=2, sticky="nsew")

    clear = Button(root, text="C", bg="#ef233c", activebackground='#d90429', relief=FLAT, name=f"btn-clear", font=my_font)
    clear.grid(row=6, column=2,columnspan=2, rowspan=2, sticky="nsew")

    root.bind('<Button-1>', keep_flat)

    return (root, text)


def config_button(root: Tk, text: StringVar):
    config = {
        'btn-1': partial(change_screen, text, '1'),
        'btn-2': partial(change_screen, text, '2'),
        'btn-3': partial(change_screen, text, '3'),
        'btn-4': partial(change_screen, text, '4'),
        'btn-5': partial(change_screen, text, '5'),
        'btn-6': partial(change_screen, text, '6'),
        'btn-7': partial(change_screen, text, '7'),
        'btn-8': partial(change_screen, text, '8'),
        'btn-9': partial(change_screen, text, '9'),
        'btn-0': partial(change_screen, text, '0'),
        'btn-point': partial(change_screen, text, '.'),
        'btn-div': partial(change_screen, text, '/'),
        'btn-mult': partial(change_screen, text, '*'),
        'btn-sub': partial(change_screen, text, '-'),
        'btn-add': partial(change_screen, text, '+'),
        'btn-equal': partial(output_result, text),
        'btn-del': partial(del_screen, text),
        'btn-clear': partial(clear_screen, text)
    }
    for child in root.children:
        if child.startswith('btn'):
            root.nametowidget(child).config(command=config[child])


def main():
    calc, text = create_calc()
    config_button(calc, text)
    
    calc.mainloop()

if __name__ == "__main__":
    main()

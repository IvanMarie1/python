from graphic import create_calc, config_button


def main():
    my_calc, text = create_calc()
    config_button(my_calc, text)

    my_calc.mainloop()


if __name__ == "__main__":
    main()

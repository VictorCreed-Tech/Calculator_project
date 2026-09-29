import tkinter

# game setup
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["+", "-", "×", "÷", "="]
top_symbols = ["AC", "+/-", "%",]

# row and column setup
row_count = len(button_values)
col_count = len(button_values[0]) if row_count > 0 else 0

# color setup
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

# window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

# window frame setup
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", anchor="e", font=(
    "Arial", 45), background=color_black, foreground=color_white, width=col_count)

label.grid(row=0, column=0, columnspan=col_count, sticky="we")

for row in range(row_count):
    for column in range(col_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=col_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row + 1, column=column)
frame.pack()
# reminder: the square root button is currently showing as as gray instead of drak gray

# A+B, A-B, A*B, A/B, A%B, A^B, √A, 1/A, A!, log(A), ln(A), sin(A), cos(A), tan(A), asin(A), acos(A), atan(A)
A = "0"
operator = None
B = None


def remove_zero_decimal(num):
    if num % 1 == 0:
        return int(num)
    else:
        return str(num)


def clear_all():
    global A, B, operator


def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
               
                clear_all()

        elif value in ["+", "-", "×", "÷"]:
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

                operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else:  # digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


# center the window of the calculator
window.update()  # upate window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# formate "(w)x(h)+(x)+(y)" for the window geometry
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()

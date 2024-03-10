import customtkinter as ct

ct.set_appearance_mode("dark")

root = ct.CTk()
root.geometry('400x200')
root.title("Pol's Calculator")


def calculator():
    try:
        calculation = output.get('0.0', 'end').strip()
        result = eval(calculation)
        output.delete('0.0', 'end')
        output.insert('0.0', str(result))
    except Exception as e:
        output.delete('0.0', 'end')
        output.insert('0.0', 'Error')


output = ct.CTkTextbox(master=root, width=150, height=85, corner_radius=20, border_width=4, border_color='grey')
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

buttons = [
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", "c", "/", "="
]

col = 0
row = 1

for button_value in buttons:
    def command(val=button_value):
        if val == "=":
            calculator()
            return
        elif val == "c":
            output.delete('0.0', 'end')
            return
        output.insert('end', str(val))
    button_loop = ct.CTkButton(master=root, text=button_value, command=command, corner_radius=20, width=65, height=55, font=('arial', 15))
    button_loop.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1


root.mainloop()

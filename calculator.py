import customtkinter as ct

ct.set_appearance_mode("dark")

root = ct.CTk()
root.geometry('361x354')
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


output = ct.CTkTextbox(master=root, width=340, height=50, corner_radius=10, border_width=5, border_color='grey')
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

button1 = ct.CTkButton(master=root, text='1', command=lambda: output.insert('end', '1'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = ct.CTkButton(master=output, text='2', command=lambda: output.insert('end', '2'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = ct.CTkButton(master=output, text='3', command=lambda: output.insert('end', '3'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = ct.CTkButton(master=output, text='4', command=lambda: output.insert('end', '4'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = ct.CTkButton(master=output, text='5', command=lambda: output.insert('end', '5'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = ct.CTkButton(master=output, text='6', command=lambda: output.insert('end', '6'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = ct.CTkButton(master=output, text='7', command=lambda: output.insert('end', '7'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = ct.CTkButton(master=output, text='8', command=lambda: output.insert('end', '8'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = ct.CTkButton(master=output, text='9', command=lambda: output.insert('end', '9'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = ct.CTkButton(master=output, text='0', command=lambda: output.insert('end', '0'), corner_radius=20, width=80,
                       height=55, font=('arial', 30))
button0.grid(row=4, column=0, padx=5, pady=5)

# Creating operation buttons
button_clear = ct.CTkButton(master=output, text='C', command=lambda: output.delete('0.0', 'end'), corner_radius=20,
                            width=80, height=55, font=('arial', 30))
button_clear.grid(row=4, column=1, padx=5, pady=5)

button_equals = ct.CTkButton(master=root, text='=', command=calculator, corner_radius=20, width=80, height=55,
                             font=('arial', 30))
button_equals.grid(row=4, column=2, padx=5, pady=5)

button_add = ct.CTkButton(master=output, text='+', command=lambda: output.insert('end', '+'), corner_radius=20,
                          width=80, height=55, font=('arial', 30))
button_add.grid(row=1, column=3, padx=5, pady=5)

button_subtract = ct.CTkButton(master=output, text='-', command=lambda: output.insert('end', '-'), corner_radius=20,
                               width=80, height=55, font=('arial', 30))
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_multiply = ct.CTkButton(master=output, text='x', command=lambda: output.insert('end', '*'), corner_radius=20,
                               width=80, height=55, font=('arial', 30))
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = ct.CTkButton(master=output, text='/', command=lambda: output.insert('end', '/'), corner_radius=20,
                             width=80, height=55, font=('arial', 30))
button_divide.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()

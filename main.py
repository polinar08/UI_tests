import customtkinter as ct

ct.set_appearance_mode("dark")

root = ct.CTk()
root.geometry("400X200")
root.title("UI Button Creator")


def log_in():
    print("@!name")


frame = ct.CTkFrame(master=root, width=350, height=150, fg_color="white")
frame.pack(pady=40, padx=80, fill="both", expand=True)

label = ct.CTkLabel(master=frame, text="log_in", font=("Roboto", 20), text_color="black")
label.pack(pady=10, padx=40)

entry = ct.CTkEntry(master=frame, width=250, height=100, fg_color="black", placeholder_text="USERNAME:")
entry.pack(pady=10, padx=40)


def button_event():
    print("login")


button = ct.CTkButton(master=frame, width=150, height=50, text="Button", command=button_event)
button.pack(pady=10, padx=40)

root.mainloop()

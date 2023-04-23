import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

check_var = tkinter.StringVar(value="on")

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

checkbox = customtkinter.CTkCheckBox(master=app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=20, pady=10)



app.mainloop()
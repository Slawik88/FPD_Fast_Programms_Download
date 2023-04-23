
import customtkinter
app = customtkinter.CTk()

def switch_event():
    print("switch toggled, current value:", switch_var.get())





for i in range(10):
    switch_var = customtkinter.StringVar(value="on")
    switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
    switch.pack()
app.mainloop()
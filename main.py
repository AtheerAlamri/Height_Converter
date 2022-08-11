from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter Converting App")
window.configure(background='light green')
window.geometry('320x220')
window.resizable(width=False, height=False)


def convert():
    value = float(feet_entry.get())
    meter = value * 0.3048
    meter_value.set('%.4f' % meter)


def clear():
    feet_value.set('')
    meter_value.set('')


# Feet Label
feet_lb1 = Label(window, text='Feet', bg='purple', fg='white', width=14)
feet_lb1.grid(column=0, row=0, padx=15, pady=15)
# Feet entry widgets
feet_value = DoubleVar()
feet_entry = Entry(window, textvariable=feet_value, width=14)
feet_entry.grid(column=1, row=0)
feet_entry.delete(0, 'end')

# Meter Label
meter_lb1 = Label(window, text='Meter', bg='brown', fg='white', width=14)
meter_lb1.grid(column=0, row=1)
# Meter entry widgets
meter_value = DoubleVar()
meter_entry = Entry(window, textvariable=meter_value, width=14)
meter_entry.grid(column=1, row=1, pady=30)
meter_entry.delete(0, 'end')

# Convert button
convert_btn = Button(window, text='Convert', bg='blue', fg='white', width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

# Clear button
clear_btn = Button(window, text='Clear', bg='black', fg='white', width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15)


window.mainloop()

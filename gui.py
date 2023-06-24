from tkinter import *
from tkinter import ttk, filedialog

def calculate(*args):
    try:
        value = float(canvas_width.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=3, sticky=W, columnspan=3)

##CANVAS##
ttk.Label(mainframe, text="Canvas Size:").grid(column=1, row=1, sticky=W)

ttk.Label(mainframe, text="inches").grid(column=3, row=1, sticky=W)
canvas_width = StringVar()
canvas_width_entry = ttk.Entry(mainframe, width=3, textvariable=canvas_width)
canvas_width_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="inches").grid(column=5, row=1, sticky=W)
canvas_length = StringVar()
canvas_length_entry = ttk.Entry(mainframe, width=3, textvariable=canvas_length)
canvas_length_entry.grid(column=4, row=1, sticky=(W))

##CARD##
ttk.Label(mainframe, text="Card Size:").grid(column=1, row=2, sticky=W)

ttk.Label(mainframe, text="inches").grid(column=3, row=2, sticky=W)
card_width = StringVar()
card_width_entry = ttk.Entry(mainframe, width=3, textvariable=card_width)
card_width_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="inches").grid(column=5, row=2, sticky=W)
card_length = StringVar()
card_length_entry = ttk.Entry(mainframe, width=3, textvariable=card_length)
card_length_entry.grid(column=4, row=2, sticky=(W))

##INPUT DIRECTORY##
#filename = filedialog.askdirectory()
def inputDirectorySelect():
    filename = filedialog.askdirectory()
      
    # Change label contents
    label_input_directory.configure(text="Input Directory: "+filename)

def outputDirectorySelect():
    filename = filedialog.askdirectory()
      
    # Change label contents
    label_input_directory.configure(text="Output Directory: "+filename)

# Create a File Explorer label
label_input_directory = Label(mainframe,
                            text = "Select Input Directory",
                            fg = "blue")

label_output_directory = Label(mainframe,
                            text = "Select Output Directory",
                            fg = "blue")

button_input = Button(mainframe,
                        text = "Browse",
                        command = inputDirectorySelect)

button_output = Button(mainframe,
                        text = "Browse",
                        command = outputDirectorySelect)
  
button_exit = Button(mainframe,
                     text = "Exit",
                     command = exit)

label_input_directory.grid(column = 1, row = 3, columnspan=3)
label_output_directory.grid(column = 1, row = 4, columnspan=3)
  
button_input.grid(column = 4, row = 3, columnspan=3)
button_output.grid(column = 4, row = 4, columnspan=3)
  
button_exit.grid(column = 5,row = 5)




for child in mainframe.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

canvas_width_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
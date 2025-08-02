import tkinter as tk
from tkinter.messagebox import showerror

# Defining window_resize function
def window_resize():
    try:
        root.geometry(f'{width_root.get()}x{height_root.get()}')
    except:
        showerror(title='Wrong Inputs',message='Width x Height are wrong. Please provide width & height as integer.')


root = tk.Tk()
root.geometry('300x260')
root.resizable(False, False)
root.title('Window Resizer')
root.iconbitmap('./resize.ico')
# Creating head of the root window
tk.Label(root, text='Window Resizer', font='Verdana 17').pack()

# Creating a fram which includes width and height entries and button to resize window
input_frame = tk.Frame(root)
input_frame.pack(pady=20, fill='y', anchor='center')

# Creating width and height labels
tk.Label(input_frame, text='Width', font=('sans-serif', 12)).grid(row=1, column=0, padx=5)
tk.Label(input_frame, text='Height', font=('sans-serif', 12)).grid(row=2, column=0, padx=5)

# Creating width and height entries
width_root = tk.IntVar()
height_root = tk.IntVar()

# setting initial width and height
width_root.set(350)
height_root.set(300)

# Entries
tk.Spinbox(input_frame, from_=100, to=10000, textvariable=width_root, wrap=False).grid(row=1, column=1, ipady=5, ipadx=10, padx=5, pady=5)
tk.Spinbox(input_frame, from_=100, to=10000, textvariable=height_root, wrap=False).grid(row=2, column=1, ipady=5, ipadx=10, padx=5, pady=5)

# creating button to resize windows
tk.Button(input_frame, text='Resize', padx=30, pady=5, command=window_resize).grid(row=3, column=0, columnspan=2, sticky='s')

root.mainloop()
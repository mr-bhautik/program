import tkinter as tk
import sys
r = tk.Tk()
r.title("tinker app")
button = tk.Button(r, text="stop", width="25", command=r.destroy)
button.pack()
r.mainloop()
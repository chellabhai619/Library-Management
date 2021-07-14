from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('300x500')

frame=Frame(root)
frame.pack(fill=BOTH,expand=1)

canvas=Canvas(frame)
canvas.pack(side=LEFT,fill=BOTH,expand=1)

scrb=ttk.Scrollbar(frame,orient=VERTICAL,command=canvas.yview)
scrb.pack(side=RIGHT,fill=Y)

canvas.configure(yscrollcommand=scrb.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta
 / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

frame2=Frame(canvas)
canvas.create_window((0,0),window=frame2,anchor="nw")

for thing in range(100):
    Button(frame2, text=f"Button{thing}").grid(row=thing,column=0,pady=10,padx=10 )
root.mainloop()
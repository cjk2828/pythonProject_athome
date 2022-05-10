import tkinter
import tkinter.messagebox
top = tkinter.Tk()

frame = tkinter.Frame(top)
frame.pack(side=tkinter.BOTTOM)

def clicked(event=None):
    message_box.insert(tkinter.END,input_text.get())
    message_box.yview(tkinter.END)
    input_text.set("")

input_text = tkinter.StringVar()
input_text.set('')

txt = tkinter.Entry(top,textvariable=input_text,width=40,height=8)
# txt.bind("<Return>",clicked)
txt.pack(side=tkinter.TOP)

btn = tkinter.Button(top,text='Enter',command=clicked)
btn.pack()

message_box = tkinter.Listbox(frame,height=10,width=20)
message_box.pack(side=tkinter.LEFT,fill=tkinter.BOTH)

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

message_box.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = message_box.yview)

top.mainloop()
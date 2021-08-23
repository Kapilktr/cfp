# Creating GUI with tkinter

from main import get_response
from tkinter import *


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))

        res = get_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("chating")
base.geometry("300x400")
base.resizable(width=FALSE, height=FALSE)

# Create Chat window
ChatLog = Text(base, bd=0, bg="Yellow", height="8", width="50", font="Arial", )

ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="circle")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("RED", 15, 'bold'), text="SEND", width="12", height=5,
                    bd=0, bg="BLUE", activebackground="#3c94ff", fg='YELLOW',
                    command=send)

# Create the box to enter message
EntryBox = Text(base, bd=0, bg="GREEN", width="39", height="5", font="Arial")
# EntryBox.bind("<Return>", send)

# Place all components on the screen
scrollbar.place(x=276, y=6, height=386)
ChatLog.place(x=6, y=6, height=296, width=270)
EntryBox.place(x=6, y=301, height=90,width=209)
SendButton.place(x=210, y=301, height=90,width=68)

base.mainloop()

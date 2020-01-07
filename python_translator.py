from tkinter import *
from tkinter import ttk
from googletrans import Translator


def translate(*args):
    try:
        word = eng.get()
        translator = Translator()
        rus.set(translator.translate(word, src='en', dest='russian').text)
    except ValueError:
        pass

root = Tk()
root.title("Google Translator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

eng = StringVar()
rus = StringVar()

feet_entry = ttk.Entry(mainframe, width=20, textvariable=eng)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=rus).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Translate", command=translate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="English: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Russian: ").grid(column=1, row=2, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', translate)

root.mainloop()

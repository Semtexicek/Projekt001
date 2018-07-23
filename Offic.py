from tkinter import *
from tkinter.ttk import *


class mainFrame():
    def __init__(self):
        self.root = Tk()
        self.root.title('Offic')
        self.root.geometry('800x600')

        mainFrame.setup_menu(self)
        mainFrame.setup_main_screen(self, 70, 24)
        mainFrame.setup_answerchoice_screen(self, 70, 11)
        mainFrame.setup_answer_screen(self)
        mainFrame.setup_map_screen(self)
        mainFrame.setup_info_screen(self)


    def setup_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label="New")
        filemenu.add_command(label = "Open")
        filemenu.add_command(label = "Save")
        filemenu.add_command(label = "Save as...")
        filemenu.add_command(label = "Close")
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.root.quit)
        menubar.add_cascade(label = "File", menu = filemenu)
        self.root.config(menu = menubar)

    def setup_main_screen(self, x, y):
        self.mainScreen = Text(self.root, wrap = WORD, width = x, heigh = y, border = 2, bg = 'black', fg = 'white')
        self.mainScreen.insert(END, 'Tady by bohl byt vypsanej text toho co se vzdycky deje, quest nebo nejakej takovej bordel.')
        self.mainScreen.configure(state = DISABLED)
        self.mainScreen.place(x = 0, y = 0) 

    def setup_answerchoice_screen(self, x, y):
        self.answerchoiceScreen = Text(self.root, wrap = WORD, width = x, heigh = y, border = 2, bg = 'black', fg = 'white')
        self.answerchoiceScreen.insert(END, 'Answer Window')
        self.answerchoiceScreen.configure(state = DISABLED)
        self.answerchoiceScreen.place(x = 0, y = 390)

    def setup_answer_screen(self):
        self.answerScreen = Entry(self.root, width = 93)
        self.answerScreen.place(x = 0, y = 578)

    def setup_map_screen(self):
        self.mapScreen = Text(self.root, wrap = WORD, width = 29, heigh = 15, border = 2, bg = 'black', fg = 'white',)
        self.mapScreen.insert(END, 'Tady bude nejaka forma mapy')
        self.mapScreen.configure(state = DISABLED)
        self.mapScreen.place(x = 565, y = 0)

    def setup_info_screen(self):
        self.infoScreen = Text(self.root, wrap = WORD, width = 29, border = 2, heigh = 22, bg = 'black', fg = 'white')
        self.infoScreen.insert(END, 'Tady by mohl byt nejakej completni log [combat log atd.]')
        self.infoScreen.configure(state = DISABLED)
        self.infoScreen.place(x = 565, y = 244)

    def write_to_main_screen(self, message):
        self.mainScreen.insert(END, message)

mainFrame()
mainloop()
from tkinter import Button, Tk

import dataX



class Interfaz():
    def __init__(self,root) -> None:
        self.button = None
        self.root = root
        self.root.geometry('400x200')


    def makeAButton(self):
        self.button = Button(self.root,text='Hi',command=Gestor.printer(gestor))
        self.button.pack()

class Gestor():
    def __init__(self, nom,tipos) -> None:
        self.nombres= nom
        self.tipos = tipos

        self.a = []
    def printer(self):
        self.a.append('1212')
        print(self.a)

if __name__ == '__main__':
    root = Tk()
    gestor = Gestor(['wdas','dsasa'],[])
    inter = Interfaz(root)
    inter.makeAButton()

    root.mainloop()

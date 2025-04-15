import tkinter
import customtkinter
from datetime import datetime
import sqlite3

class databaseHelper():

    def __init__(self):
        self.con = sqlite3.connect("todo.db")
        self.cursor = self.con.cursor()

    def close(self):

        self.con.close()

    def createDB(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS TODO(idTodo INTEGER PRIMARY KEY AUTOINCREMENT, texto VARCHAR(100),checkTODO BOOLEAN DEFAULT FALSE)")

        self.con.commit()
    
    def add(self,texto):

        self.cursor.execute("INSERT INTO TODO(texto) VALUES (?)",(texto,))
        self.con.commit()

    def check(self,id,checked):

        self.cursor.execute("UPDATE TODO SET checkTODO = ?  WHERE idTodo = ?", (id,checked,))
        self.con.commit()

    def updateTexto(self, id,texto):
         
        self.cursor.execute("UPDATE TODO SET texto = ?  WHERE idTodo = ?", (texto,id,))
        self.con.commit()

    def delete(self,id):

        self.cursor.execute("DELETE FROM TODO WHERE idTodo = ?",(id,))
        self.con.commit()

    def getALL(self):

        self.cursor.execute("SELECT * FROM TODO ")
        rows = self.cursor.fetchall()
        self.con.commit()

        return rows
    
    def getID(self,id):

        self.cursor.execute("select * from TODO where idTodo = ?",(id,))

        return self.cursor.fetchone()
    
    def getLast(self):

        self.cursor.execute("select * from TODO where idTodo = ?",(self.cursor.lastrowid,))

        return self.cursor.fetchone()
        

        
        
        
    
class App(customtkinter.CTk):
    now = datetime.now()
    database = databaseHelper()
    database.createDB()

    

    def __init__(self):
        super().__init__(fg_color="#1ea2ac")
        self.geometry("450x700")
        self.title("TO-DO")
        self.labelDay = customtkinter.CTkLabel(self, text = f"{self.now.strftime('%B')}, {self.now.strftime('%A')} {self.now.day}",fg_color="transparent",width=100, height=100,font=(" Verdana",40,"bold"))
        self.labelDay.place(x=65,y=5)

        self.textEntry = customtkinter.CTkEntry(self,placeholder_text="Add a new todo",fg_color="#ffffff",width=350, height=50,font=(" Verdana",20),corner_radius=10,border_width=0,text_color="#000000")
        self.textEntry.place(x=10,y=640)

        self.bottonAdd = customtkinter.CTkButton(self,text="Add",command=self.buttonAddTODO,width=50, height=50,font=("Verdana",20),corner_radius=10,border_width=0,fg_color="#2b7088")
        self.bottonAdd.place(x=370,y= 640)

        self.scrollTodo = scrollTODOS(self, width=350, height=520,fg_color="#1ea2ac", scrollbar_button_color = "#1ea2ac",scrollbar_button_hover_color = "#1ea2ac",itemsTodo=self.database.getALL(),database=self.database)
        self.scrollTodo.place(x= 35,y = 100)

        


    def buttonAddTODO(self):

        texto = self.textEntry.get()
        self.database.add(texto)
        itemtodo = self.database.getLast()
        self.scrollTodo.items.append(itemtodo)
        self.scrollTodo.addItem(itemtodo)


        
    def close(self):

        for item in list(zip(self.scrollTodo.items,self.scrollTodo.checkboxs)):

            self.database.updateTexto(item[0][0],item[1].winfo_children()[2].get())

        self.destroy()
        

class scrollTODOS(customtkinter.CTkScrollableFrame):

    def __init__(self, master, itemsTodo,database,**kwargs):
        super().__init__(master, **kwargs)
        self.items = itemsTodo
        self.checkboxs = []
        self.database = database


        for item in self.items:
            self.addItem(item)



    
    def addItem(self,item):


        frame = customtkinter.CTkFrame(self,height=50,width=350,corner_radius=10,fg_color="#1ea2ac")
        frame.grid(row = len(self.checkboxs),column = 0)
        frame.grid_propagate(False) # para que evite que se ajuste automaticamente

        bottonDelete = customtkinter.CTkButton(frame,text="Del",command= lambda :self.removeCheckedItem(frame,item[0]),width=20, height=20,font=("Verdana",15),corner_radius=10,border_width=0,fg_color="#2b7088")
        bottonDelete.grid(row = len(self.checkboxs),column = 2 )

        checkbox = customtkinter.CTkCheckBox(frame,text="",font=("Verdana",20,"bold"), width=10,border_color="#FFFFFF")
        checkbox.grid(row = len(self.checkboxs),column = 0)

        
        textEntry = customtkinter.CTkEntry(frame,fg_color="#1ea2ac",width=270, height=20,font=(" Verdana",20,"bold"),corner_radius=10,border_width=0,text_color="#ffffff")

        textEntry.insert(0,item[1])
        textEntry.grid(row = len(self.checkboxs),column = 1)
        

        self.checkboxs.append(frame)


    def removeCheckedItem(self,item,id):

        if item in  self.checkboxs:       
            item.destroy()
            self.checkboxs.remove(item)
            self.database.delete(id)
            return
      


def mainApp():

    app = App()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()



if __name__ == "__main__":

    mainApp()

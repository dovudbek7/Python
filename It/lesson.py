# from tkinter import *

# window = Tk() # yangi tkinter oyna obyelti
# window.title("Converter") # oyna sarlavhsai
# window.geometry('400x250') # oyna hajmi

# def convert_value():
#   value = entry.get()
#   lbl =Label(bg='#FAFAFA',text=f"{value} ", font=("Poppins SemBold", 16))
#   lbl.grid(column=0, row=1)
  
# entry = Entry(bg='#FAFAFA', font=("Poppins SemBold", 16))
# btn = Button(text="Convert", bg="#232323", foreground="#FAFAFA", font=("Poppins SemBold", 10), command=convert_value)

# entry.grid(column=0, row=0)
# btn.grid(column=1, row=0)

# window.mainloop()
import response
import requests
def get_movie_poster(query:str):
    url = 'rapid url'
    
    query = {'q':query}
    response = response
    
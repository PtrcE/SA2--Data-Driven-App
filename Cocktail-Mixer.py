from tkinter import *
import requests 
import re

def searchDrink():
    userEntry = entry.get()
    response = requests.get(f'http://www.thecocktaildb.com/api/json/v1/1/search.php?s={userEntry}')
    data = response.json()
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    #in this order the infomations will be displayed
    if data['drinks']:
        cocktails = data['drinks'][0]
        name = cocktails['strDrink']
        glass = cocktails['strGlass']
        alcohol = cocktails['strAlcoholic']
        instructions = cocktails['strInstructions']

        Label(frame2, text = f"Name: {name}").pack()
        Label(frame2, text = f"Type of Glass: {glass}").pack()
        #this is to let user aware if the drink is alcoholic or not
        if alcohol == "Alcoholic":
            alcoholic = "Yes"
            Label(frame2, text = f"Alcoholic: {alcoholic}").pack()
        else:
            alcoholic = "No"
            Label(frame2, text = f"Alcoholic: {alcoholic}").pack()
        
        
        Label(frame2, text = f"Instructions: {instructions}", wraplength=250).pack()
    else:
        Label(frame2, text = f"No cocktail found for '{userEntry}'").pack()

#creates the tkinter window
root = Tk()
root.title("Cocktail Search")
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg = '#89CFF0')

frame1 = Frame(root, bg = '#89CFF0')
frame1.place(relx=0.5, rely=0.1, anchor=CENTER)

#message bar on top of textbox
title = Label(frame1, text = "Search up your Favorite Cocktails!")
title.grid(row = 0, columnspan=2)

# creates and packs the entry widget
entry = Entry(frame1, width=30)
entry.grid(row = 1, column = 0, padx=(0,5))

#button to trigger search 
search_button = Button(frame1, text="Mix!", command=searchDrink)
search_button.grid(row = 1, column = 1, padx=(5,0))

frame2 = Frame(root, bg='#89CFF0')

# this is to run tkinter on loop 
root.mainloop()
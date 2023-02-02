from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letterslist = [choice(letters) for char in range(randint(8, 10))]
    symbolslist = [choice(symbols) for char in range(randint(2, 4))]
    numberslist = [choice(numbers) for char in range(randint(2, 4))]

    password_list = [x for x in letterslist + symbolslist + numberslist]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

def find_password():
    website = str(website_input.get())
    try:
        with open("data.json","r") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found")
    else:
        if website.lower() in data.keys():
            messagebox.showinfo(title=website,
                                message=f"Email: {data[website]['email']}\npassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for the {website} exists")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = str(website_input.get())
    email = str(email_input.get())
    password = str(password_input.get())
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)                              # opening the file and loading the data to potentially update it

        except FileNotFoundError:                                       # catching the filenotfounderror and opening a new file and dumping in new data
            with open("data.json","w") as datafile:
                json.dump(new_data,datafile,indent=4)

        else:
            data.update(new_data)                                       # updating the old data if it exists and then dumping the updated data into the new file
            with open("data.json","w") as datafile:
                json.dump(data,datafile,indent=4)

        finally:
            website_input.delete(0, END)                                # regardless of all, the user input is deleted on the ui side
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image= logo)
canvas.grid(row=0,column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# input boxes
website_input = Entry(width=35)
website_input.grid(row=1,column=1, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2, sticky="EW")
email_input.insert(0,"mufeez08@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3,column=1, sticky="EW")

#buttons

Search_button = Button(text="Search",command=find_password)
Search_button.grid(row=1,column=2, sticky="EW")

generate_pwd_button = Button(text="Generate Password",command=generate_password)
generate_pwd_button.grid(row=3,column=2, sticky="EW")

add_button = Button(text="Add",width=29,command=save)
add_button.grid(row=4,column=1,columnspan=2, sticky="EW")

window.mainloop()
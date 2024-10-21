from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = input_website.get().lower()
    email_text = input_email.get()
    password_text = input_password.get()
    file_path= "pass.txt"
    new_data = {
        website_text:{
            "email": email_text,
            "password": password_text
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=f"{website_text}", message=f"Email: {email_text} \nPassword: {password_text} \nDo you want to save?")
        # if is_ok:
        #     with open(file_path, "a") as file:
        #         file.write(f"{website_text} | {email_text} | {password_text}" + '\n')
        try:
            with open ("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    try:
        with open ("data.json", "r") as data_file:
            websites_dict = json.load(data_file)
            website_for_search = input_website.get().lower()

            get_mail = websites_dict[website_for_search]["email"]
            get_pass = websites_dict[website_for_search]["password"]
    except FileNotFoundError:
        messagebox.showinfo("No data", "You have no website saved yet")

    except KeyError:
        messagebox.showinfo("No data", "You have no website saved with this name")

    else:
        pyperclip.copy(get_pass)
        messagebox.showinfo(f"{website_for_search}", message=f"Email: {get_mail} \nPassword: {get_pass}")

    finally:
            input_website.delete(0, END)
            input_website.focus()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

input_website = Entry(width=32)
input_website.focus()
input_website.grid(column=1, row=1)

input_email = Entry(width=50)
input_email.insert(0, "amr.elsherbiny@mail.com")
input_email.grid(row=2, column=1, columnspan=2)

input_password = Entry(width=32)
input_password.grid(column=1, row=3)

pass_generator_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
pass_generator_button.grid(column=2, row=3)

search_button = Button(text="Search", highlightthickness=0, width=14, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=43, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
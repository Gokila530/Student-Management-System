from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Gokila' and passwordEntry.get() == '2025':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')



window = Tk()
window.geometry('1280x854')
window.resizable(False, False)


background_img = Image.open('background.jpg')
backgroundImage = ImageTk.PhotoImage(background_img)

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)


loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)


logo_img = Image.open('login.jpeg')
logoImage = ImageTk.PhotoImage(logo_img)
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)


username_img = Image.open('user.jpeg')
usernameImage = ImageTk.PhotoImage(username_img)
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'),
                      bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)


password_img = Image.open('password.jpeg')
passwordImage = ImageTk.PhotoImage(password_img)
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'),
                      bd=5, fg='royalblue', show='*')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)


loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15,
                     fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                     activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)


window.mainloop()
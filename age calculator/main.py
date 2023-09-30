# Import necessary modules
from tkinter import *
from datetime import date

# Create a Tkinter window
root = Tk()
root.geometry("800x600")  # Set window dimensions
root.resizable(False, False)  # Disable window resizing
root.title("Age Calculator")  # Set window title

# Load an image
photo = PhotoImage(file="image.png")
myImage = Label(image=photo)
myImage.pack(padx=15, pady=15)

# Function to calculate age


def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(
        monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))

    # Display the age
    Label(text=f"{nameValue.get()} your age is {age}",
          font=30).place(x=300, y=500)


# Create labels and input fields for name, year, month, and day
Label(text="Name", font=23).place(x=200, y=250)
Label(text="Year", font=23).place(x=200, y=300)
Label(text="Month", font=23).place(x=200, y=350)
Label(text="Day", font=23).place(x=200, y=400)

# StringVar variables to store input values
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# Create input Entry widgets
nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
dayEntry.place(x=300, y=400)

# Create a button to trigger age calculation
Button(text="Calculate Age", font=20, bg='black', fg='white',
       width=11, height=2, command=calculateAge).place(x=300, y=450)

# Start the Tkinter main loop
root.mainloop()

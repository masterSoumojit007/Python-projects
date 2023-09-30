from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox


def translate():
    # Get text without trailing newline
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        # Show an error message if no text is entered
        messagebox.showerror('Language Translator',
                             'Enter the text to translate!')
    else:
        # Clear the output text box
        text_entry2.delete(1.0, 'end')
        # Translate the input text
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        # Display the translation in the output text box
        text_entry2.insert('end', output.text)


def clear():
    # Clear both input and output text boxes
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')


# Create the main Tkinter window
root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')
root.resizable(False,False)

# Create a frame for organizing widgets
frame1 = Frame(root, width=590, height=370,
               relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0, y=0)

# Add a title label
Label(root, text='Language Translator', font=(
    "Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

# Create a variable to hold the selected auto-select value
a = tk.StringVar()

# Create a dropdown for auto-select
auto_select = ttk.Combobox(
    frame1, width=27, textvariable=a, state='readonly', font=('verdana', 10, 'bold'))

auto_select['values'] = ('Auto Select',)
auto_select.place(x=15, y=60)
auto_select.current(0)

# Create a variable to hold the selected language
l = tk.StringVar()

# Create a dropdown for choosing the language to translate to
choose_language = ttk.Combobox(
    frame1, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
# Add your list of languages here
choose_language['values'] = (
    'Afrikaans',
    'Albanian',
    'Amharic',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Chinese (Simplified)',
    'Chinese (Traditional)',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hebrew',
    'Hindi',
    'Hungarian',
    'Icelandic',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Korean',
    'Kurdish',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malay',
    'Malayalam',
    'Maltese',
    'Marathi',
    'Nepali',
    'Norwegian',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Serbian',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Swahili',
    'Swedish',
    'Tamil',
    'Telugu',
    'Thai',
    'Turkish',
    'Ukrainian',
    'Urdu',
    'Vietnamese',
    'Welsh',
    'Yoruba',
    'Zulu',
    'Esperanto',
    'Hausa',
    'Sesotho',
    'Sundanese',
    'Tajik',
    'Uzbek',
    'Kannada',
    'Kyrgyz',
    'Lao',
    'Malagasy',
    'Samoan',
    'Shona',
    'Sindhi',
    'Uighur',
    'Xhosa',
    'Yiddish'
)

choose_language.place(x=305, y=60)
choose_language.current(0)

# Create input and output text boxes
text_entry1 = Text(frame1, width=20, height=7, borderwidth=5,
                   relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5,
                   relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

# Create buttons for translation and clearing
btn1 = Button(frame1, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(frame1, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor="hand2")
btn2.place(x=300, y=300)

# Start the Tkinter main loop
root.mainloop()

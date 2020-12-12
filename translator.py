'''
Translator uses google translate API/Library to translate the text within a file and 
tkinter to create widgets within which the language to which the text is to be converted is selected and 
also to create the destination file name where the output text will be printed by the program.
'''


from googletrans import Translator, LANGUAGES, LANGCODES
from tkinter import Scrollbar, Label, Listbox, Tk, TOP, LEFT, RIGHT, mainloop, Y, END, BOTH, Button, ANCHOR, Frame, VERTICAL, CENTER, StringVar, Entry, Toplevel


# The first part of the code is to create a window within which the destination language will be selected by the user.

top = Tk()
top.title('Destination Language')

'''
The frame is created to contain the listbox and scrollbar widget so that they can be packed together without disturbing the outside elements.
This is especially useful since pack geometry manager and grid geometry manager cannot be used together.
Another reason to use the frame widget is for the positioning of its children widgets and the other widgets, outside of the frame, 
but within the window as determined by the programmer.
The difference between pack and grid geometry manager is that the pack manager sets the position of widgets automatically
and resizing the window does not affect the position of widgets while the grid manager gives manual control of the position of 
widgets to the programmer and resizing affects the position of widgets in a grid.
'''

myframe = Frame(top)
myframe.grid(row = 1, columnspan = 2)

myscrollbar = Scrollbar(myframe, orient = VERTICAL)
myscrollbar.pack(side = RIGHT, fill = Y)

label = Label(top, text = 'Select Language:', justify = CENTER)
label.grid(row = 0, columnspan = 2)

mylist = Listbox(myframe, width = 29, yscrollcommand = myscrollbar.set)

# Thw loop is to insert all the languages contained by google translate to the listbox so that it can be selected by the user.

for lang_code in LANGUAGES:
    mylist.insert(END, f'{lang_code}   {LANGUAGES[lang_code]}')
    '''
    With LANGUAGES[lang_code], the values associated with keys, which in this case is lang_code, is inserted to the side.
    Although putting the values makes the code somewhat difficult to write and understand, this makes the user understand what languages 
    are available for the user to convert the text to.
    ''' 

mylist.pack(side = LEFT, fill = BOTH)
myscrollbar.config(command = mylist.yview)

def ok():
    '''
    The ANCHOR option is used within the get method to store the option selected by user when 'OK' button is pressed, 
    and the variable "dest_lang" is used to store the value of the option selected.
    '''
    global dest_lang
    dest_lang = mylist.get(ANCHOR)
    top.quit()

def cancel():
    top.quit()

b = Button(top, text = 'OK', command = ok)
b.grid(row = 2, column = 0)

c = Button(top, text = 'CANCEL', command = cancel)
c.grid(row = 2, column = 1)

top.mainloop()

# The second part of the code is to get the file name of the text file, to which the output will be printed, from the user himself.

root = Toplevel()
root.title('Destination file name')

fn = StringVar()

mylabel2 = Label(root, text = 'Enter file name for the converted language file:')
mylabel2.grid(row = 0, columnspan = 2)

entry1 = Entry(root, textvariable = fn)
entry1.grid(row = 0, column = 2)

def submit():
    '''
    The StringVar function lets the user input a string within the function itself which, in turn, is stored within fn variable.
    The filename variable stores the user-input string which is obtained through the get method.
    This variable is then used as a formatted string in the translator part of the code to create a file of the name 'filename'.
    '''
    global filename
    filename = fn.get()
    root.quit()

button1 = Button(root, text = 'Submit', command = submit)
button1.grid(row = 1, column = 0)

button2 = Button(root, text = 'Cancel', command = cancel)
button2.grid(row = 1, column = 1)

root.mainloop()

'''
The ordering of lines of code and the function is important so as to get a error-free and fully functioning program.
The two parts of code are written by taking two different windows otherwise there is going to be a clash
between the two windows as they will be running sil=multaneously and the one written first will get executed properly while the other would not.
Also even if the two different windows were created but were run by the help of same mainloop, only the one written first will get executed.
So for two different windows, two different loops are needed.
'''

translator = Translator()
try:
    with open('text.txt', mode = 'r') as myfile:
        text = myfile.read()
        translated_text = translator.translate(text, dest = dest_lang[0:2])
        with open(f'{filename}.txt', mode = 'w', encoding = 'utf-8') as my_file:
            my_file.write(translated_text.text)
        # String slicing has been done upom the string variable dest_lang to separate lang_code and language and get the lang_code only.

except FileNotFoundError as err:
    print('check your file path first')

'''
Google translate has a class "Translated" by translation of the text is processed, 
so by default an object of the class Translated is created which is then assigned to a variable, in this case translated_text.
To get the the actual text and print it to another file, we have to get the 'text' attribute of Translated class.
'''
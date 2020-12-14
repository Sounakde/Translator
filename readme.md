#  Translator

## Project Description

The translator project translates one language to another user desired language using File I/O. The input method has been created as dialog boxes, one for selecting the language to be converted to and the other, to name and create the file in which the converted file will be stored. The translator project also contains an executable file with which the program can be run without going into the program itself.

## Technologies Used

* Python
* HTML
* TeX

## Setting Up

### Interpreter

The python interpreter which is the base of the program is given as a link for download from official python website.

* [Python](https://www.python.org/)

Choose the one you want to download based on your OS and version(for Windows only).

## Dependencies

* GoogleTrans
* Tkinter
* Pyinstaller

## Installation

Install the dependencies with the pip command like this

    pip install googletrans
    pip install tkinter
    pip install pyinstaller

Keep in mind that googletrans may require installation of v3.1.0a0 since the current version v3.0.0 is gving problems. Check the google documentation and StackOverflow to check which version to download.

## Running the program/executing the exe file

The program can be run with the command

    python translator.py

The executable file can also be run by clicking on it but make sure that the text file from which the program is going to read is in the same folder as the executable file.

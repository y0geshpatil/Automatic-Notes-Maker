# Automatic-Notes-Maker
Automatic tool for make your notes faster!

Run the main.py file from your terminal and just copy the lines from the PDF,Web and any file you are reading, It will automatically paste those lines in your notes.

It requires pyperclip to access the clipboard

Install it by : pip install pyperclip

You may get an error message that says: “Pyperclip could not find a copy/paste mechanism for your system. Please see https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error for how to fix this.”

In order to work equally well on Windows, Mac, and Linux, Pyperclip uses various mechanisms to do this. Currently, this error should only appear on Linux (not Windows or Mac). You can fix this by installing one of the copy/paste mechanisms:

sudo apt-get install xsel to install the xsel utility.
sudo apt-get install xclip to install the xclip utility.
pip install gtk to install the gtk Python module.
pip install PyQt4 to install the PyQt4 Python module.

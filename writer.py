import pyperclip

def notes(name_of_file):

    if len(pyperclip.paste()) > 0:

        r = open(name_of_file + ".txt", 'a')

        r.write('*' * 200 + "\n\n")

        r.write(pyperclip.paste() + "\n\n")
        pyperclip.copy("")
        r.close()

    return True

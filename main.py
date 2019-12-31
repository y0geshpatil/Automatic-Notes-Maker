import pyperclip
from writer import notes


def main():
    print("Enter name of the file :")
    name_of_file = "mynotes" #you can use any name for store your notes
    f = open(name_of_file + ".txt", 'w')
    f.close()

    pyperclip.copy("")
    print("Press CTRL+C to stop",end=" ")
    flag=True
    try:
        while flag:
            flag = makenotes(name_of_file)
            continue

    except KeyboardInterrupt:
        print("Thanks for Using\nDeveloped by Patil Yogesh")



main()

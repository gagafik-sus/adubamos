import os

print("""
                file help:
                c - create
                ch - check
                e - edit
                l - list
                q - exit

""")

while True:
    fc = input('file-v0.2 -$ ')

    if fc == "q":
        break

    elif fc == "c":
        cf = input('create file: ')
        os.system(f"touch {cf}")
        print(cf, " - успешно создан. сасалити")

    elif fc == "ch":
        ch = input('look at the file: ')
        os.system(f"cat {ch}")

    elif fc == "e":
        ef = input('file: ')
        editor = input('vim or nano (deflault - nano)? ')
        if editor == "vim":
	        os.system(f"vim {ef}")
        else:
	        os.system(f"nano {ef}")

    elif fc == "l":
        us = input('use sudo (y - yes)? ')
        dirr = input('dir (deflault - enter) ')
        if us == "y":
	        os.system(f"sudo ls {dirr}")
        else:
	        os.system(f"ls {dirr}")

    else:
        print('error: command not found')

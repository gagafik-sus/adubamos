import os

if not args:
    cmd = "help"
else:
    cmd = args[0]
    subargs = args[1:]

if cmd == "help":
    print("""
file commands:
c <file>            - create file
ch <file>           - show file (cat)
e <file> [editor]   - edit file (nano/vim)
l [dir]             - list directory

examples:
file c test.txt
file ch test.txt
file e test.txt nano
file l
file l /home
    """)

elif cmd == "c":
    if not subargs:
        print("usage: file c <filename>")
    else:
        filename = subargs[0]
        try:
            open(filename, "a").close()
            print(filename, "- created")
        except Exception as e:
            print("error:", e)

elif cmd == "ch":
    if not subargs:
        print("usage: file ch <filename>")
    else:
        os.system(f"cat {' '.join(subargs)}")

elif cmd == "e":
    if not subargs:
        print("usage: file e <filename> [nano|vim]")
    else:
        filename = subargs[0]
        editor = subargs[1] if len(subargs) > 1 else "nano"

        if editor not in ["nano", "vim"]:
            print("unknown editor, using nano")
            editor = "nano"

        os.system(f"{editor} {filename}")

elif cmd == "l":
    directory = subargs[0] if subargs else ""
    os.system(f"ls {directory}")

else:
    print("unknown command:", cmd)

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
    print("""
    ### ⚠️ File Edit is no longer supported

**Sorry, but the built-in file editor is no longer working.**

Please install our new text editor using APM:

```
apm
ate
```

### ✨ Recommended replacement

**ate** — a lightweight and fast text editor for AdubamOS

* Simple interface
* Keyboard-driven workflow
* Works well even on small displays

### 🚀 Usage

```
ate ./file.txt
```

---

Thank you for using **AdubamOS** 💙

    """)

        os.system(f"{editor} {filename}")

elif cmd == "l":
    directory = subargs[0] if subargs else ""
    os.system(f"ls {directory}")

else:
    print("unknown command:", cmd)

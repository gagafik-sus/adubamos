import os

if not args:
    cmd = "help"
else:
    cmd = args[0]
    subargs = args[1:]

if cmd == "help":
    print("""
        system.py 0.3

commands system:
help        - help
shell       - run system command

usage:
system shell <command>
    """)

elif cmd == "shell":
    if not subargs:
        print("usage: system shell <command>")
    else:
        command = " ".join(subargs)

        if "rm -rf /" in command:
            print("💀 nice try")
        else:
            print("running:", command)
            os.system(command)


else:
    print("unknown command:", cmd)

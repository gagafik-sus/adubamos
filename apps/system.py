import os

print()
print('system v0.2')
print('type "help"')
print()
while True:
    print()
    sc = input('system-v0.2 -$ ')

    if sc == "exit":
        break

    elif sc == "help":
        print( """

commands system:
help - help
shell - system shell (bash, fish, zsh)
exit - exit

                  """)

    elif sc == "shell":
        print("enter your system command. например: sudo rm -rf /*")
        yshell = input("type your command (you can write bash to use):  ")
        print("your command - ", yshell)
        os.system(yshell)

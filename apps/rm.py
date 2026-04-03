import os
import shutil

def main():
    if not args:
        print("usage: rm [-r] <file/folder>")
        return

    recursive = False
    targets = []

    for arg in args:
        if arg == "-r":
            recursive = True
        else:
            targets.append(arg)

    if not targets:
        print("usage: rm [-r] <file/folder>")
        return

    for target in targets:
        if not os.path.exists(target):
            print("not found:", target)
            continue

        try:
            if os.path.isfile(target):
                os.remove(target)
                print("removed file:", target)

            elif os.path.isdir(target):
                if recursive:
                    shutil.rmtree(target)
                    print("removed dir:", target)
                else:
                    print(f"{target} is a directory (use -r)")

        except Exception as e:
            print("error:", e)

main()

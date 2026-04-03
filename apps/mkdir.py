import os

if not args:
    print("usage: mkdir <folder>")
else:
    for folder in args:
        try:
            os.makedirs(folder, exist_ok=True)
            print("created:", folder)
        except Exception as e:
            print("error:", e)

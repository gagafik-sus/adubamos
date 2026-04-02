print("загрузка библиотек")
import os
import time
import random
import sys
import requests
import zlib
import base64
import subprocess
from datetime import datetime
import zipfile
import shutil

print("загрузка shell")

def shell():
    while True:
        shellcommand = input('Adubam Shell v0.9 -$ ')

        if shellcommand == "q":
            print('command: exit (q)')
            break

        elif shellcommand == "clear":
            os.system('clear')

        elif shellcommand == "help":
            print("""
commands:
help  - помощь
calc  - калькулятор
q     - выход
clear - очистка
system - комманды системы
fetch - информация о системе
clock - часы
mkdir - create dir
delete - delete
file - file commands
apm - adubam package manager
            """)
            if os.path.isdir('./mods'):
                iaiai = "modified"
                print("mods:")
                os.system('ls mods')
            else:
                iaiai = "vanilla"
                print("vanilla")

        elif os.path.exists(f"apps/{shellcommand}.py"):
            with open(f"apps/{shellcommand}.py", "r", encoding="utf-8") as f:
                code = f.read()
                exec(code, globals())

        elif os.path.exists(f"mods/{shellcommand}.py"):
            exec(open(f"mods/{shellcommand}.py").read())

        elif shellcommand == "apm":
            download_mod()

        else:
            print(shellcommand, " - комманда не найдена type - help")


def download_mod():
    BASE_URL = "https://raw.githubusercontent.com/gagafik-sus/test/main/"
    TARGET_FOLDER = "./mods"
    while True:
        mod_name = input("apm -$ ").strip()

        if mod_name == "q":
            os.system("rm -rf ./temp_folder/")
            os.system("rm -rf ./temp.zip")
            os.system("rm -rf ./temp_all.zip")
            os.system("rm -rf ./temp_folder_all/")
            break

        elif mod_name == "all":
            print("preparation for installation...")
            zip_url = "https://github.com/gagafik-sus/test/archive/refs/heads/main.zip"
            temp_zip = "temp_all.zip"
            temp_folder = "temp_folder_all"

            if os.path.exists(TARGET_FOLDER):
                if os.path.isdir(TARGET_FOLDER):
                    shutil.rmtree(TARGET_FOLDER)
                else:
                    os.remove(TARGET_FOLDER)

            if os.path.exists(temp_folder):
                shutil.rmtree(temp_folder)

            os.makedirs(TARGET_FOLDER)

            print("downloading all...")
            try:
                r = requests.get(zip_url)
                with open(temp_zip, "wb") as f:
                    f.write(r.content)

                print("installing...")
                with zipfile.ZipFile(temp_zip, "r") as zip_ref:
                    zip_ref.extractall(temp_folder)

                source_folder = os.path.join(temp_folder, "test-main")
                if os.path.exists(source_folder):
                    for file in os.listdir(source_folder):
                        if file != "README.md":
                            os.replace(os.path.join(source_folder, file), os.path.join(TARGET_FOLDER, file))
                print("Done!")
            except Exception as e:
                print(f"Error: {e}")

            os.system("rm -rf ./temp_folder/")
            os.system("rm -rf ./temp.zip")
            os.system("rm -rf ./temp_all.zip")
            os.system("rm -rf ./temp_folder_all/")

        elif mod_name == "help":
            print("""
q - exit
help - help
all - download all

just type app name
""")
        else:
            url = f"https://raw.githubusercontent.com/gagafik-sus/test/main/{mod_name}.py"
            folder = "./mods"

            if not os.path.exists(folder):
                print('mods not found')
                os.makedirs(folder)
                print(f"{folder} done!")

            file_path = os.path.join(folder, f"{mod_name}.py")

            try:
                print(f"installing {mod_name}...")
                response = requests.get(url)

                if response.status_code == 200:
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                    print(f"done!")
                else:
                    print(f"mod not found (status: {response.status_code})")
                    print(mod_name, " - комманда не найдена type - help")

            except Exception as e:
                print(f"sorry but error {e}")

if __name__ == "__main__":
    print('done')
    time.sleep(0.1)
    text = "Hello!"
    current = ""
    for char in text:
        current += char
        os.system('clear')
        print(current)
        time.sleep(0.2)

        prev_time = time.time()

    for size in range(0, 33):
        now = time.time()
        delta = now - prev_time
        fps = 1 / delta if delta > 0 else 0
        prev_time = now

        os.system("clear")

        print(f"frame: {size}/32")
        print(f"fps: {fps:.2f}")
        print()

        for y in range(size):
            line = " " * (size - y - 1)
            for x in range(y + 1):
                if x & (y - x) == 0:
                    line += "∆ "
                else:
                    line += "  "
            print(line)

        time.sleep(0.05)

    os.system('clear')
    print("welcome to..")
    time.sleep(1)

    nameos = "AdubamOS"
    oscur = ""
    for ch in nameos:
        oscur += ch
        os.system('clear')
        print(oscur)
        time.sleep(0.1)

    time.sleep(0.5)
    os.system('clear')


    if os.path.isdir('./mods'):
        iaiai = "modified"
    else:
        iaiai = "vanilla"

    print('AdubamOS pre1 1.0', iaiai)
    time.sleep(0.1)
    print("""
    |========|
    |AdubamOS|
    |(0 )( 0)|
    |    --  |
    |========|
    """)
    time.sleep(0.12)
    os.system('clear')
    print('AdubamOS pre1 1.0', iaiai)
    print("""
    |========|
    |AdubamOS|
    |(o-)(-o)|
    |    --  |
    |========|
    """)
    time.sleep(0.12)
    os.system('clear')
    print('AdubamOS pre1 1.0', iaiai)
    print("""
    |========|
    |AdubamOS|
    |( 0)(0 )|
    |    --  |
    |========|
    tg channel - t.me/adubamos
    """)
    print("github version")



    shell()

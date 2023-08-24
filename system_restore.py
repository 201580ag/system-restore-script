import subprocess
import ctypes
import time

art = '''
+-----------------------------------------------+
|  ___   ___  __ _____  ___   ___               |
| |__ \ / _ \/_ | ____|/ _ \ / _ \              |
|    ) | | | || | |__ | (_) | | | | __ _  __ _  |
|   / /| | | || |___ \ > _ <| | | |/ _` |/ _` | |
|  / /_| |_| || |___) | (_) | |_| | (_| | (_| | |
| |____|\___/ |_|____/ \___/ \___/ \__,_|\__, | |
|                                         __/ | |
|                                        |___/  |
+-----------------------------------------------+
'''

print('\x1b[37;4mhttps://github.com/201580ag\x1b[0m')
print(art)
print('\x1b[0m')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        time.sleep(3)
        exit()

def main():
    if not is_admin():
        print("\033[91mThis program requires administrator privileges.\nPlease run it as an administrator.\033[0m")
        time.sleep(3)
        exit()

    print("\033[94mDo you want to perform a system restore? (y/n)\033[0m")
    choice = input().strip().lower()
    if choice == 'y':
        command1 = 'dism /online /cleanup-image /restorehealth'
        command2 = 'sfc /scannow'
        run_command(command1)
        run_command(command2)
        print("The operation has been completed.")
    elif choice == 'n':
        print("The operation has been canceled.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()

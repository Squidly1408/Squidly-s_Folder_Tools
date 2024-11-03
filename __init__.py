import os
import winreg
import sys

def add_context_menu(main_script_path):
    # Get the directory of the script for the icon path
    script_directory = os.path.dirname(main_script_path)
    icon_path = os.path.join(script_directory, 'icon.ico')

    # Ensure the icon file exists
    if not os.path.isfile(icon_path):
        print(f"Icon file not found: {icon_path}")
        return

    # Create registry entry for all file types
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell", 0, winreg.KEY_ALL_ACCESS)
        submenu_key = winreg.CreateKey(key, "Squidly's File Tools")

        # Set icon for file context menu
        winreg.SetValueEx(submenu_key, "Icon", 0, winreg.REG_SZ, icon_path)

        # Create command subkey for files
        command_key = winreg.CreateKey(submenu_key, "command")
        command = f'"{os.path.abspath(sys.exec_prefix)}\\pythonw.exe" "{main_script_path}" "%1"'  # Using pythonw.exe
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)

        # Clean up
        winreg.CloseKey(command_key)
        winreg.CloseKey(submenu_key)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Failed to add context menu for files: {e}")

    # Create registry entry for folders
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"Directory\shell", 0, winreg.KEY_ALL_ACCESS)
        submenu_key = winreg.CreateKey(key, "Squidly's Folder Tools")

        # Set icon for folder context menu
        winreg.SetValueEx(submenu_key, "Icon", 0, winreg.REG_SZ, icon_path)

        # Create command subkey for folders
        command_key = winreg.CreateKey(submenu_key, "command")
        command = f'"{os.path.abspath(sys.exec_prefix)}\\pythonw.exe" "{main_script_path}" "%V"'  # Using pythonw.exe
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)

        # Clean up
        winreg.CloseKey(command_key)
        winreg.CloseKey(submenu_key)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Failed to add context menu for directories: {e}")

    


if __name__ == '__main__':
    # Specify the path to your main.py file here
    main_script_path = os.path.abspath("C:\\Path\\To\\main.py")  # Adjust this as needed
    add_context_menu(main_script_path)

import os
import subprocess

def get_user_sid(username):
    comandos = []
    for name in username:
        comandos.append(f'wmic useraccount where name="{name}" get sid')
    
    saidas = []
    for comando in comandos:
        saidas.append(f"{(subprocess.check_output(comando, shell=True, text=True)).strip('SID').strip().strip()}")

    return saidas


def run_regedit():
    os.system("start regedit.exe")

def create_registry_key(path, key_name):
    import winreg as reg

    key = reg.CreateKey(reg.HKEY_USERS, path)
    reg.CreateKey(key, key_name)
    reg.CloseKey(key)

def create_registry_value(path, value_name, value_data):
    import winreg as reg

    key = reg.OpenKey(reg.HKEY_USERS, path, 0, reg.KEY_WRITE)
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value_data)
    reg.CloseKey(key)

def main():
    run_regedit()
    
    username = None
    while True:
        username = input('Digite o nome do usuário: ').split(',')

        if username:

            sids = get_user_sid(username)
        
            for sid in sids:
                create_registry_key(f"{sid}\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies", "ActiveDesktop")

                create_registry_value(f"{sid}\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\ActiveDesktop", "NoChangingWallPaper", 0)
                
            print("NoChangingWallPaper registry created (value=false)! \nPower by: Nicolas & Pedro Lucas")

            break
        else:
            continue

if __name__ == "__main__":
    main()
import os
import subprocess
import winreg as reg

senhas_usuarios = [] # Adicionar senhas de acordo com os usuários!

def create_bat_file():
    bat_content = """
    @echo off
    start cmd.exe
    exit
    """
    bat_path = "start_cmd.bat"

    with open(bat_path, "w") as bat_file:
        bat_file.write(bat_content)

    return bat_path

def start_user_session(username, password):
    psexec_path = f'\\PSTools\\psexec.exe'

    bat_path = create_bat_file()

    psexec_command = f'{psexec_path} -u "{username}" -p "{password}" -i {bat_path}'

    subprocess.run(psexec_command, shell=True)

    os.remove(bat_path)

def get_user_sid(usernames):
    comandos = []
    for index, username in enumerate(usernames):
        comandos.append(f'wmic useraccount where name="{username}" get sid')
        start_user_session(username, senhas_usuarios[index])

    saidas = []
    for comando in comandos:
        saidas.append(f"{(subprocess.check_output(comando, shell=True, text=True)).strip('SID').strip().strip()}")

    return saidas

def run_regedit():
    os.system("start regedit.exe")

def create_registry_key(path, key_name):
    key = reg.CreateKey(reg.HKEY_USERS, path)
    reg.CreateKey(key, key_name)
    reg.CloseKey(key)

def create_registry_value(path, value_name, value_data):
    key = reg.OpenKey(reg.HKEY_USERS, path, 0, reg.KEY_WRITE)
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value_data)
    reg.CloseKey(key)

def edit_registry_value(path, value):
    try:
        registry_key = reg.OpenKey(reg.HKEY_USERS, path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(registry_key, "WallPaper", 0, reg.REG_SZ, value)
        reg.CloseKey(registry_key)
    except:
        return ValueError("Erro ao editar registro de WallPaper")
    
def main():
    usernames = None
    while True:
        usernames = input('Digite o nome do usuário: ').split(',')

        if usernames:
            sids = get_user_sid(usernames)

            run_regedit()

            for sid in sids:
                create_registry_key(f"{sid}\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies", "ActiveDesktop")

                create_registry_value(f"{sid}\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\ActiveDesktop", "NoChangingWallPaper", 1)

                edit_registry_value(f"{sid}\\Control Panel\\Desktop", os.path.join(os.path.dirname(os.path.realpath(__file__)), f"wallpaper\\backmcpf.png"))

            print("NoChangingWallPaper registry created (value=true)! \nPower by: Nicolas & Pedro Lucas")

            break
        else:
            continue

if __name__ == "__main__":
    main()

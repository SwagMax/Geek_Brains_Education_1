with open('parsing.txt', 'w', encoding='utf-8') as parsing:
    with open('nginx_logs.txt', encoding='utf-8') as nginx_logs:
        content = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in nginx_logs)
        for _ in content:
            print(_, file=parsing)

from collections import Counter

with open('nginx_logs.txt', encoding='utf-8') as nginx_logs:
    logs_dict = Counter()
    for _ in nginx_logs:
        logs_dict[_.split()[0]] = logs_dict[_.split()[0]] + 1

    ip, count = logs_dict.most_common(1)[0][0], logs_dict.most_common(1)[0][1]
    print(f'Spammer {ip} - {count} times')
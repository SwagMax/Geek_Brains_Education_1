def url_parse(url):
    _t_protocol, _, domain, *resource_address = url.strip('/').split('/')
#    t_protocol = _t_protocol[:-1]

    return _t_protocol, _, domain, resource_address
print(url_parse('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'))
# ('https', 'www.dns-shop.ru', ['catalog', '17a89aab16404e77', 'videokarty'])

# ('h', 't', 't', ['p', 's', ':', '/', '/', 'w', 'w', 'w', '.', 'd', 'n', 's', '-', 's', 'h', 'o', 'p', '.', 'r', 'u', '/', 'c', 'a', 't', 'a', 'l', 'o', 'g', '/', '1', '7', 'a', '8', '9', 'a', 'a', 'b', '1', '6', '4', '0', '4', 'e', '7', '7', '/', 'v', 'i', 'd', 'e', 'o', 'k', 'a', 'r', 't', 'y'])

# ('https:', '', 'www.dns-shop.ru', ['catalog', '17a89aab16404e77', 'videokarty'])



#url = 'https://geekbrains.ru/teacher/lessons/7961'
#_t_protocol, _, domain, *resource_address = url.strip('/').split('/')
#t_protocol = _t_protocol[:-1]
#print(t_protocol, domain, resource_address)

#print(url_parse('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'))


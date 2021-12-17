import requests

name_user = str(input("Digite o seu name user do git: "))

r = requests.get(f'https://api.github.com/users/{name_user}/repos')
r = r.json()

print(r)
print(f'{"Nome repositorio":<25}|{"Link repositorio":<70}|')
for c in r:

    print('-'*97)
    print(f'{c["name"]:<25}|{c["html_url"]:<70} |')
import datetime

def make_logo(old_function):
  def new_function(*args, p = 'logo/logo.txt'):
    result = old_function(*args)
    with open (p, 'a') as file:      
      file.write(f'вызвана функция {old_function.__name__} с аргументом {args}, получен результат {result}  {datetime.datetime.today()}\n')
    return result
  return new_function

import requests

hero_list = ["Hulk", "Thanos", "Captain America"]
intel = {}
name_hero = {}
@make_logo
def request_(name):
  url = "https://superheroapi.com/api/2619421814940190/search/"
  response = requests.get(url+name, timeout = 5)
  hero = response.json()
  hero_int = hero['results'][0]['powerstats']['intelligence']
  intel[name] = hero_int
  name_hero[hero_int] = name
  return intel
for hero in hero_list:
  request_(hero)
max_int = max(intel.values(), key=lambda i: int(i))
smart_hero = name_hero[max_int]

print(smart_hero, max_int)
    
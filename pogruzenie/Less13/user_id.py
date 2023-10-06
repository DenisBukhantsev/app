from pathlib import Path
import os
import json
our_path = Path.cwd()
min_lvl = 1
max_lvl = 7

def create_json(path: str = "user.json"):
  user_data = {}
  id_list = []
  while True:
    if os.path.exists(path):
      with open(path, "r", encoding= "utf-8") as file:
        user_data = json.load(file)
    if user_data:
      for users in user_data.values():
        for user in users:
          id_list.append(user[1])    
    name = input("Введите имя ")
    if not name:
      break
    while True:
      u_id = int(input("введите личный id "))
      if u_id.isdigit():
        if int(u_id) not in id_list:
          u_id = int(u_id)
          break
        else:
          print(f"id {u_id} уже занят, выбери другой")
      else:
        print("id должен быть числом")
    while True:
      u_lvl = int(input("введите уровень доступа "))
      if u_lvl.isdigit() and min_lvl <= int(u_lvl) <= max_lvl:
        break
      else:
        print(f"Уровень доступа должен быть от {min_lvl} lj {max_lvl}")
    if u_lvl in user_data:
      user_data[u_lvl].append(name, u_id)
      
    else:
      user_data[u_lvl] = [name, u_id]
    
    with open(path, "w", encoding= "utf-8") as file:
      json.dump(user_data, file, indent=6, ensure_ascii=False)

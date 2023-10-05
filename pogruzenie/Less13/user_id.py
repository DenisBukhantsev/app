from pathlib import Path
import os
import json
our_path = Path.cwd()


def create_json(path: str = "user.json"):
  user_data = {}
  id_list = []
  while True:
    if os.path.exists(path):
      with open(path, "r", encoding= "utf-8") as file:
        user_data = json.load(file)
        
    
    if not name:
      break
    u_id = int(input("введите личный id "))
    u_lvl = int(input("введите уровень доступа "))
    
    if user_data:
      for users in user_data.values():
        for user in users:
          id_list.append(user[1])
    name = input("Введите имя ")
    if u_lvl in user_data:
      user_data[u_lvl].append(name, u_id)
    else:
      user_data[u_lvl] = [name, u_id]
      

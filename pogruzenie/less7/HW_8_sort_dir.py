# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#Для дочерних объектов указывайте родительскую директорию.
#Для каждого объекта укажите файл это или директория.
#Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех #функций пакет для работы с файлами разных форматов.
from pathlib import Path
import os
import csv
import pickle
import json
our_path = Path.cwd()
def sort_dir(arg):
  result = []
  for paths, dir, files in os.walk(arg):
    
    for name in files:
      res_path = arg /paths / name
      size = res_path.stat().st_size
      result.append({"directory": paths, "Type": "file", 
                     "Name": name, "size" : f"{size} bytes"})
    for i in dir:
      path_dir = arg /paths / i
      result.append({"directory": paths, "Type": "directory", 
                     "Name": i, "size" : f"{size} bytes"})
  with open("myhw_81.json", "w", encoding= "utf-8") as jsonfile:
    json.dump(result, jsonfile)
    
  with open("mypicklefile.pickle", "wb") as picklefile:
    pickle.dump(result, picklefile)
    
  with open("mycsv.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

  #print([print(i) for i in result])
 

print(sort_dir(our_path))

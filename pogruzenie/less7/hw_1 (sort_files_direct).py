#Задача с семинара: ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, 
#текст и т.п. ✔Каждая группа включает файлы с несколькими расширениями. ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
from pathlib import Path


our_path  = Path.cwd() # тут я сделал переменую что бы он определил директорию где лежит этот пайтон файл, и передать ее в нашу функцию 
def sort_FILES(path_dir): 
  direct_format = { #создал руками словарь где ключ общее название формата а значение список с форматами, по  ключам будем создавать папки 

    'video': ['mp4', 'mov', 'avi', 'mkv'],

    'audio': ['mp3', 'wav', 'ogg', 'flac'],

    'image': ['jpg', 'png', 'bmp'],

    'text': ['pdf', 'txt', 'doc'],
  }
  
  
    
  for file in path_dir.iterdir(): # функция итер дир дает путь ко всем файлам в директории с циклом перебираем все файлы 
    for suff in direct_format: # тут просто идем по словарю
       if file.suffix.lower()[1:] in direct_format[suff]:   # суффикс дает именно формат файла из счетчика файл с путем к файлу .pdf или .avi
         result = path_dir / suff   #тут мы создаем директорию в переменной 
         if result.exists() != True: # если такой директории нет то создаем создаем ее  если есть то пропускаем создание 
           result.mkdir()
         file.rename(result.joinpath(file.name)) # rename функция меняет директорию склеивая новую директориюс нашим файлом
    
      
print(sort_FILES(our_path))
from pathlib import Path
import os
import csv
import pickle
import json
import logging

logging.basicConfig(filename="py_log.log", level= logging.INFO,  filemode="w", encoding= "utf-8",  format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
#FORMAT = 

#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")

our_path = Path.cwd()
def sort_dir(arg):
    logger.info(f"{arg = }") 
    result = []
     #не нашел аналог этой функции в pathlib, подскажите может есть такое ?
    try:
        for paths, dir, files in os.walk(arg):
            for name in files:
                res_path = arg /paths / name   # вот тут очень удобно мне показалось из прошлой домашки  функция path работает подтянул ее сюда
                size = res_path.stat().st_size
                result.append({"directory": paths, "Type": "file", "Name": name, "size" : f"{size} bytes"})
            for i in dir:
                path_dir = arg /paths / i
                result.append({"directory": paths, "Type": "directory", "Name": i, "size" : f"{size} bytes"})
    
             
         
        logger.info(f"{result = }") 
    except Error as err:
        logging.error("error", exc_info=True)
  #with open("myhw_81.json", "w", encoding= "utf-8") as jsonfile:
    #json.dump(result, jsonfile)
    
  #with open("mypicklefile.pickle", "wb") as picklefile:
    #pickle.dump(result, picklefile)
    
  #with open("mycsv.csv", "w") as csvfile: # вот тут я я чего то голову сломал с этим файлом , да и вообще тема новая 
        #writer = csv.DictWriter(csvfile, fieldnames=result[0].keys())
        #writer.writeheader()
        #writer.writerows(result)


 

print(sort_dir(our_path))

# Создайте класс с базовым исключением и дочерние классыисключения:
# ошибка уровня,
# ошибка доступа.
class UserExeption(Exception):
  def __init__(self, msg: str):
    self.msg = msg
    
  def __str__(self):
    return self.msg
    
  
class LevelError(UserExeption):
   def __init__(self):
     super().__init__("Ошибка уровня  доступа")
  
class AccessError(UserExeption):
  def __init__(self):
     super().__init__("Ошибка доступа")
raise AccessError

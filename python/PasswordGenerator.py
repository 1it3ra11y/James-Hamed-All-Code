import random

length: int = int(input("How long do you want your password to be? "))
password: str = ""

chars: list = ["1", "2", "3", "4","5", "6", "7", "8", "9", "0", "@", "!", "?", "%", "A","a", "B", "b", "C", "c", "D", "d", "E","e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "k", "K", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

while len(password) != length:
  password += random.choice(chars) 
print(password)
  
  
  
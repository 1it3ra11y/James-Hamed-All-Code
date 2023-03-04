q: str = input("Do you want to encode or decode? ")
prod: str = ""
string2: str = ""

if q.lower() == "encode":
  string: str = input("What do you want to encode? ")
  for char in string:
    if char.lower() == "a": 
      prod += "._ "
    elif char.lower() == "b": 
      prod += "_... "
    elif char.lower() == "c": 
      prod += "_._. "
    elif char.lower() == "d": 
      prod += "_.. "
    elif char.lower() == "e": 
      prod += ". "
    elif char.lower() == "f": 
      prod += ".._. "
    elif char.lower() == "g": 
      prod += "__. "
    elif char.lower() == "h": 
      prod += ".... "
    elif char.lower() == "i": 
      prod += ".. "
    elif char.lower() == "j": 
      prod += ".___ "
    elif char.lower() == "k": 
      prod += "_._ "
    elif char.lower() == "l": 
      prod += "._.. "
    elif char.lower() == "m": 
      prod += "__ "
    elif char.lower() == "n": 
      prod += "_. "
    elif char.lower() == "o": 
      prod += "___ "
    elif char.lower() == "p": 
      prod += ".__. "
    elif char.lower() == "q": 
      prod += "__._ "
    elif char.lower() == "r": 
      prod += "._. "
    elif char.lower() == "s": 
      prod += "... "
    elif char.lower() == "t": 
      prod += "_ "
    elif char.lower() == "u": 
      prod += ".._ "
    elif char.lower() == "v": 
      prod += "..._ "
    elif char.lower() == "w": 
      prod += ".__ "
    elif char.lower() == "x": 
      prod += "_.._ "
    elif char.lower() == "y": 
      prod += "_.__ "
    elif char.lower() == "z": 
      prod += "__.. "
    elif char.lower() == " ": 
      prod += " / "
    elif char.lower() == "1": 
      prod += ".____ "
    elif char.lower() == "2": 
      prod += "..___ "
    elif char.lower() == "3": 
      prod += "...__ "
    elif char.lower() == "4": 
      prod += "...._ "
    elif char.lower() == "5": 
      prod += "..... "
    elif char.lower() == "6": 
      prod += "_.... "
    elif char.lower() == "7": 
      prod += "__... "
    elif char.lower() == "8": 
      prod += "___.. "
    elif char.lower() == "9": 
      prod += "____. "
    elif char.lower() == "0": 
      prod += "_____ "
    else:
      print("There is no sequence for that character")
elif q.lower() == "decode":
  string: str = input("What do you want decoded? ")  
  for char in string:
    string2 += char
    if " " in string2:
      if string2 == "._ ":
        prod += "a"
      elif string2 == "_... ":
        prod += "b"
      elif string2 == "_._. ":
        prod += "c"
      elif string2 == "_.. ":
        prod += "d"
      elif string2 == ". ":
        prod += "e"
      elif string2 == ".._. ":
        prod += "f"
      elif string2 == "_.. ":
        prod += "g"
      elif string2 == ".... ":
        prod += "h"
      elif string2 == ".. ":
        prod += "i"
      elif string2 == ".___ ":
        prod += "j"
      elif string2 == "_._ ":
        prod += "k"
      elif string2 == "._.. ":
        prod += "l"
      elif string2 == "__ ":
        prod += "m"
      elif string2 == "_. ":
        prod += "n"
      elif string2 == "___ ":
        prod += "o"
      elif string2 == ".__. ":
        prod += "p"
      elif string2 == "__._ ":
        prod += "q"
      elif string2 == "._. ":
        prod += "r"
      elif string2 == "... ":
        prod += "s"
      elif string2 == "_ ":
        prod += "t"
      elif string2 == ".__ ":
        prod += "u"
      elif string2 == "..._ ":
        prod += "v"
      elif string2 == ".__ ":
        prod += "w"
      elif string2 == "_.._ ":
        prod += "x"
      elif string2 == "_.__ ":
        prod += "y"
      elif string2 == "__.. ":
        prod += "z"
      elif string2 == ".____ ":
        prod += "1"
      elif string2 == "..___ ":
        prod += "2"
      elif string2 == "...__ ":
        prod += "3"
      elif string2 == "...._ ":
        prod += "4"
      elif string2 == "..... ":
        prod += "5"
      elif string2 == "_.... ":
        prod += "6"
      elif string2 == "__... ":
        prod += "7"
      elif string2 == "___.. ":
        prod += "8"
      elif string2 == "____. ":
        prod += "9"
      elif string2 == "_____ ":
        prod += "n"
      elif string2 == "/ ":
        prod += " "
      else:
        print("That is not a valid morse code seqeunce")
      string2 = ""
  else:
      if string2 == "._":
        prod += "a"
      elif string2 == "_...":
        prod += "b"
      elif string2 == "_._.":
        prod += "c"
      elif string2 == "_..":
        prod += "d"
      elif string2 == ".":
        prod += "e"
      elif string2 == ".._.":
        prod += "f"
      elif string2 == "_..":
        prod += "g"
      elif string2 == "....":
        prod += "h"
      elif string2 == "..":
        prod += "i"
      elif string2 == ".___":
        prod += "j"
      elif string2 == "_._":
        prod += "k"
      elif string2 == "._..":
        prod += "l"
      elif string2 == "__":
        prod += "m"
      elif string2 == "_.":
        prod += "n"
      elif string2 == "___":
        prod += "o"
      elif string2 == ".__.":
        prod += "p"
      elif string2 == "__._":
        prod += "q"
      elif string2 == "._.":
        prod += "r"
      elif string2 == "...":
        prod += "s"
      elif string2 == "_":
        prod += "t"
      elif string2 == ".__":
        prod += "u"
      elif string2 == "..._":
        prod += "v"
      elif string2 == ".__":
        prod += "w"
      elif string2 == "_.._":
        prod += "x"
      elif string2 == "_.__":
        prod += "y"
      elif string2 == "__..":
        prod += "z"
      elif string2 == ".____":
        prod += "1"
      elif string2 == "..___":
        prod += "2"
      elif string2 == "...__":
        prod += "3"
      elif string2 == "...._":
        prod += "4"
      elif string2 == ".....":
        prod += "5"
      elif string2 == "_....":
        prod += "6"
      elif string2 == "__...":
        prod += "7"
      elif string2 == "___..":
        prod += "8"
      elif string2 == "____.":
        prod += "9"
      elif string2 == "_____":
        prod += "0"
      elif string2 == "/":
        prod += " "
      else:
        print("That is not a valid morse code seqeunce")
      string2 = ""
else:
  print("I don't understand")
print(prod)
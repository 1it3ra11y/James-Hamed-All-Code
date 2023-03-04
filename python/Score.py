score = 0
while True:  
    print("Score:", score)
    q = input("add, subtract, or end: ").lower().strip() 
    words = q.split()  
    verb = words.pop(0) 

    if verb == "end":
        break

    if words and words[0].isnumeric():  
      
        value = int(words[0])
    else:  
        value = 1

    if verb == "add":
        score += value
    elif verb == "subtract" or verb == "sub":
        score -= value
    else:
        print("Unknown verb:", verb)

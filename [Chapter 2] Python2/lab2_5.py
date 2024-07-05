def bon(w):
    num = 0
    for letter in w:
	    if w.count(letter) > 1:
		    return (ord(letter)-96)*4

secretCode = input("Enter secret code : ")
print(bon(secretCode))

words = ["selenium","java","python"] 

alphabet = "abcdefghijklmnopqrstuvwxyz"

for word in words:
    total_weight = 0 
    
    for char in word:
        for i in range(26):  
            if char == alphabet[i]:
                total_weight += (i + 1) 
                break  

    print("The weightage of the word ",word,"is: ",total_weight)

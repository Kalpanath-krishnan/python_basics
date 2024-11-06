alphabet="abcdefghijklmnopqrstuvwxyz"
tools=["selenium","java","python"]
weightage=0
for tool in tools:
    for characters in alphabet:
        for i in range(26):
         if characters in tool:
          index=i
          weightage+=index
print(weightage)
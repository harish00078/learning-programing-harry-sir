mydict ={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"iteam",
    
}
print("operations are",mydict.keys())
a = input("enter the hindi word\n")
#print("the meaning of your word is:",mydict[a])
print("the meaning of your word is:",mydict.get(a))
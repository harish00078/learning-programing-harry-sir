# this = "         harry is a good         "
# print(this)
# print(this.strip()) # strip function is used to remove the gap between value that we gave in our string.



def remove_and_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()
    
    
this = "     harry is a good      "
n = remove_and_split(this,"harry")
print(n)
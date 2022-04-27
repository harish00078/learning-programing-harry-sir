from typing import Dict


myDict = {
    "fast":"in a quick manner",
    "harry":"coder",
    "marks":[1,2,5],
    "anotherdict": {'harry':'player'},
    1:2,
}

print(type(myDict.keys()))  #prirt the key of the dictionary
print(myDict.values()) #prirt the values of the dictionary
print(myDict.items()) #prirt the (key,value) for all the contents of the dictonary

print(myDict)
updateDict= {
    "lovish":"friend",
    "harish":"friend",
    "munish":"friend",
    "harry":"a dancer"

}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updatedict

print(myDict)

print(myDict.get("harry"))# print value associated with key"harry"
print(myDict["harry"])# print value associated with key"harry"

# diffrence betweeen .get and [] syntex in dictonary;

print(myDict.get("harry2"))# returns none as harry2 is present in the dictonary
print(myDict["harry2"])# throws an error as harry2 is not persent in the dictonary

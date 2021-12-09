# Author CCG 12/9/21

def alphabet(word1,word2,word3):
    string1 = word1.lower()
    string2 = word2.lower()
    string3 = word3.lower()

    if string1 < string2 < string3:
        return("Alphabetical order is " + word1 + " , " + word2 + " , " + word3)
    elif string1 < string3 < string2:
        return("Alphabetical order is " + word1 + " , " + word3 + " , " + word2)
    elif string2 < string3 < string1:
        return("Alphabetical order is " + word2 + " , " + word3 + " , " + word1)
    elif string2 < string1 < string3:
        return("Alphabetical order is " + word2 + " , " + word1 + " , " + word3)
    elif string3 < string1 < string2:
        return("Alphabetical order is " + word3 + " , " + word1 + " , " + word2)
    elif string3 < string2 < string1:
         return("Alphabetical order is " + word3 + " , " + word2 + " , " + word1)

print(alphabet("Apple","banana","organ") == "Alphabetical order is Apple , banana , organ")
print(alphabet("apal","Order","bale") == "Alphabetical order is apal , bale , Order")
print(alphabet("the","a","z") == "Alphabetical order is a , the , z")

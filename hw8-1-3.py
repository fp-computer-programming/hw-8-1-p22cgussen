# Author CCG 12/9/21

def anagram_check(w1,w2):
    list1 = list(w1)
    list2 = list(w2)

    sort1 = list1.copy()
    sort2 = list2.copy()
    sort1.sort()
    sort2.sort()

    if sort1 == sort2:
        return("The words " + w1 + ' and ' + w2 + " are anagrams.")
    else:
        return("The words " + w1 + ' and ' + w2 + " are not anagrams.")

word1 = input("Input a word: ")
word2 = input("Input another word: ")

print(anagram_check(word1,word2))

print(anagram_check("race","acer") == "The words " + "race" + ' and ' + "acer" + " are anagrams.")
print(anagram_check("word","worde") == "The words " + "word" + ' and ' + "worde" + " are not anagrams.")
print(anagram_check("yet","yet") == "The words " + "yet" + ' and ' + "yet" + " are anagrams.")

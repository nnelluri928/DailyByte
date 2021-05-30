'''
This question is asked by Amazon. Given two strings representing sentences, 
return the words that are not common to both strings 
(i.e. the words that only appear in one of the sentences). 
You may assume that each sentence is a sequence of words (without punctuation) 
correctly separated using space characters.
'''
def main(s1,s2):
        frequency = {}
        for word in s1.split():
            frequency[word] = frequency.get(word,0) + 1
        for word in s2.split():
            frequency[word] = frequency.get(word,0) + 1
        res = []

        for key,val in frequency.items():
            if val < 2: res.append(key)
        return res

if __name__ == "__main__":
    sentence1 = "the quick"; sentence2 = "brown fox"
    print(main(sentence1,sentence2))
    sentence1 = "the tortoise beat the haire"; sentence2 = "the tortoise lost to the haire"
    print(main(sentence1,sentence2))
    sentence1 = "copper coffee pot"; sentence2 = "hot coffee pot"
    print(main(sentence1,sentence2))



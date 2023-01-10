# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program counts the vowels in given sentence

def count_vowels(sentence):
    """This function counts the vowels"""
    count = 0
    sentence = sentence.lower()
    for v in sentence:
        if v in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


if __name__ == '__main__':
    userInput = str(input("Enter the string to check for vowels: "))
    count = count_vowels(userInput)
    print('Vowel Count: ', count)

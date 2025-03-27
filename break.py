print("Break Keyword")
for i in range(1,11):
    if i==5:
        break
    print(i)

word=input("enter a word: ")
for ch in word:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print("Vowel Found: ", ch)
        break
    else:
        print("Vowel not Found",ch)
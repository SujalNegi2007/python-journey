# Word Analyser
print("Welcome To The Word Analyser")
print("Enter Your Sentence:")
Sentence = input().strip()

Words            = Sentence.split()
Count_Words      = len(Words)
Capitalise       = " ".join(w.capitalize() for w in Words)
Count_alphabets  = len(Sentence.replace(" ", ""))
Upper            = Sentence.upper()
Reversed_Words   = " ".join(reversed(Words))


print(f"Original Sentence      : {Sentence}")
print(f"No. of Words           : {Count_Words}")
print(f"No. of alphabets       : {Count_alphabets}")
print(f"Sentence as uppercase  : {Upper}")
print(f"Sentence as capitalised: {Capitalise}")
print(f"Reversed Words         : {Reversed_Words}")

print(f"Search For a Word: ")
search_word = input()
if search_word in Words:
    print(f" '{search_word}' is in your sentence!")
else:
    print(f"'{search_word}' is not in your sentence!")

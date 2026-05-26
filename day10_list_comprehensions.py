#create a list of their squares
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_nums = [num**2 for num in nums]
print(squared_nums)

#Extract only the even numbers from nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

#Extract only words longer than 3 characters from words
words = ["hello", "world", "python", "ai", "ml", "data"]
extracted_words = [word for word in words if len(word) > 3]
print(extracted_words)

#Convert all temps to Fahrenheit from temps_celsius
temps_celsius = [0, 20, 37, 100, -10, 25]
temps_fahrenheit = [(temps*9)/5 + 32 for temps in temps_celsius]
print(temps_fahrenheit)

#Extract only the passing scores (≥ 60) from scores
scores = [45, 82, 91, 33, 76, 58, 89, 22]
extracted_scores = [score for score in scores if score >= 60]
print(extracted_scores)

#create a list of names in uppercase but only for names that start with a vowel
names = ["alice", "bob", "charlie", "dave"]
checked_names = [name.upper() for name in names if name[0] in "aeiou"]
print(checked_names)

#Replace negatives with 0, keep positives as-is from nums
nums = [1, -3, 5, -7, 9, -11, 2, -4]
checked_nums = [num if num > 0  else 0 for num in nums]
print(checked_nums)

#Flatten matrix = [[1,2,3],[4,5,6],[7,8,9]] into a single list.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
checked_matrix = [num for nums in matrix for num in nums ]
print(checked_matrix)

#Extract unique words longer than 3 characters from sentence
sentence = "the quick brown fox jumps over the lazy dog"
extracted_sentences = {sen for sen in sentence.split(" ") if len(sen) > 3}
print(extracted_sentences)

#Extract just the names of people who scored above 70 from data
data = [{"name": "Alice", "score": 91}, {"name": "Bob", "score": 45}, {"name": "Charlie", "score": 78}]
extracted_data = [name["name"] for name in data  if name["score"] > 70]
print(extracted_data)

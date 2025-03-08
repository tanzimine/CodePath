# Problem 1
# def are_equivalent(word1, word2):
#     list1 = ''.join(word1)
#     list2 = ''.join(word2)

#     if(list1 == list2):
#         return True
#     else:
#         return False


# word1 = ["bat", "man"]
# word2 = ["b", "atman"]
# print(are_equivalent(word1, word2))

# word1 = ["alfred", "pennyworth"]
# word2 = ["alfredpenny", "word"]
# print(are_equivalent(word1, word2))

# word1  = ["cat", "wom", "an"]
# word2 = ["catwoman"]
# print(are_equivalent(word1, word2))


# problem 2
# def count_evens(lst):
#     count = 0
#     for element in lst:
#         if(len(element)%2 == 0):
#             count+=1
        
#     return count
    

# lst = ["na", "nana", "nanana", "batman", "!"]
# print(count_evens(lst))

# lst = ["the", "joker", "robin"]
# print(count_evens(lst))

# lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
# print(count_evens(lst))

# Problem 3

# def remove_name(people, secret_identity):
#     for element in people:
#         if secret_identity in people:
#             people.remove(secret_identity)

#     return people

# people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
# secret_identity = 'Bruce Wayne'
# print(remove_name(people, secret_identity))

# problem 5
# def move_zeroes(lst):
#     zeroLst = []
#     nonZerolst = []
#     for element in lst:
#         if element == 0:
#             zeroLst.append(element)
#         else:
#             nonZerolst.append(element)

#     finalList = nonZerolst + zeroLst
#     return finalList

# lst = [1, 0, 2, 0, 3, 0]
# print(move_zeroes(lst))



# # problem 6
# def reverse_vowels(s):
#     for index, letter in enumerate(s):

# THISSSSS 7!!!!!!!!!!!
# problem 7
# def highest_altitude(gain):
#     current_altitude = 0
#     highest_altitude = 0
    
#     for g in gain:
#         current_altitude += g
#         if current_altitude > highest_altitude:
#             highest_altitude = current_altitude
    
#     return highest_altitude





# # problem 10
# def expose_superman(trust, n):
#     if n == 1:
#         return 1 
#     colElement = set()
#     for row in trust:
#         for col in row[1:]:
#             colElement.add(col)
#     target = [n]
#     mainElement = list(colElement)

#     if mainElement == target:
#         return n
#     else:
#         return -1
    

# n = 2
# trust = [[1, 2]]
# print(expose_superman(trust, n))

# n = 3
# trust = [[1, 3], [2, 3]]
# print(expose_superman(trust, n))

# n = 3
# trust = [[1, 3], [2, 3], [3, 1]]
# print(expose_superman(trust, n))
n, k, q = map(int, input().split())

recipes = list()
questions = list()

for i in range(n):
    li, ri = map(int, input().split())
    recipes.append((li, ri))
    
for j in range(q):
    a, b = map(int, input().split())
    questions.append((a,b))

MAX_TEMP = 200000
difference_array = [0] * (MAX_TEMP + 2)
admissable = [0] * (MAX_TEMP + 2)

for li, ri in recipes:
    difference_array[li] += 1
    difference_array[ri+1] -= 1
running_sum = 0

for i in range(len(difference_array)):
    running_sum += difference_array[i]
    difference_array[i] = running_sum
    
for i in range(len(difference_array)):
    if difference_array[i] >= k:
        admissable[i] = 1

pref = [0] * (MAX_TEMP + 2)
for i in range(1, MAX_TEMP+2):
    pref[i] = pref[i-1] + admissable[i]

for a, b in questions:
    print(pref[b] - pref[a-1])

    

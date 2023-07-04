dict = {}
string = ""
for _ in range(50):
    try:
        line = input().split()
        for word in line:
            string += word
    except:
        break
    
string = list(string)
for alphabet in string:
    if alphabet not in dict:
        dict[alphabet] = 1
    else:
        dict[alphabet] += 1

max = 0
for key in dict:
    if max < dict[key]:
        max = dict[key]

answer = ""

for key in dict:
    if dict[key] == max:
        answer += key


answer = ''.join(sorted(answer))
print(answer)
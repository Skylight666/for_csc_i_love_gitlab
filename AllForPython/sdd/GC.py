import re

pattern = r"\>Rosalind\_(\d{4})"
text = []
d = {}

with open('rosalind_gc.txt', 'r') as f:
    for l in f:
        text.append(l)
#print(text)
i = 0
while (i < len(text) and re.match(pattern, text[i])):
    ind = re.match(pattern, text[i]).group(0)
    i += 1
    row = ''
    while ( i < len(text) and text[i][0] != '>'):
        row += text[i].strip()
        i += 1
    perc = ( row.count('C') + row.count('G'))/len(row) * 100
    d[ind] = perc
    
max_value = 0
max_key = 0
for i, k in d.items():
    if k > max_value:
        max_value = k
        max_key = i

print(max_key)
print(max_value)

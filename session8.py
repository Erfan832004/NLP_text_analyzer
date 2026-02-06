from collections import Counter
text ="she ate melon and lemon and banana for month ago."
for ch in ".,!?":
    text=text.replace(ch,"")
words = text.split()
stop_words= "از","a","در","that","و","or","آن","این","را"
filtered_words = [w for w in words if w not in stop_words]
counter = Counter(filtered_words)
print(filtered_words)
print(len(filtered_words))
print(counter)
print(counter.most_common(1))
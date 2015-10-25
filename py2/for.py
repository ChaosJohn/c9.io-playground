words = ['cat', 'window', 'defenestrate']

for w in words:
    print w, len(w)

# If you need to modify the sequence you are iterating over while inside the
# loop (for example to duplicate selected items), it is recommended that you
# first make a copy.
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print words

text="Angela! Your course gave me hope and confidence! Thank you for your work! This is my code".lower()

morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', \
         'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', \
         'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', \
         'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••', '.': '••••••', '!': '--••--'}

print(' '.join([morze[letter] if letter != ' ' else "\n" for letter in text]))


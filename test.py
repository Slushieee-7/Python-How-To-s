alph = "abcdefghijklmnopqrstuvwxyz"

alph[3:15]
alph[3:15:3]
alph[3:15:-3]
alph[15:3:-3]
alph[15:3]
alph[::-3]

print(alph[3:15])  # 'defghijklmno'
print(alph[3:15:3])  # 'dfhjln'
print(alph[3:15:-3])        # ''
print(alph[15:3:-3])  # 'onmlkjihgfd'
print(alph[15:3])  # ''
print(alph[::-3])  # 'zyxwvutsrqponmlkjihgfedcba'


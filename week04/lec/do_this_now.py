VOWEL_STR = 'AIEOU'
name = input('Enter fullname: ').upper().strip()
while len(name) == 0:
    name = input('Enter fullname: ').upper().strip()
num_of_vowels = 0
for i in range(len(name)):
    if name[i] in VOWEL_STR:
        num_of_vowels += 1
print(f"Out of {len(name)} characters, {name} has {num_of_vowels} vowels.")

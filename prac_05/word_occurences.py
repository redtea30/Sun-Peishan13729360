"""
CP1404/CP5632 Practical
word_occurences.py
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for x, y in CODE_TO_NAME.items():
    print("{0:3} is {1}".format(x, y))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
input_count = {}
input_text = input("Type something! \n> ")
words = input_text.split()

for word in words:
    count = input_count.get(word, 0)
    input_count[word] = count + 1

words = list(input_count.keys())
words.sort()
greatest_len = max((len(word) for word in words))

for word in words:
    print("{0:{1}} : {2}".format(word,greatest_len, input_count[word]))

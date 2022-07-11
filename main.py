import random

min = 2
max = 6
start = 0

text = "Two roads lie in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth; Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same, And both that morning equally lay In leaves no step had trodden black. Oh, I kept the first for another day! Yet knowing how way leads on to way, I doubted if I should ever come back. I shall be telling this with a sigh Somewhere ages and ages hence: Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference."

new_text = ""

c = 0
words = 0
placeholder = 0
list_of_words = []
number_of_words = random.randint(min, max)

while c < len(text):
    if text[c] == " ":
        words += 1
    if words == number_of_words:
        list_of_words.append(text[placeholder:c + 1])
        placeholder = c
        words = 0
        number_of_words = random.randint(min, max)
    c += 1

random.shuffle(list_of_words)

for i in range(len(list_of_words)):
    new_text = new_text + list_of_words[i]
    if i % 5 == 0:
        new_text = new_text + "\n"

print(new_text)


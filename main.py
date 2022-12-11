# # TODO: Create a letter using starting_letter.txt
# # for each name in invited_names.txt
# # Replace the [name] placeholder with the actual name.
# # Save the letters in the folder "ReadyToSend".

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    new_letter = letter.replace("[name]", name.strip())
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/Letter_to_{name.strip()}.txt", mode="w") as w:
        w.write(new_letter)


# # Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

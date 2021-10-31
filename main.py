#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as letter:
        old_letter = letter.read()


with open("./Input/Names/invited_names.txt") as invite_name:
        # The readlines() method returns a list containing each line in the file as a list item.
        for name in invite_name.readlines():
                ready_made_name = name.strip("\n")
                new_letter = old_letter.replace('[name]', ready_made_name)
                with open(f"./Output/ReadyToSend/letter_for_{ready_made_name}.txt", mode='w') as new_file:
                        new_file.write(new_letter)


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



#Get name from name list text document
def get_name(name_pos): 
    with open("/Users/eleanorextence/Desktop/100 Days Files/Projects/Mail Merge Project Start/Input/Names/invited_names.txt", mode= "r") as name_list:
        name = name_list.readlines()[name_pos] 
    return name
                
#Create new letter based off of the example
def create_letter(names):
    
    #Creates a new .txt file, copies the template letter, and writes the contents of the template letter to new .txt file
    with open(f"/Users/eleanorextence/Desktop/100 Days Files/Projects/Mail Merge Project Start/Output/ReadyToSend/{names}.txt", mode= "w") as new_letter:
        with open("/Users/eleanorextence/Desktop/100 Days Files/Projects/Mail Merge Project Start/Input/Letters/starting_letter.txt") as template:
            new_letter.write(template.read())

#Change name placeholder with current name in letter
def replace_name(replace_text, file_name):
    with open(f"/Users/eleanorextence/Desktop/100 Days Files/Projects/Mail Merge Project Start/Output/ReadyToSend/{file_name}.txt", "r+") as file:
        search_text = "[name]"
        
        data = file.read()
        data = data.replace(search_text, replace_text)
        
        file.seek(0)
        file.truncate()
        file.write(data)

        

#Iterate through name list to create letters
with open("/Users/eleanorextence/Desktop/100 Days Files/Projects/Mail Merge Project Start/Input/Names/invited_names.txt", mode= "r") as name_list:
    for name in range(0, len(name_list.readlines()) ):
        
        x = get_name(name)
        create_letter(x)
        replace_name(x, x)

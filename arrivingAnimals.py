"""
Python File Name: arrivingAnimals.py

Date: 09/23/2023

Programmer's Name: Donald Cao
"""
'''
Text File Handling: Your first task is to create a Python program that reads and writes to a text file. You should use the file named arrivingAnimals.txt, which is provided in the repository.

Modifying get_species Function: Modify the get_species function to handle input errors gracefully. Currently, the function assumes that there are at least five words in the input string. You should update it to provide a meaningful response when the input string has fewer than five words.

Testing and Documentation: Test your Python program thoroughly with various inputs, including edge cases, to ensure it behaves as expected. Document any changes you make to the get_species function and how it handles input errors.
'''


textFile = open("arrivingAnimals.txt", "r") # text file located in same folder.

def get_species():
    for item in textFile:
        """
        Reads text file using the for loop to produce string literal.
        Then removed '\n' with replace method.
        Finally used split method to create a list of words separated by commas.
        """
        listedItem=textFile.readline().replace('\n',"").split(',')
        #print(listedItem)

        """
        Used substring[0] to separate string by comma with split method. Then use index to find species.
        Location was vague in the instruction, thus using indexed at -1 and 2.
        Used the print command to produced a list of species with their location.
        """
        species = listedItem[0].split()[4]
        locationCity = listedItem[-2] 
        locationCountry =listedItem[-1]

        print(f'Species: {species} Location: {locationCity} City: {locationCountry}')

#Initiate an Error Handling section within get_species() funcion.
#This section determine if the source txt file is found, then written in a separate file.
try:
    with open('arrivingAnimals.txt', 'r') as input_file:
        '''
        To use for loop to split strings into substring at the comma and convert into list type.
        '''
        for item in textFile:
            listedItem=textFile.readline().replace('\n',"").split(',')
        '''
        To input each substrings into a destinated txt file. Writing over is acceptable.
        '''
        with open('arrivingAnimalsReport2.txt', "w") as output_file:
            for line in listedItem:
                # Split each line on the comma
                substrings = line.strip().split(',')
                output_file.write("\n".join(substrings))
                output_file.write("\n\n")
    #Indicate if file is inserted with text from run.
    print("\n\nData processed and written to 'arrivingAnimalsReport.txt'!")


except FileNotFoundError:
    # This is probably the most common file i/o error.
    print(f"Error: The file 'arrivingAnimals2.txt' was not found.")

except IOError as e:
    # Handle file I/O errors
    if "No space left on device" in str(e):
        # Disk full error
        print("Exception caught! Disk full. Cannot write to the file.")
    elif "Permission denied" in str(e):
        # File locked error
        print("Error: File is locked. Cannot write to the file.")
    else:
        # Other I/O errors (file is corrupted - this happens sometimes on thumb drives )
        print(f"An error occurred: {str(e)}")

except PermissionError:
    # Handle the PermissionError exception here
    print("Error: Permission denied. You don't have the necessary permissions to modify this file.")

except Exception as e:
    # Handle other exceptions you did not imagine.
    print(f"An error occurred: {str(e)}")

finally:
    # Code in this block will execute regardless of whether an exception occurred or not.
    print(f"\n\n End of try/catch block! Good job!")



get_species()
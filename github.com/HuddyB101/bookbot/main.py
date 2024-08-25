import os

def main():
    file_path = os.path.expanduser("~/bookbot/github.com/HuddyB101/bookbot/books/frankenstein.txt")
    
    with open(file_path) as f:
        #open() opens in 'r' mode(expects to read the file)
        file_contents = f.read()
        
        # print(file_contents)
        print("--- Beginning report of ---")
        print(f"{file_path}")

        word_count(file_contents)
        character_count(file_contents)

        print("--- End of Report ---")
        

def word_count(input):
    count = len(input.split())
    print(f"{count} words in file.")

def character_count(input):
    characters = {}
    lowered_string = input.lower()

    for char in lowered_string:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    characters_list = list(characters.items())
    characters_list.sort(reverse=True,  key=lambda item: item[1])
    for char1 in characters_list:
        print(f"The letter {char1[0]} appears {char1[1]} times.")


main()
print("*********welcome to hangman*********")

name = input("Name :")

print("welcome " + name + " lets play ")


secret_word = "Metallica"

guess_String = ""

lives = 10

while lives > 0:
    
    character_left = 0
    
    for character in secret_word:
        if character in guess_String:
            print(character)
            pass
        else:
            print("-")
            character_left += 1
            pass
        
        pass
    
    if character_left == 0:
        print("you won !!")
        pass
    
        
        
        
    guess = input("Guess a letter : ")
    guess_String += guess 
    
    if guess not in secret_word:
        
        lives -= 1
        
        print("wrong guess :/")
        print(f"you have {lives} left \n")
        
        if lives == 0:
            print("you died :(")
            pass
        pass
    
    
        
        
    
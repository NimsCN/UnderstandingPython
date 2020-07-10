import sys

a = "Welcome to the game"
b = a.center(75)
c = "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")

deployment1_passed = False
combat_passed = False
deployment2_passed = False

player1_hand = ["Rathalos", "Ruby", "Emerald"]
player1_creature_zone = ["Rathian"]
player1_resource_zone = ["Ruby", "Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]
player1_used_resources = ["Ruby"]
player1_unused_resources = ["Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]

player2_hand = ["Frozen Bite", "Hurl Snow-Boulder", "Barioth"]
player2_creature_zone = ["Barioth"]
player2_resource_zone = ["Sapphire", "Sapphire", "Sapphire", "Sapphire", "Sapphire"]
player2_used_resources = ["Sapphire", "Sapphire", "Sapphire"]
player2_unused_resources = ["Sapphire", "Sapphire"]

def inner_options(phase_number):
    if phase_number == 1:
        print("Here is/are the card/cards in your hand")
        print(player1_hand)
        
        print("1: Play a creature")
        print("2: Play a resource")
        print("3: Play a spell")
        print("4: Proceed to Next Phase")
        print("5: Show Hand")
        
        inner_phase_choice = int(input("Pick the phase you would like to go to "))

        while inner_phase_choice != 4:
            if inner_phase_choice == 1:
                print("Select a creature from your hand that you would like to play")
            elif inner_phase_choice == 2:
                print("Select a resource from your hand that you would like to play")
            elif inner_phase_choice == 3:
                print("Select a spell from your hand that you would like to play")
            elif inner_phase_choice == 4:
                deployment1_passed = True
                phase_number = 2
            elif inner_phase_choice == 5:
                print("Here is/are the card/cards in your hand")
                print(player1_hand)
            else:
                print("That is not a valid choice. Please select one of the following:")
                print("1: Play a creature")
                print("2: Play a resource")
                print("3: Play a spell")
                print("4: Proceed to Next Phase")
                print("5: Show Hand")
                inner_phase_choice = int(input("Select one of the above actions to take"))



def loop_player():
    print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
    phase_choice = input("Pick the phase you would like to go to ")
    
    deployment1_passed = False
    combat_passed = False
    deployment2_passed = False

    test = 0

    while test == 0:
        if phase_choice.isalpha() == True:
            print("You must select a number in order to pick a phase")
            phase_choice = input("Pick the phase you would like to go to ")
        elif phase_choice.isdigit() == True:
            phase_choice = int(phase_choice)
            test = 1
        else:
            print("You have selected nothing, Please make a choice:")
            print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            phase_choice = input("Please select one of the above options: ")


    while phase_choice > 6 or phase_choice < 1:
        print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
        phase_choice = int(input("Pick the phase you would like to go to "))

    while phase_choice <= 6 and phase_choice >= 1:
        if phase_choice == 1 and deployment1_passed == False:
            print("You are now in Deployment 1")
            """Deployment stuff"""
            deployment1_passed = True
        elif phase_choice == 2 and combat_passed == False:
            print("You are now in the combat step")
            """Combat Stuff"""
            combat_passed = True
            deployment1_passed = True
        elif phase_choice == 3 and deployment2_passed == False:
            """Deployment 2 Stuff"""
            print("You are now in Deployment 2")
            deployment2_passed = True
            deployment1_passed = True
            combat_passed = True
        elif phase_choice == 4:
            """End Turn"""
            print("You have ended your turn")
            deployment2_passed = False
            deployment1_passed = False
            combat_passed = False
            break
        elif phase_choice == 5:
            print("Here is the board")
            print("Your creatures: " + str(player1_creature_zone))
            print("Your total resources are: " + str(player1_resource_zone))
            print("Unused resources: " + str(player1_unused_resources))
            print("Your used resources are: " + str(player1_used_resources))
        
            print("\n\nHere is you opponents board")
            print("Your opponent has " + str(len(player2_hand)) + " cards in hand")
            print("Your opponents creatures: " + str(player2_creature_zone))
            print("Your opponents total resources are: " + str(player2_resource_zone))
            print("Your opponents unused resources: " + str(player2_unused_resources))
            print("Your opponents used resources are: " + str(player2_used_resources))

        elif phase_choice == 6:
            print("Here is/are the card/cards in your hand")
            print(player1_hand)
        else:
            if deployment1_passed == False and combat_passed == False and deployment2_passed == False:
               print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == False and deployment2_passed == False:
               print("Invalid Selection, please select one of the following options \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == True and deployment2_passed == False:
                print("Invalid Selection, please select one of the following options \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == True and deployment2_passed == True:
                print("Invalid Selection, you must select \n4 End Turn")
            else:
                print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
        
        phase_choice= int(input("Pick the phase you would like to go to "))

        if phase_choice > 6 or phase_choice < 1:
            while phase_choice > 6 or phase_choice < 1:
                print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
                phase_choice = int(input("Pick the phase you would like to go to "))

#menu display bugs when board options are selected

loop_player()

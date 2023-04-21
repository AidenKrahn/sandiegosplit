
#---------------------
#Carmen Sandiego
#Aiden Krahn
#Started February 28th
#made in 3 days
#----------------------
import random
from sandiego import blsp
from sandiego import geo
from sandiego import hit
#lists of countries-
#DO NOT LOOK AT CODE BEFORE PLAYING
#IT WILL SPOIL S THAT YOU GET THROUGHOUT THE GAME


#definitions

def event(location, witwics):
    if location[1] == witwics[1]:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was Carmen Sandiego!")
        print("Now that you caught her, you can go home and eat cake*.")
        print("*cake not provided")
        play = False
        #whether or not you catch Carmen Sandiego
    elif location[1] != witwics[1]:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was an impostor! (sus)")
        print("You caught the impostor, and now they agreed to give you a hint to Carmen's whereabouts...")
        hit.hint(witwics, witwics)
        print("Keep searching!")
    #if I wanted to be accurate, I could've added more here
def country_choose():
    roll = random.randint(0, 12)
    vcountry = blsp.listofcountries[roll]#v. stands for varsol
    if vcountry == "bolivia":
        witwics = blsp.bolivia
    
    elif vcountry == "chile":
        witwics = blsp.chile
        
    elif vcountry == "peru":
        witwics = blsp.peru
        
    elif vcountry == "brazil":
        witwics = blsp.brazil
        
    elif vcountry == "argentina":
        witwics = blsp.argentina
        
    elif vcountry == "uruguay":
        witwics = blsp.uruguay
        
    elif vcountry == "paraguay":
        witwics = blsp.paraguay
        
    elif vcountry == "venezuela":
        witwics = blsp.venezuela
        
    elif vcountry == "colombia":
        witwics = blsp.colombia
        
    elif vcountry == "ecuador":
        witwics = blsp.ecuador
        
    elif vcountry == "guyana":
        witwics = blsp.guyana
        
    elif vcountry == "frenchguiana":
        witwics = blsp.frenchguiana
        
    elif vcountry == "suriname":
        witwics = blsp.suriname
        
    if witwics == location:
        country_choose()
        
    return witwics

    
def fly1(coward):
    location = coward
    return location

        
#main code---
coolerdaniel = random.randint(0, 12)
location = blsp.listofcountriespart2[coolerdaniel]
#determine starting location


#clues are split up into types:
#how much information they give(lots, not much, and cannonball)
#what kind of information they give(so I don't have to write 5000 sentences, just 100.
#flag hints, location based, political specifics, population
def main(location):
    print("Carmen Sandiego is somewhere in South America!")
    print("It is your job as a detective to find clues about Carmen Sandiego's whereabouts.")
    print("She could be hiding in", blsp.listofcountries)
    print("We have a few clues as to where Carmen Sandiego is hiding.")
    print(f"You are currently in {blsp.listofcountries[coolerdaniel]}")
    print("You have 7 days to find her.")
    print("If you find her, there will be cake.")
    #witwics = blsp.fakecountry
    witwics = country_choose()
    #chooses where Carmen is
    play = True
    days = 7
    geo.geographygarble(location)
    hit.hint(witwics, witwics)
    while play == True:
        if location == witwics:
            break
        
        geo.geographygarble(location)#calculate distances between your current location and other countries
        action = input("Where do you think she is?  ")
        
        if days >= 0:
            #flying to different countries
            if action == "bolivia":
                print("You flew to Bolivia")
                location = fly1(blsp.bolivia)
                days = days - blsp.bolivia[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'argentina':
                print("You flew to Argentina")
                location = fly1(blsp.argentina)
                days = days - blsp.argentina[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'ecuador':
                print("You flew to Ecuador")
                location = fly1(blsp.ecuador)
                days = days - blsp.ecuador[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'brazil':
                print("You flew to Brazil")
                location = fly1(blsp.brazil)
                days = days - blsp.brazil[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'suriname':
                print("You flew to Suriname")
                location = fly1(blsp.suriname)
                days = days - blsp.suriname[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'frenchguiana':
                print("You flew to French Guiana")
                location = fly1(blsp.frenchguiana)
                days = days - blsp.frenchguiana[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'guyana':
                print("You flew to Guyana")
                location = fly1(blsp.guyana)
                days = days - blsp.guyana[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'chile':
                print("You flew to Chile")
                location = fly1(blsp.chile)
                days = days - blsp.chile[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'peru':
                print("You flew to Peru")
                location = fly1(blsp.peru)
                days = days - blsp.peru[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'paraguay':
                print("You flew to Paraguay")
                location = fly1(blsp.paraguay)
                days = days - blsp.paraguay[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'uruguay':
                print("You flew to Uruguay")
                location = fly1(blsp.uruguay)
                days = days - blsp.uruguay[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'venezuela':
                print("You flew to Venezuela")
                location = fly1(blsp.venezuela)
                days = days - blsp.venezuela[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
            elif action == 'colombia':
                print("You flew to Colombia")
                location = fly1(blsp.colombia)
                days = days - blsp.colombia[0]
                geo.geographygarble(location)
                print(f"Days Left =", days)
                event(location, witwics)
                
        elif days <= 0:#lose condition
            print("You ran out of time.")
            print("You failed, Carmen got away, and you're bad at geography.")
            print("You got fired, your wife left you.")
            print("You're homeless. A dog peed on you.")
            print("Better luck next time!")
            play = False


main(location)


#---------------------
#Carmen Sandiego
#Aiden Krahn
#Started February 28th
#made in 3 days
#----------------------
import random
import blsp
#lists of countries-
#DO NOT LOOK AT CODE BEFORE PLAYING
#IT WILL SPOIL HINTS THAT YOU GET THROUGHOUT THE GAME


#definitions
def hint(country):
    que = random.randint(1, 6)
    if que == 1:
        print("This countries flag contains--",country[2])
        #more hints will be added in the future: corresponding list elements will also be added
    elif que == 2:
        print("This country is near--", country[3])
        
    elif que == 3:
        print("This country exports--", country[4])
        
    elif que == 4:
        print("This country has this many people--", country[5])
        
    elif que == 5:
        antihint(witwics)
        
    elif que == 6:
        print("The countries landmark is--", country[6])
        
    else:
        antihint()

    
def antihint(witwics):
    crazy = random.randint(1, 13)
    if crazy == witwics[1]:
        antihint()
    
    elif crazy == 1:
        print("Carmen Sandiego is not in Bolivia")
        
    elif crazy == 2:
        print("Carmen Sandiego is not in Chile")
        
    elif crazy == 3:
        print("Carmen Sandiego is not in Peru")
        
    elif crazy == 4:
        print("Carmen Sandiego is not in Brazil")
        
    elif crazy == 5:
        print("Carmen Sandiego is not in Argentina")
        
    elif crazy == 6:
        print("Carmen Sandiego is not in Uruguay")
        
    elif crazy == 7:
        print("Carmen Sandiego is not in Paraguay")
        
    elif crazy == 8:
        print("Carmen Sandiego is not in Venezuela")
        
    elif crazy == 9:
        print("Carmen Sandiego is not in Colombia")
        
    elif crazy == 10:
        print("Carmen Sandiego is not in Ecuador")
        
    elif crazy == 11:
        print("Carmen Sandiego is not in Guyana")
        
    elif crazy == 12:
        print("Carmen Sandiego is not in French Guiana")
        
    elif crazy == 13:
        print("Carmen Sandiego is not in Suriname")
    
    
def event():
    global location
    global witwics
    if location == witwics:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was Carmen Sandiego!")
        print("Now that you caught her, you can go home and eat cake*.")
        print("*cake not provided")
        play = False
        #whether or not you catch Carmen Sandiego
    elif location != witwics:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was an impostor! (sus)")
        print("You caught the impostor, and now they agreed to give you a hint to Carmen's whereabouts...")
        hint(witwics)
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

    
def fly(coward, days):
    location = coward
    days += coward[0]
    return location
    
def geographygarble(lratio):#determines how long it takes 
    if lratio[1] == 1:#you to fly based on where you are and where you go
        blsp.brazil[0] = 1
        blsp.paraguay[0] = 1
        blsp.argentina[0] = 1
        blsp.chile[0] = 1
        blsp.peru[0] = 1
        blsp.ecuador[0] = 2
        blsp.colombia[0] = 3
        blsp.venezuela[0] = 2
        blsp.guyana[0] = 3
        blsp.suriname[0] = 2
        blsp.frenchguiana[0] = 2
        blsp.uruguay[0] = 2
        blsp.bolivia[0] = 0
        
    elif lratio[1] == 2:
        blsp.argentina[0] = 1
        blsp.bolivia[0] = 1
        blsp.peru[0] = 1
        blsp.ecuador[0] = 2
        blsp.colombia[0] = 3
        blsp.venezuela[0] = 3
        blsp.guyana[0] = 3
        blsp.suriname[0] = 3
        blsp.frenchguiana[0] = 3
        blsp.paraguay[0] = 2
        blsp.brazil[0] = 3
        blsp.uruguay[0] = 2
        blsp.chile[0] = 0
        
    elif lratio[1] == 3:
        blsp.ecuador[0] = 1
        blsp.colombia[0] = 1
        blsp.venezuela[0] = 2
        blsp.guyana[0] = 2
        blsp.suriname[0] = 3
        blsp.frenchguiana[0] = 3
        blsp.brazil[0] = 1
        blsp.bolivia[0] = 1
        blsp.chile[0] = 1
        blsp.argentina[0] = 2
        blsp.uruguay[0] = 3
        blsp.paraguay[0] = 2
        blsp.peru[0] = 0
        
    elif lratio[1] == 4:
        blsp.frenchguiana[0] = 1
        blsp.guyana[0] = 1
        blsp.suriname[0] = 1
        blsp.venezuela[0] = 1
        blsp.colombia[0] = 1
        blsp.ecuador[0] = 2
        blsp.peru[0] = 1
        blsp.bolivia[0] = 1
        blsp.paraguay[0] = 1
        blsp.uruguay[0] = 1
        blsp.argentina[0] = 1
        blsp.chile[0] = 2
        blsp.brazil[0] = 0
        
    elif lratio[1] == 5:
        blsp.chile[0] = 1
        blsp.bolivia[0] = 1
        blsp.paraguay[0] = 1
        blsp.uruguay[0] = 1
        blsp.peru[0] = 2
        blsp.brazil[0] = 1
        blsp.ecuador[0] = 3
        blsp.colombia[0] = 3
        blsp.venezuela[0] = 3
        blsp.guyana[0] = 3
        blsp.frenchguiana[0] = 3
        blsp.suriname[0] = 3
        blsp.argentina[0] = 0
        
    elif lratio[1] == 6:
        blsp.argentina[0] = 1
        blsp.brazil[0] = 1
        blsp.chile[0]= 2
        blsp.bolivia[0] = 2
        blsp.peru[0] = 3
        blsp.ecuador[0] = 3
        blsp.colombia[0] = 3
        blsp.venezuela[0] = 3
        blsp.guyana[0] = 3
        blsp.frenchguiana[0]  = 3
        blsp.suriname[0] = 3
        blsp.paraguay[0] = 2
        blsp.uruguay[0] = 0
        
    elif lratio[1] == 7:
        blsp.bolivia[0] = 1
        blsp.argentina[0] = 1
        blsp.brazil[0] = 1
        blsp.uruguay[0] = 2
        blsp.chile[0] = 2
        blsp.peru[0] = 3
        blsp.ecuador[0] = 3
        blsp.colombia[0] = 3
        blsp.venezuela[0] = 3
        blsp.guyana[0] = 3
        blsp.frenchguiana[0] = 3
        blsp.suriname[0] = 3
        blsp.paraguay[0] = 0
        
    elif lratio[1] == 8:
        blsp.guyana[0] = 1
        blsp.brazil[0] = 1
        blsp.colombia[0] = 1
        blsp.suriname[0] = 2
        blsp.frenchguiana[0] = 2
        blsp.ecuador[0] = 2
        blsp.peru[0] = 2
        blsp.bolivia[0] = 3
        blsp.paraguay[0] = 3
        blsp.uruguay[0] = 3
        blsp.argentina[0] = 3
        blsp.chile[0] = 3
        blsp.venezuela[0] = 0
        
    elif lratio[1] == 9:
        blsp.venezuela[0] = 1
        blsp.ecuador[0] = 1
        blsp.peru[0] = 1
        blsp.brazil[0] = 1
        blsp.guyana[0] = 2
        blsp.suriname[0] = 2
        blsp.frenchguiana[0] = 3
        blsp.bolivia[0] = 2
        blsp.chile[0] = 3
        blsp.argentina[0] = 3
        blsp.paraguay[0] = 3
        blsp.uruguay[0] = 3
        blsp.colombia[0] = 0
        
    elif lratio[1] == 10:
        blsp.peru[0] = 1
        blsp.colombia[0] = 1
        blsp.venezuela[0] = 1
        blsp.guyana[0] = 2
        blsp.suriname[0] = 2
        blsp.frenchguiana[0] = 3
        blsp.brazil[0] = 2
        blsp.bolivia[0] = 2
        blsp.chile[0] = 2
        blsp.argentina[0] = 3
        blsp.paraguay[0] = 3
        blsp.uruguay[0] = 3
        blsp.ecuador[0] = 0
        
    elif lratio[1] == 11:
        blsp.suriname[0] = 1
        blsp.frenchguiana[0] = 1
        blsp.venezuela[0] = 1
        blsp.colombia[0] = 1
        blsp.ecuador[0] = 2
        blsp.brazil[0] = 1
        blsp.bolivia[0] = 2
        blsp.peru[0] = 2
        blsp.paraguay[0] = 2
        blsp.uruguay[0] = 3
        blsp.argentina[0] = 3
        blsp.chile[0] = 3
        blsp.guyana[0] = 0
        
    elif lratio[1] == 12:
        blsp.guyana[0] = 1
        blsp.suriname[0] = 1
        blsp.brazil[0] = 1
        blsp.venezuela[0] = 1
        blsp.colombia[0] = 2
        blsp.ecuador[0] = 2
        blsp.peru[0] = 3
        blsp.bolivia[0] = 2
        blsp.paraguay[0] = 2
        blsp.uruguay[0] = 3
        blsp.argentina[0] = 3
        blsp.chile[0] = 3
        blsp.frenchguiana[0]
        
    elif lratio[1] == 13:
        blsp.guyana[0] = 1
        blsp.frenchguiana[0] = 1
        blsp.brazil[0] = 1
        blsp.venezuela[0] = 1
        blsp.colombia[0] = 2
        blsp.ecuador[0] = 3
        blsp.peru[0] = 3
        blsp.bolivia[0] = 2
        blsp.paraguay[0] = 2
        blsp.uruguay[0] = 3
        blsp.argentina[0] = 3
        blsp.chile[0] = 3
        blsp.suriname[0] = 0
        
        
#main code---
coolerdaniel = random.randint(0, 12)
location = blsp.listofcountriespart2[coolerdaniel]
#determine starting location


#clues are split up into types:
#how much information they give(lots, not much, and cannonball)
#what kind of information they give(so I don't have to write 5000 sentences, just 100.
#flag hints, location based, political specifics, population
def main():
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
    days = 0
    geographygarble(location)
    hint(witwics)
    while play == True:
        if location == witwics:
            break
        
        geographygarble(location)#calculate distances between your current location and other countries
        action = input("Where do you think she is?  ")
        
        if days < 7:
            #flying to different countries
            if action == "bolivia":
                print("You flew to Bolivia")
                fly(blsp.bolivia, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'argentina':
                print("You flew to Argentina")
                fly(blsp.argentina, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'ecuador':
                print("You flew to Ecuador")
                fly(blsp.ecuador, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'brazil':
                print("You flew to Brazil")
                fly(blsp.brazil, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'suriname':
                print("You flew to Suriname")
                fly(blsp.suriname, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'frenchguiana':
                print("You flew to French Guiana")
                fly(blsp.frenchguiana, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'guyana':
                print("You flew to Guyana")
                fly(blsp.guyana, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'chile':
                print("You flew to Chile")
                fly(blsp.chile, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'peru':
                print("You flew to Peru")
                fly(blsp.peru, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'paraguay':
                print("You flew to Paraguay")
                fly(blsp.paraguay, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'uruguay':
                print("You flew to Uruguay")
                fly(blsp.uruguay, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'venezuela':
                print("You flew to Venezuela")
                fly(blsp.venezuela, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'colombia':
                print("You flew to Colombia")
                fly(blsp.colombia, days)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
        elif days >= 7:#lose condition
            print("You ran out of time.")
            print("You failed, Carmen got away, and you're bad at geography.")
            print("You got fired, your wife left you.")
            print("You're homeless. A dog peed on you.")
            print("Better luck next time!")
            play = False


main()
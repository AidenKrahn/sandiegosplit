import random
import blsp

def hint(country, witwics):
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
        antihint(witwics)
    
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

import blsp

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
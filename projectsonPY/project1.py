import random
input = (input("Enter snake, water or gun: "))
computer= random.choice([0,1,-1])
dictonary={"snake":0,"water":-1,"gun":1}
final= dictonary[input]

if(computer== final):
       print ("its a tie")
else:     
     if(computer == 0 and final == -1):
       print ("comp Win")   
     elif(computer == 0 and final == 1):
       print ("You Win" )  
     elif(computer == -1 and final == 0):
      print ("you Win" )  
     elif(computer == -1 and final == 1):
      print ("you Win" )  
     elif(computer == 1 and final == 0):
       print ("comp win")   
     elif(computer == 1 and final == -1):
      print ("You Win" )  




   
   

   
  
        




    
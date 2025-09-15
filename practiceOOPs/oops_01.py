class Programmer:
  company = "Microsoft"

  def __init__ (self ,name , position , salary):
    self.name= name
    self.position = position
    self.salary= salary
 


data = Programmer("siddharth" , "software_Dev" , 1200000)

print(data.name ,data.position , data.salary , data.company)





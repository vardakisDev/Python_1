



import random

class Light:
    def __init__(self , name , numberofcars , color):
        self.name = name
        self.numberofcars = numberofcars
        self.color =color
  
def return_green(a , b ,c):
    if a.numberofcars<b.numberofcars:
        if b.numberofcars>c.numberofcars:
            b.color="green"
            a.color = "red"
            c.color = "red"
        else:
            c.color="green"
            a.color = "red"
            b.color = "red"
    else:
        if c.numberofcars>a.numberofcars:
            c.color="green"
            a.color = "red"
            b.color = "red"
        else:
            a.color="green"
            b.color = "red"
            c.color = "red"
def flow(a,b,c):
    if a.color =="green":
        a.numberofcars -= random.randint(5,10) 
        if a.numberofcars < 0 : a.numberofcars =0 
        b.numberofcars += random.randint(0,5)
        c.numberofcars += random.randint(0,5)
    if b.color =="green":
        b.numberofcars -= random.randint(5,10) 
        if b.numberofcars < 0 : b.numberofcars =0 
        a.numberofcars += random.randint(0,5)
        c.numberofcars += random.randint(0,5)
    if c.color =="green":
        c.numberofcars -= random.randint(5,10)
        if c.numberofcars < 0 : c.numberofcars =0  
        b.numberofcars += random.randint(0,5)
        a.numberofcars += random.randint(0,5)
    return_green(a,b,c)
    print(a.color,b.color,c.color)
    print(a.numberofcars,b.numberofcars,c.numberofcars)

        
def  watch_traffic(a , b ,c ):
    #green has the light with the most cars so we call the return_green function
    print('The flow starts now .... --->>>>')
    i=0
    
    while(i<100):
        flow(a,b,c)
        i +=1






  
light1 = Light("Light1" , random.randint(10,20) ,"red")
light2 = Light("Light2" , random.randint(10,20) , "red")
light3 = Light("Light3" , random.randint(10,20) , "red")
print('Watching *_* traffic .........: Right now there are in \n Ligth1 has :', light1.numberofcars ,'\nLight2 has:' ,light2.numberofcars , '\nLight3 has:' ,light3.numberofcars)
watch_traffic(light1,light2,light3)

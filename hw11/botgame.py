#Matt Wong and Kofi Seyki Appiah
from visual import *
from robot import *
from timeit import default_timer

GROUNDRADIUS = 150

def main():
    ground = cylinder(pos=(0,-1,0), axis=(0,1,0), radius = GROUNDRADIUS, material=materials.earth)
    userbot1 = ranbot()
    userbot2 = myrobot()
    GameName = text(text="DO NOT TOUCH THE EDGES OF THE WORLD",axis=(100,1,0),pos=(0,50,0), align="center", height= 12, color= color.blue, width=8)
    
    
    
    counter = 0
    start=default_timer()
    while True:
        
        rate(50)  # 30 frames per second
        if scene.kb.keys: # is there an event waiting to be processed?
            s = scene.kb.getkey() # obtain keyboard information
            if s == ",":          # if the user pressed the comma...  
                userbot1.turn(5)   # ... turn 5 degrees
            elif s == ".":
                userbot1.turn(-5)
            elif s == 'x':
                userbot1.speed += 0.1
            elif s == 'z':
                userbot1.speed -= 0.1
                    
            elif s == "4":     # if the user pressed the 4...
                userbot2.turn(5)   # ... turn 5 degrees
            elif s == "6":
                userbot2.turn(-5)
            elif s == '5':
                userbot2.speed += 0.1
            elif s == '8':
                userbot2.speed -= 0.1
            else: pass
                
        
        userbot1.forward(userbot1.speed)
        if mag(userbot1.base) >= GROUNDRADIUS:
            userbot1.turn(180)
            counter+=1
            userbot1.speed+=0.2
        
        
        userbot2.forward(userbot2.speed)
        if mag(userbot2.base) >= GROUNDRADIUS:
            userbot2.turn(180)
            counter+=1
            userbot2.speed+=0.2

        if counter=6:
            end_time=default_timer()-start
            print "YOUR SCORE IS", end_time
            print "GAME OVER!!!!! RESTART GAME"
            return




if __name__ == "__main__" : main()



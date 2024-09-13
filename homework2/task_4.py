car_speed = float (input ("enter a speed: "))
if car_speed < 30:
    print ("SLOW")  
elif car_speed > 120:
    print ("VERY FAST")
elif 60 < car_speed <= 120:
    print ("FAST")
elif 30 < car_speed <= 60:
    print ("MODERATE")
else:
    print ("Invalid speed")

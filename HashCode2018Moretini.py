import copy
import sys
import math
import random
from random import randint
import numpy as np

class Car(object):
    def __init__(self, _id):
        self.rides=[]
        self.time_position=[]#time, x, y
        self.id=_id
        self.time_position.append([0,0,0])
        self.time_position.append([999999,0,0])

class Ride(object):
    def __init__(self, inde, a,b,x,y,s,f):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        self.s=s
        self.f=f
        self.benefit=0
        self.index=inde

def evaluate_distance(a,b,x,y):
    return abs(x-a)+abs(y-b)

def evaluate_distancee(ride):
    return abs(ride.a-ride.x)+abs(ride.b-ride.y)

def evaluate_distanceee(time_pos, a,b):
    return abs(time_pos[1]-a)+abs(time_pos[2]-b)

def car_can_do_ride(ride, car):
    for i in range(0, len(car.time_position),2):
        time_needed_m=evaluate_distanceee(car.time_position[i],ride.a,ride.b)#move
        time_needed_r=evaluate_distancee(ride)                    #ride
        time_needed_b=evaluate_distanceee(car.time_position[i+1],ride.x,ride.y)#back
        time_needed=time_needed_b+time_needed_m+time_needed_r
        #time disponible in this slot is bigger than the time needed?
        start=car.time_position[i][0] if car.time_position[i][0]>ride.s-time_needed_m else ride.s-time_needed_m
        finish=car.time_position[i+1][0] if car.time_position[i+1][0]<ride.f+time_needed_b else ride.f+time_needed_b
        if(finish-start>=time_needed):
            #car.rides.append(ride.index)
            if(car.time_position[i][0]+time_needed_m<ride.s):
                if(ride.s+time_needed_r<ride.f):
                    car.rides.append(ride.index)
                    car.time_position.append([ride.s-4, ride.a,ride.b])
                    car.time_position.append([ride.s+time_needed_r+4, ride.x,ride.y])
                    car.time_position.sort(key=lambda x: x[0], reverse=False)
            else:
                if(car.time_position[i][0]+time_needed_m+time_needed_r<ride.f):
                    car.rides.append(ride.index)
                    car.time_position.append([car.time_position[i][0]+time_needed_m-4, ride.a,ride.b])
                    car.time_position.append([car.time_position[i][0]+time_needed_m+time_needed_r+4, ride.x,ride.y])#+4 e -4 perchè qualcosa nel codice è errato e accetta delle rides che non può portare a termine
                    car.time_position.sort(key=lambda x: x[0], reverse=False)
            #car.time_position.sort(key=lambda x: x[0], reverse=False)
            #print(car.time_position)
            return True
    return False

def main():
    Rides=[]
    Cars=[]
    f = open( 'data4.in' , 'r' )
    row=f.readline().split(' ')
    nCars=int(row[2])
    line = f.readline()
    index=0
    while line :
        data=line.split(' ');
        Rides.append(Ride(index,int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5])))
        index=index+1
        line = f.readline()
    f.close()
    for i in range(0,nCars):
        Cars.append(Car(i))
    for r in Rides:
        r.benefit=evaluate_distancee(r)
    Rides.sort(key=lambda x: x.benefit, reverse=True)
    indexRides=0
    while(indexRides<len(Rides)):
        print(indexRides)
        possible=False
        for c in Cars:
            if(indexRides>=len(Rides)):
                break
            if(car_can_do_ride(Rides[indexRides],c)):
                indexRides=indexRides+1
                possible=True
        if not possible:
            indexRides=indexRides+1
    f1=open('./output4', 'w+')
    for c in Cars:
        ridesSTR=""
        for r in c.rides:
            ridesSTR=ridesSTR+" "+str(r)
        f1.write(str(len(c.rides))+ ridesSTR+'\n')
        print(str(len(c.rides))+ ridesSTR)
    f1.close()


if  __name__ =='__main__':
    main()

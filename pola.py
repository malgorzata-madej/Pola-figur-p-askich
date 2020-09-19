import math

#Kwadrat
def kwadrat(a):
    pole = a**2
    return pole

#Prostokąt
def prostokat(a,b):
    pole = a*b
    return pole

#Trójkąt
def trojkat(a,h):
    pole = (a*h)/2
    return pole

#Trapez
def trapez(a,b,h):
    pole = (a+b)*h/2
    return pole

#Romb
def romb(p,q):
    pole = (p*q)/2
    return pole

#Koło
def kolo(r):
    pole = math.pi *r**2
    return pole


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:53:46 2021

@author: Troilus D'Troy'
"""

from PIL import Image, ImageDraw, ImageFont

#=============================================================================
#Functions

#drawfunctions
def hexdraw(x,y,des,rot):
    cx=x
    cy=y
    rot=float(rot)
    if des=='F' or des=='FI' or des=='FIe' or des=='FMI' or des=='FO' or des=='FOe' or des=='FM':
        #draw full hex
        if rot==0 or rot==1 or rot==2 or rot==4:
            #going to need to come back and define other cases when try to draw engines
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                          (cx,cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                             fill=MBColor(ls[31]),outline=(0,0,0))
        #draw wire orientation
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx+.866*r,cy+r/2),(cx+r/2,cy+.71*r),(cx+.866*r,cy)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx+.866*r,cy),(cx+r/2,cy-.71*r),(cx+.866*r,cy-r/2)),\
                             fill=(0,0,0),outline=(0,0,0))
        #draw engine
        if ls[32]=='True' and rot==0:
            draw.polygon(((cx+.866*r,cy+r/4),(cx+.7*r,cy+r/4),(cx+.7*r,cy-r/4),\
                          (cx+.866*r,cy-r/4)),fill=(255,51,51),outline=(0,0,0))
        #looks a little off
        elif ls[32]=='True' and rot==1:
            draw.polygon(((cx+r*.213,cy-r*.875),(cx+.663*r,cy-r*.613),(cx+.575*r,cy-r*.475),\
                          (cx+r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
        elif ls[32]=='True' and rot==2:
            draw.polygon(((cx-r*.213,cy-r*.875),(cx-.663*r,cy-r*.613),(cx-.575*r,cy-r*.475),\
                          (cx-r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
    elif des=='aIe' or des=='aOe' or des=='aM' or des=='aOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r)),fill=MBColor(ls[31]),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy+r),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(ls[31]),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==4:
            draw.polygon(((cx-.866*r,cy-r/2),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(ls[31]),outline=(0,0,0))
            #the 2nd coord is still wrong a bit
            draw.polygon(((cx+.866*r,cy+r/2),(cx+r*.70,cy+.4*r),(cx+.866*r,cy)),\
                         fill=(0,0,0),outline=(0,0,0))
    elif des=='bI' or des=='bIe' or des=='bMe' or des=='bOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy-r/2)),\
                          fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(ls[31]),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(ls[31]),outline=(0,0,0))
    elif des=='cOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2)),\
                         fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r)),\
                         fill=MBColor(ls[31]),outline=(0,0,0))
    elif des=='dIe' or des=='dOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx-.433*r,cy-3/4*r),(cx+.433*r,cy+3/4*r)),\
                     fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      (cx+.866*r,cy),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2),(cx+.433*r,cy+3/4*r),\
                      (cx-.433*r,cy-3/4*r),(cx,cy-r)),\
                     fill=MBColor(ls[31]),outline=(0,0,0))
    elif des=='gIe':
        if rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      ((cx+r/2),cy-.866*r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(ls[31]),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy+r),(cx-r/2,cy+3/4*r),(cx-r/2,cy-3/4*r),\
                      ((cx),cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(ls[31]),outline=(0,0,0))

#=============================================================================
def MBColor(MB):
    colors=[(255,153,153),(255,204,153),(255,255,153),(204,255,153),(153,255,153),\
            (153,255,204),(153,255,255),(153,204,255),(153,153,255),(204,153,255),\
            (255,153,255),(255,153,204),(224,224,224),
            (255,153,153),(255,204,153),(255,255,153),(204,255,153),(153,255,153),\
            (153,255,204),(153,255,255),(153,204,255),(153,153,255),(204,153,255),\
            (255,153,255),(255,153,204),(224,224,224)]
    return colors[int(MB)]
#=============================================================================
#Determine Shape

#Function to move wagon to (0,0) coordinates before evaluating shape
def ToOrigin(list1):
    list1.sort(key=lambda i:i[1])
    i=0
    newlist=[]
    for hx in list1:
        #move x to 0
        if i==0 and hx[1]!=0:
            xo=hx[1]
            hx[1]=0
        elif i==0 and hx[1]==0:
            xo=0
        else:
            hx[1]=hx[1]-xo
        #move y to 0
        if i==0 and hx[2]!=0:
            yo=hx[2]
            hx[2]=0
        elif i==0 and hx[2]==0:
            yo=0
        else:
            hx[2]=hx[2]-yo    
        i+=1
        newlist.append(hx)
    return newlist







#=============================================================================


filepath = 'geometry.hgcal.txt'

file=open(filepath)
data=file.readlines()
header=data[0]

#columns
#print(header)

#dividing data up based on spaces
#linesplit=data[1].strip().split(' ')
#print(linesplit[2])

#trying to draw the hexagons based on 
xmax=2000
ymax=2000
xoff=700
yoff=100
r=55

#Set new image
im1=Image.new('RGB',(xmax,ymax),(128,128,128))
draw=ImageDraw.Draw(im1)

#input
layer=str(29)
MB=str(22)
MBlist=[]

#DrawLayer

for i in data:
    ls=i.strip().split(' ')
    if ls[0]==layer:
        x=ls[1]
        y=ls[2]
        cx=float(x)*100+xoff-float(y)*50
        cy=ymax-(float(y)*90+yoff)
        hexdraw(cx,cy,ls[3],ls[6])
        # specified font size 
        font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20) 
        txt=ls[3]+'\n('+ls[1]+','+ls[2]+')'
        draw.text((cx-18,cy-20),str(txt), fill=(0,0,0),font=font)
        #Saving Motherboard hexes
        if ls[31]==MB:
            #u,v,itype,irot,triglinks,datalinksLD,datalinksHD,isEngine,HDorLD,u,v
            MBlist.append([int(ls[0]),int(ls[1]),int(ls[2]),ls[3],int(ls[6]),int(float(ls[25])),\
                          int(float(ls[27])),int(float(ls[29])),ls[32],int(ls[37]),\
                              int(ls[1]),int(ls[2])])



#Move to origin
testlist=ToOrigin(MBlist)

#need a rotate function based on if not flat
#def Rotate(list1):
    

slope=[]
for hx in testlist:
    print(hx)

#Lists for all different shapes of wagons
#Linear
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
L6=[]
#Triangle
T3=[]
#Unknown Catchalls
U1=[]
U2=[]
U3=[]
U4=[]
U5=[]
U6=[]
#Wide variety of 2+pieces.  Actually need to go back and create ifs in the len3 section


#categorize based off slope. 
#determine slopes
i=0
for i in range(0,len(testlist)-1,1):
    if (testlist[i+1][1]-testlist[i][1])==0:
        s=float('inf')
    else:
        s=(testlist[i+1][2]-testlist[i][2])/(testlist[i+1][1]-testlist[i][1])
    slope.append(s)

print(slope)


#if slope is 45deg, rotates it flat and updates slope variable
if len(set(slope))==1 and slope[0]==1.0:
    for i in range(0,len(testlist),1):
        testlist[i][2]=0
    for i in range(0,len(testlist)-1,1):
        slope[i]=0
#if slope is vertical, rotates 90 and update slope
if len(set(slope))==1 and slope[0]==float('inf'):
    for i in range(0,len(testlist),1):
        testlist[i][1]=testlist[i][2]
        testlist[i][2]=0
    for i in range(0,len(testlist)-1,1):
        slope[i]=0       
slope.sort()   

print(slope)

for hx in testlist:
    print(hx)


#this sorts by motherboard shape.  I need to divide the list up into wagon shapes
#before feeding it into this counter
#linear length 2
if len(set(slope))==1 and slope[0]==0 and len(testlist)==2:
    shape='Linear'
    L2.append()
#linear length 3
elif len(set(slope))==1 and slope[0]==0 and len(testlist)==3:
    shape='Linear'
    L3.append([testlist])
#linear length 4
elif len(set(slope))==1 and slope[0]==0 and len(testlist)==4:
    shape='Linear'
    L4.append([testlist])
#linear length 5
elif len(set(slope))==1 and slope[0]==0 and len(testlist)==5:
    shape='Linear'
    L5.append([testlist])    
#linear length 6
elif len(set(slope))==1 and slope[0]==0 and len(testlist)==6:
    shape='Linear'
    L6.append([testlist]) 
#Triangles
elif len(set(slope))==2 and slope==[0.0,float('inf')]:
    shape='Triangle'
    T3.append([testlist])
#Unknowns
elif len(testlist)==2:
    shape='Unknown'
    U2.append([testlist])
elif len(testlist)==3:
    shape='Unknown'
    U3.append([testlist])
elif len(testlist)==4:
    shape='Unknown'
    U4.append([testlist])
elif len(testlist)==5:
    shape='Unknown'
    U5.append([testlist])
else:
    shape='Error'

print(shape, ', Length= ', len(testlist), ' ', [d[2] for d in testlist],\
          ', ', [d[3] for d in testlist])

print('\n    Total Counts')
print('L1: ',len(L1))
print('L2: ',len(L2))
print('L3: ',len(L3))
print('L4: ',len(L4))
print('L5: ',len(L5))
print('L6: ',len(L6))
print('T3: ',len(T3))
print('U1: ',len(U1))
print('U2: ',len(U2))
print('U3: ',len(U3))
print('U4: ',len(U4))
print('U5: ',len(U5))

    
       
#Layer Image 
#im1.save('imagetest1.jpg',quality=95)
#im1.show()

#Drawing to test hex shapes
im2=Image.new('RGB',(xmax,ymax),(128,128,128))
draw=ImageDraw.Draw(im2)

#Wagon Images
#im2.save('imagetest2.jpg',quality=95)
#im2.show()
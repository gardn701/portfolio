# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:53:46 2021

@author: Troilus D'Troy'
"""

from PIL import Image, ImageDraw, ImageFont
import math

#=============================================================================
#Functions

#drawfunctions
def hexdraw(x,y,des,rot,mb,eng):
    cx=x
    cy=y
    rot=float(rot)
    if des=='F' or des=='FI' or des=='FIe' or des=='FMI' or des=='FO'\
        or des=='FOe' or des=='FM' or des=='FMe':
        #draw full hex
        if rot==0 or rot==1 or rot==2 or rot==3 or rot==4 or rot==5:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                          (cx,cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                             fill=MBColor(mb,des),outline=(0,0,0))
        #orientation
        draworfull(cx,cy,r,rot)            
        #draw engine
        if eng=='True' and rot==0:
            draw.polygon(((cx+.866*r,cy+r/4),(cx+.7*r,cy+r/4),(cx+.7*r,cy-r/4),\
                          (cx+.866*r,cy-r/4)),fill=(255,51,51),outline=(0,0,0))
        #looks a little off
        elif eng=='True' and (rot==1):
            draw.polygon(((cx+r*.213,cy-r*.875),(cx+.663*r,cy-r*.613),(cx+.575*r,cy-r*.475),\
                          (cx+r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and (rot==2):
            draw.polygon(((cx-r*.213,cy-r*.875),(cx-.663*r,cy-r*.613),(cx-.575*r,cy-r*.475),\
                          (cx-r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))

        #changed where these draw for the even layers that are reversed and engines should be opp side
        #this might need to be changed for causing problems in wagon drawing
        #draws for board
        elif eng=='True' and rot==3 and bow==0:
            draw.polygon(((cx+.866*r,cy+r/4),(cx+.7*r,cy+r/4),(cx+.7*r,cy-r/4),\
                          (cx+.866*r,cy-r/4)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and (rot==4) and bow==0:
            draw.polygon(((cx+r*.213,cy-r*.875),(cx+.663*r,cy-r*.613),(cx+.575*r,cy-r*.475),\
                          (cx+r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and (rot==5) and bow==0:
            draw.polygon(((cx-r*.213,cy-r*.875),(cx-.663*r,cy-r*.613),(cx-.575*r,cy-r*.475),\
                          (cx-r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
        #draws for wagons, these are the more 'proper' placements
        elif eng=='True' and rot==3 and bow !=0:
            draw.polygon(((cx-.866*r,cy+r/4),(cx-.7*r,cy+r/4),(cx-.7*r,cy-r/4),\
                          (cx-.866*r,cy-r/4)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and rot==4 and bow !=0:
            draw.polygon(((cx-r*.213,cy+r*.875),(cx-.663*r,cy+r*.613),(cx-.575*r,cy+r*.475),\
                          (cx-r*.125,cy+r*.737)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and rot==5 and bow !=0:
            draw.polygon(((cx+r*.213,cy+r*.875),(cx+.663*r,cy+r*.613),(cx+.575*r,cy+r*.475),\
                          (cx+r*.125,cy+r*.737)),fill=(255,51,51),outline=(0,0,0)) 
        
    elif des=='aIe' or des=='aOe' or des=='aM' or des=='aOe' or des=='aMe':
        if rot==4:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r)),fill=MBColor(mb,des),outline=(0,0,0))
            #draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx,cy+3/4*r)),\
            #                 fill=(0,0,0),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb,des),outline=(0,0,0))
            #draw.polygon(((cx,cy+r),(cx,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
            #                 fill=(0,0,0),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx-.866*r,cy-r/2),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb,des),outline=(0,0,0))
            #the 2nd coord is still wrong a bit
            #draw.polygon(((cx+.866*r,cy+r/2),(cx+r*.70,cy+.4*r),(cx+.866*r,cy)),\
            #             fill=(0,0,0),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2)),fill=MBColor(mb,des),outline=(0,0,0))
    elif des=='bI' or des=='bIe' or des=='bMe' or des=='bOe':
        if rot==4:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy-r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
            #draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
            #                 fill=(0,0,0),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb,des),outline=(0,0,0))
    elif des=='cOe':
        if rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==4:
            draw.polygon(((cx,cy+r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx+.866*r,cy+r/2),(cx+.866*r,cy-r/2),(cx,cy-r)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==0:
            draw.polygon(((cx,cy-r),(cx-.866*r,cy-r/2),(cx+.866*r,cy-r/2)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r)),\
                         fill=MBColor(mb,des),outline=(0,0,0))
    elif des=='dIe' or des=='dOe':
        if rot==5:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx-.433*r,cy-3/4*r),(cx+.433*r,cy+3/4*r)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      (cx+.866*r,cy),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx+.866*r,cy+r/2),(cx+.866*r,cy-r/2),\
                      (cx+.433*r,cy-3/4*r),(cx-.433*r,cy+3/4*r)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2),(cx+.433*r,cy+3/4*r),\
                      (cx-.433*r,cy-3/4*r),(cx,cy-r)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy-r),(cx-.866*r,cy-r/2),(cx-.866*r,cy),\
                      (cx+.866*r,cy),(cx+.866*r,cy-r/2)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==4:
            draw.polygon(((cx-.433*r,cy+3/4*r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.433*r,cy-r*3/4)),\
                     fill=MBColor(mb,des),outline=(0,0,0))        
    elif des=='gIe':
        if rot==2:
            draw.polygon(((cx,cy+r),(cx-r/2,cy+r*.71),(cx-r/2,cy-r*.71),\
                      (cx,cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb,des),outline=(0,0,0))        
        elif rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      ((cx-r/2),cy-.866*r),(cx+.866*r,cy),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      ((cx+r/2),cy-.866*r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb,des),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx-.866*r,cy),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      ((cx+r*.866),cy-r/2),(cx+.866*r,cy+r/2),(cx+r/2,cy+.866*r)),\
                     fill=MBColor(mb,des),outline=(0,0,0))

        #orientation
        #draworfull(cx,cy,r,rot)

#=============================================================================
#draws orientation arrow on hex in irot direction for full black arrowhead
def draworfull(cx,cy,r,rot):
    if rot==0 or rot==6:
        draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                         fill=(0,0,0),outline=(0,0,0))
    elif rot==1:
        draw.polygon(((cx+.866*r,cy+r/2),(cx+r/2,cy+.71*r),(cx+.866*r,cy)),\
                         fill=(0,0,0),outline=(0,0,0))
    elif rot==2:
        draw.polygon(((cx+.866*r,cy),(cx+r/2,cy-.71*r),(cx+.866*r,cy-r/2)),\
                         fill=(0,0,0),outline=(0,0,0))
    elif rot==3:
        draw.polygon(((cx,cy-r),(cx-.433*r,cy-3/4*r),(cx+.433*r,cy-3/4*r)),\
                         fill=(0,0,0),outline=(0,0,0))
    elif rot==4:
        draw.polygon(((cx-.866*r,cy),(cx-.866*r,cy-r/2),(cx-r/2,cy-.71*r)),\
                         fill=(0,0,0),outline=(0,0,0))         
    elif rot==5:
        draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy),(cx-r/2,cy+.71*r)),\
                         fill=(0,0,0),outline=(0,0,0)) 

#=============================================================================
def MBColor(MB,des):
    colorsld=[(153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224),\
             (153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224),\
                (153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224)]
    colorshd=[(53,155,155),(155,53,53),(53,104,155),(155,104,53),\
            (53,53,155),(155,155,53),(104,53,155),(104,155,53),(104,2,0),\
            (155,53,155),(53,155,53),(155,53,104),(53,155,104),(124,124,124),\
             (53,155,155),(155,53,53),(53,104,155),(155,104,53),\
            (53,53,155),(155,155,53),(104,53,155),(104,155,53),(104,2,0),\
            (155,53,155),(53,155,53),(155,53,104),(53,155,104),(124,124,124),\
             (53,155,155),(155,53,53),(53,104,155),(155,104,53),\
            (53,53,155),(155,155,53),(104,53,155),(104,155,53),(104,2,0),\
            (155,53,155),(53,155,53),(155,53,104),(53,155,104),(124,124,124)]
    #the data has some weird namings with MBs that jump from ~15 to restart at 100
    #they start at 100 for the section between 60-120 deg that they duplicated
    #the first 28 layers used to only be 60 deg drawings
    if bow==0:
        mb=int(MB)
        while mb>41:
            mb-=41
        if des=='FI' or des=='FIe' or des=='aIe' or des=='bI' or des=='bIe' or des=='dIe' or des=='gIe':
            pick=colorshd[mb]
        else:
            pick=colorsld[mb]  
    elif bow==1:
        pick=(0,200,0)
    elif bow==2:
        pick=(220,220,220)
    elif bow==3:
        pick=(0,100,0)
    return pick
#=============================================================================
#Repositioning Wagon for evaluation

#Function to move wagon to (0,0) coordinates before evaluating shape
def ToOrigin(list1):
    #list1.sort(key=lambda i:i[1])
    dis=1000
    for hx in list1:
        if  (hx[1]**2+hx[2]**2)**.5 < dis:
            xo=hx[1]
            yo=hx[2]
            dis=(hx[1]**2+hx[2]**2)**.5 
    
    for hx in list1:
        #move x to 0
        hx[1]=hx[1]-xo
        #move y to 0
        hx[2]=hx[2]-yo    
        

def Slope(wagon):
    slope=[]
    
    i=0
    for i in range(0,len(wagon)-1,1):
        if (wagon[i+1][1]-wagon[i][1])==0:
            if wagon[i+1][2]>wagon[i][2]:
                s=float('inf')
            elif wagon[i+1][2]<wagon[i][2]:
                s=float('-inf')
        else:
            s=(wagon[i+1][2]-wagon[i][2])/(wagon[i+1][1]-wagon[i][1])
            if wagon[i+1][1]<wagon[i][1] and wagon[i+1][2]<wagon[i][2]:
                s=-1*s
        slope.append(s)

    return slope

#Rotate to be flat

def Rotate(wagon):
    #changing rotation check to work off engine piece irot instead of slope for nontriangles
    erot=''
    for line in wagon:
        if line[8]=='True':
            erot=line[4]
            #fix for negative rots
            #if erot==-1:
            #    erot=5
            #elif erot==-2:
            #    erot=4
            #elif erot==-3:
            #    erot=3
            #elif erot==-4:
            #    erot=2
            #elif erot==-5:
            #    erot=1
    
    #categorize based off slope. 
    #determine slopes
    slope=Slope(wagon)
    
    #want to rotate things like triangle into a default orientation to make it easier to see which are same
    r2s=''
    
    #catch single hex pieces from breaking code
    if slope==[]:
        slope=[]
    #Catching Triangles to rotate to uniform orientation
    elif slope==[0.0,float('inf')]:
        r2s='T'
    elif slope==[1.0, float('-inf')]:
        wagon.sort(key=lambda i:(i[1],i[2]))
        slope=[0.0,float('inf')]
        r2s='T'
    elif slope==[float('-inf'),1.0]:
        wagon[1][1]=1
        wagon[1][2]=0
        wagon[2][1]=1
        wagon[2][2]=1
        slope=[0.0,float('inf')]
        r2s='T'
        for hx in wagon:
            hx[4]+=1
    elif slope==[0.0,-1.0]:
        wagon[1][1]=1
        wagon[1][2]=1
        wagon[2][1]=1
        wagon[2][2]=0
        wagon.sort(key=lambda i:(i[1],i[2]))
        slope=[0.0,float('inf')]
        r2s='T'
        for hx in wagon:
            hx[4]+=1
    elif slope==[float('inf'),0.0]:
        wagon[1][1]=1
        wagon[1][2]=1
        wagon[2][1]=1
        wagon[2][2]=0
        wagon.sort(key=lambda i:(i[1],i[2]))
        slope=[0.0,float('inf')]
        r2s='T'
        for hx in wagon:
            hx[4]-=1
    elif slope==[-1.0,0.0]:
        wagon[1][1]=1
        wagon[1][2]=0
        wagon[2][1]=1
        wagon[2][2]=1
        wagon.sort(key=lambda i:(i[1],i[2]))
        slope=[0.0,float('inf')]
        r2s='T'
        for hx in wagon:
            hx[4]+=2
    #special catch for U pieces with 3rd in R2.  Something changed and broke this from 
    #processing correctly, so adding this to fix.  Probably an extra sort?
    #I sort by u then v, which is fine, but when you go negative y the order is kind of wrong
    #to try and process semi-linearly
    elif slope==[-1.0,float('inf')]:
        wagon.sort(key=lambda i:(i[1],-i[2]))
        slope=[0.0,float('-inf')]
    elif slope==[float('inf'),-1.0]:
        wagon.sort(key=lambda i:(i[1],-i[2]))
        slope=[0.0,1.0]
    #correction for U pieces that bend on first hex instead of engine hex
    elif slope==[float('-inf'),0.0] and erot==0:
        for i in range(0,len(wagon),1):
            u=wagon[i][1]
            v=wagon[i][2]
            #change u,v
            wagon[i][1]=u-v
            wagon[i][2]=u
            #change irot
            wagon[i][4]+=1
        #change slopes
        for i in range(0,len(wagon)-1,1):
            if slope[i]==float('-inf'):
                slope[i]=0.0
            elif slope[i]==0.0:
                slope[i]=1.0
                #0 can go forwars or backwards... need to account for
            elif slope[i]==1.0:
                slope[i]=float('inf')
    #everything else
    #if wagon has engine, rotate based on that erot value first
    #for non engine wagons, still need to rotate slopes based on slopes
    #Rotate 1, slope 45deg
    elif erot==1:
        for i in range(0,len(wagon),1):
            u=wagon[i][1]
            v=wagon[i][2]
            #change u,v
            wagon[i][1]=v
            wagon[i][2]=v-u
            #change rotation values
            wagon[i][4]=wagon[i][4]-1
        #change slopes
        for i in range(0,len(wagon)-1,1):
            if slope[i]==1.0:
                slope[i]=0.0
            elif slope[i]==0.0:
                slope[i]=float('-inf')
            elif slope[i]==float('inf'):
                slope[i]=1.0
            elif slope[i]==float('-inf'):
                slope[i]=-1.0    
        erot=0
        print("triggered erot 1")
    #Rotate inf, slope 90deg
    elif erot==2:
        for i in range(0,len(wagon),1):
            u=wagon[i][1]
            v=wagon[i][2]
            #change u,v
            wagon[i][1]=v-u
            wagon[i][2]=-1*u
            #change irot
            wagon[i][4]-=2
        #change slopes
        for i in range(0,len(wagon)-1,1):
            if slope[i]==float('inf'):
                slope[i]=0.0
            elif slope[i]==0.0:
                slope[i]=-1.0
                #0 can go forwards or backwards... need to account for
            elif slope[i]==1.0:
                slope[i]=float('-inf')
        erot=0
    elif erot==4:
        for i in range(0,len(wagon),1):
            u=wagon[i][1]
            v=wagon[i][2]
            #change u,v
            wagon[i][1]=-1*v
            wagon[i][2]=u-v
            #change irot
            wagon[i][4]+=2
        #change slopes
        for i in range(0,len(wagon)-1,1):
            if slope[i]==float('inf'):
                slope[i]=-1.0
            elif slope[i]==0.0:
                slope[i]=float('-inf')
                #0 can go forwards or backwards... need to account for
            elif slope[i]==1.0:
                slope[i]=0.0
        erot=0
    elif erot==-1 or erot==5:
        for i in range(0,len(wagon),1):
            u=wagon[i][1]
            v=wagon[i][2]
            #change u,v
            wagon[i][1]=v
            wagon[i][2]=u
            #change irot
            wagon[i][4]-=2
        #change slopes
        for i in range(0,len(wagon)-1,1):
            if slope[i]==float('-inf'):
                slope[i]=0.0
            elif slope[i]==0.0:
                slope[i]=1.0
                #0 can go forwards or backwards... need to account for
            elif slope[i]==1.0:
                slope[i]=float('inf')
        erot=0
    elif erot==0 and r2s!='T':
        #wagon.sort(key=lambda i:(i[1],i[2]))
        #print(wagon)
        #slope=Slope(wagon)
        #print(slope)
    #there was an engine piece with rot0 but had piece coming out at slope 1, need to lay flat
    #there might be other occurances where I need to add additional slope checks
           
        if slope[0]==1.0:
            for i in range(0,len(wagon),1):
                u=wagon[i][1]
                v=wagon[i][2]
                #change u,v
                wagon[i][1]=v
                wagon[i][2]=v-u
                #change rotation values
                wagon[i][4]=wagon[i][4]-1
            #change slopes
            for i in range(0,len(wagon)-1,1):
                if slope[i]==1.0:
                    slope[i]=0.0
                elif slope[i]==0.0:
                    slope[i]=float('-inf')
                elif slope[i]==float('inf'):
                    slope[i]=1.0
        elif slope[0]==float('-inf'):
            for i in range(0,len(wagon),1):
                u=wagon[i][1]
                v=wagon[i][2]
                #change u,v
                wagon[i][1]=u-v
                wagon[i][2]=u
                #change irot
                wagon[i][4]+=1
                #change slopes
            for i in range(0,len(wagon)-1,1):
                if slope[i]==float('-inf'):
                    slope[i]=0.0
                elif slope[i]==0.0:
                    slope[i]=1.0
                    #0 can go forwards or backwards... need to account for
                elif slope[i]==1.0:
                    slope[i]=float('inf')
    elif erot=='':
        if slope[0]==1.0:
            for i in range(0,len(wagon),1):
                u=wagon[i][1]
                v=wagon[i][2]
                #change u,v
                wagon[i][1]=v
                wagon[i][2]=v-u
                #change rotation values
                wagon[i][4]=wagon[i][4]-1
            #change slopes
            for i in range(0,len(wagon)-1,1):
                if slope[i]==1.0:
                    slope[i]=0.0
                elif slope[i]==0.0:
                    slope[i]=-1.0
                elif slope[i]==float('inf'):
                    slope[i]=float('inf')
        #Rotate inf, slope 90deg
        elif slope[0]==float('inf'):
            for i in range(0,len(wagon),1):
                u=wagon[i][1]
                v=wagon[i][2]
                #change u,v
                wagon[i][1]=v-u
                wagon[i][2]=-1*u
                #change irot
                wagon[i][4]-=2
            #change slopes
            for i in range(0,len(wagon)-1,1):
                if slope[i]==float('inf'):
                    slope[i]=0.0
                elif slope[i]==0.0:
                    slope[i]=-1.0
                    #0 can go forwars or backwards... need to account for
                elif slope[i]==1.0:
                    slope[i]=float('-inf')
        elif slope[0]==float('-inf'):
            for i in range(0,len(wagon),1):
                u=wagon[i][1]
                v=wagon[i][2]
                #change u,v
                wagon[i][1]=u-v
                wagon[i][2]=u
                #change irot
                wagon[i][4]+=1
            #change slopes
            for i in range(0,len(wagon)-1,1):
                if slope[i]==float('-inf'):
                    slope[i]=0.0
                elif slope[i]==0.0:
                    slope[i]=1.0
                    #0 can go forwars or backwards... need to account for
                elif slope[i]==1.0:
                    slope[i]=float('inf')
    
    #print(slope)
    
    #trying to catch the 6 piece triangle MBs.  Proving hard to separate
    if len(slope)==5:
        r2s='B'
    
    
    
    
    #rotate triangles again, putting engine in spot (1,0)
    if r2s=='T' and (wagon[0][8]=='True' or wagon[1][8]=='True' or wagon[2][8]=='True'):
        t=0
        for line in wagon:
            if line[8]=='True':
                t=t
                break
            else:
                t+=1
        
        #print('t rotate 2 triggered')
        #print(wagon)
        owagon=wagon
        wagon=[]
        if t==0:
            owagon[0][1]=1
            owagon[0][2]=0
            owagon[1][1]=1
            owagon[1][2]=1
            owagon[2][1]=0
            owagon[2][2]=0
            owagon.sort(key=lambda i:(i[1],i[2]))
            for hx in owagon:
                hx[4]+=2
            wagon=owagon
        elif t==1:
            wagon=owagon
        elif t==2:
            owagon[0][1]=1
            owagon[0][2]=1
            owagon[1][1]=0
            owagon[1][2]=0
            owagon[2][1]=1
            owagon[2][2]=0
            owagon.sort(key=lambda i:(i[1],i[2]))
            for hx in owagon:
                hx[4]-=2
            wagon=owagon
        #print(wagon)
    
    return wagon,slope

#=============================================================================
#Generate wagon names
def wname(MB,slope):
    name=''
    shape=''
     
    #HD or LD
    if MB[0][9] ==0:
        name+='LD'
    elif MB[0][9]==1:
        name+='HD'
    
    #Triangles need some sort to evaluate equally.  Read them either
    #(0,0)->(1,0)->(1,1) or (0,0)->(0,1)->(1,1)
    #additional sort, to catch after the split
    #MB.sort(key=lambda i:(i[1],i[2]))
    
    #Linear, Triangle, or Unusual
    if len(set(slope))==1 and slope[0]==0:
        name+='L'
    elif slope==[]:
        name+='L'
        shape='L'
    elif len(set(slope))==2 and (slope==[0.0,float('inf')]):
        name+='T'
    else:
        shape='U'
        name+='U'
    
    #number of hexes in wagon
    name+=str(len(MB))
    
    #hex designations
    i=0
    for line in MB:
        #describing rotation of odd pieces
        #R1=NE, R2=SE, add more if needed
        if shape=='U' and i>1 and slope[i-1]!=0.0:
            name+='R'
            if slope[i-1]==1.0:
                name+=str(1)
            elif slope[i-1]==float('-inf'):
                name+=str(2)
            else:
                name+=str(9)
        i+=1
        
        #including b as F's here
        if line[3]=='FO' or line[3]=='FI' or line[3]=='FM' or line[3]=='FIe' or line[3]=='FOe'\
            or line[3]=='bOe' or line[3]=='F' or line[3]=='FMI' or line[3]=='bMe' \
            or line[3]=='FMe' or line[3]=='bIe':
            name+='F'
        elif line[3]=='aOe' or line[3]=='aIe' or line[3]=='aM' or line[3]=='aMe':
            name+='a'
        elif line[3]=='dOe' or line[3]=='dIe':
            name+='d'
        elif line[3]=='gIe' or line[3]=='gOe':
            name+='g'
        
 
        #Rotation values
        if shape=='L' and len(MB)==1 and\
            (line[3]=='FO' or line[3]=='FI' or line[3]=='FM' or line[3]=='FIe' or line[3]=='FOe'\
            or line[3]=='bOe' or line[3]=='F' or line[3]=='FMI' or line[3]=='bMe' \
            or line[3]=='FMe' or line[3]=='bIe'):
            name+=str(0)
            #this catches any stray single pieces with odd rotations and makes 0 for naming
        #correct negative rotations
        elif line[4]==-1:
            name+=str(5)
        elif line[4]==-2:
            name+=str(4)
        elif line[4]==-3:
            name+=str(3)
        elif line[4]==-4:
            name+=str(2)
        elif line[4]==-5:
            name+=str(1)
        elif line[4]==6:
            name+=str(0)
        else:
            name+=str(line[4])
        
        #isEngine
        if line[8]=='True':
            name+='E'
        
    return name

#=============================================================================
#lets move all wagon drawing functions here and call as needed
#into dynamic spaces

def wagondraw(x,y,wname):
    
    xf=x
    yf=y
    diag=0 
    
    wname=wname[2:]
     
    shape=wname[0]
    wname=wname[2:]
     
    wl=0
    n=0
    
    while n<len(wname):
        
        #draw triangle wagons, need a counter that draws their placement fixed
        if shape=='T':
            #hexshape
            if wname[n]=='F':
                des='FO'
            elif wname[n]=='a':
                des='aOe'
            elif wname[n]=='b':
                des='bOe'
            elif wname[n]=='d':
                des='dOe'
            elif wname[n]=='g':
                des='gOe'
            
            rot=wname[n+1]
            
            #Need exception for if indexes for E/R dont exist for last hex
            if n+2<len(wname):
                #engine check
                if wname[n+2]=='E':
                    eng='True'
                    n+=1
                else:
                    eng='False'
            else:
                eng='False'
            
            if wl==0:
                x=xf
                y=yf
            elif wl==1:
                x=xf+70
                y=yf
            elif wl==2:
                x=xf+35
                y=yf-60
    
        #draw linear wagons.  placement is dynamic
        elif shape=='L' or shape=='U':
            
            #hexshape
            if wname[n]=='F':
                des='FO'
            elif wname[n]=='a':
                des='aOe'
            elif wname[n]=='b':
                des='bOe'
            elif wname[n]=='d':
                des='dOe'
            elif wname[n]=='g':
                des='gOe'
            
            rot=wname[n+1]
            
            if diag==0:
                x=xf+70*wl
            elif diag==1:
                x=xf+70*wl-35
                y=yf-60
            elif diag==2:
                x=xf+70*wl-35
                y=yf+60
            
            
            #Need exception for if indexes for E/R dont exist for last hex
            if n+2<len(wname):
                #engine check
                if wname[n+2]=='E':
                    eng='True'
                    n+=1
                    if n+2<len(wname) and wname[n+2]=='R':
                        diag=int(wname[n+3])
                        n+=2
                #offlinear
                elif wname[n+2]=='R':
                    diag=int(wname[n+3])
                    eng='False'
                    n+=2
                else:
                    eng='False'
                    diag=0
            else:
                eng='False'
                diag=0
            
        #print(des,rot,eng,diag,x,y)
        
        hexdraw(x,y,des,rot,1,eng)
        #increase wagon length count to offset new hexes
        wl+=1
            
        n+=2
        if n>=len(wname):
            break
    

#=============================================================================
def VertToiRot(ls):
    #correct irot for partials only
    vslopes=[]
    des=ls[3]
    tol=.035
    
    if des=='F' or des=='FI' or des=='FIe' or des=='FMI' or des=='FO'\
        or des=='FOe' or des=='FM' or des=='FMe':
        pass
    else:
        #save slopes between vertices
        for v in range(0,int(ls[7])*2-1,2):
            #some pixels dont actually subtract to 0, so giving it space
            if math.isclose(0,(round(float(ls[8+v+2]))-round(float(ls[8+v]))),abs_tol=2.1):
                if round(float(ls[8+v+3]))>round(float(ls[8+v+1])):
                    vs=float('inf')
                elif round(float(ls[8+v+3]))<round(float(ls[8+v+1])):
                      vs=float('-inf')
            else:
                vs=(round(float(ls[8+v+3]))-round(float(ls[8+v+1])))/\
                    (round(float(ls[8+v+2]))-round(float(ls[8+v])))
                vs=round(vs,2)
            vslopes.append(vs)
        
        #print('orot',ls[6])
        #evaluate irot value from slopes for each shape
        #using figure 13 from the baseline report 1/20 as a standard for irot values
        if des=='aIe' or des=='aOe' or des=='aM' or des=='aOe' or des=='aMe':
            if math.isclose(0.58,vslopes[0],abs_tol=tol):
                if vslopes[3]==float('inf'):
                    ls[6]=0
                elif vslopes[3]==float('-inf'):
                    ls[6]=3
            elif math.isclose(-0.58,vslopes[0],abs_tol=tol):
                if vslopes[1]==float('inf'):
                    ls[6]=2
                elif vslopes[1]==float('-inf'):
                    ls[6]=5
            elif vslopes[0]==float('-inf'):
                ls[6]=1
            elif vslopes[0]==float('inf'):
                ls[6]=4
        elif des=='bI' or des=='bIe' or des=='bMe' or des=='bOe':
            if vslopes[0]==0.0:
                if vslopes[1]==float('-inf'):
                    ls[6]=0
                elif vslopes[1]==float('inf'):
                    ls[6]=3
            elif math.isclose(1.74,vslopes[0],abs_tol=tol):
                if vslopes[3]==float('inf'):
                    ls[6]=1
                elif vslopes[3]==float('-inf'):
                    ls[6]=4
            elif math.isclose(-1.74,vslopes[0],abs_tol=tol):
                if vslopes[2]==float('inf'):
                    ls[6]=2
                elif vslopes[2]==float('-inf'):
                    ls[6]=5
        elif des=='cOe':
            if vslopes[0]==-0.0:
                ls[6]=3
            #python doesn't actually differentiate the -0 and 0, so this doesn't trigger
            #i fixed it for b's, but c's slopes for 0 and 3 are the same, no way to differentiate
            #but at least rotation 0 is never used in the drawings.
            #some method to differentiate will be needed in future if it gets used
            elif vslopes[0]==0.0:
                ls[6]=0
            elif math.isclose(1.74,vslopes[0],abs_tol=tol):
                if vslopes[2]==float('inf'):
                    ls[6]=4
                elif vslopes[2]==float('-inf'):
                    ls[6]=1
            elif math.isclose(-1.74,vslopes[0],abs_tol=tol):
                if vslopes[1]==float('inf'):
                    ls[6]=5
                elif vslopes[1]==float('-inf'):
                    ls[6]=2
        elif des=='dIe' or des=='dOe':
            if vslopes[0]==float('inf'):
                ls[6]=0
            elif vslopes[0]==float('-inf'):
                ls[6]=3
            elif math.isclose(0.58,vslopes[0],abs_tol=tol):
                if vslopes[3]==float('inf'):
                    ls[6]=2
                elif vslopes[3]==float('-inf'):
                    ls[6]=5
            elif math.isclose(-0.58,vslopes[0],abs_tol=tol):
                if vslopes[4]==float('inf'):
                    ls[6]=1
                elif vslopes[4]==float('-inf'):
                    ls[6]=4
        elif des=='gIe':
            if vslopes[0]==float('inf'):
                ls[6]=0
            elif vslopes[0]==float('-inf'):
                ls[6]=3
            elif math.isclose(0.59,vslopes[0],abs_tol=tol):
                if vslopes[1]==float('inf'):
                    ls[6]=5
                elif vslopes[1]==float('-inf'):
                    ls[6]=2
            elif math.isclose(-0.59,vslopes[0],abs_tol=tol):
                if vslopes[2]==float('inf'):
                    ls[6]=4
                elif vslopes[2]==float('-inf'):
                    ls[6]=1
        
    #if vslopes!=[]:
    #    print(des,ls[6],vslopes)
    
    
    
    #des=ls[3]
    
    #if des=='aIe' or des=='aOe' or des=='aM' or des=='aOe' or des=='aMe':
        
        
    
    
    return ls
#=============================================================================
#=============================================================================
#=========================Main Program========================================
#=============================================================================
#=============================================================================

#cd C:\Users\ikerz\OneDrive\Documents\College\2021 Spring\CMS

filepath = 'geometry.hgcal_NS_210505_142458.txt'

file=open(filepath)
data=file.readlines()
header=data[0]

sumwagons=[]

#Full range 1-51
layerstart=36
layerend=37

#for testing, show me MB# data, for 2 print loops below
showme=30

for l in range(layerstart,layerend,1):


    #trying to draw the hexagons based on 
    xmax=2000
    ymax=2000
    xoff=850
    yoff=100
    #radius
    r=55
    #board drawing or wagon drawing
    bow=0
    #Set new image
    im1=Image.new('RGB',(xmax,ymax),(128,128,128))
    draw=ImageDraw.Draw(im1)
    
    #input
    layer=str(l)
    MBlist=[]
    MBCount=0
    
    
    
    #DrawLayer and create a data set
    for i in data:
        ls=i.strip().split(' ')        
        
        if ls[0]==layer:
            #Need a temporary function to read vertice information and correct irot values
            #since as of 5/9/21 irot values are arbitrary in source data
            ls=VertToiRot(ls)
            
            #Drawing Layer
            x=ls[1]
            y=ls[2]
            cx=float(x)*100+xoff-float(y)*50
            cy=ymax-(float(y)*90+yoff)
            hexdraw(cx,cy,ls[3],ls[6],ls[31],ls[32])
            font = ImageFont.truetype('arial.ttf', 20) 
            #Label Hexes with shape designation and (u,v) location
            #txt=ls[3]+'\n('+ls[1]+','+ls[2]+')'
            #Label Hexes with trigger and daq counts and (u,v) location
            if ls[37]=='0':
                dc=float(ls[27])
            elif ls[37]=='1':
                dc=float(ls[29])
            txt=str(int(math.trunc(float(ls[25]))))+'T'+str(int(math.trunc(dc)))+'D'+\
                '\n('+ls[1]+','+ls[2]+')'
            
            #hex labels black for ld, white for hd
            if ls[37]=='0':
                draw.text((cx-23,cy-20),str(txt), fill=(0,0,0),font=font)
            elif ls[37]=='1':
                draw.text((cx-23,cy-20),str(txt), fill=(255,255,255),font=font)
            
            
            #Saving Motherboard hexes, ignoring triangles
            if ls[3]!='cOe':
                    #u,v,itype,irot,triglinks,datalinksLD,datalinksHD,isEngine,HDorLD,u,v,MB
                    MBlist.append([int(ls[0]),int(ls[1]),int(ls[2]),ls[3],int(ls[6]),int(float(ls[25])),\
                           int(float(ls[27])),int(float(ls[29])),ls[32],int(ls[37]),\
                           int(ls[1]),int(ls[2]),int(ls[31])])
            #Total MB count for layer
            if int(ls[31]) > MBCount:
                MBCount=int(ls[31])
    
    MBCount+=1
    
    #Going to try and rework identifying wagons better
    wagons=[]
    
    
    missingMB=0
    
    for m in range(0,MBCount,1):
        MB=[]
        for line in MBlist:
            if line[12]==m:
                MB.append(line)
        
        #some MB have out of order hexes.  Sort by 2 indexes!
        MB.sort(key=lambda i:(i[1],i[2]))
        #Move to origin
        ToOrigin(MB)
    
    
        if m==showme:
            for index in range(0,len(MB),1):
                print(MB[index])
    
        #Change B irot to F with engine irot value.  Moved here from rotation function
        #so that it corrects before splitting and then there's no engine to check.
        #this will permanently change the irot value in processed data, beware!
        erot=0
    
        for line in MB:
            if line[8]=='True':
                erot=line[4]
                #fix for negative rots
                if erot==-1:
                    erot=5
                elif erot==-2:
                    erot=4
                elif erot==-3:
                    erot=3
                elif erot==-4:
                    erot=2
                elif erot==-5:
                    erot=1
        for line in MB:
            if line[3]=='bOe' or line[3]=='bIe' or line[3]=='bMe':
                line[4]=erot
    
        #Separating function
        #first takes care of exceptions when there's missing MB numbers in data file
        if MB==[]:
            #print('MB ' + str(m) + ' is missing')
            missingMB+=1
        
        #HD Modules
        elif MB[0][9]==1:
            
            HDs=[]
            
            MB,HDs=Rotate(MB)
            
            if m==showme:
                print(HDs)
                for line in MB:
                    print(line)
            
            #Categorizing HD Wagons
            wagons.append([wname(MB,HDs),MB])   
        
            
        #LD Modules
        elif MB[0][9]==0:
           
            if m==showme:
                print(Slope(MB))
            
            #only need to rotate if engine piece is not irot 0
            #the whole rotation function could be improved by not making it work off slopes
            #and instead work off eng rotation value
            engrot=0
            junk=''
            for hx in MB:
                if hx[8]=='True':
                    engrot=hx[4]
            if engrot!=0:
                MB,junk=Rotate(MB)
                MB.sort(key=lambda i:(i[1],i[2]))
            if m==showme:
                print(junk)
            
            #Split Wagons before evaluating
            L=[]
            R=[]
            switch=0
            diag=[]
            h=0
            
            Rs=[]
            Ls=[]
    
            #Divides MBs into L and R wagon shapes
            for hx in MB:
                if switch==0:
                    L.append(hx)
                    h+=1
                    if hx[8]=='True':
                        switch=1
                        if h<3:
                            hxe=hx
                            #Check diagonal connections to engine hex for weird shapes
                            #changed the if statement to prioritize R4/R3 hexes first for addition to L
                            #save up to 3 hx in L before stopping
                            for hx in MB:
                                #ignore if hx is already part of L wagon, to prevent duping
                                if any(list == hx for list in L):
                                    continue
                                elif (hx[1]==hxe[1] and hx[2]==hxe[2]+1):
                                    diag.append(hx)
                                    L.append(hx)
                                    h+=1
                                    if h>2:                                
                                        break
                                elif (hx[1]==hxe[1]-1 and hx[2]==hxe[2]-1):
                                    diag.append(hx)
                                    L.append(hx)
                                    h+=1
                                    if h>2:                                
                                        break
                                elif (hx[1]==hxe[1]+1 and hx[2]==hxe[2]+1):
                                    diag.append(hx)
                                    L.append(hx)
                                    h+=1
                                    if h>2:                                
                                        break
                                    else:
                                    #check for unusual 3 long pieces starting from engine hex
                                    #on early layers these wagon groups look like triangles with 6hexes
                                    #this check might need to be added to the next elif statement below
                                        for hx in MB:
                                            if any(list == hx for list in L):
                                                continue
                                            elif (hx[1]==hxe[1]+2 and hx[2]==hxe[2]+2):
                                                diag.append(hx)
                                                L.append(hx)
                                                h+=1
                                                if h>2:                                
                                                    break
                                elif (hx[1]==hxe[1] and hx[2]==hxe[2]-1):
                                    diag.append(hx)
                                    L.append(hx)
                                    h+=1
                                    if h>2:                                
                                        break
                                    else:
                                        for hx in MB:
                                            if any(list == hx for list in L):
                                                continue
                                            elif (hx[1]==hxe[1] and hx[2]==hxe[2]-2):
                                                diag.append(hx)
                                                L.append(hx)
                                                h+=1
                                                if h>2:                                
                                                    break
                elif switch==1:
                    if hx not in diag:
                        R.append(hx)
                    
            
            
            
            if m==showme:
                print('\nLeft, slope: ',Ls, '  ')
                for index in range(0,len(L),1):
                    print(L[index])
                print('\nRight, slope:',Rs, '  ')
                for index in range(0,len(R),1):
                    print(R[index]) 
                print(h)
            
            #Realign wagons and save
            L,Ls=Rotate(L)
            wagons.append([wname(L,Ls),L])
            
            if R != []:    
                ToOrigin(R)
                R,Rs=Rotate(R)        
                wagons.append([wname(R,Rs),R])
            elif R == []:
                print('MB' + str(m) + ' was not split')
    
        
            if m==showme:
                print('\nLeft, slope: ',Ls, '  ', wname(L,Ls))
                for index in range(0,len(L),1):
                    print(L[index])
                print('\nRight, slope:',Rs, '  ', wname(R,Rs))
                for index in range(0,len(R),1):
                    print(R[index])            
        
        
        #print('MB:',m,shape, ', Length= ', len(MB), ' ', [d[2] for d in MB],\
         #         ', ', [d[3] for d in MB])
    
    
      
    #print list of wagons
    wtypes=[]
    #want list of wagon types
    for line in wagons:
        #print(line)
        wtypes.append(line[0])
        sumwagons.append(line[0])
    
    #sumwagons.append(wtypes)
    uniwtypes=set(wtypes)
    uniwtypes=sorted(uniwtypes)
    
    #print(set(uniwtypes))
    
    #Prints a list of all wagon names with types
    #I should add a text export list of Wagons/MBs etc.
    #for i in range(0,len(set(uniwtypes)),1):
    #    print(wtypes.count(uniwtypes[i]), '   ', str(uniwtypes[i]))
    
    #print(wagons[1])
    for i in wagons:
        print("MB", i[1][0][12],"-", i[0])
    
    
    
    
    #color isnt actually doing anything here...
    color=(0,155,0)
    r=40
    bow=1
    
    xth=30
    yth=100
    xhh=100
    yhh=120
    
    font = ImageFont.truetype('arial.ttf', 30) 
    
        
    
    #HD Wagon Drawings
    #text='HD Wagon Counts' + '\n=================='
    #draw.text((50,10),str(text), fill=(0,0,0),font=font)
    #text='LD Wagon Counts' + '\n==========================================================================='
    #draw.text((500,10),str(text), fill=(0,0,0),font=font)
    
    #counters
    i=0
    #maxcol=5
    col=0
    #maxrow=7,7,7,8
    row=0
    t=0

    
    for type in uniwtypes:
        if type[:2] =='HD':
            bow=3
        elif type[:2]=='LD':
            bow=1
            
        xth=30+400*col
        xhh=100+400*col
        if type[2]=='T' or (type[2]=='U' and int(type[3])>2):
            #t+=1
            row+=.6
        yth=50+90*row+70*t
        yhh=70+90*row+70*t
        
        draw.text((xth,yth),str(wtypes.count(type)), fill=(0,0,0),font=font)
        wagondraw(xhh,yhh,type)
        
        row+=1
            
        if row>=6.3:
            col+=1
            row=0
            t=0
            
        i+=1
    
   
    #show what's ungrouped
    print('\n')
    #for hx in LDU3[0][0]:
    #    print(hx)
    
    #Label Image
    title='Layer: ' + str(layer) \
        +'\nMotherboards: ' + str(MBCount - missingMB) \
        +'\nWagons: ' + str(len(wtypes))
    font = ImageFont.truetype('arial.ttf', 30) 
    draw.text((50,1800),str(title), fill=(0,0,0),font=font)
    
    #Legend for Hex Shapes
    bow=2
    r=40
    xt=30
    yt=1250
    xh=xt+70
    yh=yt+15
    draw.text((xt,yt-90),'irot=0, CCW', fill=(0,0,0),font=font)
    draw.text((xt,yt),'F', fill=(0,0,0),font=font)
    hexdraw(xh,yh,'FM',0,color,'False')
    draw.text((xt,yt+90),'a', fill=(0,0,0),font=font)
    hexdraw(xh,yh+90,'aOe',0,color,'False')
    draw.text((xt,yt+90*2),'b', fill=(0,0,0),font=font)
    hexdraw(xh,yh+90*2,'bOe',0,color,'False')
    draw.text((xt,yt+90*3),'c', fill=(0,0,0),font=font)
    hexdraw(xh,yh+90*3,'cOe',0,color,'False')
    draw.text((xt,yt+90*4),'d', fill=(0,0,0),font=font)
    hexdraw(xh,yh+90*4,'dOe',0,color,'False')
    draw.text((xt,yt+90*5),'g', fill=(0,0,0),font=font)
    hexdraw(xh,yh+90*5,'gIe',0,color,'False')
           
    
    #Color Legend for MBs
    #commented out because MB numbers were incorrectly going over 100 in data
    #and also I changed the color on HD MBs in drawing but not here yet, so that needs updating
    #bow=0
    #font = ImageFont.truetype('ariblk.ttf', 30) 
    #for i in range(0,MBCount,1):
    #    draw.text((300+45*i,1950),str(i), fill=MBColor(i,'F'),font=font)
    
    
    #Layer Image 
    savename='Layer ' + str(layer) + '.jpg'
    im1.save(savename,quality=95)
    #im1.show()
    
    print('Layer ' + str(layer) + ' processed.')



#Summary Reports
xmax=2000
ymax=2000
im2=Image.new('RGB',(xmax,ymax),(128,128,128))
draw=ImageDraw.Draw(im2)

#Wagon Images
uniwtypes=set(sumwagons)
uniwtypes=sorted(uniwtypes)

#Draw Summary
#counters
i=0
#maxcol=5
col=0
#maxrow=7,7,7,8
row=0
t=0
maxrows=20


for type in uniwtypes:
    if type[:2] =='HD':
        bow=3
    elif type[:2]=='LD':
        bow=1
        
    xth=15+400*col
    xhh=100+400*col
    if type[2]=='T' or (type[2]=='U' and int(type[3])>2):
        #t+=1
        row+=.6
    yth=50+90*row+70*t
    yhh=70+90*row+70*t
    
    font = ImageFont.truetype('arial.ttf', 30)
    draw.text((xth,yth),str(sumwagons.count(type)), fill=(0,0,0),font=font)
    wagondraw(xhh,yhh,type)
    
    row+=1
        
    if row>=maxrows:
        col+=1
        row=0
        t=0
        
    i+=1

#Label Image
title='Layer Range: ' + str(layerstart) + '-' + str(layerend-1) +\
      '\n# Wagon Types: ' + str(len(uniwtypes)) +\
      '\nTotal # Wagons: ' + str(len(sumwagons))
font = ImageFont.truetype('arial.ttf', 30) 
draw.text((1650,1850),str(title), fill=(0,0,0),font=font)

#print(set(uniwtypes))

#for i in range(0,len(set(uniwtypes)),1):
#    print(sumwagons.count(uniwtypes[i]), '   ', str(uniwtypes[i]))





im2.save('WagonSummary.jpg',quality=95)
#im2.show()
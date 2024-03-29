# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:53:46 2021

@author: Troilus D'Troy'
"""

from PIL import Image, ImageDraw, ImageFont

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
            #going to need to come back and define other cases when try to draw engines
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                          (cx,cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                             fill=MBColor(mb),outline=(0,0,0))
        #orientation
        draworfull(cx,cy,r,rot)            
        #draw engine
        if eng=='True' and rot==0:
            draw.polygon(((cx+.866*r,cy+r/4),(cx+.7*r,cy+r/4),(cx+.7*r,cy-r/4),\
                          (cx+.866*r,cy-r/4)),fill=(255,51,51),outline=(0,0,0))
        #looks a little off
        elif eng=='True' and rot==1:
            draw.polygon(((cx+r*.213,cy-r*.875),(cx+.663*r,cy-r*.613),(cx+.575*r,cy-r*.475),\
                          (cx+r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
        elif eng=='True' and rot==2:
            draw.polygon(((cx-r*.213,cy-r*.875),(cx-.663*r,cy-r*.613),(cx-.575*r,cy-r*.475),\
                          (cx-r*.125,cy-r*.737)),fill=(255,51,51),outline=(0,0,0))
    elif des=='aIe' or des=='aOe' or des=='aM' or des=='aOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r)),fill=MBColor(mb),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy+r),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==4:
            draw.polygon(((cx-.866*r,cy-r/2),(cx,cy-r),(cx+.866*r,cy-r/2),\
                      (cx+.866*r,cy+r/2)),fill=MBColor(mb),outline=(0,0,0))
            #the 2nd coord is still wrong a bit
            draw.polygon(((cx+.866*r,cy+r/2),(cx+r*.70,cy+.4*r),(cx+.866*r,cy)),\
                         fill=(0,0,0),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2)),fill=MBColor(mb),outline=(0,0,0))
    elif des=='bI' or des=='bIe' or des=='bMe' or des=='bOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy-r/2)),\
                          fill=MBColor(mb),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx,cy-r),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb),outline=(0,0,0))
            draw.polygon(((cx,cy+r),(cx-.433*r,cy+3/4*r),(cx+.433*r,cy+3/4*r)),\
                             fill=(0,0,0),outline=(0,0,0))
        elif rot==4:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r),\
                      (cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                          fill=MBColor(mb),outline=(0,0,0))
    elif des=='cOe':
        if rot==0:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2)),\
                         fill=MBColor(mb),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(mb),outline=(0,0,0))
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                         fill=MBColor(mb),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx+.866*r,cy+r/2),(cx+.866*r,cy-r/2),(cx,cy-r)),\
                         fill=MBColor(mb),outline=(0,0,0))
        elif rot==5:
            draw.polygon(((cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),(cx,cy-r)),\
                         fill=MBColor(mb),outline=(0,0,0))
    elif des=='dIe' or des=='dOe':
        if rot==0 or rot==6:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy-r/2),\
                      (cx-.433*r,cy-3/4*r),(cx+.433*r,cy+3/4*r)),\
                     fill=MBColor(mb),outline=(0,0,0))
        elif rot==1:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      (cx+.866*r,cy),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2),(cx+.433*r,cy+3/4*r),\
                      (cx-.433*r,cy-3/4*r),(cx,cy-r)),\
                     fill=MBColor(mb),outline=(0,0,0))
    elif des=='gIe':
        if rot==0 or rot==6:
            draw.polygon(((cx,cy+r),(cx-r/2,cy+r*.71),(cx-r/2,cy-r*.71),\
                      (cx,cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb),outline=(0,0,0))        
        elif rot==2:
            draw.polygon(((cx,cy+r),(cx-.866*r,cy+r/2),(cx-.866*r,cy),\
                      ((cx+r/2),cy-.866*r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb),outline=(0,0,0))
        elif rot==3:
            draw.polygon(((cx,cy+r),(cx-r/2,cy+3/4*r),(cx-r/2,cy-3/4*r),\
                      ((cx),cy-r),(cx+.866*r,cy-r/2),(cx+.866*r,cy+r/2)),\
                     fill=MBColor(mb),outline=(0,0,0))
        #orientation
        draworfull(cx,cy,r,rot)

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
def MBColor(MB):
    colors=[(153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224),\
             (153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224),\
                (153,255,255),(255,153,153),(153,204,255),(255,204,153),\
            (153,153,255),(255,255,153),(204,153,255),(204,255,153),(204,102,0),\
            (255,153,255),(153,255,153),(255,153,204),(153,255,204),(224,224,224)]
    if bow==0:
        pick=colors[int(MB)]
    elif bow==1:
        pick=(0,155,0)
    elif bow==2:
        pick=(220,220,220)
    return pick
#=============================================================================
#Repositioning Wagon for evaluation

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


#Rotate to be flat

def Rotate(wagon):
    #categorize based off slope. 
    #determine slopes
    
    slope=[]
    
    i=0
    for i in range(0,len(wagon)-1,1):
        if (wagon[i+1][1]-wagon[i][1])==0:
            s=float('inf')
        else:
            s=(wagon[i+1][2]-wagon[i][2])/(wagon[i+1][1]-wagon[i][1])
        slope.append(s)
    
    #if slope is 45deg, rotates it flat and updates slope variable
    if len(set(slope))==1 and slope[0]==1.0:
        for i in range(0,len(wagon),1):
            wagon[i][2]=0
        for i in range(0,len(wagon)-1,1):
            slope[i]=0
    #if slope is vertical, rotates 90 and update slope
    elif len(set(slope))==1 and slope[0]==float('inf'):
        for i in range(0,len(wagon),1):
            wagon[i][1]=wagon[i][2]
            wagon[i][2]=0
        for i in range(0,len(wagon)-1,1):
            slope[i]=0  
    
    return wagon,slope

#=============================================================================
#LD Assignments

def LDAssign(MB,slope):
        #linear length 1
        if len(set(slope))==0 and slope==[] and len(MB)==1:
            if MB[0][8]=='True':
                LDL1E.append(MB)
            elif MB[0][8]=='False':
                LDL1.append(MB)
        #Linear length 2
        elif len(set(slope))==1 and slope[0]==0 and len(MB)==2:
            if MB[1][8]=='True':
                LDL2E.append(MB)
            elif MB[1][8]=='False':
                if MB[1][3]=='FOe' or MB[1][3]=='FO' or MB[1][3]=='bOe':
                    LDL2.append(MB)
                elif MB[1][3]=='aOe':
                    LDL2a.append(MB)
        #linear length 3
        elif len(set(slope))==1 and slope[0]==0 and len(MB)==3:
            if MB[2][8]=='True':
                LDL3E.append(MB)
            elif MB[2][8]=='False':
                if MB[2][3]=='FOe' or MB[2][3]=='FO' or MB[2][3]=='bOe':
                    LDL3.append(MB)
                elif MB[2][3]=='dOe':
                    LDL3d.append(MB)
                elif MB[2][3]=='aOe':
                    LDL3a.append(MB)
        #length 3, NE bend
        elif slope==[0.0,1.0] and (MB[0][3]=='FO' or MB[0][3]=='FM')\
            and (MB[1][3]=='FO' or MB[1][3]=='FM')\
            and (MB[2][3]=='FOe'):
            if MB[1][8]=='True':
                LD3R1FE.append(MB)
            else:
                LDU3.append(MB)
        #linear length 4
        elif len(set(slope))==1 and slope[0]==0 and len(MB)==4:
            LDL4.append([MB])
        #linear length 5
        elif len(set(slope))==1 and slope[0]==0 and len(MB)==5:
            LDL5.append([MB])    
        #linear length 6
        elif len(set(slope))==1 and slope[0]==0 and len(MB)==6:
            LDL6.append([MB]) 
        #Triangles
        #F1a5F1 
        elif len(set(slope))==2 and slope==[0.0,float('inf')]:
            if ((MB[0][3]=='FO' or MB[0][3]=='FM' or MB[0][3]=='bOe') and MB[0][4]==1)\
                and (MB[1][3]==('aOe') and MB[1][4]==5)\
                and (MB[2][3]=='FO' or MB[2][3]=='FM' or MB[2][3]=='bOe') and MB[2][4]==1:
               LDT3F1a5F1.append([MB])
            elif ((MB[0][3]=='FO' or MB[0][3]=='FM' or MB[0][3]=='bOe') and MB[0][4]==0)\
                and (MB[1][3]==('bOe') and MB[1][4]==1)\
                and (MB[2][3]=='aOe' ) and MB[2][4]==2:
               LDT3F0b1a2.append([MB])
            else:
                LDU3.append([MB])
        #Unknowns
        elif len(MB)==2:
            LDU2.append([MB])
        elif len(MB)==3:
            LDU3.append([MB])
        elif len(MB)==4:
            LDU4.append([MB])
        elif len(MB)==5:
            LDU5.append([MB])
        elif len(MB)==6:
            LDU6.append([MB])
        else:
            LDEr.append([MB])
    #sorting was messing up figuring out an unknown, but sort actually made
    #a rotated triangle sort into correct T3 group, now it goes into U3
    #Need if for triangles, then can use sort to group?
    #slope.sort() 

#=============================================================================

filepath = 'geometry.hgcal.txt'

file=open(filepath)
data=file.readlines()
header=data[0]


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
layer=str(34)
MBlist=[]
MBCount=0


#DrawLayer and create a data set
for i in data:
    ls=i.strip().split(' ')
    if ls[0]==layer:
        #Drawing Layer
        x=ls[1]
        y=ls[2]
        cx=float(x)*100+xoff-float(y)*50
        cy=ymax-(float(y)*90+yoff)
        hexdraw(cx,cy,ls[3],ls[6],ls[31],ls[32])
        font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20) 
        txt=ls[3]+'\n('+ls[1]+','+ls[2]+')'
        draw.text((cx-18,cy-20),str(txt), fill=(0,0,0),font=font)
        
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

#for testing, show me MB# data, for 2 print loops below
showme=29


#Lists for all different shapes of wagons
#high density wagon lists
#Linear
HDL1=[]
HDL2=[]
HDL3FFF=[]
HDL3aFF=[]
#Triangle
HDT3111E=[]
HDT3121E=[]
#Unknown Catchalls
HDU1=[]
HDU2=[]
HDU3=[]
HDEr=[]
#Wide variety of 2+pieces.  Actually need to go back and create ifs in the len3 section

#low density wagon lists
#Linear
LDL1=[]
LDL1E=[]
LDL2=[]
LDL2a=[]
LDL2E=[]
LDL3=[]
LDL3a=[]
LDL3d=[]
LDL3E=[]
LD3R1FE=[]
LDL4=[]
LDL5=[]
LDL6=[]
#Triangle
LDT3=[]
LDT3F1a5F1=[]
LDT3F0b1a2=[]
#Unknown Catchalls
LDU1=[]
LDU2=[]
LDU3=[]
LDU4=[]
LDU5=[]
LDU6=[]
LDEr=[]

missingMB=0

for m in range(0,MBCount,1):
    MB=[]
    for line in MBlist:
        if line[12]==m:
            MB.append(line)
    
    #some MB have out of order hexes.  Sort by 2 indexes!
    MB.sort(key=lambda i:(i[1],i[2]))
    #Move to origin
    MB=ToOrigin(MB)


    if m==showme:
        for index in range(0,len(MB),1):
            print(MB[index])

    
    #Separating function
    #first takes care of exceptions when there's missing MB numbers in data file
    if MB==[]:
        print('MB ' + str(m) + ' is missing')
        missingMB+=1
    
    #HD Modules
    elif MB[0][9]==1:
        
        HDs=[]
        
        MB,HDs=Rotate(MB)
    
       
        #Categorizing HD Wagons
        #linear length 1
        if len(set(HDs))==1 and HDs[0]==0 and len(MB)==1:
            HDL1.append()
        #Linear length 2
        elif len(set(HDs))==1 and HDs[0]==0 and len(MB)==2:
            HDL2.append()
        #linear length 3
        elif len(set(HDs))==1 and HDs[0]==0 and len(MB)==3:
            #edge check, since these are HD only the first hex may not be F
            if MB[0][3]=='FIe' or MB[0][3]=='bIe':
                HDL3FFF.append([MB])
            elif MB[0][3]=='aIe':
                HDL3aFF.append([MB])
        #Triangles
        #This catches triangles on layer 34, but not really all varieties
        #Will come back to this after I do LD triangles
        elif len(set(HDs))==2 and HDs==[0.0,float('inf')]:
            HDT3111E.append([MB])
        elif len(set(HDs))==2 and HDs==[float('inf'),0.0]:
            HDT3121E.append([MB])
        #Unknowns
        elif len(MB)==2:
            HDU2.append([MB])
        elif len(MB)==3:
            HDU3.append([MB])
        else:
            HDEr.append([MB])
        
    #LD Modules
    elif MB[0][9]==0:
 
        #Split Wagons before evaluating
        
        L=[]
        R=[]
        switch=0
        diag=0
        h=0
        
        Rs=[]
        Ls=[]
        
        MB,junk=Rotate(MB)
        
        for hx in MB:
            if switch==0:
                L.append(hx)
                h+=1
                if hx[8]=='True':
                    switch=1
                    hxe=hx
                    #Check diagonal connections to engine hex for weird shapes
                    for hx in MB:
                        if (hx[1]==hxe[1]+1 and hx[2]==hxe[2]+1)\
                            or (hx[1]==hxe[1] and hx[2]==hxe[2]-1)\
                            or (hx[1]==hxe[1]-1 and hx[2]==hxe[2]-1)\
                            or (hx[1]==hxe[1] and hx[2]==hxe[2]+1):
                            diag=hx
                            L.append(hx)
            elif switch==1:
                if hx !=diag:
                    R.append(hx)
         
        if m==showme:
            #print('Left, ',L)
            #print('Right, ',R)
            print(h)
        
        L,Ls=Rotate(L)
        R,Rs=Rotate(R)
           
        LDAssign(L,Ls)
        LDAssign(R,Rs)        
  
    
        if m==showme:
            print('\nLeft, slope: ',Ls)
            print(len(Ls), len(set(Ls)))
            for index in range(0,len(L),1):
                print(L[index])
            print('\nRight, slope:',Rs)
            for index in range(0,len(R),1):
                print(R[index])            
    
    
    #print('MB:',m,shape, ', Length= ', len(MB), ' ', [d[2] for d in MB],\
     #         ', ', [d[3] for d in MB])

#color isnt actually doing anything here...
color=(0,155,0)
r=40
bow=1

xth=30
yth=100
xhh=100
yhh=120

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30) 

#come back and turn this draw section into a better function with ifs and fors

#HD Wagon Drawings
text='HD Wagon Counts' + '\n======================'
draw.text((50,10),str(text), fill=(0,0,0),font=font)
#L1
draw.text((xth,yth),str(len(HDL1)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh,'FM',0,color,'True')
#L2
draw.text((xth,yth+90),str(len(HDL2)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90,'FM',0,color,'True')
#L3FFF
draw.text((xth,yth+90*2),str(len(HDL3FFF)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*2,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90*2,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*2,'FM',0,color,'True')
#L3aFF
draw.text((xth,yth+90*3),str(len(HDL3aFF)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*3,'aIe',3,color,'False')
hexdraw(xhh+70,yhh+90*3,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*3,'FM',0,color,'True')
#T3111E
draw.text((xth,yth+90*4.5),str(len(HDT3111E)), fill=(0,0,0),font=font)
hexdraw(xhh+70*.5,yhh+90*4,'FI',1,color,'True')
hexdraw(xhh,yhh+90*4+60,'FI',1,color,'False')
hexdraw(xhh+70,yhh+90*4+60,'FI',1,color,'False')
#T3121E
draw.text((xth+200,yth+90*4.5),str(len(HDT3121E)), fill=(0,0,0),font=font)
hexdraw(xhh+70*.5+200,yhh+90*4,'FI',1,color,'False')
hexdraw(xhh+200,yhh+90*4+60,'FI',0,color,'False')
hexdraw(xhh+70+200,yhh+90*4+60,'FI',0,color,'True')


#LD Wagon Drawings
xth=530
yth=100
xhh=600
yhh=120

text='LD Wagon Counts' + '\n====================================================================='
draw.text((500,10),str(text), fill=(0,0,0),font=font)

#Column 1, With Engines
#L1
draw.text((xth,yth),str(len(LDL1E)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh,'FM',0,color,'True')
#L2
draw.text((xth,yth+90),str(len(LDL2E)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90,'FM',0,color,'True')
#L3
draw.text((xth,yth+90*2),str(len(LDL3E)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*2,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90*2,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*2,'FM',0,color,'True')

#Column 2, Without Engines
xth=880
yth=100
xhh=950
yhh=120
#L1
draw.text((xth,yth),str(len(LDL1)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh,'FM',0,color,'False')
#L2
draw.text((xth,yth+90),str(len(LDL2)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90,'FM',0,color,'False')
#L3
ym=2
draw.text((xth,yth+90*ym),str(len(LDL3)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*ym,'FM',0,color,'False')
#L3a
ym=3
draw.text((xth,yth+90*ym),str(len(LDL3a)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*ym,'aOe',0,color,'False')
#L3d
ym=4
draw.text((xth,yth+90*ym),str(len(LDL3d)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90*ym,'FM',0,color,'False')
hexdraw(xhh+70*2,yhh+90*ym,'dOe',0,color,'False')

#Column 3
xth=1230
yth=100
xhh=1300
yhh=120
#L1a
draw.text((xth,yth+90),str(len(LDL2)), fill=(0,0,0),font=font)
hexdraw(xhh,yhh+90,'FM',0,color,'False')
hexdraw(xhh+70,yhh+90,'aOe',0,color,'False')
#LD3R1F
draw.text((xth,yth+90*2.5),str(len(LD3R1FE)), fill=(0,0,0),font=font)
hexdraw(xhh+3*70*.5,yhh+90*2,'FI',0,color,'False')
hexdraw(xhh,yhh+90*2+60,'FI',0,color,'False')
hexdraw(xhh+70,yhh+90*2+60,'FI',0,color,'True')


#Column 4
xth=1580
yth=100
xhh=1650
yhh=120
#LDT3F1a5F1
draw.text((xth,yth+45),str(len(LDT3F1a5F1)), fill=(0,0,0),font=font)
hexdraw(xhh+70*.5,yhh,'bOe',1,color,'False')
hexdraw(xhh,yhh+60,'FO',1,color,'False')
hexdraw(xhh+70,yhh+60,'aOe',5,color,'False')
#LDT3F0b1a2
draw.text((xth,yth*2.25+60),str(len(LDT3F0b1a2)), fill=(0,0,0),font=font)
hexdraw(xhh+70*.5,yhh*2.25,'aOe',2,color,'False')
hexdraw(xhh,yhh*2.25+60,'FO',0,color,'False')
hexdraw(xhh+70,yhh*2.25+60,'bOe',1,color,'False')



sumwag=len(HDL1)+len(HDL2)+len(HDL3FFF)+len(HDL3aFF)+len(HDT3111E)+len(HDT3121E)\
      +len(HDU1)+len(HDU2)+len(HDU3)+len(HDEr)\
      +len(LDL1)+len(LDL1E)+len(LDL2)+len(LDL2E)+len(LDL2a)+len(LDL3)+len(LDL3E)\
      +len(LDL3a)+len(LDL3d)+len(LD3R1FE)\
      +len(LDL4)+len(LDL5)+len(LDL6)+len(LDT3F1a5F1)+len(LDT3F0b1a2)+len(LDU1)\
      +len(LDU2)+len(LDU3)+len(LDU4)+len(LDU5)+len(LDU6)+len(LDEr)

print('\n    Total Counts')
print('L1: ',len(HDL1),'HD   ',len(LDL1),', ',len(LDL1E),'E',' LD')
print('L2: ',len(HDL2),'HD   ',len(LDL2),', ',len(LDL2a),', ',len(LDL2E),'E',' LD')
print('L3: ',len(HDL3FFF),'FFF, ',len(HDL3aFF),'aFF ','HD   ',len(LDL3),', ',len(LDL3E),'E',len(LD3R1FE),'R1F ',' LD')
print('L4:         ',len(LDL4),'LD')
print('L5:         ',len(LDL5),'LD')
print('L6:         ',len(LDL6),'LD')
print('T3: ',len(HDT3111E), ',', len(HDT3121E),'HD   ',\
      len(LDT3F1a5F1),', ', len(LDT3F0b1a2),'LD')
print('U1: ',len(HDU1),'HD   ',len(LDU1),'LD')
print('U2: ',len(HDU2),'HD   ',len(LDU2),'LD')
print('U3: ',len(HDU3),'HD   ',len(LDU3),'LD')
print('U4:         ',len(LDU4),'LD')
print('U5:         ',len(LDU5),'LD')
print('U6:         ',len(LDU6),'LD')
print('Er: ',len(HDEr),'HD   ',len(LDEr),'LD')
print(sumwag,' wagons  ', MBCount-missingMB,'MBs')

#show what's ungrouped
print('\n')
#for hx in LDU3[0][0]:
#    print(hx)

#Label Image
title='Layer: ' + str(layer) \
    +'\nMotherboards: ' + str(MBCount - missingMB) \
    +'\nWagons: ' + str(sumwag)
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30) 
draw.text((50,1800),str(title), fill=(0,0,0),font=font)

#Legend for Hex Shapes
bow=2
r=40
xt=30
yt=1250
xh=xt+70
yh=yt+15
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
       
#Layer Image 
savename='Layer ' + str(layer) + '.jpg'
im1.save(savename,quality=95)
im1.show()

#Drawing to test hex shapes
#im2=Image.new('RGB',(xmax,ymax),(128,128,128))
#draw=ImageDraw.Draw(im2)

#Wagon Images
#im2.save('imagetest2.jpg',quality=95)
#im2.show()
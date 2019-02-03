from visual import *

#myscreen=display( title="my environment")
myscreen.width=800
myscreen.height=800

myscreen.autoscale=False #no autoscale is done by python
myscreen.range=(40,36,36 ) #scaling of my working area
myscreen.background=color.gray(5)

            #label
#myintro=text( pos=(0,18,0) ,height=4,text='my world' , align='center' ,depth=-.3 ,material=materials.earth)

 
            #MAKING MY CENTER FOR REFERENCE

mycentre=sphere(color=color.green , radius=.3 ,pos =(0,3,0))


            #MAKING MY TERRAIN

land=box(length=36 , width=36 , height=.75 , pos=(0,0,0) )
            #land.material=materials.earth
land.color=(1,1,0.750)


            #ULTRASONIC SENSOR MODELLING

box_ultra_end=box( material=materials.earth ,length=.25 , width=10 , height=5 , pos=(-20.9,4.65,0) )


tube_ultra2=cylinder(material=materials.earth , pos=(-20.9,4.65,-2.5 ) , radius=1.5 ,length=2.5)

tube_ultra3=cylinder( material=materials.earth, pos=(-20.9,4.65,2.5 ) , radius=1.5 ,length=2.5)


            #COLOR SENSOR MODELLING

box_color_end= box(length=.25 , width=10 ,height =5 ,pos=(-20.9,10,0), material=materials.earth)


led1=sphere(material=materials.emissive, radius=.6 , pos=(-20.3 , 11 , 2.5))
led2=sphere(material=materials.emissive, radius=.6 , pos=(-20.3 , 11, -2.5))


led3=sphere(material=materials.emissive, radius=.6 , pos=(-20.3 , 8.2 , 2.5))
led4=sphere(material=materials.emissive, radius=.6 , pos=(-20.3 , 8.2, -2.5))


            #servo motor modeling

servo_box=box(length=3.8,width=4.8,height=3.9,pos=(-23,1.2,0),color=(20,20,255))
servo_handle=box(length=2,width=.7,height=.65,pos=(-22.2,3.8,0),color=(255,255,255))


            #MAKING CROPS

myland_crops=box(length=36, width= 35,height=.8 ,pos=(0,0,0),color=color.green)

            # MAKING BARS USING HELIX
"""bar=helix(pos=(7.5,2,-18), axis=(0,0,18) , radius=1.7,length=36,thickness=.5,coils=10)
bar.material=materials.marble"""

            #making borders of crops
            
outer_line=curve(pos=[(-18,0.3,-18),(-18,0.3,18),(18,.3,18),(18,.3,-18),(-18,0.3,-18)],material=materials.bricks,radius=.33,color=(1,1,255))

inner_h_line1=curve(pos=[(-11,.3,-3),(18,.3,-3)],radius=.33,material=materials.bricks)
inner_h_line2=curve(pos=[(-11,.3,6),(18,.3,6)], radius=.33,material=materials.bricks)
inner_h_line1=curve(pos=[(-18,.3,-3),(18,.3,-3)],radius=.33,material=materials.bricks)
inner_h_line2=curve(pos=[(-18,.3,6),(18,.3,6)], radius=.33,material=materials.bricks)
inner_h_line2=curve(pos=[(-18,.3,12),(18,.3,12)], radius=.33,material=materials.bricks)
inner_h_line2=curve(pos=[(-18,.3,-12),(18,.3,-12)], radius=.33,material=materials.bricks)

inner_v_line=curve(pos=[(-4,.3,-18),(-4,.3,18)],radius=.33,material=materials.bricks)
inner_v_line=curve(pos=[(-10,.3,-18),(-10,.3,18)],radius=.33,material=materials.bricks)
inner_v_line=curve(pos=[(-14,.3,-18),(-14,.3,18)],radius=.33,material=materials.bricks)
inner_v_line=curve(pos=[(0,.3,-18),(0,.3,18)],radius=.33,material=materials.bricks)
inner_v_line=curve(pos=[(6,.3,-18),(6,.3,18)],radius=.33,material=materials.bricks)
inner_v_line=curve(pos=[(12,.3,-18),(12,.3,18)],radius=.33,material=materials.bricks)



#making terrain for houses

house_terrain=box( pos=(-30,0,0),width=36,length=10,height=.75,material=materials.marble)
upper_gap=box(width=14,length=7.2,height=.75,pos=(-21.4,0,-11),material=materials.marble)
lower_gap=box(width=14,length=7.2,height=.75,pos=(-21.4,0,11),material=materials.marble)



            #making house

for x in range(5):
    house=box(length= 1.5,color=(255,0,0) ,width=1 ,height=1.3 ,pos=(-26,.6,x*4.4))
for x in range(4):
    if x==0:continue
    house=box(length= 1, width=1 ,height=1.7 ,pos=(-26,.8,-x*5.6))

for x in range(5):
    house=box(length= 1.5, width=2 ,height=2 ,pos=(-30,1,x*4))
for x in range(4):
    if x==0:continue
    house=box(length= 1, color=(255,0,0),width=1 ,height=1.8 ,pos=(-30,.8,-x*4))

for x in range(5):
    house=box(length= .775, width=1 ,color=(255,0,0),height=2.6 ,pos=(-34,1,x*2.7))
for x in range(4):
    if x==0:continue
    house=box(length= 1, width=2 ,height=1.6 ,pos=(-34,1,-x*4))

#making my cardboard paper

target_paper=box(length=.25,width=12 ,height=12 ,pos=(-16,8,0))
    



    



         










               


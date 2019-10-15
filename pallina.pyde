width=500
x=100
y=120
x2=1
y2=1
lrect=(width/2)-25
lrect2=(width/2)+25
def setup():
    size(500,440)
    background(0,0,255)
    stroke(0,255,0)
def draw():
    global x,y,x2,y2,lrect,lrect2
    background(255,255,255)
    ellipse(x,y,50,50)
    x+=2*(x2)
    y+=2*(y2)
    fill(255,0,140)
    if x>=width or x<0:
        x2*= -1
    rect(lrect,height-25,80,25)
    if y+25>height-25 and x>=lrect and x<=lrect+80 :
        y2*= -1
    rect(lrect2,0,80,25)
    if y<=40 and x>=lrect2 and x<=lrect2+80 :
        y2*= -1
        
def keyPressed():
    global lrect,lrect2
    if keyCode == RIGHT:
        print("right")
        lrect=lrect+25
        if lrect>=width-80:
            lrect=500-80
        
    if keyCode == LEFT:
        print("left")
        lrect=lrect-25
        if lrect<=0:
            lrect=0
    if key == "a" and lrect2>0:
        print("a")
        lrect2=lrect2-25
    
    if key == "d" and lrect2<=width-80:
        print("d")
        lrect2=lrect2+25

        
         
        

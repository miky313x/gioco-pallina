width=500
x=100
y=120
x2=1
y2=1
lrect=(width/2)-25
def setup():
    size(500,440)
    background(0,0,255)
    stroke(0,255,0)
def draw():
    global x,y,x2,y2,lrect
    background(255,255,255)
    ellipse(x,y,50,50)
    x+=2*(x2)
    y+=2*(y2)
    fill(255,0,140)
    if y<=0:
        y2*= -1
    if x>=width or x<0:
        x2*= -1
    rect(lrect,height-25,80,25)
    if y+25>height-25 and x>=lrect and x<=lrect+80 :
        y2*= -1
    if y>=height:
        print("game over")
        exit()
        
def keyPressed():
    global lrect
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

        
         
        

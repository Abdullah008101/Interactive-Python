# template for "Stopwatch: The Game"
import simplegui
import random
import time

# define global variables
ctr=a=b=c=d = 0
ctrstop=0
ctrwin=0
flag=True
        
    
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a,b,c,d,ctrwin
    d = t%10
    
    t /= 10
    a=0
    b=0
    c=0
    if t>0:
        c = t%10
        t=t/10
        if t>0:
            a = t/6
            b = t%6




# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global flag
    flag = True
def stop():
    global flag
    if flag==True:
        timer.stop()
        global ctrstop,d,ctrwin
        ctrstop += 1
        if d==0:
            ctrwin += 1
    flag = False
def reset():
    global ctr,ctrstop,ctrwin
    ctr = ctrstop = ctrwin = 0
    timer.stop()
def exit_timer():
    frame.stop()
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global ctr
    ctr += 1
    

# define draw handler
def draw_handler(canvas):
    global ctr, a,b,c,d, ctrwin, ctrstop
    format(ctr)
    canvas.draw_text(str(ctrwin)+"/"+str(ctrstop), (135,30), 30, "Red")
    
    canvas.draw_text(str(a)+":"+str(b)+str(c)+"."+str(d),(60,100),30,"Black")
    

    
# create frame
frame = simplegui.create_frame('Stop watch game', 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background('White')
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.add_button("Exit ",exit_timer,100)

# start frame
frame.start()

# Please remember to review the grading rubric

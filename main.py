import random
from tkinter import *
from sentences import writing_ideas


"""
what do we need?
1)a gui app,set up a display , a button for generating the prompt,start and restart buttons
2)input box to write down 
3)a timer that track user input, finish the process when nothing typed within 5 sec
4)a timer that track 5 mins and finish the proccess after that
5)give them the result if time reach to 5mins

"""
#CONSTANT
chance = 5
timer = None
t_timer = None
# count = 5
total_time_min = 5
total_time_sec = total_time_min * 60
#GUI CONFIG
window = Tk()
window.geometry("800x700")
window.config(bg="gray")
# window.config(padx=120,pady=70)
window.title("Deadly Writing App")

#__________________FUNCTIONS_______________
"""generating random prompt to start from that"""
def generate_prompt(event=None):

    random_prompt = random.choice(writing_ideas)
    text_input.delete("1.0", 'end-1c')
    text_input.insert(END,random_prompt)

def start_writing():
    timer_dead(chance)
    total_timer(total_time_sec)
    print("challange run")
    start_bt.config(command=nothing)
    """disable the generate button after start"""
    generate_bt.config(command=nothing)


"""a way to disable button"""
def nothing(event=None):
    pass

"""checking if any input recieved within 5 mins"""
def timer_dead(count):
    global timer,t_timer
    dead_time_Label.config(text=f"{count}")
    if count == 0:
        print("You Are Dead Now")
        timer_label.config(text=f"You loose")
        window.bind('<Key>', nothing)
        window.after_cancel(t_timer)
        text_input.delete("1.0", 'end-1c')

    else:

        timer = window.after(1000,timer_dead,count -1)

def key_pressed(event=None):
    global chance,timer
    window.after_cancel(timer)
    chance = 5
    timer_dead(chance)


def total_timer(count):
    global t_timer,timer
    r_in_min = count / 60
    r_in_sec_ = count % 60
    if r_in_sec_ == 0:
        r_in_sec_ = "00"
    elif r_in_sec_ < 10:
        r_in_sec_ = f"0{r_in_sec_}"

    timer_label.config(text=f"Time 0{int(r_in_min)}:{r_in_sec_}")
    t_timer = window.after(1000, total_timer, count - 1)
    if count == 0:
        window.after_cancel(t_timer)
        window.after(timer)
        print("done")
        timer_label.config(text=f"FINISHED,check your note and take a copy ..!")
        window.bind('<Key>', nothing)


def reset_function():
    global timer,t_timer,chance,total_time_sec
    text_input.delete("1.0", 'end-1c')
    try:
        window.after_cancel(timer)
        window.after_cancel(t_timer)
        timer_label.config(text=f"Time 05:00")
        dead_time_Label.config(text="5")
        chance = 5
        total_time_sec = 300
        start_bt.config(command=start_writing)
        window.bind('<Key>', key_pressed)
        generate_bt.config(command=generate_prompt)
    except:
        pass
#UI Configuration
"""Buttons"""
generate_bt = Button(text="Generate Prompt",command=generate_prompt,width=15,height=3,font=("Courier",10))
generate_bt.place(x=250,y=150)

"""it will act as a restart button after first run"""
start_bt = Button(text="Start Writing",command=start_writing,width=15,height=3,font=("Courier",10))
start_bt.place(x=450,y=150)

reset_bt = Button(text="Reset",command=reset_function,width=10,height=2,font=("Courier",10),bg="red")
reset_bt.place(x=370,y=220)
"""Labels"""

#describtion Label
desc_label = Label(text="Write within 5 mins and see what it`ll be,\nbut if you stop for 5 sec all progress will be lost ",font=("Courier",15),fg="black")
desc_label.place(x=95,y=70)

#main time Label

timer_label = Label(text=f"Time 05:00",font=("Courier",20),bg="gray",fg="orange")
timer_label.place(x=320,y=300)

#dead time Label

dead_time_Label = Label(text="5",font=("arial",45),bg="gray",fg="red")
dead_time_Label.place(x=380,y=600)


"""Input"""

text_input = Text(window, height=10, width=80)
text_input.focus_set()
text_input.place(x=87,y=400)




window.bind('<Key>', key_pressed)

window.mainloop()

import pgzrun
import random
import time

#variables for the game window
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag" , "battery" , "bottle" , "chips"]

game_over=False
game_completed=False
current_level=1
items=[]
animations=[]

def draw():
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("GAME OVER", "Try again")
    elif game_completed:
        display_message("YOU WON", "well done")
    else:
        for item in items:
            item.draw()

def display_message(heading, subheading):
    screen.draw.text(heading,fontsize=60,center=CENTER,color="white")
    screen.draw.text(subheading,fontsize=30,center=(CENTER_X,CENTER_Y+40),color="white")

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)
    schedule_timer()

def make_items(number_of_extra_items):
    items_to_create=get_options_to_create(number_of_extra_items)
    new_items=create_image(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_options_to_create(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_image(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x=(index+1)*gap_size
        item.x=new_x

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration=START_SPEED-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def on_mouse_down(pos):
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else: 
                handle_game_over()

def handle_game_complete():
    global current_level,items,animations,game_completed
    #stop_animations(animations)
    if current_level ==FINAL_LEVEL:
        game_completed=True
    else:
        current_level=current_level+1
        items=[]
        animations=[]

def handle_game_over():
    global game_over
    game_over=True

def stop_animations(animations):
    for animation in animations:
        if animation.running:
            animation.stop()

def schedule_timer():
    clock.schedule_unique(handle_game_over, 3.0)








    























pgzrun.go()
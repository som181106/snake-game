import tkinter as tk
import random

ROWS = 25
COLS = 25
TILE_SIZE=25

WINDOW_WIDTH = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE

class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
window=tk.Tk()
window.title("Snake Game by THE SOM")

canvas= tk.Canvas(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,bg="black",highlightthickness=0, borderwidth=0)  
canvas.pack()
window.update()

window_width=window.winfo_width()
window_height=window.winfo_height() 
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()   

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.resizable(False,False)
 
snake= Tile(5*TILE_SIZE,5*TILE_SIZE)
food =Tile(10*TILE_SIZE,10*TILE_SIZE)
snake_body=[]   
velocityx=0
velocityy=0
game_over = False
score=0
def change_direction(event):   
    global velocityx,velocityy
    if(game_over):
        return

    if(event.keysym=="Up" and velocityy!=1):
        velocityx=0
        velocityy=-1
    elif(event.keysym=="Down" and velocityy!=-1):
        velocityx=0
        velocityy=1 
    elif(event.keysym=="Left" and velocityx!=1):
        velocityx=-1
        velocityy=0
    elif(event.keysym=="Right" and velocityx!=-1):
        velocityx=1
        velocityy=0
def move():
    global snake,game_over,food,snake_body,score
    if(game_over):
        return
    if(snake.x<0 or snake.x>=WINDOW_WIDTH or snake.y<0 or snake.y>=WINDOW_HEIGHT):
        game_over=True
        return
    for tile in snake_body:
        if(snake.x==tile.x and snake.y==tile.y):
            game_over=True
            return

    if(snake.x==food.x and snake.y==food.y):
        snake_body.append(Tile(food.x,food.y))
        food.x=random.randint(0,COLS-1)*TILE_SIZE
        food.y=random.randint(0,ROWS-1)*TILE_SIZE
        score+=1
    for i in range(len(snake_body)-1,-1,-1):
        tile= snake_body[i]
        if(i==0):
            tile.x=snake.x
            tile.y=snake.y
        else:
            prev_tile= snake_body[i-1]
            tile.x=prev_tile.x
            tile.y=prev_tile.y 

    snake.x+=velocityx*TILE_SIZE
    snake.y+=velocityy*TILE_SIZE

def draw():
    global snake,food,snake_body,score
    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x,food.y,food.x+TILE_SIZE,food.y+TILE_SIZE,fill="green")
    canvas.create_rectangle( snake.x, snake.y, snake.x+ TILE_SIZE, snake.y + TILE_SIZE, fill= "red" )
    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x+TILE_SIZE,tile.y+TILE_SIZE,fill="red")
    window.after(100,draw) 
    if(game_over):
        canvas.create_text(WINDOW_WIDTH//2,WINDOW_HEIGHT//2,text=f'GAME OVER...SCORE:{score} ',fill="white",font=("Arial",30))
        return
    else:
        canvas.create_text(30,20,font= "Arial 12", text=f'Score:{score}',fill="white")

draw()    
window.bind("<KeyRelease>", change_direction)
window.mainloop() 


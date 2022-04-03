from tkinter import *
import random
dire=((1,0),(-1,0),(0,1),(0,-1))
data=[[0 for i in range(22)] for j in range(22)]
for i in range(20):
    for j in range(20):
        if i%2 and j%2:
            data[i][j]=1
p=0
s=[[random.randint(0,10),random.randint(0,10)]]
while p>=0:
    d=random.randint(0,3)
    nothave=1
    for i in range(4):
        if 0<=s[p][0]+dire[d][0]<11 and 0<=s[p][1]+dire[d][1]<11 and data[2*(s[p][0]+dire[d][0])-1][2*(s[p][1]+dire[d][1])-1]==1:
            nothave=0
            p+=1
            if len(s)==p:
                s.append([s[p-1][0]+dire[d][0],s[p-1][1]+dire[d][1]])
            else:
                s[p][0]=s[p-1][0]+dire[d][0]
                s[p][1]=s[p-1][1]+dire[d][1]
            data[2*s[p][0]-1][2*s[p][1]-1]=2
            data[2*s[p-1][0]-1+dire[d][0]][2*s[p-1][1]-1+dire[d][1]]=2
            break
        if d==3:
            d=0
        else:
            d+=1
    if nothave:
        p-=1
for i in range(21):
    data[0][i]=0
    data[i][0]=0
    data[20][i]=0
    data[i][20]=0
data[0][1]=2
data[20][19]=2
dx=0
dy=1
t=Tk()
t.title("迷宫")
t.geometry("630x630")
t.configure(bg="mintcream")

labels=[]

for i in range(21):
    labels.append([])
    for j in range(21):
        if not data[i][j]:
            l=Label(t, bg="DimGray", relief="raised", padx=12, pady=4)
            l.place(x=30 * i, y=30 * j)
            labels[-1].append(l)
        else:
            l=Label(t, bg="mintcream", relief="raised", padx=12, pady=4)
            l.place(x=30 * i, y=30 * j)
            labels[-1].append(l)
queue=[]
queue_=[]
queue.append((0,1))
queue_.append((20,19))
visited={(0,1):1,(20,19):2}
print(labels)
labels[0][1].configure(bg='LightSkyBlue')
labels[20][19].configure(bg='Pink')
def Update(event):
    global queue
    global queue_
    nque=[]
    for i in range(len(queue)):
        for dxy in dire:
            if data[queue[i][0]+dxy[0]][queue[i][1]+dxy[1]] and (queue[i][0]+dxy[0],queue[i][1]+dxy[1]) not in visited.keys():
                nque.append((queue[i][0]+dxy[0],queue[i][1]+dxy[1]))
                visited[(queue[i][0]+dxy[0],queue[i][1]+dxy[1])]=1
                labels[queue[i][0]+dxy[0]][queue[i][1]+dxy[1]].configure(bg='LightSkyBlue')
    queue=nque
    nque_=[]
    for i in range(len(queue_)):
        for dxy in dire:
            if data[queue_[i][0]+dxy[0]][queue_[i][1]+dxy[1]]:
                if (queue_[i][0]+dxy[0],queue_[i][1]+dxy[1]) in visited.keys() and visited[(queue_[i][0]+dxy[0],queue_[i][1]+dxy[1])]!=2:
                    labels[queue_[i][0]+dxy[0]][queue_[i][1]+dxy[1]].configure(bg='MediumOrchid')
                    t.unbind("<Left>")
                    Label(t,text="Game Over",bg="Gold",relief="raised",font=("FZYaoti",30),\
                    fg="Black",padx=4,pady=4).place(x=241,y=284)
                if  (queue_[i][0]+dxy[0],queue_[i][1]+dxy[1]) not in visited.keys():
                    nque_.append((queue_[i][0]+dxy[0],queue_[i][1]+dxy[1]))
                    visited[(queue_[i][0]+dxy[0],queue_[i][1]+dxy[1])]=2
                    labels[queue_[i][0]+dxy[0]][queue_[i][1]+dxy[1]].configure(bg='Pink')
    queue_=nque_

t.focus_set()
t.bind("<Left>",Update)
t.mainloop()

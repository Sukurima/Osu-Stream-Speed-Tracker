from tkinter import *
import time
import threading

def round_rectangle(canvas ,x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1,
              x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius,
              x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2,
              x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius,
              x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

def click_one(event):
    global Clicks
    MainCanvas.itemconfig(FirstButton, fill="#ff0000")
    window.update()
    time.sleep(0.05)
    MainCanvas.itemconfig(FirstButton, fill="#111111")
    Clicks += 1
    ClicksVar.set(Clicks)

def click_two(event):
    global Clicks
    MainCanvas.itemconfig(SecondButton, fill="#ff0000")
    window.update()
    time.sleep(0.05)
    MainCanvas.itemconfig(SecondButton, fill="#111111")
    Clicks += 1
    ClicksVar.set(Clicks)

def test_timer():
    temptime = TimeScaleVariable
    while temptime != 0:
        TimerVar.set(temptime)
        time.sleep(1)
        temptime -= 1
    TimerVar.set(temptime)
    finish_test()

def start_test():
    global TimeScaleVariable
    global FirstButton
    global SecondButton
    global GameCount
    global Clicks
    if GameCount != 0:
        Clicks = 0
        ClicksVar.set(Clicks)
        TimeScaleVariable = TimeScale.get()
        ResultLabel.pack_forget()
        window.unbind("<p>")
        StartTestButton.place_forget()
        TimeScale.place_forget()
        FirstButton = round_rectangle(MainCanvas ,385, 255, 475, 345, fill="#111111")
        SecondButton = round_rectangle(MainCanvas ,485, 255, 575, 345, fill="#111111")
        window.bind("<KeyRelease-d>", click_one)
        window.bind("<KeyRelease-f>", click_two)
        ClickLabel.place(x=462, y=350)
        TimerLabel.place(x=853, y=10)
        ResultLabel.place_forget()

        TimerThread = threading.Thread(target=test_timer, args=())
        TimerThread.start()
    else:
        Clicks = 0
        ClicksVar.set(Clicks)
        GameCount += 1
        TimeScaleVariable = TimeScale.get()
        window.unbind("<p>")
        StartTestButton.place_forget()
        TimeScale.place_forget()
        FirstButton = round_rectangle(MainCanvas ,385, 255, 475, 345, fill="#111111")
        SecondButton = round_rectangle(MainCanvas ,485, 255, 575, 345, fill="#111111")
        window.bind("<KeyRelease-d>", click_one)
        window.bind("<KeyRelease-f>", click_two)
        ClickLabel.place(x=462, y=350)
        TimerLabel.place(x=853, y=10)
        ResultLabel.place_forget()

        TimerThread = threading.Thread(target=test_timer, args=())
        TimerThread.start()


def finish_test():
    global Clicks
    ResultVar.set(str(int(Clicks*(60/TimeScaleVariable)))+"CPM")
    ClickLabel.place_forget()
    TimerLabel.place_forget()
    MainCanvas.delete(FirstButton)
    MainCanvas.delete(SecondButton)
    ResultLabel.place(x=410, y=290)
    StartTestButton.place(x=397, y=340)
    TimeScale.place(x=795, y=50)
    window.unbind("<KeyRelease-d>")
    window.unbind("<KeyRelease-f>")

window = Tk()
window.geometry("960x600")
window.config(bg="#000000")

Clicks = 0
ClicksVar = IntVar()
TimerVar = IntVar()
ResultVar = StringVar()
GameCount = 0

TimeScaleVariable = ""

MainCanvas = Canvas(window, width=960, height=600, bg="#000000")
MainCanvas.pack()

ClickLabel = Label(MainCanvas, font=("Premium", 15), width=3, height=1, textvariable=ClicksVar, bg="#111111", fg="#777777")
TimerLabel = Label(MainCanvas, font=("Premium", 18), width=3, height=1, textvariable=TimerVar, bg="#111111", fg="#777777")
TimeScale = Scale(MainCanvas, from_=5, to=120, font=("Premium", 15), orient=HORIZONTAL, length=150, width=12, resolution=5, bg="#000000", fg="#ff0000", troughcolor="#111111")
TimeScale.place(x=795, y=50)
ResultLabel = Label(MainCanvas, font=("Premium", 23), width=8, height=1, textvariable=ResultVar, bg="#111111", fg="#777777")


StartTestButton = Button(MainCanvas, command=start_test, width=12, height=1, text="Click to start",font=("Premium", 18),
                         bg="#222222", fg="#777777", activebackground="#000000", activeforeground="#555555")
StartTestButton.place(x=397, y=300)

window.mainloop()
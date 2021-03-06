from tkinter import *


def Chrg_lmt():
    lmt= str(enter.get())
    #power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "r")
    #print("Current Charge Threshold:")
    #print(power_cfg.read())
    power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "w")
    print("Updating Threshold.....")
    power_cfg.write(lmt);
    print("Threshold Set To: ",lmt)



def add(event):
    a=int(enter.get())
    b=a+1
    if(b<=100):
        enter.set(b)
    else:
        b=100
        enter.set(b)
    return


def sub(event):
    a=int(enter.get())
    b=a-1
    enter.set(b)
    return

#******* GUI code***********



root=Tk()
root.geometry('240x90')
root.title('Charge Limiter')
power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "r")
pwr_val=int(power_cfg.read())


if(pwr_val==100):
    enter=IntVar(value = "80")
    Chrg_lmt()
    exit(0)

else:

    power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "r")
    pwr_val=int(power_cfg.read())
    enter=IntVar(value = pwr_val)

    label=Label(root,text="Set Limit",bg='skyblue',fg='red').grid(row=2,column=1)

    entry_1=Entry(root,textvariable=enter).grid(row=3,column=1)

    button1=Button(root,text='+')
    button1.grid(row=3,column=2)
    button1.bind('<Button-1>',add)

    button2=Button(root,text='-')
    button2.grid(row=3,column=0)
    button2.bind('<Button-1>',sub)

    button3=Button(root,text='Apply', command=Chrg_lmt)
    button3.grid(row=4,column=1)
    button3.bind()

    root.mainloop()

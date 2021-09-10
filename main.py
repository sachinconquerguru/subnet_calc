import re
from tkinter import *
sub_addr_lst = []
network_lst = []
inver_lst = []
brodcast_lst = []
win= Tk()
win.geometry("750x250")

def main_fun():
    ipr = ip.get()
    subnet=int(subnet_add.get())
    sub_net_str=''.join(str("1"*subnet+"0"*(32-subnet))) 
    network_addr = re.findall('........',sub_net_str) # first 8 character in a string append to list as first element eg1:['11111111', '11111111', '11111000', '00000000']
    sub_addr_lst = [int(i,2) for i in network_addr] # converting binary to decimal eg :['11111111', '11111111', '11111000', '00000000'] >>> [255, 255, 248, 0]
    subnet_mask_ipv4 =".".join(map(str, sub_addr_lst))
    ip_split = list(ipr.split("."))
    network_lst = [int(ip_split[j]) & sub_addr_lst[j] for j in range(len(ip_split))] # network address =  AND(&) bitwise operation bt subnet address and ip address  
    network_address = ".".join(map(str, network_lst))
    str_inverted_subnet=''.join(str("0"*subnet+"1"*(32-subnet)))
    inverted= re.findall('........',str_inverted_subnet)
    inver_lst = [int(i,2) for i in inverted]
    brodcast_lst = [int(network_lst[j]) | inver_lst[j] for j in range(len(network_lst))] # broadcast address =  OR(|) bitwise operation bt Inverted subnet address and network address
    brodacast_address = ".".join(map(str, brodcast_lst))
    no_of_available_ip_address= (pow(2, 32-subnet))-2 # The subnet's formula is  (2 power n) - 2 , n is here number of zero in subnet address , eg: pow(2, 32-subnet))-2
    network_lst[3] = int(network_lst[3]) + 1
    start_range = ".".join(map(str, network_lst))
    brodcast_lst[3] = int(brodcast_lst[3]) - 1
    end_range = ".".join(map(str, brodcast_lst))
    range1 = start_range + " - " + end_range
    new= Toplevel(win)
    new.geometry("750x400")
    new.title("Result")
    Label(new, text="ip address : ", font=('Helvetica 17 bold')).place(x=10,y=40)
    Label(new, text=ipr, font=('Helvetica 17 bold')).place(x=300,y=40)
    Label(new, text="subnet mask : ", font=('Helvetica 17 bold')).place(x=10,y=70)
    Label(new, text=subnet_mask_ipv4, font=('Helvetica 17 bold')).place(x=300,y=70)
    Label(new, text="Network address : ", font=('Helvetica 17 bold')).place(x=10,y=100)
    Label(new, text=network_address, font=('Helvetica 17 bold')).place(x=300,y=100)
    Label(new, text="Broadcast address : ", font=('Helvetica 17 bold')).place(x=10,y=130)
    Label(new, text=brodacast_address, font=('Helvetica 17 bold')).place(x=300,y=130)
    Label(new, text="No.of available IP address:", font=('Helvetica 17 bold')).place(x=10,y=160)
    Label(new, text=no_of_available_ip_address, font=('Helvetica 17 bold')).place(x=320,y=160)
    Label(new, text="Range : ", font=('Helvetica 17 bold')).place(x=10,y=190)
    Label(new, text=range1, font=('Helvetica 17 bold')).place(x=300,y=190)

def clear():
	ip.set('')
	subnet_add.set('')

win.title('subnet calculator')
win.geometry('400x300')
win.config(bg='#A67449')
label1 = Label(win, text="enter the ip address : ", bg="red", fg="white").place(x=10,y=40)
label2 = Label(win, text="enter the subnetmask : ", bg="red", fg="white").place(x=10,y=80)
ip = StringVar(win)
subnet_add=StringVar(win)
ip_addr = Entry(win, bd =5,textvariable=ip).place(x=190,y=40)
sub_net_mask = Entry(win, bd =5,textvariable=subnet_add).place(x=190,y=80)
button1 = Button(win,text="Calculate",command=main_fun).place(x=140,y=150)
button2 = Button(win,text="clear",command=clear).place(x=250,y=150)
label1 = Label(win, text="example (ip : 192.168.1.8, subnetmask : 21)", bg="red", fg="white").place(x=40,y=200)
win.mainloop()
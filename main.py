import re
from tkinter import *
win= Tk()
win.geometry("750x250")
def main_fun():
    ipr = ip.get()
    subnet=int(subnet_add.get())
    sub_net_str=''.join(str("1"*subnet+"0"*(32-subnet))) 
    asd = re.findall('........',sub_net_str)
    final_subnet_ip_binary = ".".join(asd)
    subnet_lst = final_subnet_ip_binary.split(".")
    count = 0
    jkl = []
    for i in subnet_lst:
        b_num = list(subnet_lst[count])
        value = 0
        for i in range(len(b_num)):            
            digit = b_num.pop()
            if digit == '1':       
                value = value + pow(2, i)
        count+=1
        jkl.append(value)
    subnet_mask_ipv4 =".".join(map(str, jkl))
    network_lst = []
    new = list(ipr.split("."))
    for i in range(len(new)):
        network_lst.append(int(new[i]) & jkl[i])
    network_address = ".".join(map(str, network_lst))
    str_inverted_subnet=''.join(str("0"*subnet+"1"*(32-subnet)))
    inverted= re.findall('........',str_inverted_subnet)
    finalstr_inverted_subnet = ".".join(inverted)
    subnetinvert_lst = finalstr_inverted_subnet.split(".")
    count3 = 0
    inver_lst = []
    for i in subnet_lst:
        b_num = list(subnetinvert_lst[count3])
        value = 0
        for i in range(len(b_num)):           
            digit = b_num.pop()
            if digit == '1':      
                value = value + pow(2, i)
        count3+=1
        inver_lst.append(value)
    brodcast_lst = []
    new1 = list(network_address.split("."))
    for i in range(len(new)):
        brodcast_lst.append(int(new1[i]) | inver_lst[i])
    brodacast_address = ".".join(map(str, brodcast_lst))
    No_of_available_IP_address= pow(2, 32-subnet)
    useable_ip_address = No_of_available_IP_address - 2
    network_lst_for_range = list(network_address.split("."))
    network_lst_for_range[3] = int(network_lst_for_range[3]) + 1
    start_range = ".".join(map(str, network_lst_for_range))
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
    Label(new, text=useable_ip_address, font=('Helvetica 17 bold')).place(x=320,y=160)
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


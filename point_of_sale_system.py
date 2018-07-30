from tkinter import*
import tkinter.messagebox
import time
import random
import  os
import sqlite3
#import pyside
#===================DAT BASE=================================


conn = sqlite3.connect('BILLS .db')

c= conn.cursor()
print ("Opened database successfully");



#===================DAT BASE=================================





operator = ""





#### creating window and its geometry ######

root = Tk()
root.geometry("1600x800+0+0")
root.title("Point of Sale  System")


#### creating Frame ######

top = Frame(root, width = 1600, height = 50, relief = FLAT)
top.pack(side = TOP)

left = Frame(root, width = 800, height = 700, relief = FLAT)
left.pack(side = LEFT)

right = Frame(root, width = 300, height = 700, relief = FLAT)
right.pack(side = RIGHT)


##### creating label of title and time ###

label_info = Label(top, font = ('arial',50,'bold'), text ="Point of Sale System", fg = "#4CBB17", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

local_time = time.asctime(time.localtime(time.time()))

label_info = Label(top, font = ('arial',20,'bold'), text = local_time, fg = "#4CBB17", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 1)


######## creating calculator #######

total_inp = StringVar()
def btn_click(str):
	global operator
	operator =  str
	total_inp.set(operator)




#def buttonClick(self, str):
#        self.task = str(self.task) + str("")
#        self.UserIn.set(self.task)
#        self.userinput.insert(END, str+'\n')



#def fun_clear():
#	global operator
#	operator = ""
#	total_inp.set(operator)

def calculate():
	global operator
	try:
		sumup = str(eval(operator))
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		sumup = 0
		fun_clear()
	total_inp.set(sumup)
	operator = ""



#-------------------------------------text display-----------------------------------------------------------------------------------




#txt = Entry(right, font = ('arial',20,'bold'), textvariable = txt_inp, bd = 30, insertwidth = 40, bg = "powderblue", justify = 'right')
#txt.grid(columnspan = 4,row= 0 ,column= 0)

#txt = Entry(right, font = ('arial',40,'bold'), textvariable = txt_inp, bd = 30, insertwidth = 40, bg = "powderblue", justify = 'right')
#txt.grid(columnspan = 4,row= 0 ,column= 0)



#------------------------------------------------------------------------------------------------------------------------



###########now on left frame  enter menu ####################################################################

rand = StringVar()
fries_inp = StringVar()
Pizza_inp = StringVar()
burger_inp = StringVar()
drinks_inp = StringVar()
total_inp = StringVar()
subtotal_inp = StringVar()
services_inp = StringVar()
tax_inp = StringVar()
cost_inp = StringVar()
cake= StringVar()
Patties_inp = StringVar()
#Sandwich_inp = stringVar()
def ref():

	f1 = open('value.txt','r')
	line = f1.readlines()
	fries_p =   float(line[0])
	Pizza_p =   float(line[1])
	burger_p =  float(line[2])
	drinks_p =  float(line[3])
                                                 #Cake_p   =  float(line[4])
	Patties_p=  float(line[5])
    #Sandwich_p= float(line[6])
	f1.close()

	x = random.randint(00000,99999)
	random_ref = str(x)
	rand.set(random_ref)
	try:
		if fries_inp.get() == "":
			CoF = 0
		else:
			CoF = float(fries_inp.get())*fries_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		fries_inp.set("")

	try:
		if Pizza_inp.get() == "":
			CoS = 0
		else:
			CoS = float(Pizza_inp.get())*Pizza_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		Pizza_inp.set("")

	try:
		if burger_inp.get() == "":
			CoB = 0
		else:
			CoB = float(burger_inp.get())*burger_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		burger_inp.set("")

	try:
		if drinks_inp.get() == "":
			CoD = 0
		else:
			CoD = float(drinks_inp.get())*drinks_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		drinks_inp.set("")

	try:
		if Cake_inp.get() == "":
			CoP = 0
		else:
			CoP = float(Cake())*Cake_p
	except Exceptie:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		cake_inp.set("")

	try:
		if Patties_inp.get() == "":
			CoC = 0
		else:
			CoC = float(Patties_inp.get())*Patties_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		Patties_inp.set("")










	CostOfMeal = (CoF+CoS+CoB+CoD+CoP+CoC)

#	PayTax = (CostOfMeal)
#	ServiceCharge = (CostOfMeal)
#	totalTax = PayTax + ServiceCharge
	totalCost = (CostOfMeal)

	#services_inp.set(str('%.0f' % (ServiceCharge)))
	#tax_inp.set(str('%.0f' % (PayTax)))
	#subtotal_inp.set(str('%.0f' % (CostOfMeal)))
	total_inp.set(str('%.0f' % (totalCost)))
	#cost_inp.set(str('%.1f' % (totalTax)))

def bck():
	root.destroy()
	import question



def qexit():
	root.destroy()

def reset():
	rand.set("")
	fries_inp.set("")
	Pizza_inp.set("")
	burger_inp.set("")
	drinks_inp.set("")
	total_inp.set("")
	subtotal_inp.set("")
	services_inp.set("")
	tax_inp.set("")
	cost_inp.set("")
	Cake_inp.set("")
	Patties_inp.set("")
    #Sandwich_inp.set("")


#-------------------------------------------------order NO-----------------------------------------------------------------------
lblreference = Label(left, font=('arial',16,'bold'),text = "Order No", bd = 16, anchor = 'w')
lblreference.grid(row=0,column=0,sticky = E)

txt_customer = Entry(left,font=('arial',16,'bold'), textvariable=rand, bd=6, insertwidth =4,bg = "powder blue", justify ='right')
txt_customer.grid(row=0,column=1)




lblreference = Label( font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0,sticky= E )
txtreference = Entry(font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)





#-------------------------------------------------#--FRIES-----------------------------------------------#-------------------------------------------------

btn_fries  = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Fries", bg= "#95C8D8",command = lambda: btn_click("Fries"))
btn_fries.grid(row=1, column= 0)



#fries = Button(left, font=('arial',16,'bold'),text = "Fries", bd = 10, anchor = 'w',bg="#95C8D8" )
#fries.grid(row=1,column=0,sticky = E)

#txt_fries = Entry(left,font=('arial',16,'bold'), textvariable=fries_inp, bd=10, insertwidth = 4,bg ="powder blue", justify ='right')
#txt_fries.grid(row=1,column=1)

#-------------------------------------------------#------PIZZA-------------------------------------------#-------------------------------------------------
#######################################################################################################################################################################################
btn_Pizza = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Pizza", bg= "#FFF200",command = lambda: btn_click("Pizza"))
#############################################################################################################################################################################################
btn_Pizza.grid(row=2, column= 0)
#######################################################################################################################################################################################


#samosa = Button(left, font=('arial',16,'bold'),text = "Pizza ", bd = 10, anchor = 'w',bg ="#FFF200" )
#samosa.grid(row=2,column=0,sticky = E)

#txt_Pizza = Entry(left,font=('arial',16,'bold'), textvariable=Pizza_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_Pizza.grid(row=2,column=1)
#-------------------------------------------------#----SANDWICH---------------------------------------------#-------------------------------------------------
btn_burger  = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Burger", bg= "#FA8072",command = lambda: btn_click("Burger"), anchor = 'w')
btn_burger.grid(row=3, column= 0)



#burger = Button(left, font=('arial',16,'bold'),text = "Sandwich", bd = 10, anchor = 'w',bg ="#FA8072" )
#burger.grid(row=3,column=0,sticky = E)
#txt_burger = Entry(left,font=('arial',16,'bold'), textvariable=burger_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_burger.grid(row=3,column=1)
#-------------------------------------------------#--DRINKS-----------------------------------------------#-------------------------------------------------
btn_drinks  = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Drinks", bg= "#D0F0C0",command = lambda: btn_click("Drinks"))
btn_drinks.grid(row=4, column= 0)


#drinks = Button(left, font=('arial',16,'bold'),text = "Drinks", bd = 10, anchor = 'w' , bg = "#D0F0C0")
#drinks.grid(row=4,column=0,sticky = E)
#txt_drinks = Entry(left,font=('arial',16,'bold'), textvariable=drinks_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_drinks.grid(row=4,column=1)
#-------------------------------------------------#--------CAKE-----------------------------------------#-------------------------------------------------
btn_Cake  = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Cake", bg= "#EEDC82",command = lambda: btn_click("cake"))
btn_Cake .grid(row=5, column= 0)

btn_Cake  = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "", bg= "#EEDC82",command = lambda: btn_click("") ,anchor = 'w')
btn_Cake .grid(row=1, column=1)


#paneer_tikka = Button(left, font=('arial',16,'bold'),text = "Cake", bd = 10, anchor = 'w',bg = "#EEDC82" )
#paneer_tikka.grid(row=5,column=0,sticky = E)
#txt_paneer_tikka = Entry(left,font=('arial',16,'bold'), textvariable=paneer_tikka_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_paneer_tikka.grid(row=5,column=1)

#-------------------------------------------------#---------PATTIES----------------------------------------#-------------------------------------------------
btn_Patties = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=5, text= "Patties", bg= "#FFF200",command = lambda: btn_click("Patties"))
btn_Patties.grid(row=6, column= 0)                                                                                                                                                  #---------------------------------------#--------------------------active buttons--------------------------------------------------------------#-------------------------------------------------
#---------------------------------------#--------active buttons -------------------------------------------------------------------------------#-------------------------------------------------












#txt_Patties = Entry(left,font=('arial',16,'bold'), textvariable=chicken_tikka_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_Patties.grid(row=6,column=1)
#===========================================================================================================================================
#def show_entry_fields():






#Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

#mainloop(



#==========================================================================================================================================================================







####################################################TEXT INPUT##################################################################################
#txt_total = Entry(left,font=('arial',41,'bold'), textvariable=total_inp, bd=10, insertwidth =204,bg = "white", justify ='right')
#txt_total.grid(row=0,column=9)









txt_total = Entry(left,font=('flat',49,'bold'), textvariable=total_inp, bd=8, insertwidth =10,bg = "#89CFEF" ,width =20)
#"""justify ='right'""")
txt_total.grid(row=0,column=4,pady= 5,padx=20)
#txt_total. height=2, width=10
#txt_total.geometry(1000*520*0*0)


########################################################################

#txt = Entry(left,font=('arial',49,'bold'), textvariable=total_inp, bd=10, insertwidth =204,bg = "white", justify ='right')
#txt.grid(row=0,column=9)




##################################################################################################################################

#width = 70,height = 22



### right Frame Button ###########


#btn_Cash = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',15,'bold'), width=10, text= "Cash", bg= "#FFDO",command = ref)
#btn_Cash.grid(row=8, column= 1)

#btn_Card = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',15,'bold'), width=10, text= "Card", bg= "#EB9605",command = ref)
#btn_Card.grid(row=8, column= 2)
##################################################################################################################################



#-----------------------------------------buttons------------------------------------------



btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=9, text= "Total", bg= "powder blue",command = ref)
btn_total.grid(row=9, column= 1)



btn_reset = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',15,'bold'), width=9, text= "Void", bg= "#D0F0C0",command = reset)
btn_reset.grid(row=9, column= 2)


btn_bck = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=9, text= "Back", bg= "#FFBF00",command = bck)
btn_bck.grid(row=9 , column= 3)



#btn_exit = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',15,'bold'), width=10, text= "Exit", bg= "#FFBF00",command = qexit)
#btn_exit.grid(row=9, column= 3)

root.mainloop()






#Cookies= Button(left, font=('arial',16,'bold'),text = "Cookies", bd = 16, anchor = 'w' )
#Cookies .grid(row=2,column=0,)
#txt_Cookies  = Entry(left,font=('arial',16,'bold'), textvariable=Cookies_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_Cookies .grid(row=2,column=1)













    # command=btn_click("Tea")





#yes_no_label = Label(window, text="Yes or no?")
#yes_no_label.grid(row=0, column=1)



#Tea = Button(left, font=('arial',16,'bold'),text = "Tea", bd = 16, anchor = 'w' )
#Tea .grid(row=6,column=0,)
#txt_Tea  = Entry(left,font=('arial',16,'bold'), textvariable=chicken_tikka_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_Tea .grid(row=6,column=1)

#def buttonClick(self):
#    self.Patties_Button = Button(master, command=self.buttonClick, text="Patties")
#    self.submit_Button.grid(row=9, column= 0)
   # """ handle button click event and output text from entry area"""


#txt_inp.place(x=10,y=10)

#Button(command=click).place(x=100,y=40)

#root.mainloop()

#btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Patties", bg= "green",command=btn_click("Patties"))
#btn_total.grid(row=6, column= 0)










#btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Chicken Tikka", bg= "powder blue", justify ='right)
#btn_total.grid(row=1, column= 3)

#subtotal = Label(left, font=('arial',16,'bold'),text = "Cost of Meal", bd = 16, anchor = 'w' )
#subtotal.grid(row=1,column=2,sticky = E)
#txt_subtotal = Entry(left,font=('arial',16,'bold'), textvariable=subtotal_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_subtotal.grid(row=1,column=3)

#services = Label(left, font=('arial',16,'bold'),text = "Service Charge", bd = 16, anchor = 'w' )
#services.grid(row=2,column=2,sticky = E)
#txt_services = Entry(left,font=('arial',16,'bold'), textvariable=services_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_services.grid(row=2,column=3)

#tax = Label(left, font=('arial',16,'bold'),text = "GST", bd = 16, anchor = 'w' )
#tax.grid(row=3,column=2,sticky = E)
#txt_tax = Entry(left,font=('arial',16,'bold'), textvariable=tax_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_tax.grid(row=3,column=3)

#cost = Label(left, font=('arial',16,'bold'),text = "Total Tax", bd = 16, anchor = 'w' )
#cost.grid(row=4,column=2,sticky = E)
#txt_cost = Entry(left,font=('arial',16,'bold'), textvariable=cost_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
#txt_cost.grid(row=4,column=3)

#total = Label(left, font=('arial',17,'bold'),text = "Total ", bd = 18, )
#total.grid(row= 0,column=2)
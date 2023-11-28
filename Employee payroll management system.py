from struct import pack
import time
from tkinter import *
from tkinter import messagebox,ttk
from turtle import heading
import pymysql
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("Employee Payroll Management System | Develped by Vinay")
        self.root.geometry("1320x720+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="black",fg="white").place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("times new roman",15),bg="gray",fg="white").place(x=1300,y=15,height=30)

        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_contactno=StringVar()
        self.var_proofid=StringVar()
        self.var_experience=StringVar()
        self.var_bank=StringVar()


      #########################------frame1------##################################################################################################################################################
    
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=850,height=720)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",25,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
   
       

        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=70)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_emp_code,bg="#fff0da",fg="black")
        self.txt_code.place(x=220,y=85,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="green",fg="black").place(x=500,y=80,height=30)


        lbl_designation=Label(Frame1,text="Designation:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=130)
        txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="#fff0da",fg="black").place(x=180,y=135,width=200)
        lbl_doj=Label(Frame1,text="D.O.J:",font=("times new roman",20),bg="white",fg="black").place(x=420,y=130)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="#fff0da",fg="black").place(x=580,y=130)

        lbl_name=Label(Frame1,text="Name:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=190)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="#fff0da",fg="black").place(x=180,y=195,width=200)
        lbl_dob=Label(Frame1,text="D.O.B:",font=("times new roman",20),bg="white",fg="black").place(x=420,y=190)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="#fff0da",fg="black").place(x=580,y=190)

        lbl_age=Label(Frame1,text="Age:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=250)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="#fff0da",fg="black").place(x=180,y=255,width=200)
        lbl_experience=Label(Frame1,text="Experience:",font=("times new roman",20),bg="white",fg="black").place(x=420,y=250)
        txt_experience=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="#fff0da",fg="black").place(x=580,y=250)

        lbl_gender=Label(Frame1,text="Gender:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=310)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="#fff0da",fg="black").place(x=180,y=315,width=200)
        lbl_proofid=Label(Frame1,text="Proof ID:",font=("times new roman",20),bg="white",fg="black").place(x=420,y=310)
        txt_proofid=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proofid,bg="#fff0da",fg="black").place(x=580,y=310)

        lbl_email=Label(Frame1,text="Email:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=370)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="#fff0da",fg="black").place(x=180,y=375,width=200)
        lbl_contactno=Label(Frame1,text="Contact No:",font=("times new roman",20),bg="white",fg="black").place(x=420,y=370)
        txt_contactno=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contactno,bg="#fff0da",fg="black").place(x=580,y=370)

        lbl_bank=Label(Frame1,text="Bank Account:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=430)
        txt_bank=Entry(Frame1,font=("times new roman",15),textvariable=self.var_bank,bg="#fff0da",fg="black").place(x=180,y=435)


        lbl_address=Label(Frame1,text="Address:",font=("times new roman",20),bg="white",fg="black").place(x=30,y=490)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="#fff0da",fg="black")
        self.txt_address.place(x=180,y=495,width=600,height=200)


        #######################------frame2------############################################################################################################################

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_basicsalary=StringVar()
        self.var_totaldays=StringVar()
        self.var_absents=StringVar()
        self.var_medical=StringVar()
        self.var_providedfund=StringVar()
        self.var_convence=StringVar()
        self.var_netsalary=StringVar()
        





        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=870,y=70,width=660,height=350)
        title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",25,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        lbl_month=Label(Frame2,text="Month:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="#fff0da",fg="black").place(x=100,y=75,width=100)
        lbl_year=Label(Frame2,text="Year:",font=("times new roman",20),bg="white",fg="black").place(x=200,y=70)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="#fff0da",fg="black").place(x=280,y=75,width=100)
        lbl_basicsalary=Label(Frame2,text="Basic Salary:",font=("times new roman",20),bg="white",fg="black").place(x=390,y=70)
        txt_basicsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_basicsalary,bg="#fff0da",fg="black").place(x=540,y=75,width=100)

        lbl_totaldays=Label(Frame2,text="Total Days:",font=("times new roman",20),bg="white",fg="black").place(x=30,y=110)
        txt_totaldays=Entry(Frame2,font=("times new roman",15),textvariable=self.var_totaldays,bg="#fff0da",fg="black").place(x=180,y=115,width=100)
        lbl_absents=Label(Frame2,text="Absents:",font=("times new roman",20),bg="white",fg="black").place(x=320,y=110)
        txt_absents=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absents,bg="#fff0da",fg="black").place(x=430,y=115,width=100)

        lbl_medical=Label(Frame2,text="Medical:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=180)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="#fff0da",fg="black").place(x=120,y=185,width=150)
        lbl_providedfund=Label(Frame2,text="Provided Fund:",font=("times new roman",20),bg="white",fg="black").place(x=280,y=180)
        txt_providedfund=Entry(Frame2,font=("times new roman",15),textvariable=self.var_providedfund,bg="#fff0da",fg="black").place(x=460,y=185,width=190)

        lbl_convence=Label(Frame2,text="Convence:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="#fff0da",fg="black").place(x=140,y=225,width=130)
        lbl_netsalary=Label(Frame2,text="Net Salary:",font=("times new roman",20),bg="white",fg="black").place(x=280,y=220)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_netsalary,bg="#fff0da",fg="black").place(x=410,y=225,width=240)

        btn_calcuate=Button(Frame2,text="Calcuate",command=self.calculate,font=("times new roman",20),bg="orange",fg="black").place(x=230,y=260,height=30)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",20),bg="green",fg="black")
        self.btn_save.place(x=400,y=260,height=30)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",20),bg="yellow",fg="black").place(x=530,y=260,height=30)

        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",20),bg="red",fg="white")
        self.btn_update.place(x=280,y=305,height=30)
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",20),bg="blue",fg="white")
        self.btn_delete.place(x=460,y=305,height=30)


        ###############################-----------frame3---------####################################################################################################################

        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=870,y=430,width=660,height=360)



        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
            
                    


        Cal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_frame.place(x=2,y=2,width=288,height=350)

        txt_result=Entry(Cal_frame,bg="#fff0da",textvariable=self.var_txt,font=("times new roman",25,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=60)

        btn_7=Button(Cal_frame,text='7',command=lambda:btn_click(7),font=("times now roman",15,"bold")).place(x=0,y=62,w=70,h=70)
        btn_8=Button(Cal_frame,text='8',command=lambda:btn_click(8),font=("times now roman",15,"bold")).place(x=72,y=62,w=70,h=70)
        btn_9=Button(Cal_frame,text='9',command=lambda:btn_click(9),font=("times now roman",15,"bold")).place(x=144,y=62,w=70,h=70)
        btn_div=Button(Cal_frame,text='/',command=lambda:btn_click('/'),font=("times now roman",15,"bold")).place(x=216,y=62,w=70,h=70)
        btn_4=Button(Cal_frame,text='4',command=lambda:btn_click(4),font=("times now roman",15,"bold")).place(x=0,y=134,w=70,h=70)
        btn_5=Button(Cal_frame,text='5',command=lambda:btn_click(5),font=("times now roman",15,"bold")).place(x=72,y=134,w=70,h=70)
        btn_6=Button(Cal_frame,text='6',command=lambda:btn_click(6),font=("times now roman",15,"bold")).place(x=144,y=134,w=70,h=70)
        btn_mul=Button(Cal_frame,text='*',command=lambda:btn_click('*'),font=("times now roman",15,"bold")).place(x=216,y=134,w=70,h=70)
        btn_1=Button(Cal_frame,text='1',command=lambda:btn_click(1),font=("times now roman",15,"bold")).place(x=0,y=206,w=70,h=70)
        btn_2=Button(Cal_frame,text='2',command=lambda:btn_click(2),font=("times now roman",15,"bold")).place(x=72,y=206,w=70,h=70)
        btn_3=Button(Cal_frame,text='3',command=lambda:btn_click(3),font=("times now roman",15,"bold")).place(x=144,y=206,w=70,h=70)
        btn_sub=Button(Cal_frame,text='-',command=lambda:btn_click('-'),font=("times now roman",15,"bold")).place(x=216,y=206,w=70,h=70)
        btn_0=Button(Cal_frame,text='0',command=lambda:btn_click(0),font=("times now roman",15,"bold")).place(x=0,y=278,w=70,h=70)
        btn_deci=Button(Cal_frame,text='C',command=clear_cal,font=("times now roman",15,"bold")).place(x=72,y=278,w=70,h=70)
        btn_add=Button(Cal_frame,text='+',command=lambda:btn_click('+'),font=("times now roman",15,"bold")).place(x=144,y=278,w=70,h=70)
        btn_equal=Button(Cal_frame,text='=',command=result,font=("times now roman",15,"bold")).place(x=216,y=278,w=70,h=70)


        
        Sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Sal_frame.place(x=294,y=2,width=358,height=350)

        title_sal=Label(Sal_frame,text="Salary Receipt",font=("times new roman",25,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        Sal_frame2=Frame(Sal_frame,bg="white",bd=2,relief=RIDGE)
        Sal_frame2.place(x=2,y=48,width=350,height=250)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress:Xyz , Floor4
----------------------------------------------
Employee ID\t\t:  
Salary Of\t\t:  Mon-YYYY
Generated On\t\t:  DD-MM-YYYY
----------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.------
Net salary\t\t:  Rs.-------
----------------------------------------------
This is computer generated slip, not
required any signature
'''

        scroll_y=Scrollbar(Sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(Sal_frame2,font=("times new roman",15),bg='#fff0da',yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)

        self.btn_print=Button(Sal_frame,text="Print",state=DISABLED,command=self.print,font=("times new roman",20),bg="green",fg="black")
        self.btn_print.place(x=230,y=310,height=30)
    
        self.check_connection()
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            #print(rows)
            if row==None:
                    messagebox.showerror("Error","Invalid Employee Id , Please try a Valid employee ID",parent=self.root)
            else:
                #print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_dob.set(row[6])
                self.var_doj.set(row[7])
                self.var_experience.set(row[8])
                self.var_proofid.set(row[9])
                self.var_contactno.set(row[10])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[11])
                self.var_bank.set(row[12])

                self.var_month.set(row[13]) 
                self.var_year.set(row[14]) 
                self.var_basicsalary.set(row[15]) 
                self.var_totaldays.set(row[16]) 
                self.var_absents.set(row[17]) 
                self.var_medical.set(row[18]) 
                self.var_providedfund.set(row[19]) 
                self.var_convence.set(row[20]) 
                self.var_netsalary.set(row[21])
                file_=open('Salary_receipt/'+str(row[22]),'r')
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state="readonly") 
                self.btn_print.config(state=NORMAL)
                
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to :{str(ex)}')


    def clear(self):

        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL) 

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_experience.set('')
        self.var_proofid.set('')
        self.var_contactno.set('')
        self.txt_address.delete('1.0',END)
        self.var_bank.set('')

        self.var_month.set('') 
        self.var_year.set('') 
        self.var_basicsalary.set('') 
        self.var_totaldays.set('') 
        self.var_absents.set('') 
        self.var_medical.set('') 
        self.var_providedfund.set('') 
        self.var_convence.set('') 
        self.var_netsalary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)


    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee ID must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                        messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    #print(op)
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to :{str(ex)}')

    def update(self):
        if self.var_emp_code.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
            #print(rows)
                if row==None:
                    messagebox.showerror("Error","This employee ID is invalid ,try again with valid Employee ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contactno`=%s,`address`=%s,`bank`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absents`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_recipt`=%s WHERE `e_id`=%s",
                    (   
                      self.var_designation.get(),
                      self.var_name.get(),
                      self.var_age.get(),
                      self.var_gender.get(),
                      self.var_email.get(),
                      self.var_dob.get(),
                      self.var_doj.get(),
                      self.var_experience.get(),
                      self.var_proofid.get(),
                      self.var_contactno.get(),
                      self.txt_address.get('1.0',END),
                      self.var_bank.get(),
 
                      self.var_month.get(),
                      self.var_year.get(),
                      self.var_basicsalary.get(),
                      self.var_totaldays.get(),
                      self.var_absents.get(),
                      self.var_medical.get(),
                      self.var_providedfund.get(),
                      self.var_convence.get(),
                      self.var_netsalary.get(),
                      self.var_emp_code.get()+".txt",
                      self.var_emp_code.get()
                    )
                    )

                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Updated Successfully")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to :{str(ex)}')


    def add(self):
        if self.var_emp_code.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
            #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This employee ID has already avilable in our record,tryanother ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                      self.var_emp_code.get(),
                      self.var_designation.get(),
                      self.var_name.get(),
                      self.var_age.get(),
                      self.var_gender.get(),
                      self.var_email.get(),
                      self.var_dob.get(),
                      self.var_doj.get(),
                      self.var_experience.get(),
                      self.var_proofid.get(),
                      self.var_contactno.get(),
                      self.txt_address.get('1.0',END),
                      self.var_bank.get(),
 
                      self.var_month.get(),
                      self.var_year.get(),
                      self.var_basicsalary.get(),
                      self.var_totaldays.get(),
                      self.var_absents.get(),
                      self.var_medical.get(),
                      self.var_providedfund.get(),
                      self.var_convence.get(),
                      self.var_netsalary.get(),
                      self.var_emp_code.get()+".txt"
                    )

                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully")
                    self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to :{str(ex)}')

    def calculate (self):
        if self.var_month.get()=='' or self.var_year.get()==''or self.var_totaldays.get=='' or self.var_providedfund.get()==''or self.var_basicsalary.get()=='' or self.var_absents.get()=='' or self.var_medical.get()==''or self.var_convence.get()=='' :
            messagebox.showerror('Error','All feilds are required')
        else:
            per_day=int(self.var_basicsalary.get())/int(self.var_totaldays.get())
            work_day=int(self.var_totaldays.get())-int(self.var_absents.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_providedfund.get())
            addition=int(self.var_convence.get())
            netsalary=sal_-deduct+addition
            self.var_netsalary.set(str(round(netsalary,2)))
            #============update the recipt
            newsample=f'''\tCompany Name, XYZ\n\tAddress:Xyz , Floor4
----------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
----------------------------------------------
Total Days\t\t:  {self.var_totaldays.get()}
Total Present\t\t:  {str(int(self.var_totaldays.get())-int(self.var_absents.get()))}
Total Absent\t\t:  {self.var_absents.get()}
Convence\t\t:  Rs.{self.var_convence.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_providedfund.get()}
Gross Payment\t\t:  Rs.{self.var_basicsalary.get()}
Net salary\t\t:  Rs.{self.var_netsalary.get()}
----------------------------------------------
This is computer generated slip, not
required any signature
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,newsample)


    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to :{str(ex)}')
        
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to :{str(ex)}')


    def employee_frame(self):  
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System | Develped by Sahithi | Webcode")
        self.root2.geometry("1000x500+200+120")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        self.root2.focus_force()
        
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'doj', 'dob', 'experience', 'proof_id', 'contactno', 'address', 'bank', 'month', 'year', 'basic_salary', 't_days', 'absents', 'medical', 'pf', 'convence', 'net_salary', 'salary_recipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('doj',text='Date of Job')
        self.employee_tree.heading('dob',text='Date of Birth')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof ID')
        self.employee_tree.heading('contactno',text='Contact No')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('bank',text='Bank')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('t_days',text='Total Days')
        self.employee_tree.heading('absents',text='Absents')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='Provided Fund')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_recipt',text='Salary Recipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=150)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contactno',width=100)
        self.employee_tree.column('address',width=200)
        self.employee_tree.column('bank',width=100)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absents',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_recipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()

        self.root2.mainloop()

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file_,'print')   
root=Tk()
obj= EmployeeSystem(root)
root.mainloop()
from doctest import master
from tkinter import *
from tkinter import ttk, messagebox as mb
import mysql.connector as mysql
import qrcode
#@JOHN LLOYD D. DE SAPE

window = Tk()
#Window Title
window.title("Student Information System with Vaccination Card Status")
window.iconbitmap("sisvcs.ico")
#Window Customization
window.geometry('925x600')
window.configure(bg='#f0f0f0')
window.resizable(False, False)

#----------------------------------------------------------------------------------------------------------------------#
#Background Image of the Registration Frame
#----------------------------------------------------------------------------------------------------------------------#
registration_image = PhotoImage(file = "Background Image/register.png")
#----------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------#
#Background Image of the Login Frame
#----------------------------------------------------------------------------------------------------------------------#
login_image = PhotoImage(file = "Background Image/login.png")
#----------------------------------------------------------------------------------------------------------------------#
#@JOHN LLOYD D. DE SAPE

#----------------------------------------------------------------------------------------------------------------------#
#Background Image of the student details frame
#----------------------------------------------------------------------------------------------------------------------#
data_image = PhotoImage(file = "Background Image/bg_data.png")
#----------------------------------------------------------------------------------------------------------------------#

#@JOHN LLOYD D. DE SAPE

class App:
    
    def __init__(self, master):
        self.master = master
        self.register()
#----------------------------------------------------------------------------------------------------------------------#
    #CONNECT TO MY DATABASE "SISVCS"
#----------------------------------------------------------------------------------------------------------------------#
    global condb, mydb
    
    try:
        condb = mysql.connect(host = "localhost", user="root", password = "", database = "sisvcs")
        mydb = condb.cursor(buffered = True)
    
    except Exception as error:
        print(f"Failed!!!, {error}")
#----------------------------------------------------------------------------------------------------------------------#
#@JOHN LLOYD D. DE SAPE

    """
#----------------------------------------------------------------------------------------------------------------------#
#                                              SELECTING DATA FUNCTION                                                 #
#----------------------------------------------------------------------------------------------------------------------#
    """      
        
    def select_data(self, event):
        fname1.delete(0, END)
        stuid1.delete(0, END)
        Age1.delete(0, END)
        Gender1.delete(0, END)
        dept1.delete(0, END)
        Course1.delete(0, END)
        add1.delete(0, END)
        mobile1.delete(0, END)
        batch1.delete(0, END)
        vacm1.delete(0, END)
        dosen1.delete(0, END)
#@JOHN LLOYD D. DE SAPE        
        fname1.get()
        stuid1.get()
        Age1.get()
        Gender1.get()
        dept1.get()
        Course1.get()
        add1.get()
        mobile1.get()
        batch1.get()
        vacm1.get()
        dosen1.get()
        
        selected = tree.focus()
        values = tree.item(selected, 'values')
  #@JOHN LLOYD D. DE SAPE
      
        fname1.insert(0, values[1])
        stuid1.insert(0, values[0])
        Age1.insert(0, values[2])
        Gender1.insert(0, values[3])
        dept1.insert(0, values[4])
        Course1.insert(0, values[5])
        add1.insert(0, values[6])
        mobile1.insert(0, values[7])
        batch1.insert(0, values[8])
        vacm1.insert(0, values[9])
        dosen1.insert(0, values[10])

        
        
        
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                               UPDATING DATA FUNCTION                                                 #
#----------------------------------------------------------------------------------------------------------------------#
    """     
    def update_data(self):
        
        selected = tree.focus()
        
        
        f = fname1.get()
        s = stuid1.get()
        a = Age1.get()
        g = Gender1.get()
        d = dept1.get()
        c = Course1.get()
        ad= add1.get()
        m = mobile1.get()
        b = batch1.get()
        v = vacm1.get()
        do = dosen1.get()
        tree.item (selected, text = "", values = (s,f,a,g,d,c,ad,m,b,v,do))
        
        query_update = "UPDATE student SET fullname = %s, age = %s, gender = %s, department = %s, course = %s, address = %s, mobile_no = %s, batch_number = %s, vac_manufacturer = %s, dose_number = %s WHERE student_id = %s"
        update_value = (f,a,g,d,c,ad,m,b,v,do,s)
        
        mydb.execute(query_update, update_value)
        condb.commit()
        """
#----------------------------------------------------------------------------------------------------------------------#
#                                   NEW STUDENT'S QR CODE AFTER UPDATING THE DATA                                      #
#----------------------------------------------------------------------------------------------------------------------#
        """       
        qrcode_design = qrcode.QRCode(version=1, box_size=40, border=3)
        qrcode_design.add_data(f"""
        Eastern Visayas State University
+-------STUDENT'S DATA--------+

STUDENT ID    : {f}
FULL NAME     : {s}
AGE           : {a}
GENDER        : {g}
DEPARTMENT    : {d}
COURSE        : {c}
ADDRESS       : {ad}
MOBILE NUMBER : {m}


+------VACCINATION STATUS------+
BATCH NUMBER             : {b}
VACCINATION MANUFACTURER : {v}
DOSE NUMBER              : {do}


""")
        qrcode_design.make(fit=True)
        generate_qrcode = qrcode_design.make_image(fill_color="#000000", back_color="#9e9b9b")
        generate_qrcode.save('yournewqrcode.png')
        mb.showinfo("Success", "Student data sucessfully update")
        generate_qrcode.show()
        condb.commit()
        
        
        
        fname1.delete(0, END)
        stuid1.delete(0, END)
        Age1.delete(0, END)
        Gender1.delete(0, END)
        dept1.delete(0, END)
        Course1.delete(0, END)
        add1.delete(0, END)
        mobile1.delete(0, END)
        batch1.delete(0, END)
        vacm1.delete(0, END)
        dosen1.delete(0, END)
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
   
   
        
 #@JOHN LLOYD D. DE SAPE
       
        
        
        
        
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                               DELETING DATA FUNCTION                                                 #
#----------------------------------------------------------------------------------------------------------------------#
    """       
    
    def delete_data(self):
        selected_item=tree.selection()[0]
        print(tree.item(selected_item)['values'])
        s_id =tree.item(selected_item)['values'][0]
        delete_query = "DELETE FROM student WHERE student_id = %s"
        select_data = (s_id, )
        mydb.execute(delete_query, select_data)
        condb.commit()
        tree.delete(selected_item)
        mb.showinfo("Success", "Student data successfully deleted")
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

   
    """
#----------------------------------------------------------------------------------------------------------------------#
#                             ADDING/INSERTING DATA WITH QRCODE GENERATOR FUNCTION                                     #
#----------------------------------------------------------------------------------------------------------------------#
    """
    def add_data(self):
        fname = fullname.get()
        stuid = student_id.get()
        Age = age.get()
        Gender = gender.get()
        dept = department.get()
        Course = course.get()
        add = address.get()
        mobile = mobile_no.get()
        batch = batch_number.get()
        vacm = vac_manufacturer.get()
        dosen = dose_number.get()
#@JOHN LLOYD D. DE SAPE
        
        
        if fname == "" or stuid == "" or Age == "" or Gender == "" or dept == "" or Course == "" or add == "" or mobile == "" or batch == "" or vacm == "" or dosen == "":
            mb.showinfo("Failed", "All Fields are required")
        
        else:
            query = "INSERT INTO student(student_id, fullname, age, gender, department, course, address, mobile_no, batch_number, vac_manufacturer, dose_number) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            query_value = (stuid, fname, Age, Gender, dept, Course, add, mobile, batch, vacm, dosen)
            mydb.execute(query,query_value)
            qrcode_design = qrcode.QRCode(version=1, box_size=40, border=3)
            qrcode_design.add_data(f"""
        Eastern Visayas State University
+-------STUDENT'S DATA--------+

STUDENT ID    : {fname}
FULL NAME     : {stuid}
AGE           : {Age}
GENDER        : {Gender}
DEPARTMENT    : {dept}
COURSE        : {Course}
ADDRESS       : {add}
MOBILE NUMBER : {mobile}


+------VACCINATION STATUS------+
BATCH NUMBER             : {batch}
VACCINATION MANUFACTURER : {vacm}
DOSE NUMBER              : {dosen}


""")
            qrcode_design.make(fit=True)
            generate_qrcode = qrcode_design.make_image(fill_color="#000000", back_color="#9e9b9b")
            generate_qrcode.save('yourqrcode.png')
            mb.showinfo("Successfully Registered", "Please save your QR Code")
            generate_qrcode.show()
            condb.commit()
            
            fullname.delete(0, END)
            student_id.delete(0, END)
            age.delete(0, END)
            department.delete(0, END)
            course.delete(0, END)
            address.delete(0, END)
            mobile_no.delete(0, END)
            batch_number.delete(0, END)
            vac_manufacturer.delete(0, END)
            dose_number.delete(0, END)
            
            
            
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
#@JOHN LLOYD D. DE SAPE
#@JOHN LLOYD D. DE SAPE
           
            
    
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                           REGISTRATION FRAME FUNCTION                                                #
#----------------------------------------------------------------------------------------------------------------------#
    """
    def register(self):
        for i in self.master.winfo_children():
                i.destroy()
               #Style TTk 
        style = ttk.Style()
        style.theme_use('default')
#----------------------------------------------------------------------------------------------------------------------#        
        #Registration/Submit and Login Button Style
        style.configure('Submit.TButton', background='#6d0e0e', foreground='white', borderwidth=0, width=13,  font=('Franklin Gothic Demi', 12))
        style.map('Submit.TButton', foreground=[('active', 'white')], background=[('active', '#6d0e0e')])
 
#----------------------------------------------------------------------------------------------------------------------#       
        #Login Link Style
        style.configure('Login_link.TButton', background='white', foreground='#6d0e0e', borderwidth=0, width=8, font=('Franklin Gothic Demi', 8))
        style.map('Login_link.TButton', foreground=[('active', '#6d0e0e')], background=[('active', 'white')])
    
#----------------------------------------------------------------------------------------------------------------------#
        #GLOBAL FUNCTION SO THAT VARIABLES CAN BE CALL OUTSIDE ON THIS FUNCTION
        global fullname, student_id, age, gender, department, course, address, mobile_no, batch_number, vac_manufacturer, dose_number
        
#----------------------------------------------------------------------------------------------------------------------#
        #FRAME OF THE REGISTRATION WINDOW
        frame = Frame(window, width = 925, height = 600)
#----------------------------------------------------------------------------------------------------------------------#       
        
        #BACKGROUND IMAGE OF THE REGISTRATION FRAME
        image = Label (frame, image = registration_image)
        image.place(x=0, y=0, relwidth=1, relheight=1)
#----------------------------------------------------------------------------------------------------------------------#     
        
#@JOHN LLOYD D. DE SAPE

        """
#----------------------------------------------------------------------------------------------------------------------#
#                                        STUDENT'S DATA REGISTRATION FRAME                                             #
#----------------------------------------------------------------------------------------------------------------------#
        """  
        #STUDENT'S DATA FRAME
        
        bg_reg_frame = Frame(frame, bg="#6d0e0e",width=468, height=186)
        bg_reg_frame.place(x=37, y=200)
        reg_frame = Frame(frame, bg="#f5f5f5",width=462, height=180)
        reg_frame.place(x=40, y=203)
        
#@JOHN LLOYD D. DE SAPE
    
        
#----------------------------------------------------------------------------------------------------------------------#  
        #FULL NAME LABEL
        text= Label(reg_frame, text="FULL NAME",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        fullname = Entry(reg_frame, width=43,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(reg_frame, width=303, height=2, bg='black')
        
        text.place(x=20, y=20)
        fullname.place(x=100, y=20)
        frames.place(x=100, y=35)
#----------------------------------------------------------------------------------------------------------------------#
        #STUDENT ID LABEL
        text = Label(reg_frame, text="STUDENT ID",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        student_id = Entry(reg_frame, width=43,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(reg_frame, width=303, height=2, bg='black')
        
        text.place(x=20, y=40)
        student_id.place(x=100,y=40)
        frames.place(x=100, y=55)
#----------------------------------------------------------------------------------------------------------------------#       
#       #AGE LABEL
        text = Label(reg_frame, text="AGE",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        age = Entry(reg_frame, width=18,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(reg_frame, width=128, height=2, bg='black')

        text.place(x=20, y=60)
        age.place(x=55, y=60)
        frames.place(x=55, y=75)
 #----------------------------------------------------------------------------------------------------------------------#       
        #GENDER LABEL
        text = Label(reg_frame, text="GENDER",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        gender = Entry (reg_frame, width=23,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(reg_frame, width=163, height=2, bg='black')
        
        text.place(x=185, y=60)
        gender.place(x=240, y=60)
        frames.place(x=240, y=75)
#----------------------------------------------------------------------------------------------------------------------#        
        #DETAPARTMENT LABEL
        text = Label(reg_frame, text="DEPARTMENT",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        department = Entry(reg_frame, width=42,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(reg_frame, width=295, height=2, bg='black')

        text.place(x=20, y=80)
        department.place(x=107,y=80)
        frames.place(x=107, y=95)
 #----------------------------------------------------------------------------------------------------------------------#       
        #COURSE LABEL
        text = Label(reg_frame, text="COURSE",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        course = Entry(reg_frame, width=46,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames = Frame(reg_frame, width=323, height=2, bg='black')

        text.place(x=20, y=100)
        course.place(x=80,y=100)
        frames.place(x=80, y=115)
 #----------------------------------------------------------------------------------------------------------------------#       
        #ADDRESS LABEL
        text = Label(reg_frame, text="ADDRESS",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        address = Entry(reg_frame, width=46,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames = Frame(reg_frame, width=323, height=2, bg='black')
        
        
        text.place(x=20, y=120)
        address.place(x=80,y=120)
        frames.place(x=80, y=135)
#----------------------------------------------------------------------------------------------------------------------#        
        #MOBILE NUMBER LABEL 
        text = Label(reg_frame, text="MOBILE NUMBER",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5' )
        mobile_no = Entry(reg_frame, width=39,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames = Frame(reg_frame, width=275, height=2, bg='black')

        text.place(x=20, y=140)
        mobile_no.place(x=129,y=140)
        frames.place(x=129, y=155)
#----------------------------------------------------------------------------------------------------------------------#

        """
#----------------------------------------------------------------------------------------------------------------------#
#                                               VACCINATION STATUS FRAME                                               #
#----------------------------------------------------------------------------------------------------------------------#
        """
        bg_vac_frame = Frame(frame, bg="#6d0e0e",width=468, height=101)
        bg_vac_frame.place(x=37, y=421)
        vac_frame = Frame(frame, bg="#f5f5f5",width=462, height=95)
        vac_frame.place(x=40, y=424)      
#----------------------------------------------------------------------------------------------------------------------# 
        #BATCH NUMBER
        text= Label(vac_frame, text="BATCH NUMBER",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        batch_number = Entry(vac_frame, width=40,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(vac_frame, width=282, height=2, bg='black')
        
        text.place(x=20, y=20)
        batch_number.place(x=124, y=20)
        frames.place(x=124, y=35)
#----------------------------------------------------------------------------------------------------------------------# 
        #BRAND/MANUFACTURER
        text= Label(vac_frame, text="BRAND/MANUFACTURER",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        vac_manufacturer = Entry(vac_frame, width=33,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(vac_frame, width=233, height=2, bg='black')
        
        text.place(x=20, y=40)
        vac_manufacturer.place(x=173, y=40)
        frames.place(x=173, y=55)
#----------------------------------------------------------------------------------------------------------------------# 
        #DOSE NUMBER
        text= Label(vac_frame, text="DOSE NUMBER",fg='black', font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        dose_number = Entry(vac_frame, width=40,fg='black',border=0, font=('Franklin Gothic Demi', 8, 'bold'), bg='#f5f5f5')
        frames=Frame(vac_frame, width=282, height=2, bg='black')

        text.place(x=20, y=60)
        dose_number.place(x=124, y=60)
        frames.place(x=124, y=75)
#----------------------------------------------------------------------------------------------------------------------#
        #SUBMIT BUTTON       
        btn_submit = ttk.Button(frame,style="Submit.TButton", text="SUBMIT", cursor="hand2",command=self.add_data)
        btn_submit.place(x=203, y=528)
#----------------------------------------------------------------------------------------------------------------------#
        #LOGIN HYPERLINK BUTTON
        login_link = ttk.Button(frame,style="Login_link.TButton", text="Log In", cursor="hand2",command=self.login)
        frames = Frame(login_link, width=30, height=2, bg='black')

     
        frames.place(x=13, y=18)
        login_link.place(x=235, y=560)
#----------------------------------------------------------------------------------------------------------------------#     
#@JOHN LLOYD D. DE SAPE
        
        frame.pack()
#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

    
    
    
#@JOHN LLOYD D. DE SAPE
    
#@JOHN LLOYD D. DE SAPE
        
#@JOHN LLOYD D. DE SAPE

        
    
    

                


    """
#----------------------------------------------------------------------------------------------------------------------#
#                                            STUDENT'S DATA/ADMIN'S SESSION                                            #
#----------------------------------------------------------------------------------------------------------------------#
    """
    
    def database(self):
     
        #DESTROY THE CURENT FRAME
        for i in self.master.winfo_children():
            i.destroy()
    
   
        global fname1, stuid1, Age1, Gender1, dept1, Course1, add1, mobile1, batch1, vacm1, dosen1, tree
        frame = Frame(window, width=925, height=600)
 #----------------------------------------------------------------------------------------------------------------------#       
        #BACKGROUND IMAGE OF THE LOGIN FRAME
        image = Label (frame, image = data_image )
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        frame_data = Frame(frame, width=600, height=315, bg="#6d0e0e")
        
        frame_data.place(x=298, y=163)
       
        mydb.execute("SELECT * FROM student ORDER BY course DESC")
        
        tree=ttk.Treeview(frame_data, height=15)
        tree['show'] = 'headings'
        
    
        style = ttk.Style(frame_data)
        style.theme_use('clam')
        style.configure("Treeview.Heading", foreground='black',background=['yellow'],bordercolor=['yellow'],border=2,font=('Helvetica', 8,"bold"))
        style.configure(".",font=('Helvetica', 6, 'bold') )


 #----------------------------------------------------------------------------------------------------------------------#       
        #Data buttons Style
        style.configure('Data.TButton', background='#6d0e0e', foreground='white', borderwidth=0, width=11,  font=('Franklin Gothic Demi', 13, ))
        style.map('Data.TButton', foreground=[('active', 'white')], background=[('active', '#6d0e0e')])
        
        tree["columns"]=("student_id","fullname", "age","gender","department","course","address","mobile_no","batch_number","vac_manufacturer","dose_number")
#----------------------------------------------------------------------------------------------------------------------#     
        #Assign the width,minwidth and anchor to the respective columns
        tree.column("student_id", width=50, minwidth=50, anchor="center")
        tree.column("fullname", width=70, minwidth=30, anchor="center")
        tree.column("age", width=20, minwidth=30, anchor="center")
        tree.column("gender",width=25, minwidth=30, anchor="center")
        tree.column("department",width=70, minwidth=30, anchor="center")
        tree.column("course", width=80, minwidth= 30, anchor="center")
        tree.column("address",width=80, minwidth=40, anchor="center")
        tree.column("mobile_no",width=30, minwidth=20, anchor="center")
        tree.column("batch_number",width=30, minwidth=20, anchor="center")
        tree.column("vac_manufacturer",width=40, minwidth=30, anchor="center")
        tree.column("dose_number",width=100, minwidth=20, anchor="center")
#----------------------------------------------------------------------------------------------------------------------#
        #Assign the heading names to the respective columns
        tree.heading("student_id", text="STUDENT ID", anchor="center")
        tree.heading("fullname", text="FULLNAME" ,anchor="center")
        tree.heading("age", text="AGE", anchor="center")
        tree.heading("gender", text="GENDER", anchor="center")
        tree.heading("department", text="DEPARTMENT", anchor="center")
        tree.heading("course", text="COURSE", anchor="center")
        tree.heading("address", text="ADDRESS", anchor="center")
        tree.heading("mobile_no", text="MOBILE NUMBER", anchor="center")
        tree.heading("batch_number", text="BATCH NUMBER", anchor="center")
        tree.heading("vac_manufacturer", text="VAC MANUFACTURER", anchor="center")
        tree.heading("dose_number", text="DOSE NUMBER", anchor="center")
        
        #SHOWS THE STUDENTS DATA FROM THE DATABASE
      
#@JOHN LLOYD D. DE SAPE
#@JOHN LLOYD D. DE SAPE
            
      
                
        i = 1
        for ro in mydb:
            tree.insert('', i, text="",values=(ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11]),tags=("color",))
            
            i=+1 
       
        tree.tag_configure("color",foreground="black",background="#f5f5f5")
     
        
      
        ##d9d9d9
        fname1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        fname1.place(x=34, y=110)
        
        stuid1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        stuid1.place(x=34, y=159)
        
        Age1 = Entry(frame, width=12,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        Age1.place(x=34, y=203)
        
        Gender1 = Entry(frame, width=16, border=0,font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        Gender1.place(x=149, y=203)
        
        
        dept1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        dept1.place(x=34, y=248)
        
        Course1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        Course1.place(x=34, y=294)
        
        add1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        add1.place(x=34, y=341)
        
        mobile1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        mobile1.place(x=34, y=387)
        
        
        batch1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        batch1.place(x=34, y=433)
        
        vacm1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        vacm1.place(x=34, y=480)

        dosen1 = Entry(frame, width=30,border=0, font=('Franklin Gothic Demi', 10), bg='#f5f5f5')
        dosen1.place(x=34, y=526)
        
        """
#----------------------------------------------------------------------------------------------------------------------#
#                                            SEARCH BY STUDENT ID ENTRY FUNCTION                                       #
#----------------------------------------------------------------------------------------------------------------------#
"""     
        def search(ev):
            mydb.execute("SELECT * FROM student WHERE student_id LIKE '%"+var_search.get()+"%'")
            row = mydb.fetchall()
            
            if len(row)>0:
                tree.delete(*tree.get_children())
                for i in row:
                    tree.insert('', 'end', text="",values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]),tags=("color",))
                tree.tag_configure("color",foreground="black",background="#f5f5f5")
            
            else:
                tree.delete(*tree.get_children())
        
        
        var_search = StringVar()
        search_entry= Entry(frame,textvariable=var_search, width=27,border=0, font=('Franklin Gothic Demi', 12), bg='#f5f5f5')
        search_entry.place(x=647, y=116)
        search_entry.bind('<Key>', search)
        
 #----------------------------------------------------------------------------------------------------------------------#       
    
#@JOHN LLOYD D. DE SAPE
#@JOHN LLOYD D. DE SAPE
        
        
        
 #----------------------------------------------------------------------------------------------------------------------#       
         #SUBMIT BUTTON       
        btn_update = ttk.Button(frame,style="Data.TButton", text="UPDATE", cursor="hand2",command=self.update_data)
        btn_update.place(x=360, y=505)
        
        btn_delete = ttk.Button(frame,style="Data.TButton", text="DELETE", cursor="hand2",command=self.delete_data)
        btn_delete.place(x=490, y=505)
        
        btn_logout = ttk.Button(frame,style="Data.TButton", text="LOGOUT", cursor="hand2",command=self.ask_admin)
        btn_logout.place(x=620, y=505)
                
        vsb = ttk.Scrollbar(frame_data,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)     
        
        tree.bind ('<ButtonRelease-1>', self.select_data)
        tree.pack()
        
        frame.pack() 
 #----------------------------------------------------------------------------------------------------------------------#       
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                            ADMIN AUTHENTICATION  FUNCTION                                            #
#----------------------------------------------------------------------------------------------------------------------#
    """
    def authentication(self):
        user_admin = username.get()
        password_admin = password.get()
        query_login = "SELECT * FROM admin WHERE username = %s AND password = %s"
        mydb.execute(query_login, (user_admin, password_admin))
        result = mydb.fetchall()
        
        if result:
            mb.showinfo("Success", "Successfully Login")
            self.database()
        else:
            mb.showerror("Login Failed", "Credentials Error")
            
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                           ASKING ADMIN TO LOGOUT FUNCTION                                            #
#----------------------------------------------------------------------------------------------------------------------#
    """            
        
    def ask_admin(self):
        message=mb.askyesno("Hello Admin","Are you sure do you want to logout?")
        
        if message:
            self.login()
        else:
            self.database()
        
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                            SHOW AND HIDE PASSWORD FUNCTION                                           #
#----------------------------------------------------------------------------------------------------------------------#
    """

    def show_password(self):
        if password.cget('show')=='*':
            password.config(show='')
        else:
            password.config(show='*')
    
    """
#----------------------------------------------------------------------------------------------------------------------#
#                                               LOGIN FRAME FUNCTION                                                   #
#----------------------------------------------------------------------------------------------------------------------#
    """
    def login(self):
        #DESTROY THE CURENT FRAME
        for i in self.master.winfo_children():
            i.destroy()
        #Style TTk 
        style = ttk.Style()
        style.theme_use('default')
        
    
        #Back Link Style
        style.configure('Back.TButton', background='white', foreground='#6d0e0e', borderwidth=0, width=8, font=('Franklin Gothic Demi', 8))
        style.map('Back.TButton', foreground=[('active', '#6d0e0e')], background=[('active', 'white')])
        
        global username, password
        #SIZE OF THE LOGIN FRAME FUNCTION 
        frame = Frame(window, width = 925, height = 600)
        
        #BACKGROUND IMAGE OF THE LOGIN FRAME
        image = Label (frame, image = login_image )
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
#@JOHN LLOYD D. DE SAPE
        
        #FRAME FOR USERNAME AND PASSWORD FRAME
        bg_login_frame = Frame(frame, bg="#6d0e0e",width=341, height=196)
        login_frame = Frame(frame, width = 335, height =190, bg = "#f5f5f5")
        bg_login_frame.place(x=525, y=222)
        login_frame.place(x=528, y=225)
        
        #USERNAME LABEL
        text = Label(login_frame,text="USERNAME",fg='black', font=('Franklin Gothic Demi', 15, 'bold'), bg='#f5f5f5')
        username = Entry(login_frame, width=30,fg='black', border=0,font=('Franklin Gothic Demi', 12, ), bg='#f5f5f5')
        line=Frame(username, width=300, height=2, bg='black')

        
        text.place(x=20, y=23)
        username.place(x=15, y=55)
        line.place(x=0, y=20)
        
        #PASSWORD LABEL
        text = Label(login_frame,text="PASSWORD",fg='black', font=('Franklin Gothic Demi', 15, 'bold'), bg='#f5f5f5')
        password = Entry(login_frame, width=30,fg='black', border=0,show='*',font=('Franklin Gothic Demi', 12, ), bg='#f5f5f5')
        line=Frame(password, width=300, height=2, bg='black')
        
        
        text.place(x=20, y=83)
        password.place(x=15, y=115)
        line.place(x=0, y=20)
        
        #SHOW PASSWORD USING CHECK BUTTON
        show_pwd = Checkbutton(login_frame, text="show password", command=self.show_password, bg='#f5f5f5')
        show_pwd.place(x=15, y=150)
        
        
        #LOGIN BUTTON       
        btn_login = ttk.Button(frame,style="Submit.TButton", text="LOG IN", cursor="hand2", command=self.authentication)
        btn_login.place(x=632, y=442)
        
        #BACK BUTTON
        btn_back = ttk.Button(frame,style="Back.TButton", text="Back", cursor="hand2",command=self.register)
        btn_back.place(x=665, y=475)
        
        line = Frame(btn_back, width=25, height=2, bg='black')
        line.place(x=15, y=18)
        
        frame.pack()
   
        
        

App(window)
#@JOHN LLOYD D. DE SAPE

window.mainloop()
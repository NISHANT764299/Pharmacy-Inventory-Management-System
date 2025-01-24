from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Entry

class PharamacyManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System ")
        self.root.geometry("1550x800+0+0")
        
        #=========Add Variables========
        self.refMed_var = StringVar()
        self.addmed_var = StringVar()
        
        # ==========main variable=====

        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        #==========Create a title==========
        
        lab_title = Label(self.root,text="PHARAMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                        bg='white',fg = 'darkgreen',font =("times new roman",40,"bold"),padx =2,pady=4)
        
        lab_title.pack(side = TOP,fill = X)
        
        
        img1 = Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\medical-cross-and-health-pharmacylogo.jpg")
                
        img1=img1.resize((80,60), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1, borderwidth=0)
        b1.place(x=70, y = 20)
        
        
        #=======Dataframe=========
        DataFrame =Frame(self.root, bd=15, relief= RIDGE, padx=20)
        DataFrame.place (x=0,y=100, width=1280,height=350)
        
        
        DataFrameLeft=LabelFrame(DataFrame, bd = 10, relief=RIDGE, padx=20, text="Medicine Information",
                                 fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place( x = 0, y = 5 ,width=800, height = 300 )
        
        DataFramerRight = LabelFrame(DataFrame, bd = 10 ,relief=RIDGE, padx=20, text="Medicine Add Department", 
                                   fg="darkgreen", font=("arial", 12, "bold"))
        DataFramerRight.place( x = 810, y = 5 ,width=400, height=300)
        
        
                #=========button============
                
        ButtonFrame=Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0,y=450, width=1280,height=65)

        #====================Main Button======

        btnAddData=Button(ButtonFrame, text="Medicine Add", font=("arial", 12, "bold"), bg="darkgreen", fg="white",command=self.add_data) 
        btnAddData.grid(row=0,column=0)
        btnUpdateMed=Button (ButtonFrame, text="UPDATE", font=("arial", 13, "bold"), width=12, bg="darkgreen", fg="white",command=self.Update_data) 
        btnUpdateMed.grid(row=0,column=1)
        btnDeleteMed=Button (ButtonFrame, text="DELETE", font=("arial", 13, "bold"), width=12,bg="red", fg="white",command=self.delete) 
        btnDeleteMed.grid(row=0,column=2)
        btnRestMed=Button (ButtonFrame, text="RESET", font=("arial", 13, "bold"), width=12, bg="darkgreen", fg="white",command=self.reset) 
        btnRestMed.grid(row=0,column=3)
        btnExitMed=Button( ButtonFrame, text="EXIT", font=("arial", 13, "bold"), width=12, bg="darkgreen", fg="white",command=self.Exit_app) 
        btnExitMed.grid(row=0,column=4)

        # ==========Search By========

        lblSearch=Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white") 
        lblSearch.grid(row=0, column=5, sticky=W)
        
        #variable
        self.search_var = StringVar()
        serch_combo = ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=8,font=("arial", 17, "bold"),state="readonly")
        serch_combo["values"] = ("Ref_no","MedName","LotNo")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)
        
        
        self.searchtex_var = StringVar()
        txtSerch= Entry(ButtonFrame,bd=3,textvariable=self.searchtex_var,relief=RIDGE, width=10, font=("arial", 17, "bold"))
        txtSerch.grid(row = 0,column=7)
        searchBtn=Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=8,bg="darkgreen", fg="white",command=self.Search_data)
        searchBtn.grid(row=0,column=8)
        showAll=Button(ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=10,bg="darkgreen", fg="white",command=self.fatch_data)
        showAll.grid(row=0,column=9)

        #=========label and entry========

        lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno.grid(row=0,column=0, sticky=W)
        
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref_no from m_and_ddata")
        ref_n = my_cursor.fetchall()
        

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var, width=25,font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]= ref_n
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)


        lblCepName=Label(DataFrameLeft,font=("arial", 12, "bold"), text="Company Name:",padx=2,pady=6)
        lblCepName.grid(row =1,column=0,sticky=W)

        txtCepName= Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial", 13, "bold"),bg="white", bd =2, relief= RIDGE,width=27)
        txtCepName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"), text="Type Of Medicine", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",font=("arial", 12, "bold"), width=25)
        comTypeofMedicine["value"]=("Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row =2, column=1)       

        #======AddMedicine==========

        IblMedicineName=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=6)
        IblMedicineName.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from m_and_ddata")
        med = my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",font=("arial", 12, "bold"), width=25)

        comMedicineName['value']= med
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2,pady=6)
        lblLotNo.grid(row=4,column=0, sticky=W)
        txtLotNo =Entry(DataFrameLeft,textvariable=self.lot_var, font=("arial", 13, "bold"), bg="white", bd=2,relief=RIDGE,width=27)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate= Label (DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0, sticky=W)
        txtIssueDate =Entry (DataFrameLeft,textvariable=self.issuedate_var,font=("arial", 13, "bold"), bg="white",bd =2,relief= RIDGE,width=27)
        txtIssueDate.grid(row=5,column=1)

        lblExDate= Label (DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2,pady=6)
        lblExDate.grid(row=6,column=0, sticky=W)
        txtExDate =Entry(DataFrameLeft,textvariable=self.expdate_var, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=27)
        txtExDate.grid(row=6,column=1)


        lbluses =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:",padx=2,pady=4)
        lbluses.grid(row=7,column=0, sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial", 13, "bold"), bg="white",bd=2,relief =RIDGE, width=27)
        txtUses.grid(row=7,column=1)

        lb1PrecWarning =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&warning:",padx=15)
        lb1PrecWarning.grid(row=0,column=2, sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var, font=("arial", 12, "bold"), bg="white", bd =2, relief=RIDGE,width=23)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial", 12, "bold"), text="Dosage:",padx=15, pady=6)
        lblDosage.grid(row=1,column=2, sticky=W)
        txtDosage =Entry (DataFrameLeft,textvariable=self.dosage_var, font=("arial", 12, "bold"), bg="white", bd=2,relief=RIDGE, width=23)
        txtDosage.grid(row=1,column=3)

        lblPrice =Label(DataFrameLeft,font=("arial", 12, "bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2, sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var, font=("arial", 12, "bold"), bg="white",bd=2,relief=RIDGE,width=23)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt =Entry(DataFrameLeft,textvariable=self.product_var,font=("arial", 12, "bold"), bg="white",bd =2, relief =RIDGE, width=23)
        txtProductQt.grid(row=3,column=3,)
        
        #==============Image=================
                
        lblhome=Label(DataFrameLeft, font=("arial", 15, "bold"), text="Stay Home Stay Safe",
                      padx=2, pady=6, bg="white", fg="orange")
        lblhome.place(x=450,y=130)
        
        img2=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\images (2).jpeg")
        img2=img2.resize((120,100),Image.LANCZOS)
        self.photoimg2 =ImageTk.PhotoImage(img2)
        bl=Button(self.root,image=self.photoimg2,borderwidth=0)
        bl.place(x=460,y=310)
        
        
        img3=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\images (1).jpeg")
        img3=img3.resize((120,100),Image.LANCZOS)
        self.photoimg3 =ImageTk.PhotoImage(img3)
        bl=Button(self.root,image=self.photoimg3,borderwidth=0)
        bl.place(x=580,y=310)

        
        img4=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\images.jpeg")
        img4=img4.resize((120,100),Image.LANCZOS)
        self.photoimg4 =ImageTk.PhotoImage(img4)
        bl=Button(self.root,image=self.photoimg4,borderwidth=0)
        bl.place(x=700,y=310)


    #=============rightSideImage==========

        img5=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\download (2).jpeg")
        img5=img5.resize((122,80), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        bl=Button(self.root,image=self.photoimg5, borderwidth=0)
        bl.place(x=860,y=140)

        img6=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\download.jpeg")
        img6=img6.resize((122,80), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        bl=Button(self.root,image=self.photoimg6, borderwidth=0)
        bl.place(x=982,y=140)

        img7=Image.open("C:\\Users\\nisha\\OneDrive\\Desktop\\potato detection\\py_sql\\download (1).jpeg")
        img7=img7.resize((129,130), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        bl=Button(self.root,image=self.photoimg7, borderwidth=0)
        bl.place(x=1104,y=140)
        
                
        lblrefno=Label(DataFramerRight,font=("arial", 10, "bold"), text="Reference No:")
        lblrefno.place(x=0,y=82)
        txtrefno=Entry(DataFramerRight,textvariable=self.refMed_var,font=("arial", 12, "bold"), bg="white",bd =2,relief= RIDGE,width=12)
        txtrefno.place(x=110,y=80)

        lblmedName =Label(DataFramerRight,font=("arial", 10, "bold"), text="Medicine Name:")
        lblmedName.place(x=0,y=112)
        txtmedName= Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial", 12, "bold"), bg="white",bd=2,relief=RIDGE,width=12)
        txtmedName.place(x=110,y=110)

        #===============side frame===============

        side_frame =Frame(DataFramerRight,bd=4,relief =RIDGE,bg="white")
        side_frame.place(x=0,y=140,width =223,height=130)
        
        
        # sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        # sc_x.pack(side=BOTTOM, fill=X) 
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, columns=("ref", "medname"), 
                                         yscrollcommand=sc_y.set)

        #sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name") 

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=80)
        self.medicine_table.column("medname", width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)


        
        
    #===============Medicine Add Button================

        down_frame= Frame(DataFramerRight, relief =RIDGE,bg="darkgreen")
        down_frame.place(x=240,y=140,width=100, height=120)

        btnAddmed=Button(down_frame, text="ADD", font=("arial", 10, "bold"), width=12,bg="lime", fg="white", pady=2,command=self.AddMed)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed =Button(down_frame, text="UPDATE", font=("arial", 10, "bold"), width=12,bg="purple",fg="white", pady=2,command=self.update_med)
        btnUpdatemed.grid(row=1,column=0)

        btrDeletemed=Button(down_frame, text="DELETE", font=("arial", 10, "bold"), width=12,bg="red", fg="white", pady=2,command=self.Delete_med)
        btrDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame, text="CLEAR", font=("arial", 10, "bold"), width=12,bg="orange", fg="white", pady=2,command=self.Clear_med)
        btnClearmed.grid(row=3,column=0) 
        
        
        
        #============Dataframe Details=============
        Framedetails = Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place (x=0,y=508, width=1280,height=130)
        
        scroll_x = ttk.Scrollbar(Framedetails, orient="horizontal")
        scroll_x.pack(side="bottom", fill="x")

        scroll_y = ttk.Scrollbar(Framedetails, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        self.pharmacy_table = ttk.Treeview(
            Framedetails, 
            columns=("reg", "companyname", "type", "tabletname", "lotno", "issueda",
                    "expdate", "uses", "warning", "dosage", "price", "productqt"),
            xscrollcommand=scroll_x.set, 
            yscrollcommand=scroll_y.set
        )

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table.heading("reg", text="Registration No.")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No.")
        self.pharmacy_table.heading("issueda", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Expiry Date")
        self.pharmacy_table.heading("uses", text="Uses")
        #self.pharmacy_table.heading("sideeffect", text="Side Effects")
        self.pharmacy_table.heading("warning", text="Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Quantity")

        self.pharmacy_table.column("reg", width=100)
        self.pharmacy_table.column("companyname", width=150)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletname", width=150)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issueda", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=150)
       # self.pharmacy_table.column("sideeffect", width=150)
        self.pharmacy_table.column("warning", width=150)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)
        
        self.pharmacy_table['show'] = 'headings'

        self.pharmacy_table.pack(fill="both", expand=1)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        

                        
            
        #==================Add Medicine Functionality Declaration=============
        
    
    def AddMed(self):
        self.mediname = self.addmed_var.get()
        self.ref_no =  self.refMed_var.get()
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into m_and_ddata values(%s, %s)",(self.ref_no,self.mediname))

        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")
        
            
            
    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from m_and_ddata")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
                conn.commit()
            conn.close()
            
    def Medget_cursor(self,event = ""):
        self.ref_no = self.refMed_var
        self.medname = self.addmed_var
        cursor_row=self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content.get("values", [])
        self.ref_no.set(row[0])
        self.medname.set(row[1])
        
    def update_med(self):
        self.mediname = self.addmed_var.get()
        self.ref_no =  self.refMed_var.get()
        if self.refMed_var.get()=="" or self.refMed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
            my_cursor=conn.cursor()
            my_cursor.execute("update m_and_ddata set MedName = %s where Ref_no = %s",(self.mediname,self.ref_no))
            
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            
            messagebox.showinfo("Success","Medicine has been Updated")
            
    def Delete_med(self):
        ref_no = self.refMed_var.get()
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        sql = "delete from m_and_ddata where Ref_no=%s"
        val = (ref_no,)
        my_cursor.execute(sql,val)
        
        conn.commit()  
        self.fetch_dataMed()
        conn.close()
        
        messagebox.showinfo("Success","Medicine has been Deleted")
        
    def Clear_med(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
        
        
#============Main Table Data=============
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
            my_cursor=conn.cursor()

            my_cursor.execute("insert into pharamacy_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", (
                                                                                                        self.ref_var.get(),
                                                                                                        self.cmpName_var.get(),
                                                                                                        self.typeMed_var.get(),
                                                                                                        self.medName_var.get(),
                                                                                                        self.lot_var.get(),
                                                                                                        self.issuedate_var.get(),
                                                                                                        self.expdate_var.get(),
                                                                                                        self.uses_var.get(),
                                                                                                        self.warning_var.get(),
                                                                                                        self.dosage_var.get(),
                                                                                                        self.price_var.get(),
                                                                                                        self.product_var.get()
                                                                                            ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "data has been inserted")
    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharamacy_data")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        #self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        #self.typeMed_var.set(row[2]),
        #self.medName_var.set(row[3]),
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.warning_var.set(row[8]),
        self.dosage_var.set(row[9]),
        self.price_var.set(row[10]),
        self.product_var.set(row[11])


         
    def delete(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        
        sql="delete from pharamacy_data where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql, val)


        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Delete", "Info deleted successed")   



    def reset(self):
        self.cmpName_var.set("");
        # self.ref_var.set(""),
        # self.typeMed_var.set(""),
        #self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")
        
    def Update_data(self):
        self.cmpName =self.cmpName_var.get()
        self.typeMed =self.typeMed_var.get()
        self.medName =self.medName_var.get()
        self.lot =self.lot_var.get()
        self.issuedate =self.issuedate_var.get()
        self.expdate =self.expdate_var.get()
        self.uses =self.uses_var.get()
        self.warning=self.warning_var.get()
        self.dosage=self.dosage_var.get()
        self.price =self.price_var.get()
        self.product =self.product_var.get()
        self.ref_N =self.ref_var.get()
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        my_cursor.execute("""
            UPDATE pharamacy_data 
            SET CmpName=%s, TypeMed=%s, MedName=%s, LotNo=%s, IssueDate=%s, ExpDate=%s, 
                Uses=%s, Warning=%s, Dosage=%s, Price=%s, Product=%s 
            WHERE Ref_no=%s
        """, (
            self.cmpName,
            self.typeMed,
            self.medName,
            self.lot,
            self.issuedate,
            self.expdate,
            self.uses,
            self.warning,
            self.dosage,
            self.price,
            self.product,
            self.ref_N
        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated succssfully")
        
        
    def Search_data(self):
        search_column = self.search_var.get()
        search_text = self.searchtex_var.get()
        conn=mysql.connector.connect(host="localhost", username="root", password="Nishant@123", database="pharamacy_database")
        my_cursor=conn.cursor()
        query = "SELECT * FROM pharamacy_data WHERE " + search_column + " LIKE %s"
        my_cursor.execute(query, ('%' + search_text + '%',))
        row = my_cursor.fetchall()
        
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    
    def Exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.destroy()
        
        
    
            
            
            
            
            
if __name__ == "__main__":
    root = Tk()
    obj = PharamacyManagementSystem(root)
    root.mainloop()    
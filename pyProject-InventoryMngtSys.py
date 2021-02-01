#import modules
from tkinter import *
import sqlite3

#class for front end UI(user interface)
class Product:

    def __init__(self,root):
        #create object reference instance of Database class as p
        p =Database()
        p.conn()
        
        self.root = root
        self.root.title('WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM')
        self.root.geometry('1325x690')
        self.root.config(bg='pink')

        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()

        '''Create the frame'''
        MainFrame = Frame(self.root, bg='red')
        MainFrame.grid()
        HeadFrame = Frame(MainFrame, bd=2, padx=20, pady=10, bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)
        ITilte = Label(HeadFrame, font=('arial',50,'bold'), fg='red', text='  Warehouse Inventory Sales Purchase ', bg='white').grid()

        OperationFrame = Frame(MainFrame, bd=2, width=1100, height=60, padx=50, pady=20, bg='white', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame, bd=2, width=1290, height=400, padx=30, pady=20, bg='white', relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame, bd=2, width=400, height=380, padx=36, pady=10, bg='pink', relief=RIDGE,
                                   font=('arial',15,'bold'), text='Product Item Detail:')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame, bd=2, width=300, height=380, padx=20, pady=10, bg='pink', relief=RIDGE,
                                    font=('arial',15,'bold'), text='Product Item Information:')
        RightBodyFrame.pack(side=RIGHT)

        '''add the widgets to LeftBodyFrame'''

        self.labelpID = Label(LeftBodyFrame, font=('arial',15,'bold'), text='Product Id', padx=2, pady=2, bg='white', fg='blue')
        self.labelpID.grid(row=0,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pId, width=35)
        self.txtpID.grid(row=0,column=1,sticky=W)

        self.labelpName = Label(LeftBodyFrame, font=('arial',15,'bold'), text='Product Name', padx=2, pady=2, bg='white', fg='blue')
        self.labelpName.grid(row=1,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pName, width=35)
        self.txtpID.grid(row=1,column=1,sticky=W)

        self.labelpPrice = Label(LeftBodyFrame, font=('arial',15,'bold'), text='Product price: ', padx=2, pady=2, bg='white', fg='blue')
        self.labelpPrice.grid(row=2,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pPrice, width=35)
        self.txtpID.grid(row=2,column=1,sticky=W)

        self.labelpQty = Label(LeftBodyFrame, font=('arial',15,'bold'), text='Product quantity: ', padx=2, pady=2, bg='white', fg='blue')
        self.labelpQty.grid(row=3,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pQty, width=35)
        self.txtpID.grid(row=3,column=1,sticky=W)

        self.labelpCompony =Label(LeftBodyFrame, font=('arial',15,'bold'), text='Manufacturarer Compony: ', padx=2, pady=2, bg='white', fg='blue')
        self.labelpCompony.grid(row=4,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pCompany, width=35)
        self.txtpID.grid(row=4,column=1,sticky=W)

        self.labelpContact = Label(LeftBodyFrame, font=('arial',15,'bold'), text='Contacts: ', padx=2, pady=2, bg='white', fg='blue')
        self.labelpContact.grid(row=5,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'), textvariable=pContact, width=35)
        self.txtpID.grid(row=5,column=1,sticky=W)

        self.labelC1 = Label(LeftBodyFrame, padx=2, pady=2, bg='pink')
        self.labelC1.grid(row=6,column=0,sticky=W)

        self.labelC2 = Label(LeftBodyFrame, padx=2, pady=2, bg='pink')
        self.labelC2.grid(row=7,column=0,sticky=W)

        self.labelC3 = Label(LeftBodyFrame, padx=2, pady=2, bg='pink')
        self.labelC3.grid(row=8,column=0,sticky=W)

        self.labelC4 = Label(LeftBodyFrame, padx=2, pady=2, bg='pink')
        self.labelC4.grid(row=9,column=0,sticky=W)

        self.labelC5 = Label(LeftBodyFrame, padx=2, pady=2, bg='pink')
        self.labelC5.grid(row=10,column=0,sticky=W)

        ''' add scoll bar'''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column=1, sticky='ns')

        '''list box'''
        productList = Listbox(RightBodyFrame, width=40, height=16, font=('arial',12,'bold'),yscrollcommand=scroll.set)
        productList.grid(row=0, column=0, padx=8)
        scroll.config(command=productList.yview)

        ''' add bottons to Operation frame'''
        self.buttonSave = Button(OperationFrame, text='Save', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonSave.grid(row=0, column=0)
        
        self.buttonShowData = Button(OperationFrame, text='Show Data', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonShowData.grid(row=0, column=1)
        
        self.buttonClear = Button(OperationFrame, text='Reset', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonClear.grid(row=0, column=2)
        
        self.buttonDel = Button(OperationFrame, text='Delete', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonDel.grid(row=0, column=3)
        
        self.buttonSearch = Button(OperationFrame, text='Search', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonSearch.grid(row=0, column=4)

        self.buttonUpdate = Button(OperationFrame, text='Update', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonUpdate.grid(row=0, column=5)
        
        self.buttonClose = Button(OperationFrame, text='close', font=('arial',14,'bold'),height=1, width=10, bd=4)
        self.buttonClose.grid(row=0, column=6)


# Back End Databases Operations
class Database:
    def conn(self):
        print('database : connection mathod called')
        con = sqlite3.connect('inventory.db')
        cursor = con.cursor()
        query = (' create table if not exists product(pid integer primery key,\
                pname text, qty text, compony text, contact bigint)')
        cursor.execute(query)
        con.commit()
        con.close()
        print('database : connection mathod finished')

    def insert(self, pid,name,price,qty,company,contact):
        print('database : insert mathod called')
        con = sqlite3.connect('inventory.db')
        cursor = con.cursor()
        query =  ('insert into product values(?,?,?,?,?,?)')
        cursor.execute(query,(pid,pname,price,qty,company,contact))
        con.commit()
        con.close()
        print('Database : insert method finished\n')
                
    def show(self):
        print('database : show method called')
        con = sqlite3.connect('inventory.db')
        cursor = con.cursor()
        query = ('select * from product') #it gives inthe form of rows need to fetch after execute 
        cursor.execute(query)
        rows = cursor.fetchall()
        con.commit()
        con.close()
        print('database : show method finished\n')
        return rows

    def delete(self):
        print('database : show method called',pid)
        con = sqlite3.connect('inventory.db')
        cursor = con.cursor()
        query = ('delete from product where pid=?', (pid,))
        cursor.execute(query)
        con.commit()
        con.close()
        print(pid,'database : show method fiinished\n')

    def search(self,pid='',pname='',price='',qty='',company='',contact=''):
        print('database : search method called',pid)
        con = sqlite3.connect('inventory.db')
        cursor =con.cursor()
        query = ('select * from product where pid=? or pname=? or price=? or \
                    qty=? or compony =? or contact =?')
        cursor.execute(query)
        row = cursor.fetchall()
        con.close()
        print(pid,'database : search method called')
        return row


    def update(self,pid='',pname='',price='',qty='',company='',contact=''):
        print('database : update method called',pid)
        con = sqlite3.connect('inventory.db')
        cursor =con.cursor()
        query = ('update product set  pid=? or pname=? or price=? or \
                    qty=? or compony =? or contact =? where pid =?',(pid,pname,price,qty,company,
                                                                     contact,pid))
    
        cursor.execute(query)
        con.commit()
        con.close()
        print(pid,'database : update method called')



















        
if __name__ == '__main__':
    root=Tk()
    application = Product(root)
    root.mainloop()
    

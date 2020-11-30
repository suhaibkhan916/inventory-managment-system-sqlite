from tkinter.filedialog import asksaveasfile
from tkinter import *
from tkinter import messagebox,filedialog
import time
import random
from tkinter import Toplevel
from tkinter.ttk import Treeview
from tkinter import ttk
import sqlite3
import pandas
import csv
import os
import tempfile
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont, pdfmetrics
from reportlab.lib import colors
mydata=[]
def tick():
    time_string=time.strftime('%H:%M:%S')
    date_string=time.strftime('%d:%m,%y')
    clock.config(text='Date:'+date_string+"\n"+'Time:'+time_string)
    clock.after(200,tick)
def introlabelcolors():
    colors = [ 'green', 'blue', 'cyan', 'black']
    fg=random.choice(colors)
    title.config(fg=fg)
    title.after(200,introlabelcolors)
def introlabeltick():
    global count ,text
    if count>=len(ss):
        count= 0
        text=''
        title.config(text=text)
    else:
        text=text+ss[count]
        title.config(text=text)
        count +=1
    title.after(200,introlabeltick)
################################################################# SALE HOME  FUNCTION ##################################
def home(event):
    home_frame = Frame(bd=4, relief=RIDGE, bg="AntiqueWhite")
    witdth_value = admin_window.winfo_screenwidth()
    height_value = admin_window.winfo_screenheight()


    home_frame.place(x=370, y=70, width=witdth_value, height=height_value)

    add_product_title = Label(home_frame, text="Home", font=("times new roman ", 25, "bold"),
                              fg="Blue", bg="light cyan")
    add_product_title.pack(fill=X, side=TOP)

    #_____________________________products in stock frame________________
    productsinstock=IntVar()
    soldproducts=IntVar()
    noofcustomers=IntVar()
    conn=sqlite3.connect('japan.db')
    cur=conn.cursor()
    cur.execute("SELECT COUNT(p_id) FROM products")
    productsinstock=cur.fetchone()
    conn.commit()
    products_in_stock_frame=Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    products_in_stock_frame.place(x=40,y=90)
    productlbl=Label(products_in_stock_frame,text="Products in Stock",font=("times",15,"bold"),bg="AntiqueWhite",fg="black")
    productlbl.place(x=33,y=0)
    varproductlbl=Label(products_in_stock_frame,text=productsinstock,font=("times",15,"bold"),bg="AntiqueWhite",fg="black")
    varproductlbl.place(x=90,y=45)
    #---------------------------------------------------------------------------------------------------
    cur = conn.cursor()
    cur.execute("SELECT COUNT(sales_id) FROM sales_reports_table")
    soldproducts = cur.fetchone()
    conn.commit()
    soldproducts_frame = Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    soldproducts_frame.place(x=450, y=90)
    sold_productlbl = Label(soldproducts_frame, text="Products Sold", font=("times", 15, "bold"), bg="AntiqueWhite",
                       fg="black")
    sold_productlbl.place(x=33, y=0)
    sold_productlbl = Label(soldproducts_frame, text=soldproducts, font=("times", 15, "bold"), bg="AntiqueWhite",
                          fg="black")
    sold_productlbl.place(x=90, y=45)
    # ---------------------------------------------------------------------------------------------------
    userscount=IntVar()

    cur.execute("SELECT COUNT(u_id) FROM user_table")
    userscount = cur.fetchone()
    no_of_users_frame = Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    no_of_users_frame.place(x=860, y=90)

    sold_productlbl = Label(no_of_users_frame, text="No of Users", font=("times", 15, "bold"), bg="AntiqueWhite",
                            fg="black")
    sold_productlbl.place(x=48, y=0)
    sold_productlbl = Label(no_of_users_frame, text=userscount, font=("times", 15, "bold"), bg="AntiqueWhite",
                            fg="black")
    sold_productlbl.place(x=90, y=45)
    #----------------------------------------------------------------------------------------------------
    customer=IntVar()
    cur.execute("SELECT COUNT(c_id) FROM customer_table")
    customer=cur.fetchone()
    customers_frmae = Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    customers_frmae.place(x=40, y=290)

    customers_lbl = Label(customers_frmae, text="Customers Dealed", font=("times", 15, "bold"), bg="AntiqueWhite",
                            fg="black")
    customers_lbl.place(x=30, y=0)
    customers_lbl = Label(customers_frmae, text=customer, font=("times", 15, "bold"), bg="AntiqueWhite",
                            fg="black")
    customers_lbl.place(x=90, y=45)
    #------------------------------------------------------------------------------------------------------
    inventory=IntVar()
    cur.execute("SELECT COUNT(inventory_id) FROM inventory")
    inventory = cur.fetchone()
    inventory_frame = Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    inventory_frame.place(x=450, y=290)

    inventory_lbl = Label(inventory_frame, text="Items Inventory", font=("times", 15, "bold"), bg="AntiqueWhite",
                          fg="black")
    inventory_lbl.place(x=30, y=0)
    inventory_lbl = Label(inventory_frame, text=inventory, font=("times", 15, "bold"), bg="AntiqueWhite",
                          fg="black")
    inventory_lbl.place(x=90, y=45)
    # ------------------------------------------------------------------------------------------------------
    supliers=IntVar()
    cur.execute("SELECT COUNT(sup_id) FROM supliers_table")
    supliers = cur.fetchone()
    supliers_frame = Frame(home_frame,relief=RIDGE,bg="AntiqueWhite",height=137,width=230,bd=10)
    supliers_frame.place(x=860, y=290)
    suplierrs_lbl = Label(supliers_frame, text="Supliers", font=("times", 15, "bold"), bg="AntiqueWhite",
                          fg="black")
    suplierrs_lbl.place(x=30, y=0)
    suplierrs_lbl = Label(supliers_frame, text=supliers, font=("times", 15, "bold"), bg="AntiqueWhite",
                          fg="black")
    suplierrs_lbl.place(x=90, y=45)
def invoice(event):
    productid = StringVar()
    barcodeentry = StringVar()
    productname = StringVar()
    producttype = StringVar()
    purchasedfrom = StringVar()
    madeby = StringVar()
    model = StringVar()
    purchaseprice = DoubleVar()
    retailprice = DoubleVar()
    description = StringVar()
    #new variables added for invoice
    invoiceid=IntVar()
    customername=StringVar()
    customercontact=StringVar()
    customeraddress=StringVar()
    quantity=IntVar()
    discount=DoubleVar()
    shipmentcharges=DoubleVar()
    setupcharges=DoubleVar()
    othercharges=DoubleVar()

    payment=DoubleVar()
    grosstotal=DoubleVar()
    remaningamount=DoubleVar()



    def trace_callback(*args):
        try:
            quantity.get()
            discount.get()
            shipmentcharges.get()
            setupcharges.get()
            othercharges.get()
            payment.get()
        except:
            messagebox.showerror("warning", "the 0.0 assigned fields only accepts Numbers  ")
            quantity.set(0)
            discount.set(0.0)
            shipmentcharges.set(0.0)
            setupcharges.set(0.0)
            othercharges.set(0.0)
            payment.set(0.0)
        quantity.trace('w',trace_callback)
        discount.trace('w',trace_callback)
        shipmentcharges.trace('w',trace_callback)
        othercharges.trace('w',trace_callback)
        payment.trace('w',trace_callback)

    def generateinvoce():
        invoicetable = Toplevel(master=invoice_frame)
        invoicetable.title("Customer Invoice ")
        invoicetable.grab_set()
        invoicetable.geometry("600x700+7"
                              "00+0")
        # invoicetable.iconbitmap('logo.ico')
        invoicetable.config(bg='white')
        invoicetable.resizable(False, False)

        bgimage = PhotoImage(file=r"pic2.PNG")
        Label(invoicetable, image=bgimage).place(relwidth=1, relheight=1)


        invoice_id = invoiceid.get()
        productidvalue = productid.get()
        barcodevalue = barcodeentry.get()
        productnamevalue = productname.get()
        producttypevalue = producttype.get()
        retailpricevalue = retailprice.get()
        customernamevalue = customername.get()
        customercontactvalue = customercontact.get()
        customeraddressvalue = customeraddress.get()
        quantityvalue = quantity.get()
        discountvalue = discount.get()
        shipmentchargesvalue = shipmentcharges.get()
        setupchargesvalue = setupcharges.get()
        otherchargesvalue = othercharges.get()
        paymentvalue = payment.get()
        grosstotalvalue = grosstotal.get()
        remaningamountvalue = remaningamount.get()
        date=time.strftime("%d/%m/%y")

        def printinvoice():
            try:

                # date = time.strftime("%d/%m/%y")
                fileName = filedialog.asksaveasfile(mode="wb", title="Save Invoice", defaultextension=".pdf",
                                                    filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
                # fileName = 'invoice.pdf'
                documentTitle = 'Document title!'
                title = 'JMC Invoice'
                subTitle = 'Japan Medical Company'

                textLines = [
                    'Japan medical Company temrm and conditions',
                    'Japan medical Company Contact 03021454012',
                    'Website and email space.']

                # def drawMyRuler(pdf):
                #     pdf.drawString(100, 810, 'x100')
                #     pdf.drawString(200, 810, 'x200')
                #     pdf.drawString(300, 810, 'x300')
                #     pdf.drawString(400, 810, 'x400')
                #     pdf.drawString(500, 810, 'x500')
                #     pdf.drawString(10, 100, 'y100')
                #     pdf.drawString(10, 200, 'y200')
                #     pdf.drawString(10, 300, 'y300')
                #     pdf.drawString(10, 400, 'y400')
                #     pdf.drawString(10, 500, 'y500')
                #     pdf.drawString(10, 600, 'y600')
                #     pdf.drawString(10, 700, 'y700')
                #     pdf.drawString(10, 800, 'y800')

                pdf = canvas.Canvas(fileName)
                #################the title has been set here
                pdf.setTitle(documentTitle)

                ######################################VARIABLES

                invoiceidd = str(invoice_id)
                productname = productnamevalue
                customername = customernamevalue
                productprice = str(retailpricevalue)
                quantity = str(quantityvalue)
                discount = str(discountvalue)
                shipment = str(shipmentchargesvalue)
                setup = str(setupchargesvalue)
                other = str(otherchargesvalue)
                payhment = str(paymentvalue)
                total = str(grosstotalvalue)
                remaning = str(remaningamountvalue)
                # date=time.strftime("%d/%m/%y %s:%m:%h")

                date=time.strftime("%b %d %Y %H:%M:%S")

                ###################################### titles for the variable

                invoiceidlbl = "Invoice Id:"
                productnamelbl = "Product Name"
                customernamelbli = "Customer Name"
                prductpricelbl = "Product Price"
                quantitylbl = "Qty"
                discountlbl = "Discount"
                shipmentchargeslbl = "Shipment Charges"
                setupchargeslbl = "Setup Charges"
                otherchargeslbl = "Other Charges"
                amountpaidlbl = "Amount Paid"
                remaninglbl = "Remaning Amount"
                totallbl = "Total Amount"
                datetitle=":Date:"

                ##########################################
                # drawMyRuler(pdf)

                #########################################

                pdf.drawCentredString(300, 780, title)

                pdfmetrics.registerFont(
                    TTFont('abc', 'times.ttf')
                )
                pdf.setFont('abc', 40)

                # 2) Sub Title
                # RGB - Red Green and Blue
                pdf.setFillColorRGB(0, 0, 255)
                pdf.setFont("Courier-Bold", 24)
                pdf.drawCentredString(290, 720, subTitle)

                # 3) Draw a line
                pdf.line(10, 710, 600, 710)  # horizental line[starting,left height,ending ,right height]
                text = pdf.beginText(40, 680)
                text.setFont("Courier", 18)
                text.setFillColor(colors.blue)
                for line in textLines:
                    text.textLine(line)

                pdf.drawText(text)

                pdf.line(10, 620, 590, 620)  # another horizental line box

                pdf.line(10, 620, 10, 100)  # vertical line 1 box
                #####################################################invoice id and its value
                pdf.line(10, 590, 590, 590)  # another horizental line near invoice
                pdf.drawString(20, 600, invoiceidlbl)
                pdf.drawString(200, 600, invoiceidd)
                #####################################################data and time
                pdf.drawString(270, 600, datetitle)
                pdf.drawString(350, 600, date)
                #####################################################product name and its value
                pdf.line(10, 560, 590, 560)  # another horizental line near invoice
                pdf.drawString(20, 565, productnamelbl)
                pdf.drawString(200, 565, productname)

                #####################################################customer name and its value
                pdf.line(10, 530, 590, 530)  # another horizental line near invoice
                pdf.drawString(20, 535, customernamelbli)
                pdf.drawString(200, 535, customername)

                #####################################################customer name and its value
                pdf.line(10, 500, 590, 500)  # another horizental line near invoice
                pdf.drawString(20, 505, prductpricelbl)
                pdf.drawString(200, 505, productprice)

                #####################################################customer name and its value
                pdf.line(10, 470, 590, 470)  # another horizental line near invoice
                pdf.drawString(20, 475, quantitylbl)
                pdf.drawString(200, 475, quantity)

                #####################################################customer name and its value
                pdf.line(10, 440, 590, 440)  # another horizental line near invoice
                pdf.drawString(20, 445, shipmentchargeslbl)
                pdf.drawString(200, 445, shipment)

                #####################################################customer name and its value
                pdf.line(10, 410, 590, 410)  # another horizental line near invoice
                pdf.drawString(20, 415, setupchargeslbl)
                pdf.drawString(200, 415, setup)

                #####################################################customer name and its value
                pdf.line(10, 380, 590, 380)  # another horizental line near invoice
                pdf.drawString(20, 385, otherchargeslbl)
                pdf.drawString(200, 385, other)

                #####################################################customer name and its value
                pdf.line(10, 350, 590, 350)  # another horizental line near invoice
                pdf.drawString(20, 355, discountlbl)
                pdf.drawString(200, 355, discount)

                #####################################################customer name and its value
                pdf.line(10, 250, 590, 250)  # another horizental line near invoice
                pdf.drawString(20, 255, totallbl)
                pdf.drawString(200, 255, total)

                #####################################################customer name and its value
                pdf.line(10, 200, 590, 200)  # another horizental line near invoice
                pdf.drawString(20, 205, amountpaidlbl)
                pdf.drawString(200, 205, payhment)

                #####################################################customer name and its value
                pdf.line(10, 150, 590, 150)  # another horizental line near invoice
                pdf.drawString(20, 155, remaninglbl)
                pdf.drawString(200, 155, remaning)

                # pdf.line(10, 400, 590, 400)# another horizental line box

                pdf.line(590, 620, 590, 100)  # vertical line 2 box

                pdf.line(10, 100, 590, 100)  # another horizental line box

                pdf.save()
                messagebox.showinfo("congrates", "file is exported successfully to pdf please Print the file")
            except:
                messagebox.showerror("warning","somthing went wrong please try to save the file using .pdf at the end")









        def exportdailyrecords():
            try:

                # filedialog.asksaveasfile(mode="wb", title="Save Invoice", defaultextension=".pdf",
                #                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
                ff = filedialog.asksaveasfile()
                gg = todaysreporttable.get_children()
                '''  'sales_id','p_id','invoice_id',  'p_name',  'c_name',  'c_contact',  'c_address',  'total_amount',  'date',  'profit'''

                invoic_id,product_id, p_bar, pprice, pname, ptype, cname, ccontact, caddress, qty, dis,shipmentcharg,setupcharg,othercharg,amountpaid,reman = [], [], [], [], [], [], [], [], [], [],[], [], [], [], [], []
                for i in gg:
                    content = todaysreporttable.item(i)
                    pp = content['values']
                    product_id.append(pp[0]), \
                    invoic_id.append(pp[1]), \
                    p_bar.append(pp[2]), \
                    pprice.append(pp[3]), \
                    pname.append(pp[4]), \
                    ptype.append(pp[5]), \
                    cname.append(pp[6]), \
                    ccontact.append(pp[7]), \
                    caddress.append(pp[8]), \
                    qty.append(pp[9]), \
                    dis.append(pp[10]), \
                    shipmentcharg.append(pp[11]),\
                    setupcharg.append(pp[12]),\
                    othercharg.append(pp[13]),\
                    amountpaid.append(pp[14]),\
                    reman.append(pp[15]),

                dd = ['Invoice Id',
            'Product Id',
            'Product Barcode',
            'Product Price',
            'Product Name',
            'Product Type',
            'Customer Name',
            'Customer Contact',
            'Customer Address',
            'Quantity',
            'Discount',
            'Shipment Charges',
            'Setup Charges',
            'Other Charges',
            'Amount Paid',
            'Remaning']
                df = pandas.DataFrame(list(
                    zip(invoic_id,product_id, p_bar, pprice, pname, ptype, cname, ccontact, caddress, qty, dis,shipmentcharg,setupcharg,othercharg,amountpaid,reman)), columns=dd)

                # paths = '{}.csv'.format(ff)

                df.to_csv(ff, index=False)

                # paths, mode = 'w', encoding = None, index=False

                messagebox.showinfo("notification", "data exported successfully {}")
            except:
                messagebox.showerror("warning", "somthing went wrong please try saving file with filename.csv")
        ######################################################Invoice tree view and scroll bar  ################################
        show_sales_report_dataframe = Frame(invoicetable, bg="snow", relief=GROOVE, bd=5)
        show_sales_report_dataframe.place(x=0, y=200, width=600, height=400)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('time new roman', 15, 'bold'), foreground='blue')
        style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', bg='light cyan', anchor="center")
        scrollbar_x = Scrollbar(show_sales_report_dataframe, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(show_sales_report_dataframe, orient=VERTICAL)
        todaysreporttable = Treeview(show_sales_report_dataframe, column=(
            'Invoice Id',
            'Product Id',
            'Product Barcode',
            'Product Price',
            'Product Name',
            'Product Type',
            'Customer Name',
            'Customer Contact',
            'Customer Address',
            'Quantity',
            'Discount',
            'Shipment Charges',
            'Setup Charges',
            'Other Charges',
            'Amount Paid',
            'Remaning'),
                                     yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.config(command=todaysreporttable.xview)
        scrollbar_y.config(command=todaysreporttable.yview)
        todaysreporttable.heading('Invoice Id', text='Invoice Id')
        todaysreporttable.heading('Product Id', text='Product Id')
        todaysreporttable.heading('Product Barcode', text='Product Barcode')
        todaysreporttable.heading('Product Price', text='Product Price')
        todaysreporttable.heading('Product Name', text='Product Name')
        todaysreporttable.heading('Product Type', text='Product Type')
        todaysreporttable.heading('Customer Name', text='Customer Name')
        todaysreporttable.heading('Customer Contact', text='Customer Address')
        todaysreporttable.heading('Customer Address', text='Customer Address')
        todaysreporttable.heading('Quantity', text='Quantity')
        todaysreporttable.heading('Discount', text='Discount')
        todaysreporttable.heading('Shipment Charges', text='Shipment Charges')
        todaysreporttable.heading('Setup Charges', text='Setup Charges')
        todaysreporttable.heading('Other Charges', text='Other Charges')
        todaysreporttable.heading('Amount Paid', text='Amount Paid')
        todaysreporttable.heading('Remaning', text='Remaning')

        todaysreporttable['show'] = 'headings'

        todaysreporttable.column('Invoice Id',width=200)
        todaysreporttable.column('Product Id',width=200)
        todaysreporttable.column('Product Barcode',width=200)
        todaysreporttable.column('Product Price',width=200)
        todaysreporttable.column('Product Name',width=200)
        todaysreporttable.column('Product Type',width=200 )
        todaysreporttable.column('Customer Name',width=200)
        todaysreporttable.column('Customer Contact',width=200)
        todaysreporttable.column('Customer Address',width=200)
        todaysreporttable.column('Quantity',width=200)
        todaysreporttable.column('Discount', width=200)
        todaysreporttable.column('Shipment Charges',width=200)
        todaysreporttable.column('Setup Charges', width=200)
        todaysreporttable.column('Other Charges', width=200)
        todaysreporttable.column('Amount Paid', width=200)
        todaysreporttable.column('Remaning', width=200)


        todaysreporttable.pack(fill=BOTH, expand=True)
        # todaysreporttable.bind('<<TreeviewSelect>>', invoicecallback)
        todaysreporttable.config(selectmode='browse')

        conn = sqlite3.connect('japan.db')
        cur = conn.cursor()
        select="select * from invoice_table where invoice_id=?"
        data=cur.execute(select,(invoice_id,))
        todaysreporttable.delete(*todaysreporttable.get_children())
        for i in data:
            storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            todaysreporttable.insert('', END, values=storedata)

        conn.commit()


        # '''TOP Label '''
        invoice_barcode_lbl = Label(invoicetable, text="Customer Invoice ", font=("times new roman ", 20,"bold"),
                                    fg="black",
                                    bg="white")
        invoice_barcode_lbl.pack(side=TOP,fill=X)
        '''Daily reference in the bill '''
        invoice_barcode_lbl = Label(invoicetable, text="daily", font=("times new roman ", 10),
                                    fg="black",
                                    bg="white")
        invoice_barcode_lbl.place(x=100, y=110)

        '''Date label '''
        invoice_barcode_lbl = Label(invoicetable, text=date, font=("times new roman ", 10),
                                    fg="black",
                                    bg="white")
        invoice_barcode_lbl.place(x=390, y=110)
        # ##########################################SECTION 1 Product ID #############################################
        '''Export sales report Button  '''
        export_daily_sales_report = Button(invoicetable, text="Export Invoice (CSV)", font=("times new roman ", 12, "bold"),
                                    fg="black",
                                    bg="snow",bd=5,command=exportdailyrecords)
        export_daily_sales_report.place(x=30, y=620)

        '''print invoice Button  '''
        export_daily_sales_report = Button(invoicetable, text="Print Invoice",
                                           font=("times new roman ", 12, "bold"),
                                           fg="black",
                                           bg="snow", bd=5, command=printinvoice)
        export_daily_sales_report.place(x=300, y=620)

        # ############################################################################################################
        invoicetable.mainloop()

    def invoicecallback(event):
        invoicetable.selection()
        curItem = invoicetable.focus()
        content = invoicetable.item(curItem)
        pp = content['values']
        if len(pp) != 0:

            invoiceid.set(pp[0])
            productid.set(pp[1])
            barcodeentry.set(pp[2])
            retailprice.set(pp[3])
            productname.set(pp[4])
            producttype.set(pp[5])
            customername.set(pp[6])
            customercontact.set(pp[7])
            customeraddress.set(pp[8])
            quantity.set(pp[9])
            discount.set(pp[10])
            shipmentcharges.set(pp[11])
            setupcharges.set(pp[12])
            othercharges.set(pp[13])
            payment.set(pp[14])
            grosstotal.set(pp[15])
            remaningamount.set(pp[16])
    def callback(event):
        producttable.selection()
        curItem = producttable.focus()
        content = producttable.item(curItem)
        pp = content['values']
        if len(pp) != 0:
            productid.set(pp[0])
            barcodeentry.set(pp[1])
            productname.set(pp[2])
            producttype.set(pp[3])
            purchasedfrom.set(pp[4])
            madeby.set(pp[5])
            model.set(pp[6])
            purchaseprice.set(pp[7])
            retailprice.set(pp[8])
            description.set(pp[9])

            # here i can add another item as i want to change
    def searchinvoice():
        try:
            invoiceidvalue = invoiceid.get()
            if invoiceidvalue == '':
                messagebox.showerror("warning!!!", "please insert some data in the field")

            elif invoiceidvalue != '':
                conn = sqlite3.connect('japan.db')
                selectquery = "SELECT * FROM invoice_table WHERE invoice_id=?"
                cur = conn.cursor()
                cur.execute(selectquery, (invoiceidvalue,))
                storedata = cur.fetchall()
                invoicetable.delete(*invoicetable.get_children())
                for i in storedata:
                    storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17]]
                    invoicetable.insert('', END, values=storedata)
                conn.commit()
                conn.close()
        except:
            messagebox.showerror("Error", "somthing Went Wrong try again with valid Barcode id")

    def search():
        try:
            barcodevalue = barcodeentry.get()
            if barcodevalue == '':
                messagebox.showerror("warning!!!", "please insert some data in the field")

            elif barcodevalue != '':
                conn = sqlite3.connect('japan.db')
                selectquery = "SELECT * FROM products WHERE p_barcode=?"
                cur = conn.cursor()
                cur.execute(selectquery, (barcodevalue,))
                storedata = cur.fetchall()
                producttable.delete(*producttable.get_children())
                for i in storedata:
                    storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                    producttable.insert('', END, values=storedata)
                conn.commit()
                conn.close()
        except:
            messagebox.showerror("Error", "somthing Went Wrong try again with valid Barcode id")

    def delete():
        conn = sqlite3.connect("japan.db")
        cur = conn.cursor()
        for selected_item in producttable.selection():
            cur.execute("DELETE FROM products WHERE p_id=?", (producttable.set(selected_item, '#1'),))
            conn.commit()
            producttable.delete(selected_item)
        messagebox.showinfo("notification", " This Product has been Removed successfully From the stock")
        conn.close()
        clear()

    def updateinvoice():
        trace_callback(quantity,discount,shipmentcharges,othercharges,payment)
        productnamevalue=productname.get()
        purchasepricevalue=purchaseprice.get()

        invoiceidvalue=invoiceid.get()
        customernamevalue = customername.get()
        customercontactvalue = customercontact.get()
        customeraddressvalue = customeraddress.get()
        quantityvalue = quantity.get()
        discountvalue = discount.get()
        shipmentchargesvalue = shipmentcharges.get()
        setupchargesvalue = setupcharges.get()
        otherchargesvalue = othercharges.get()
        paymentvalue = payment.get()
        grosstotalvalue = grosstotal.get()
        remaningamountvalue = remaningamount.get()
        productidvalue=productid.get()


        #########################
        # try:
        if invoiceidvalue == 0 or invoiceidvalue == '':
            messagebox.showerror("warning!!!", "Please Select The invoice to update")
        else:
            conn = sqlite3.connect('japan.db')
            cur = conn.cursor()
            # selectfromsales='SELECT '

            update = "UPDATE invoice_table SET  c_name = ?, c_contact = ?, c_address = ?, quantity = ?, discount = ?,shipment_charges = ?, setup_charges = ?, other_charges = ?, payment = ?, total = ?, remaning = ?, date = CURRENT_TIMESTAMP WHERE invoice_id = ?;"
            updatecustomertable = "update customer_table set c_name=?,c_contact=?,c_address=?,quantity=?,discount=?,shipment_charges=?,setup_charges=?,other_charges=?,payment=?,total=?,remaning=? where c_id = c_id and invoice_id=?"
            cur.execute(update, (
                customernamevalue, customercontactvalue, customeraddressvalue, quantityvalue, discountvalue,
                shipmentchargesvalue, setupchargesvalue, otherchargesvalue, paymentvalue, grosstotalvalue,
                remaningamountvalue, invoiceidvalue))
            cur.execute(updatecustomertable, (
                customernamevalue, customercontactvalue, customeraddressvalue, quantityvalue, discountvalue,
                shipmentchargesvalue, setupchargesvalue, otherchargesvalue, paymentvalue, grosstotalvalue,
                remaningamountvalue, invoiceidvalue))

            updatesales = "UPDATE sales_reports_table SET p_name = ?,p_price = ?,c_name = ?,c_contact = ?,c_address = ?,total_amount = ?,date =CURRENT_TIMESTAMP ,profit = total_amount-p_price WHERE sales_id = sales_id AND   invoice_id = ? "
            cur.execute(updatesales, (
            productnamevalue, purchasepricevalue, customernamevalue, customercontactvalue, customeraddressvalue,
            grosstotalvalue, invoiceidvalue))
            conn.commit()
            messagebox.showinfo("notification", "invoices , customers , sales report data updated successfully")
            showinvoicedata()

        #
        # except:
        #     messagebox.showerror("Error", "Somthing Went Wrong Please Try again Cehck the barcode it should be unique")

    def showdata():
        conn = sqlite3.connect('japan.db')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM products')
        producttable.delete(*producttable.get_children())
        for i in data:
            storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            producttable.insert('', END, values=storedata)
        conn.commit()
        conn.close()
    def showinvoicedata():
        conn = sqlite3.connect('japan.db')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM invoice_table')
        invoicetable.delete(*invoicetable.get_children())
        for i in data:
            storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17]]
            invoicetable.insert('', END, values=storedata)
        conn.commit()
        conn.close()
    def exportinvoicedata():

        try:
            ff = filedialog.asksaveasfile()
            gg = invoicetable.get_children()
            invoice_id, p_id, p_barcode, retail_price, p_name, p_type, c_name, c_contact, c_address, quantity, discount, shipment_charges, setup_charges, other_charges, payment, total, remaning, date = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
            for i in gg:
                content = invoicetable.item(i)
                pp = content['values']
                invoice_id.append(pp[0]), \
                p_id.append(pp[1]), \
                p_barcode.append(pp[2]), \
                retail_price.append(pp[3]), \
                p_name.append(pp[4]), \
                p_type.append(pp[5]), \
                c_name.append(pp[6]), \
                c_contact.append(pp[7]), \
                c_address.append(pp[8]), \
                quantity.append(pp[9]), \
                discount.append(pp[10]), \
                shipment_charges.append(pp[11]), \
                setup_charges.append(pp[12]), \
                other_charges.append(pp[13]), \
                payment.append(pp[14]), \
                total.append(pp[15]), \
                remaning.append(pp[16]), \
                date.append(pp[17]),

            dd = ['invoice_id', 'p_id', 'p_barcode', 'retail_price', 'p_name', 'p_type', 'c_name', 'c_contact', 'c_address',
                  'quantity', 'discount', 'shipment_charges', 'setup_charges', 'other_charges', 'payment', 'total',
                  'remaning', 'date']

            df = pandas.DataFrame(list(
                zip(invoice_id, p_id, p_barcode, retail_price, p_name, p_type, c_name, c_contact, c_address, quantity,
                    discount, shipment_charges, setup_charges, other_charges, payment, total, remaning, date)), columns=dd)

            # paths = '{}.csv'.format(ff)

            df.to_csv(ff, index=False)

            # paths, mode = 'w', encoding = None, index=False

            messagebox.showinfo("notification", "data exported successfully {}")
        except:
            messagebox.showerror("warning", "somthing went wrong please try saving file with filename.csv")
    def exportproductsdata():
        try:
            ff = filedialog.asksaveasfile()
            gg = producttable.get_children()
            id, barcode, product_name, p_type, purchased_from, made_by, mmodel, r_price, decs, addeddate, updateddate = [], [], [], [], [], [], [], [], [], [], []
            for i in gg:
                content = producttable.item(i)
                pp = content['values']
                id.append(pp[0]), \
                barcode.append(pp[1]), \
                product_name.append(pp[2]), \
                p_type.append(pp[3]), \
                purchased_from.append(pp[4]), \
                made_by.append(pp[5]), \
                mmodel.append(pp[6]), \
                r_price.append(pp[8]), \
                decs.append(pp[9]), \
                addeddate.append(pp[10]), \
                updateddate.append(pp[11])

            dd = ['Product Id ', 'Product Barcode', 'Product Name', 'Product Type', 'Purchased From ', 'Made By',
                  'Model ',  'Retail Price', 'Description', 'Added Date', 'Updated Date']
            df = pandas.DataFrame(list(
                zip(id, barcode, product_name, p_type, purchased_from, made_by, mmodel, r_price, decs,
                    addeddate, updateddate)), columns=dd)

            # paths = '{}.csv'.format(ff)

            df.to_csv(ff, index=False)

            # paths, mode = 'w', encoding = None, index=False

            messagebox.showinfo("notification", "data exported successfully {}")
        except:
            messagebox.showerror("warning", "somthing went wrong please try saving file with filename.csv")

    def addinvoicedetails():
        trace_callback(quantity, discount, shipmentcharges, othercharges, payment)
        if barcodeentry.get() == '' or productid.get() == '' or retailprice.get() == '' or productname.get() == '' or producttype.get() == '' or customername.get() == '' \
                or customercontact.get() == '' or customeraddress.get() == '' or quantity.get() == ''\
                or discount.get() == '' or shipmentcharges.get() == '' or setupcharges.get() == ''\
                or othercharges.get() == '' or grosstotal.get() == '' or remaningamount.get() == ''or payment.get() == '':
            messagebox.showerror("warning!!!", "please fill all the inpput fields")
        else:
            invoiceidvalue=invoiceid.get()
            productidvalue=productid.get()
            barcodevalue=barcodeentry.get()
            productnamevalue=productname.get()
            producttypevalue=producttype.get()
            retailpricevalue=retailprice.get()
            customernamevalue=customername.get()
            customercontactvalue=customercontact.get()
            customeraddressvalue=customeraddress.get()
            quantityvalue=quantity.get()
            discountvalue=discount.get()
            shipmentchargesvalue=shipmentcharges.get()
            setupchargesvalue=setupcharges.get()
            otherchargesvalue=othercharges.get()
            paymentvalue=payment.get()
            grosstotalvalue=grosstotal.get()
            remaningamountvalue=remaningamount.get()
            purchasepricevalue=purchaseprice.get()
            try:
                conn = sqlite3.connect('japan.db')
                cur = conn.cursor()
                insertsql='INSERT INTO invoice_table VALUES(NULL, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?,?,CURRENT_TIMESTAMP)'
                cur.execute(insertsql, (
                productidvalue, barcodevalue,retailpricevalue,productnamevalue,producttypevalue,customernamevalue,customercontactvalue,customeraddressvalue,quantityvalue,discountvalue,shipmentchargesvalue,setupchargesvalue,otherchargesvalue,paymentvalue,grosstotalvalue,remaningamountvalue))
                conn.commit()
                res = messagebox.askyesno("notification",
                                          "Product barcode{},   Prouduct name{} added successfully Do You Want To add the invoice".format(barcodevalue,productnamevalue))

                if res == True:
                    clear()
            except:
                messagebox.showerror("warning!!!", "this id is already exist please enter another")
            selectquery = "SELECT * FROM invoice_table"
            data = cur.execute(selectquery)
            invoicetable.delete(*invoicetable.get_children())
            for i in data:
                storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11],i[12],i[13],i[14],i[15],i[16],i[17]]
                invoicetable.insert('', END, values=storedata)
            delete()
        setfields()

    def totalamount():
        try:
            retailpricecount=retailprice.get()
            quantitycount=quantity.get()
            discountcount=discount.get()
            shipmentchargescount=shipmentcharges.get()
            setupchargescount=setupcharges.get()
            otherchargescount=othercharges.get()
            grosstotalcount=grosstotal.get()
            remaningamountcount=remaningamount.get()
            paymentcount = payment.get()


            if retailpricecount=='' or quantitycount==''or discountcount=='' or shipmentchargescount==''\
                or setupchargescount=='' or otherchargescount==''or grosstotalcount=='' or remaningamountcount==''\
                or paymentcount=='':
                messagebox.showerror("warning","please fill the complete details to calculate the total  ")
            else:
                #______________________________________________________________________
                #added the three value first
                threevaluestotal = shipmentchargescount + setupchargescount + otherchargescount
                threevaluestotal_retail = threevaluestotal + retailpricecount

                #here i added the retail value of the product with three values
                threevaluestotal_retail_mul_quantity = threevaluestotal_retail * quantitycount

                #here i have multiplied the quantity with all the sum
                threevaluestotal_retail_mul_quantity_discount = threevaluestotal_retail_mul_quantity - discountcount

                #i have then subtracted the discount value from the total
                grosstotal.set(threevaluestotal_retail_mul_quantity_discount)

                #now here i have sutract the payment from the total and the remaning amount is listed in the field
                remaning = threevaluestotal_retail_mul_quantity_discount-paymentcount
                remaningamount.set(remaning)


        except:
            messagebox.showerror("warning","make sure to fill the details before getting the total amount\n Fisrt Total The Other Amount then after enter the  payment then click on total ")
    def setfields():
        retailprice.set(0.0)
        quantity.set(0)
        discount.set(0.0)
        shipmentcharges.set(0.0)
        setupcharges.set(0.0)
        othercharges.set(0.0)
        grosstotal.set(0.0)
        remaningamount.set(0.0)
        payment.set(0.0)

    def clear():
        invoiceid.set(0)
        productid.set(0)
        barcodeentry.set('')
        retailprice.set('')
        productname.set('')
        producttype.set('')
        customername.set('')
        customercontact.set('')
        customeraddress.set('')
        retailprice.set(0.0)
        quantity.set(0)
        discount.set(0.0)
        shipmentcharges.set(0.0)
        setupcharges.set(0.0)
        othercharges.set(0.0)
        grosstotal.set(0.0)
        remaningamount.set(0.0)
        payment.set(0.0)

    ############################################# wegits of manage product entry########################################
    invoice_frame = Frame(bd=4, relief=RIDGE, bg="snow")
    invoice_frame.place(x=370, y=70, width=1150, height=720)
    add_product_title = Label(invoice_frame, text="Make Invoice", font=("times new roman ", 20, "bold"),
                              fg="black", bg="snow")
    add_product_title.place(x=360,y=10)
    # '''invoice id label '''
    # invoice_barcode_lbl = Label(invoice_frame, text="invoice id:", font=("times new roman ", 12, "bold"), fg="black",
    #                             bg="snow")
    # invoice_barcode_lbl.place(x=20, y=0)
    #
    # '''entry invoice id '''
    # invoice_barcode_entry = Entry(invoice_frame, state=DISABLED, textvariable=invoiceid,
    #                               font=("times new roman ", 12), bd=5,
    #                               relief=GROOVE)
    # invoice_barcode_entry.place(x=170, y=0)


    '''invoice_ barcode label '''
    invoice_barcode_lbl = Label(invoice_frame, text="Barcode No:", font=("times new roman ", 12, "bold"), fg="black",
                        bg="snow")
    invoice_barcode_lbl.place(x=20, y=60)

    '''entry barcode'''
    invoice_barcode_entry = Entry(invoice_frame, state=DISABLED,textvariable=barcodeentry, font=("times new roman ", 12), bd=5,
                          relief=GROOVE)
    invoice_barcode_entry.place(x=170, y=60)

    '''id label '''
    invoice_barcode_lbl = Label(invoice_frame, text="Product Id:", font=("times new roman ", 12, "bold"), fg="black",
                        bg="snow")
    invoice_barcode_lbl.place(x=20, y=20)

    '''entry id'''
    invoice_prductidentry = Entry(invoice_frame, state=DISABLED, textvariable=productid, font=("times new roman ", 12),
                          bd=5,
                          relief=GROOVE)
    invoice_prductidentry.place(x=170, y=20)

    '''product price label'''
    invoice_product_name_lbl = Label(invoice_frame, text="Product Price:", font=("times new roman ", 12, "bold"), fg="black",
                             bg="snow")
    invoice_product_name_lbl.place(x=20, y=100)

    '''entry retail price '''
    invoice_product_name_entry = Entry(invoice_frame, state=DISABLED,textvariable=retailprice, font=("times new roman ", 12), bd=5,
                               relief=GROOVE)
    invoice_product_name_entry.place(x=170, y=100)
    #_______________________________________________________________________________________________
    '''Product name label'''
    invoice_product_name_lbl = Label(invoice_frame, text="Product Name:", font=("times new roman ", 12, "bold"),
                                     fg="black",
                                     bg="snow")
    invoice_product_name_lbl.place(x=20, y=140)

    '''product  name'''
    invoice_product_name_entry = Entry(invoice_frame, state=DISABLED,textvariable=productname, font=("times new roman ", 12), bd=5,
                                       relief=GROOVE)
    invoice_product_name_entry.place(x=170, y=140)
    #_________________________________________________________________________________________________

    '''product_type lable '''
    invoice_product_typelbl = Label(invoice_frame, text="Product Type:", font=("times new roman ", 12, "bold"), fg="black",
                            bg="snow")
    invoice_product_typelbl.place(x=20, y=180)

    '''product_type  entry '''
    invoice_product_type_entry = Entry(invoice_frame,state=DISABLED, textvariable=producttype, font=("times new roman ", 12), bd=5,
                               relief=GROOVE)
    invoice_product_type_entry.place(x=170, y=180)

    '''Customer name label '''
    customer_name_lbl = Label(invoice_frame, text="Customer Name:", font=("times new roman ", 12, "bold"),
                              fg="black", bg="snow")
    customer_name_lbl.place(x=20, y=220)

    '''purchased price entry '''
    customer_name_entry = Entry(invoice_frame, textvariable=customername, font=("times new roman ", 12), bd=5,
                                relief=GROOVE)
    customer_name_entry.place(x=170, y=220)

    #________________________________________________________________
    '''Customer_contact label'''
    Customer_contact_lbl = Label(invoice_frame, text="Customer Contact:", font=("times new roman ", 12,"bold"),
                                     fg="black",
                                     bg="snow")
    Customer_contact_lbl.place(x=20, y=260)

    '''Customer_contact_entry'''
    Customer_contact_entry = Entry(invoice_frame, textvariable=customercontact, font=("times new roman ", 12,), bd=5,
                                       relief=GROOVE)
    Customer_contact_entry.place(x=170, y=260)

    #_______________________________________________________________

    '''customer_address_lbl '''
    customer_address_lbl = Label(invoice_frame, text="Customer Address:", font=("times new roman ", 12, "bold"), fg="black",
                         bg="snow")
    customer_address_lbl.place(x=20, y=300)

    '''customer_address_entry'''
    customer_address_entry = Entry(invoice_frame, textvariable=customeraddress, font=("times new roman ", 12), bd=5, relief=GROOVE)
    customer_address_entry.place(x=170, y=300)

    '''quantity_lbl '''
    quantity_lbl = Label(invoice_frame, text="Quantity:", font=("times new roman ", 12, "bold"), fg="black",
                              bg="snow")
    quantity_lbl.place(x=20, y=340)

    '''quantity_entry'''
    quantity_entry = Entry(invoice_frame, textvariable=quantity, font=("times new roman ", 12), bd=5,
                                relief=GROOVE)
    quantity_entry.place(x=170, y=340)

    # ________________________________________________________________
    '''discount_lbl'''
    discount_lbl = Label(invoice_frame, text="Discount:", font=("times new roman ", 12, "bold"),
                                     fg="black",
                                     bg="snow")
    discount_lbl.place(x=20, y=380)

    '''discount_entry'''
    discount_entry = Entry(invoice_frame, textvariable=discount, font=("times new roman ", 12), bd=5,
                                       relief=GROOVE)
    discount_entry.place(x=170, y=380)

    # _______________________________________________________________

    '''shipment_charges '''
    shipment_charges_lbl = Label(invoice_frame, text="Shipment Charges:", font=("times new roman ", 12, "bold"),
                               fg="black", bg="snow")
    shipment_charges_lbl.place(x=20, y=420)

    '''shipment_charges entry  '''
    shipment_charges_entry = Entry(invoice_frame, textvariable=shipmentcharges, font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    shipment_charges_entry.place(x=170, y=420)

    '''setup_charges_label '''
    setup_charges_label = Label(invoice_frame, text="Setup Charges:", font=("times new roman ", 12, "bold"), fg="black",
                             bg="snow")
    setup_charges_label.place(x=20, y=460)

    '''setup_charges_entry'''
    setup_charges_entry = Entry(invoice_frame, textvariable=setupcharges, font=("times new roman ", 12), bd=5,
                               relief=GROOVE)
    setup_charges_entry.place(x=170, y=460)

    # ________________________________________________________________
    '''other_charges_label'''
    other_charges_label = Label(invoice_frame, text="Other Charges:", font=("times new roman ", 12, "bold"),
                                     fg="black",
                                     bg="snow")
    other_charges_label.place(x=20, y=500)

    '''other_charges_entry'''
    other_charges_entry = Entry(invoice_frame, textvariable=othercharges, font=("times new roman ", 12), bd=5,
                                       relief=GROOVE)
    other_charges_entry.place(x=170, y=500)

    # _______________________________________________________________

    '''payment_label'''
    other_charges_label = Label(invoice_frame, text="Payment:", font=("times new roman ", 12, "bold"),
                                fg="black",
                                bg="snow")
    other_charges_label.place(x=20, y=540)

    '''payment_entry'''
    other_charges_entry = Entry(invoice_frame, textvariable=payment, font=("times new roman ", 12), bd=5,
                                relief=GROOVE)
    other_charges_entry.place(x=170, y=540)

    # _______________________________________________________________

    '''gross_total_label '''
    gross_total_label = Label(invoice_frame, text="Total:", font=("times new roman ", 12, "bold"), fg="black",
                            bg="snow")
    gross_total_label.place(x=20, y=580)


    '''entry of gross total  '''
    gross_total_entry = Entry(invoice_frame, state=DISABLED,textvariable=grosstotal, font=("times new roman ", 12), bd=5,
                                      relief=GROOVE)
    gross_total_entry.place(x=170, y=580)

    # ________________________________________________________________
    '''remaning_abel'''
    remaning_lbl = Label(invoice_frame, text="Remaning Amount:", font=("times new roman ", 12, "bold"),
                                     fg="black",
                                     bg="snow")
    remaning_lbl.place(x=20, y=620)

    '''remaning_amount_entry'''
    remaning_amount_entry = Entry(invoice_frame, state=DISABLED,textvariable=remaningamount, font=("times new roman ", 12), bd=5,
                                       relief=GROOVE)
    remaning_amount_entry.place(x=170, y=620)





    # _______________________________________________________________

    '''search product label '''
    invoice_Search_lbl = Label(invoice_frame, text="Barcode:", font=("times new roman ", 12, "bold"),
                       fg="black",
                       bg="snow")
    invoice_Search_lbl.place(x=670, y=670)

    '''entry of search   '''
    invoice_product_search_entry = Entry(invoice_frame, textvariable=barcodeentry, font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    invoice_product_search_entry.place(x=750, y=670)

    '''search invoice label '''
    invoice_search_lbl = Label(invoice_frame, text="Invoice Id:", font=("times new roman ", 12, "bold"),
                               fg="black",
                               bg="snow")
    invoice_search_lbl.place(x=660, y=620)

    '''entry of search   '''
    invoice_search_entry = Entry(invoice_frame, textvariable=invoiceid, font=("times new roman ", 12), bd=5,
                                         relief=GROOVE)
    invoice_search_entry.place(x=750, y=620)

    ######################################################Buttons#######################################################
    '''clear button'''
    add_product_clear_button = Button(invoice_frame, text="Clear Fields", width=10, height=1,
                                      font=("time new roman", 10, "bold"), activebackground='light cyan',
                                      activeforeground='black', bd=4, command=clear)
    add_product_clear_button.place(x=20, y=660)

    '''Total button '''
    invoice_total_button = Button(invoice_frame, text="Total", width=10, height=1,
                                    font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                    activeforeground='black', command=totalamount)
    invoice_total_button.place(x=140, y=660)

    '''invoice  button '''
    make_invoice_button = Button(invoice_frame, text="Add To Invoice", width=15, height=1,
                                  font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                  activeforeground='black', command=addinvoicedetails)
    make_invoice_button.place(x=260, y=660)

    '''invoice  update button '''
    make_invoice_button = Button(invoice_frame, text="Update Invoice", width=15, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=updateinvoice)
    make_invoice_button.place(x=420, y=660)
    #
    # '''delete button '''
    # delete_product_add_button = Button(invoice_frame, text="Delete Product", width=20, height=1,
    #                                    font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                    activeforeground='black', command=delete)
    # delete_product_add_button.place(x=15, y=640)
    #
    # '''update button '''
    # update_product_add_button = Button(invoice_frame, text="Update Product", width=20, height=1,
    #                                    font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                    activeforeground='black', command=update)
    # update_product_add_button.place(x=215, y=640)

    '''search button '''
    search_product_button = Button(invoice_frame, text="Search Product", width=20, height=1,
                                   font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                   activeforeground='black', command=search)
    search_product_button.place(x=960, y=665)

    '''search invoice '''
    search_invoice_button = Button(invoice_frame, text="Search Invoice", width=20, height=1,
                                   font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                   activeforeground='black', command=searchinvoice)
    search_invoice_button.place(x=960, y=620)

    '''show button '''
    show_product_button = Button(invoice_frame, text="Show Products Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=showdata)
    show_product_button.place(x=950, y=10)

    '''Export  button '''
    show_product_button = Button(invoice_frame, text="Export Products Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=exportproductsdata)
    show_product_button.place(x=740, y=10)

    '''show invoice records button '''
    show_invoice_button = Button(invoice_frame, text="Show Invoice Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=showinvoicedata)
    show_invoice_button.place(x=950, y=540)

    '''Export invoices records  button '''
    export_invoice_button = Button(invoice_frame, text="Export Invoices Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=exportinvoicedata)
    export_invoice_button.place(x=740, y=540)

    '''Generate Invoice  button '''
    generate_invoice_button = Button(invoice_frame, text="Generate Invoice ", width=20, height=1,
                                   font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                   activeforeground='black', command=generateinvoce)
    generate_invoice_button.place(x=520, y=540)

    ######################################################Product Tree List and scroll bar##############################
    showdataframe = Frame(invoice_frame, bg="snow", relief=GROOVE, bd=5)
    showdataframe.place(x=400, y=60, width=730, height=220)

    style = ttk.Style()
    style.configure('Treeview.Heading', font=('time new roman', 15, 'bold'), foreground='blue')
    style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', bg='light cyan', anchor="center")

    scrollbar_x = Scrollbar(showdataframe, orient=HORIZONTAL)
    scrollbar_y = Scrollbar(showdataframe, orient=VERTICAL)
    producttable = Treeview(showdataframe, column=(
        'ID', 'Bar Code', 'Product Name', 'Product Type', 'Purchased From', 'Made By', 'Model', 'Purchase Price',
        'Retail Price', 'Description', 'Added Date', 'Update Date'),
                            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_x.pack(side=BOTTOM, fill=X)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.config(command=producttable.xview)
    scrollbar_y.config(command=producttable.yview)

    producttable.heading('ID', text='ID')
    producttable.heading('Bar Code', text='Bar Code')
    producttable.heading('Product Name', text='Product Name')
    producttable.heading('Product Type', text='Product Type')
    producttable.heading('Purchased From', text='Purchased From')
    producttable.heading('Made By', text='Made By')
    producttable.heading('Model', text='Model')
    producttable.heading('Purchase Price', text='Purchase Price')
    producttable.heading('Retail Price', text='Retail Price')
    producttable.heading('Description', text='Description')
    producttable.heading('Added Date', text='Added Date')
    producttable.heading('Update Date', text='Update Date')
    producttable['show'] = 'headings'
    producttable.column('ID', width=50)
    producttable.column('Bar Code', width=200)
    producttable.column('Product Name', width=200)
    producttable.column('Product Type', width=200)
    producttable.column('Purchased From', width=200)
    producttable.column('Made By', width=300)
    producttable.column('Model', width=100)
    producttable.column('Purchase Price', width=200)
    producttable.column('Retail Price', width=200)
    producttable.column('Description', width=300)
    producttable.column('Added Date', width=200)
    producttable.column('Update Date', width=200)
    producttable.pack(fill=BOTH, expand=True)
    producttable.bind('<<TreeviewSelect>>', callback)
    producttable.config(selectmode='browse')

    ######################################################Invoice tree view and scroll bar  ################################
    showdataframe = Frame(invoice_frame, bg="snow", relief=GROOVE, bd=5)
    showdataframe.place(x=400, y=300, width=730, height=220)

    style = ttk.Style()
    style.configure('Treeview.Heading', font=('time new roman', 15, 'bold'), foreground='blue')
    style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', bg='light cyan', anchor="center")

    scrollbar_x = Scrollbar(showdataframe, orient=HORIZONTAL)
    scrollbar_y = Scrollbar(showdataframe, orient=VERTICAL)
    invoicetable = Treeview(showdataframe, column=(
        'Invoice Id','Product Id' ,'Product Barcode', 'Product Price', 'Product Name', 'Product Type', 'Customer Name', 'Customer contact', 'Customer Address',
        'Quantity', 'Discount', 'Shipment Charges', 'Setup Charges','Other Charges','Amount Paid','Total','Remaining','Date'),
                            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_x.pack(side=BOTTOM, fill=X)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.config(command=invoicetable.xview)
    scrollbar_y.config(command=invoicetable.yview)

    invoicetable.heading('Invoice Id', text='Invoice Id')
    invoicetable.heading('Product Id', text='Product Id')
    invoicetable.heading('Product Barcode', text='Product Barcode')
    invoicetable.heading('Product Price', text='Product Price')
    invoicetable.heading('Product Name', text='Product Name')
    invoicetable.heading('Product Type', text='Product Type')
    invoicetable.heading('Customer Name', text='Customer Name')
    invoicetable.heading('Customer contact', text='Customer contact')
    invoicetable.heading('Customer Address', text='Customer Address')
    invoicetable.heading('Quantity', text='Quantity')
    invoicetable.heading('Discount', text='Discount')
    invoicetable.heading('Shipment Charges', text='Shipment Charges')
    invoicetable.heading('Setup Charges', text='Setup Charges')
    invoicetable.heading('Other Charges', text='Other Charges')
    invoicetable.heading('Total', text='Total')
    invoicetable.heading('Amount Paid', text='Amount Paid')
    invoicetable.heading('Remaining', text='Remaining')
    invoicetable.heading('Date', text='Date')
    invoicetable['show'] = 'headings'
    invoicetable.column('Invoice Id', width=100)
    invoicetable.column('Product Id', width=200)
    invoicetable.column('Product Barcode', width=200)
    invoicetable.column('Product Price', width=200)
    invoicetable.column('Product Name', width=200)
    invoicetable.column('Product Type', width=300)
    invoicetable.column('Customer Name', width=100)
    invoicetable.column('Customer Name', width=200)
    invoicetable.column('Customer contact', width=200)
    invoicetable.column('Customer Address', width=300)
    invoicetable.column('Quantity', width=200)
    invoicetable.column('Shipment Charges', width=200)
    invoicetable.column('Setup Charges', width=200)
    invoicetable.column('Other Charges', width=200)
    invoicetable.column('Amount Paid', width=200)
    invoicetable.column('Total', width=200)
    invoicetable.column('Remaining', width=200)
    invoicetable.column('Date', width=200)
    invoicetable.pack(fill=BOTH, expand=True)
    invoicetable.bind('<<TreeviewSelect>>', invoicecallback)
    invoicetable.config(selectmode='browse')
def customercradits(event):


    customerid=IntVar()
    invoiceid=IntVar()
    customername=StringVar()
    customeraddress=StringVar()
    customercontact=StringVar()
    quantity=IntVar()
    discount=DoubleVar()
    shipmentcharges=DoubleVar()
    setupcharges=DoubleVar()
    othercharges=DoubleVar()
    payment=DoubleVar()
    totelamount=DoubleVar()
    remaning=DoubleVar()
    date=StringVar()

    def callback(event):
        customerstable.selection()
        curItem = customerstable.focus()
        content = customerstable.item(curItem)
        pp = content['values']
        if len(pp) != 0:
            customerid.set(pp[0])
            invoiceid.set(pp[1])
            customername.set(pp[2])
            customeraddress.set(pp[3])
            customercontact.set(pp[4])
            quantity.set(pp[5])
            discount.set(pp[6])
            shipmentcharges.set(pp[7])
            setupcharges.set(pp[8])
            othercharges.set(pp[9])
            payment.set(pp[10])
            totelamount.set(pp[11])
            remaning.set(pp[12])
            date.set(pp[13])

            # here i can add another item as i want to change

    def search():
        try:
            customernamevalue = customername.get()
            if customernamevalue == '':
                messagebox.showerror("warning!!!", "please insert some data in the field")

            elif customernamevalue != '':
                conn = sqlite3.connect('japan.db')
                selectquery = "SELECT * FROM customer_table WHERE c_name=?"
                cur = conn.cursor()
                cur.execute(selectquery, (customernamevalue,))
                storedata = cur.fetchall()
                customerstable.delete(*customerstable.get_children())
                for i in storedata:
                    storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11],i[12],i[13]]
                    customerstable.insert('', END, values=storedata)
                conn.commit()
                conn.close()
        except:
            messagebox.showerror("Error", "somthing Went Wrong try again with valid Barcode id")

    def showdata():
        conn = sqlite3.connect('japan.db')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM customer_table')
        customerstable.delete(*customerstable.get_children())
        for i in data:
            storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11],i[12],i[13]]
            customerstable.insert('', END, values=storedata)
        conn.commit()
        conn.close()

    def exportproductsdata():
        try:
            ff = filedialog.asksaveasfile()
            gg = customerstable.get_children()
            customer_id,invoice_id,customer_name,customer_contact,customer_address,quantity_,discount_val,shipment_charges,setup_charges,other_charges,pay_mant,total_amount,remaning_amount,datee = [], [], [], [], [], [], [], [], [], [], [], [],[],[]

            for i in gg:
                content = customerstable.item(i)
                pp = content['values']
                customer_id.append(pp[0]), \
                invoice_id.append(pp[1]), \
                customer_name.append(pp[2]), \
                customer_contact.append(pp[3]), \
                customer_address.append(pp[4]), \
                quantity_.append(pp[5]), \
                discount_val.append(pp[6]), \
                shipment_charges.append(pp[7]), \
                setup_charges.append(pp[8]), \
                other_charges.append(pp[9]), \
                pay_mant.append(pp[10]), \
                total_amount.append(pp[11])
                remaning_amount.append(pp[12])
                datee.append(pp[13])

            dd = ['c_id','invoice_id','c_name','c_contact','c_address','quantity',  'discount',  'shipment_charges',  'setup_charges',  'other_charges',  'payment',  'total',  'remaning',  'date']
            df = pandas.DataFrame(list(
                zip(customer_id,invoice_id,customer_name,customer_contact,customer_address,quantity_,discount_val,shipment_charges,setup_charges,other_charges,pay_mant,total_amount,remaning_amount,datee)), columns=dd)

            # paths = '{}.csv'.format(ff)

            df.to_csv(ff, index=False)

            # paths, mode = 'w', encoding = None, index=False

            messagebox.showinfo("notification", "data exported successfully {}")
        except:
            messagebox.showerror("warning", "somthing went wrong please try saving file with filename.csv")



    ############################################# wegits of manage product entry##############################
    add_product_frame = Frame(bd=4, relief=RIDGE, bg="snow")
    add_product_frame.place(x=370, y=70, width=1150, height=720)
    add_product_title = Label(add_product_frame, text="Customers", font=("times new roman ", 20, "bold"),
                              fg="black", bg="snow")
    add_product_title.pack(fill=X, side=TOP)



    '''invoice_id lbl'''
    invoice_id_lbl = Label(add_product_frame, text="Invoice Id:", font=("times new roman ", 12, "bold"), fg="black",
                        bg="snow")
    invoice_id_lbl.place(x=20, y=20)

    '''Invoice Id entry'''
    invoice_entry = Entry(add_product_frame, textvariable=invoiceid,state=DISABLED, font=("times new roman ", 12), bd=5,
                          relief=GROOVE)
    invoice_entry.place(x=170, y=20)

    '''customer name  lbl'''
    customer_name_lbl = Label(add_product_frame, text="Customer Name:", font=("times new roman ", 12, "bold"), fg="black",
                           bg="snow")
    customer_name_lbl.place(x=20, y=60)

    '''customer name entry'''
    customer_name_entry = Entry(add_product_frame, textvariable=customername,state=DISABLED, font=("times new roman ", 12), bd=5,
                          relief=GROOVE)
    customer_name_entry.place(x=170, y=60)

    #---------------
    '''customer contact lbl'''
    customer_contact_lbl = Label(add_product_frame, text="Customer Address:", font=("times new roman ", 12, "bold"),
                              fg="black",
                              bg="snow")
    customer_contact_lbl.place(x=20, y=100)

    '''customer contact entry'''
    customer_contact_entry = Entry(add_product_frame, textvariable=customercontact,state=DISABLED, font=("times new roman ", 12), bd=5,
                                relief=GROOVE)
    customer_contact_entry.place(x=170, y=100)

    # ---------------
    '''customer address lbl'''
    customer_address_lbl = Label(add_product_frame, text="Customer Contact:", font=("times new roman ", 12, "bold"),
                                 fg="black",
                                 bg="snow")
    customer_address_lbl.place(x=20, y=140)

    '''customer address entry'''
    customer_address_entry = Entry(add_product_frame, textvariable=customeraddress,state=DISABLED, font=("times new roman ", 12), bd=5,
                                   relief=GROOVE)
    customer_address_entry.place(x=170, y=140)

    # ---------------
    '''customer quantity lbl'''
    customer_quantity_lbl = Label(add_product_frame, text="Quantity:", font=("times new roman ", 12, "bold"),
                                 fg="black",
                                 bg="snow")
    customer_quantity_lbl.place(x=20, y=180)

    '''customer address entry'''
    customer_quantity_entry = Entry(add_product_frame, textvariable=quantity,state=DISABLED, font=("times new roman ", 12), bd=5,
                                   relief=GROOVE)
    customer_quantity_entry.place(x=170, y=180)
    # ---------------
    '''customer quantity lbl'''
    customer_quantity_lbl = Label(add_product_frame, text="discount:", font=("times new roman ", 12, "bold"),
                                  fg="black",
                                  bg="snow")
    customer_quantity_lbl.place(x=20, y=220)

    '''customer address entry'''
    customer_quantity_entry = Entry(add_product_frame, textvariable=discount,state=DISABLED, font=("times new roman ", 12), bd=5,
                                    relief=GROOVE)
    customer_quantity_entry.place(x=170, y=220)

    # ---------------
    '''customer discount lbl'''
    customer_discount_lbl = Label(add_product_frame, text="Shipment Charges:", font=("times new roman ", 12, "bold"),
                                  fg="black",
                                  bg="snow")
    customer_discount_lbl.place(x=20, y=260)

    '''customer shipment entry'''
    customer_discount_entry = Entry(add_product_frame, textvariable=shipmentcharges, state=DISABLED,font=("times new roman ", 12), bd=5,
                                    relief=GROOVE)
    customer_discount_entry.place(x=170, y=260)

    # ---------------
    '''customer shipment lbl'''
    customer_shipment_lbl = Label(add_product_frame, text="Setup Charges:", font=("times new roman ", 12, "bold"),
                                  fg="black",
                                  bg="snow")
    customer_shipment_lbl.place(x=20, y=300)

    '''customer address entry'''
    customer_discount_entry = Entry(add_product_frame, textvariable=setupcharges, state=DISABLED,font=("times new roman ", 12), bd=5,
                                    relief=GROOVE)
    customer_discount_entry.place(x=170, y=300)

    # ---------------
    '''customer shipment lbl'''
    customer_shipment_lbl = Label(add_product_frame, text="Other Charges:", font=("times new roman ", 12, "bold"),
                                  fg="black",
                                  bg="snow")
    customer_shipment_lbl.place(x=20, y=340)

    '''customer setupup entry'''
    customer_setupup_entry = Entry(add_product_frame, textvariable=othercharges, state=DISABLED,font=("times new roman ", 12),
                                    bd=5,
                                    relief=GROOVE)
    customer_setupup_entry.place(x=170, y=340)


    # ---------------
    '''customer payment  lbl'''
    customer_payment_lbl = Label(add_product_frame, text="Amount Paid:", font=("times new roman ", 12, "bold"),
                                  fg="black",
                                  bg="snow")
    customer_payment_lbl.place(x=20, y=380)

    '''customer setupup entry'''
    customer_payment_entry = Entry(add_product_frame, textvariable=payment,state=DISABLED, font=("times new roman ", 12),
                                    bd=5,
                                    relief=GROOVE)
    customer_payment_entry.place(x=170, y=380)

    # ---------------
    '''customer Total  lbl'''
    customer_Total_lbl = Label(add_product_frame, text="Total Amount:", font=("times new roman ", 12, "bold"),
                                 fg="black",
                                 bg="snow")
    customer_Total_lbl.place(x=20, y=420)

    '''customer setupup entry'''
    customer_Total_entry = Entry(add_product_frame, state=DISABLED,textvariable=totelamount, font=("times new roman ", 12),
                                   bd=5,
                                   relief=GROOVE)
    customer_Total_entry.place(x=170, y=420)

    # ---------------
    '''customer Total  lbl'''
    customer_Total_lbl = Label(add_product_frame, text="Remaning:", font=("times new roman ", 12, "bold"),
                               fg="black",
                               bg="snow")
    customer_Total_lbl.place(x=20, y=460)

    '''customer setupup entry'''
    customer_Total_entry = Entry(add_product_frame, state=DISABLED,textvariable=remaning, font=("times new roman ", 12),
                                 bd=5,
                                 relief=GROOVE)
    customer_Total_entry.place(x=170, y=460)

    # ---------------
    '''customer Total  lbl'''
    customer_Total_lbl = Label(add_product_frame, text="Payment Date:", font=("times new roman ", 12, "bold"),
                               fg="black",
                               bg="snow")
    customer_Total_lbl.place(x=20, y=500)

    '''customer setupup entry'''
    customer_Total_entry = Entry(add_product_frame, textvariable=date, state=DISABLED, font=("times new roman ", 12),
                                 bd=5,
                                 relief=GROOVE)
    customer_Total_entry.place(x=170, y=500)

    ##################################

    '''customer_search_entry label  '''
    paymeny_lbl = Label(add_product_frame, text="Search Customer Name:", font=("times new roman ", 12, "bold"),
                       fg="black",
                       bg="snow")
    paymeny_lbl.place(x=100, y=570)
    '''customer_search_entry  '''
    customer_search_entry = Entry(add_product_frame, textvariable=customername, font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    customer_search_entry.place(x=100, y=600)

    ######################################################Buttons#########################################


    '''search button '''
    search_product_button = Button(add_product_frame, text="Search Product", width=22, height=1,
                                   font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                   activeforeground='black', command=search)
    search_product_button.place(x=100, y=635)

    '''show products record button '''
    show_product_button = Button(add_product_frame, text="Show  Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=showdata)
    show_product_button.place(x=950, y=10)

    '''Export  button '''
    show_product_button = Button(add_product_frame, text="Export Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=exportproductsdata)
    show_product_button.place(x=740, y=10)

    ######################################################Product Tree List and scroll bar  ################################
    showdataframe = Frame(add_product_frame, bg="snow", relief=GROOVE, bd=5)
    showdataframe.place(x=400, y=60, width=730, height=650)

    style = ttk.Style()
    style.configure('Treeview.Heading', font=('time new roman', 15, 'bold'), foreground='blue')
    style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', bg='light cyan', anchor="center")

    scrollbar_x = Scrollbar(showdataframe, orient=HORIZONTAL)
    scrollbar_y = Scrollbar(showdataframe, orient=VERTICAL)
    customerstable = Treeview(showdataframe, column=('ID','Invoice ID','Name','Contact','Address','Quantity','Discount','Shipment Charges',
                                                     'Setup Charges','Other Charges','Amount Paid','Net Amount', 'Remaning','Date'
                           ),yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_x.pack(side=BOTTOM, fill=X)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.config(command=customerstable.xview)
    scrollbar_y.config(command=customerstable.yview)

    customerstable.heading('ID', text='ID')
    customerstable.heading('Invoice ID', text='Invoice ID')
    customerstable.heading('Name', text='Name')
    customerstable.heading('Contact', text='Contact')
    customerstable.heading('Address', text='Address')
    customerstable.heading('Quantity', text='Quantity')
    customerstable.heading('Discount', text='Discount')
    customerstable.heading('Shipment Charges', text='Shipment Charges')
    customerstable.heading('Setup Charges', text='Setup Charges')
    customerstable.heading('Other Charges', text='Other Charges')
    customerstable.heading('Amount Paid', text='Amount Paid')
    customerstable.heading('Net Amount', text='Net Amount')
    customerstable.heading('Remaning', text='Remaning')
    customerstable.heading('Date', text='Date')
    customerstable['show'] = 'headings'
    customerstable.column('ID', width=50)
    customerstable.column('Invoice ID', width=100)
    customerstable.column('Name', width=200)
    customerstable.column('Contact', width=200)
    customerstable.column('Address', width=200)
    customerstable.column('Quantity', width=200)
    customerstable.column('Discount', width=200)
    customerstable.column('Shipment Charges', width=200)
    customerstable.column('Setup Charges', width=200)
    customerstable.column('Other Charges', width=200)
    customerstable.column('Amount Paid', width=200)
    customerstable.column('Net Amount', width=200)
    customerstable.column('Remaning', width=200)
    customerstable.column('Date', width=200)
    customerstable.pack(fill=BOTH, expand=True)

    customerstable.bind('<<TreeviewSelect>>', callback)
    customerstable.config(selectmode='browse')
def inventoryreport(event):
    productid=IntVar()
    inventoryid=IntVar()
    productbarcode=StringVar()
    productname = StringVar()
    producttype = StringVar()
    purchasedfrom = StringVar()
    madeby = StringVar()
    model = StringVar()
    purchaseprice = DoubleVar()
    retailprice = DoubleVar()
    description = StringVar()


    def callback(event):
        inventorytable.selection()
        curItem = inventorytable.focus()
        content = inventorytable.item(curItem)
        pp = content['values']
        if len(pp) != 0:
            inventoryid.set(pp[0])
            productid.set(pp[1])
            productbarcode.set(pp[2])
            productname.set(pp[3])
            producttype.set(pp[4])
            purchasedfrom.set(pp[5])
            madeby.set(pp[6])
            model.set(pp[7])
            purchaseprice.set(pp[8])
            retailprice.set(pp[9])
            description.set(pp[10])

            # here i can add another item as i want to change

    def search():
        # try:
        productbarcodevalue = productbarcode.get()
        if productbarcodevalue == '':
            messagebox.showerror("warning!!!", "please insert some data in the field")

        elif productbarcodevalue != '':
            conn = sqlite3.connect('japan.db')
            selectquery = "SELECT * FROM inventory WHERE p_barcode=?"
            cur = conn.cursor()
            cur.execute(selectquery, (productbarcodevalue,))
            storedata = cur.fetchall()
            inventorytable.delete(*inventorytable.get_children())
            for i in storedata:
                storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]]
                inventorytable.insert('', END, values=storedata)
            conn.commit()
            conn.close()
        # except:
        #     messagebox.showerror("Error", "somthing Went Wrong try again with valid Barcode id")

    def showdata():
        conn = sqlite3.connect('japan.db')
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM inventory')
        inventorytable.delete(*inventorytable.get_children())
        for i in data:
            storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]]
            inventorytable.insert('', END, values=storedata)
        conn.commit()
        conn.close()

    def exportproductsdata():
        try:
            ff = filedialog.asksaveasfile()
            gg = inventorytable.get_children()
            inventoryid_,id, barcode, product_name, p_type, purchased_from, made_by, mmodel, p_price, r_price, decs, addeddate, updateddate = [], [], [], [], [], [], [], [], [], [], [], [],[]
            for i in gg:
                content = inventorytable.item(i)
                pp = content['values']
                inventoryid_.append(pp[0]), \
                id.append(pp[1]), \
                barcode.append(pp[2]), \
                product_name.append(pp[3]), \
                p_type.append(pp[4]), \
                purchased_from.append(pp[5]), \
                made_by.append(pp[6]), \
                mmodel.append(pp[7]), \
                p_price.append(pp[8]), \
                r_price.append(pp[9]), \
                decs.append(pp[10]), \
                addeddate.append(pp[11]), \
                updateddate.append(pp[12])

            dd = ['Inventory Id','Product Id ', 'Product Barcode', 'Product Name', 'Product Type', 'Purchased From ', 'Made By',
                  'Model ', 'Purchase Price', 'Retail Price', 'Description', 'Added Date', 'Updated Date']
            df = pandas.DataFrame(list(
                zip(inventoryid_,id, barcode, product_name, p_type, purchased_from, made_by, mmodel, p_price, r_price, decs,
                    addeddate, updateddate)), columns=dd)

            # paths = '{}.csv'.format(ff)

            df.to_csv(ff, index=False)

            # paths, mode = 'w', encoding = None, index=False

            messagebox.showinfo("notification", "data exported successfully {}")
        except:
            messagebox.showerror("warning", "somthing went wrong please try saving file with filename.csv")

    def clear():

        supname.set('')
        supcontact.set('')
        totalamount.set(0.0)
        amountpaid.set(0.0)

    def adddetails():

        if supname.get() == '' or supcontact.get() == '' or totalamount.get() == '' or amountpaid.get() == '' or remaningamount.get() == '':
            messagebox.showerror("warning!!!", "please fill all the inpput fields")
        else:
            supidvalue = supid.get()
            supnamevalue = supname.get()
            supcontactvalue = supcontact.get()
            totalamountvalue = totalamount.get()
            amountpaidvalue = amountpaid.get()
            remaningamountvalue = remaningamount.get()

            try:
                conn = sqlite3.connect('japan.db')
                cur = conn.cursor()
                remaningamountvalue = totalamountvalue - amountpaidvalue
                insertsql = 'INSERT INTO supliers_table VALUES(NULL,?,?,?,?,?,CURRENT_TIMESTAMP,NULL)'
                cur.execute(insertsql,
                            (supnamevalue, supcontactvalue, totalamountvalue, amountpaidvalue, remaningamountvalue))
                conn.commit()
                res = messagebox.askyesno("notification", "Suplier Name:{} added successfully".format(supnamevalue),
                                          parent=add_product_frame)
                if res == True:
                    clear()
            except:
                messagebox.showerror("warning!!!", "this id is already exist please enter another",
                                     parent=add_product_frame)
            selectquery = "SELECT * FROM supliers_table"
            data = cur.execute(selectquery)
            inventorytable.delete(*inventorytable.get_children())
            for i in data:
                storedata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                inventorytable.insert('', END, values=storedata)

    def updatedetails():

        if supid.get() == 0:
            messagebox.showerror("warnning", "select the supliers ")
            return
        supidvalue = supid.get()
        supnamevalue = supname.get()
        supcontactvalue = supcontact.get()
        totalamountvalue = totalamount.get()
        amountpaidvalue = amountpaid.get()
        remaningamountvalue = remaningamount.get()
        remaningamountvalue = totalamountvalue - amountpaidvalue

        try:
            conn = sqlite3.connect('japan.db')
            cur = conn.cursor()
            update = "UPDATE supliers_table SET sup_name =  ?, sup_contact =  ?, total_amount =  ?, amount_paid_by_company =  ?, remaning_amount =  ?, update_date =CURRENT_TIMESTAMP WHERE sup_id = ?;"
            cur.execute(update,
                        (supnamevalue, supcontactvalue, totalamountvalue, amountpaidvalue, remaningamountvalue,
                         supidvalue))
            conn.commit()
            messagebox.showinfo("notification", "data updated successfully")
            showdata()
        except:
            messagebox.showerror("Error", "Somthing Went Wrong Please Try again")

    def daletedetails():
        if supid.get() == 0:
            messagebox.showerror("warnning", "select the supliers ")
            return
        conn = sqlite3.connect("japan.db")
        cur = conn.cursor()
        for selected_item in inventorytable.selection():
            # it prints the selected row id
            cur.execute("DELETE FROM supliers_table WHERE sup_id=?", (inventorytable.set(selected_item, '#1'),))
            conn.commit()
            inventorytable.delete(selected_item)
        messagebox.showinfo("notification", " data is deleted successfully")
        conn.close()
        clear()

    ############################################# wegits of manage product entry##############################
    add_product_frame = Frame(bd=4, relief=RIDGE, bg="snow")
    add_product_frame.place(x=370, y=70, width=1150, height=720)
    add_product_title = Label(add_product_frame, text="Inventory ", font=("times new roman ", 20, "bold"),
                              fg="black", bg="snow")
    add_product_title.pack(fill=X, side=TOP)

    '''Inventory Id'''
    inventory_id_lbl = Label(add_product_frame, text="Inventory Id:", font=("times new roman ", 12, "bold"), fg="black",
                          bg="snow")
    inventory_id_lbl.place(x=20, y=20)

    '''inventory Id entry'''
    inventory_id_entry = Entry(add_product_frame, state=DISABLED, textvariable=inventoryid, font=("times new roman ", 12), bd=5,
                            relief=GROOVE)
    inventory_id_entry.place(x=170, y=20)

    #################################
    '''p id  name'''
    p_id_lbl = Label(add_product_frame, text="Product Id:", font=("times new roman ", 12, "bold"), fg="black",
                             bg="snow")
    p_id_lbl.place(x=20, y=60)

    '''product  Id entry'''
    p_id_entry = Entry(add_product_frame,  state=DISABLED,textvariable=productid, font=("times new roman ", 12), bd=5,
                               relief=GROOVE)
    p_id_entry.place(x=170, y=60)

    ##################################
    #################################
    '''Barcode'''
    barocde_lbl = Label(add_product_frame, text="Barcode:", font=("times new roman ", 12, "bold"),
                                fg="black",
                                bg="snow")
    barocde_lbl.place(x=10, y=100)

    ''' barcode entry'''
    barocde_entry = Entry(add_product_frame, state=DISABLED,textvariable=productbarcode, font=("times new roman ", 12), bd=5,
                                  relief=GROOVE)
    barocde_entry.place(x=170, y=100)

    ##################################

    #################################
    '''Product name '''
    prodduct_name_lbl = Label(add_product_frame, text="Product Name:",
                                     font=("times new roman ", 12, "bold"),
                                     fg="black",
                                     bg="snow")
    prodduct_name_lbl.place(x=10, y=140)

    '''product name entry'''
    prodduct_name_entry = Entry(add_product_frame, state=DISABLED,textvariable=productname, font=("times new roman ", 12), bd=5,
                                       relief=GROOVE)
    prodduct_name_entry.place(x=170, y=140)

    ##################################

    #################################
    ''' Amount to be paid '''
    p_type_lbl = Label(add_product_frame, text="Product Type:",
                                    font=("times new roman ", 12, "bold"),
                                    fg="black",
                                    bg="snow")
    p_type_lbl.place(x=10, y=180)

    '''Invoice Id entry'''
    p_type_entry = Entry(add_product_frame,state=DISABLED, textvariable=producttype, font=("times new roman ", 12), bd=5,
                                      relief=GROOVE)
    p_type_entry.place(x=170, y=180)

    ##################################

    #################################
    ''' Remaning Amount '''
    purchased_from_lbl = Label(add_product_frame, text="Purchased From:",
                                        font=("times new roman ", 12, "bold"),
                                        fg="black",

                                        bg="snow")
    purchased_from_lbl.place(x=10, y=220)

    '''Invoice Id entry'''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=purchasedfrom,
                                          font=("times new roman ", 12), bd=5,
                                          relief=GROOVE)
    purchased_from_entry.place(x=170, y=220)

    ##################################

    #################################
    ''' made by '''
    purchased_from_lbl = Label(add_product_frame, text="Made By:",
                               font=("times new roman ", 12, "bold"),
                               fg="black",

                               bg="snow")
    purchased_from_lbl.place(x=10, y=260)

    '''made by '''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=madeby,
                                 font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    purchased_from_entry.place(x=170, y=260)

    ##################################

    #################################
    ''' model '''
    purchased_from_lbl = Label(add_product_frame, text="Made By:",
                               font=("times new roman ", 12, "bold"),
                               fg="black",

                               bg="snow")
    purchased_from_lbl.place(x=10, y=300)

    '''model'''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=model,
                                 font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    purchased_from_entry.place(x=170, y=300)

    ##################################

    #################################
    ''' purchase price  '''
    purchased_from_lbl = Label(add_product_frame, text="Purchase Price:",
                               font=("times new roman ", 12, "bold"),
                               fg="black",

                               bg="snow")
    purchased_from_lbl.place(x=10, y=340)

    '''purchase price '''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=purchaseprice,
                                 font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    purchased_from_entry.place(x=170, y=340)

    ##################################

    #################################
    ''' retial price  '''
    purchased_from_lbl = Label(add_product_frame, text="Purchase Price:",
                               font=("times new roman ", 12, "bold"),
                               fg="black",

                               bg="snow")
    purchased_from_lbl.place(x=10, y=380)

    '''retial price '''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=retailprice,
                                 font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    purchased_from_entry.place(x=170, y=380)

    ##################################

    #################################
    ''' desc '''
    purchased_from_lbl = Label(add_product_frame, text="Descripton:",
                               font=("times new roman ", 12, "bold"),
                               fg="black",

                               bg="snow")
    purchased_from_lbl.place(x=10, y=420)

    '''desc'''
    purchased_from_entry = Entry(add_product_frame, state=DISABLED, textvariable=description,
                                 font=("times new roman ", 12), bd=5,
                                 relief=GROOVE)
    purchased_from_entry.place(x=170, y=420)

    ##################################

    #################################

    '''customer_search_entry label  '''
    paymeny_lbl = Label(add_product_frame, text="Search Product Barcode:", font=("times new roman ", 12, "bold"),
                        fg="black",
                        bg="snow")
    paymeny_lbl.place(x=100, y=550)
    '''customer_search_entry  '''
    customer_search_entry = Entry(add_product_frame, textvariable=productbarcode, font=("times new roman ", 12), bd=5,
                                  relief=GROOVE)
    customer_search_entry.place(x=100, y=600)

    ######################################################Buttons#########################################

    # '''clear button '''
    # search_product_button = Button(add_product_frame, text="Clear Input", width=15, height=1,
    #                                font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                activeforeground='black', command=clear)
    # search_product_button.place(x=60, y=280)
    #
    # '''Add button '''
    # search_product_button = Button(add_product_frame, text="Add Details", width=15, height=1,
    #                                font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                activeforeground='black', command=adddetails)
    # search_product_button.place(x=210, y=280)
    #
    # '''Update button '''
    # search_product_button = Button(add_product_frame, text="Update Details", width=15, height=1,
    #                                font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                activeforeground='black', command=updatedetails)
    # search_product_button.place(x=210, y=340)
    #
    # '''Delete button '''
    # search_product_button = Button(add_product_frame, text="Delete Details", width=15, height=1,
    #                                font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
    #                                activeforeground='black', command=daletedetails)
    # search_product_button.place(x=60, y=340)

    '''search button '''
    search_product_button = Button(add_product_frame, text="Search Product", width=22, height=1,
                                   font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                   activeforeground='black', command=search)
    search_product_button.place(x=100, y=660)

    '''show products record button '''
    show_product_button = Button(add_product_frame, text="Show  Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=showdata)
    show_product_button.place(x=950, y=10)

    '''Export  button '''
    show_product_button = Button(add_product_frame, text="Export Records", width=20, height=1,
                                 font=("time new roman", 10, "bold"), bd=4, activebackground='light cyan',
                                 activeforeground='black', command=exportproductsdata)
    show_product_button.place(x=740, y=10)

    ######################################################Product Tree List and scroll bar  ################################
    showdataframe = Frame(add_product_frame, bg="snow", relief=GROOVE, bd=5)
    showdataframe.place(x=400, y=60, width=730, height=650)

    style = ttk.Style()
    style.configure('Treeview.Heading', font=('time new roman', 15, 'bold'), foreground='blue')
    style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', bg='light cyan', anchor="center")

    scrollbar_x = Scrollbar(showdataframe, orient=HORIZONTAL)
    scrollbar_y = Scrollbar(showdataframe, orient=VERTICAL)
    inventorytable = Treeview(showdataframe, column=(
    'Inventory Id', 'Product Id', 'Product Barcode', 'Product Name', 'Product Type', 'Purchased From',
    'Made By', 'Model', 'Purchase Price', 'Retail Price', 'Description', 'Added Date', 'Updated Date'), yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_x.pack(side=BOTTOM, fill=X)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.config(command=inventorytable.xview)
    scrollbar_y.config(command=inventorytable.yview)

    inventorytable.heading('Inventory Id', text='Inventory Id')
    inventorytable.heading('Product Id', text='Product Id')
    inventorytable.heading('Product Barcode', text='Product Barcode')
    inventorytable.heading('Product Name', text='Product Name')
    inventorytable.heading('Product Type', text='Product Type')
    inventorytable.heading('Purchased From', text='Purchased From')
    inventorytable.heading('Made By', text='Made By')
    inventorytable.heading('Model', text='Model')
    inventorytable.heading('Purchase Price', text='Purchase Price')
    inventorytable.heading('Retail Price', text='Retail Price')
    inventorytable.heading('Description', text='Description')
    inventorytable.heading('Added Date', text='Added Date')
    inventorytable.heading('Updated Date', text='Updated Date')

    inventorytable['show'] = 'headings'
    inventorytable.column('Inventory Id', width=150)
    inventorytable.column('Product Id', width=150)
    inventorytable.column('Product Barcode', width=200)
    inventorytable.column('Product Name', width=200)
    inventorytable.column('Product Type', width=200)
    inventorytable.column('Purchased From', width=200)
    inventorytable.column('Made By', width=200)
    inventorytable.column('Model', width=200)
    inventorytable.column('Purchase Price', width=200)
    inventorytable.column('Retail Price', width=200)
    inventorytable.column('Description', width=200)
    inventorytable.column('Added Date', width=200)
    inventorytable.column('Updated Date', width=200)
    inventorytable.pack(fill=BOTH, expand=True)

    inventorytable.bind('<<TreeviewSelect>>', callback)
    inventorytable.config(selectmode='browse')
################################################################# MANAGE EXPENSES REPORT FUNCTION ######################
def expensereport(event):
    print("expenses ")
################################################################# MANAGE ACCOUNTS FUNCTION #############################
def accounts(event):
    print("accounts")
admin_window = Tk()
witdth_value = admin_window.winfo_screenwidth()
height_value = admin_window.winfo_screenheight()
admin_window.geometry("%dx%d+0+0" % (witdth_value, height_value))
admin_window.title("Japan Medical Company System |User ")
# admin_window.iconbitmap('logo.ico')
ss = 'Welcome to Japan Medical Company System | User'
count = 0
text = ''

title = Label(text=ss, bd=10, relief=GROOVE,
              font=("times new roman", 30, "bold"), bg="snow", fg="blue")
title.pack(side=TOP, fill=X)
introlabeltick()
introlabelcolors()
clock = Label(admin_window, font=("times new roman", 14, " bold"), width=15, bg='snow')
clock.place(x=10, y=5)
tick()
######################################################################side bar frame####################################
Options_Frame = Frame(bd=4, relief=RIDGE, bg="light cyan")
Options_Frame.place(x=1, y=70, width=350, height=720)
scrollbar_x = Scrollbar(Options_Frame, orient=VERTICAL)
scrollbar_x.pack(side=RIGHT, fill=Y)
######################################################################side bar wegts####################################
homelbl = Label(Options_Frame, text="Home", bd=5, relief=GROOVE, anchor="w", font=("times new roman", 20, " bold"),
                width=20, bg='light cyan', fg="black", activebackground='blue', activeforeground='white', )
homelbl.pack(side=TOP, expand=True)
homelbl.bind("<Button-1>", home)
# productlbl = Label(Options_Frame, text="Products", bd=5, anchor="w", relief=GROOVE,
#                    font=("times new roman", 20, " bold"),
#                    width=20, bg='light cyan', fg="black", activebackground='blue', activeforeground='white', )
# productlbl.pack(side=TOP, expand=True)
# productlbl.bind("<Button-1>", products)

invoicelbl = Label(Options_Frame, text="Invoice", bd=5, anchor="w", relief=GROOVE,
                   font=("times new roman", 20, " bold"),
                   width=20, bg='light cyan', fg="black", activebackground='blue', activeforeground='white', )
invoicelbl.pack(side=TOP, expand=True)
invoicelbl.bind("<Button-1>", invoice)



debtorsandcraditorsrlbl = Label(Options_Frame, text="Customers Credits ", anchor="w", bd=5, relief=GROOVE,
                                font=("times new roman", 20, " bold"),
                                width=20, bg='light cyan', fg="black", activebackground='blue',
                                activeforeground='white', )
debtorsandcraditorsrlbl.pack(side=TOP, expand=True)
debtorsandcraditorsrlbl.bind("<Button-1>", customercradits)


inventoryreportlbl = Label(Options_Frame, text="Inventory Report", anchor="w", bd=5, relief=GROOVE,
                           font=("times new roman", 20, " bold"),
                           width=20, bg='light cyan', fg="black", activebackground='blue', activeforeground='white', )
inventoryreportlbl.pack(side=TOP, expand=True)
inventoryreportlbl.bind("<Button-1>", inventoryreport)

admin_window.mainloop()
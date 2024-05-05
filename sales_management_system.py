from tkinter import *
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet 
import pymysql
import datetime as dt


def invprint():
    invn = int(invno.get()) 
    if invn != 0:
    #Select Invoice details from MySQL DB
        connection = pymysql.connect(host='localhost', user='root', password='Ritanya@2021', database='sys')
        mycursorsel = connection.cursor()
        sql = "select inv_no,inv_date,prod_name,cust_name,prod_qty, \ prod_rate,PRICE,CGST_Amount,SGST_Amount,IGST_Amount from sales.invoice where inv_no=%s"
        mycursorsel.execute(sql, invn) 
        dbdata=mycursorsel.fetchall() 
        datalist=[]
        totvalue=0
        if dbdata:
            for r in dbdata: 
                datalist.append(r[0]) 
                datalist.append("2022-03-15") 
                datalist.append(r[2]) 
                datalist.append(r[4]) 
                datalist.append(r[5]) 
                datalist.append(r[6]) 
                datalist.append(r[7]) 
                datalist.append(r[8]) 
                datalist.append(r[9]) 
                totvalue= r[5]+r[6]+r[7]+r[8]
            DATA = [
                ["Bill To:", "ABC MARKETING", "", "", "", "", "", "", ""],
                ["Inv No", "Inv Date", "Prod Name", "Qty", "Rate", "Price", "SGST", "CGST", "IGST"],
                    ]


            DATA.append(datalist)
            DATA.append(["Total", "", "", "", "", "", "","", totvalue]) 
        mycursorsel.close()
        connection.close()
        pdf = SimpleDocTemplate("invoice1.pdf", pagesize=A4) 
        styles = getSampleStyleSheet()
        title_style = styles["Heading2"] 
        title_style.alignment = 1
        m = '''HYDRO ENGINEERING - \nTAX INVOICE '''
        title = Paragraph(m, title_style) 
        style = TableStyle(
                [
                    ("BOX", (0, 0), (-1, -1), 1, colors.black),
                    ("GRID", (0, 1), (8, 8), 1, colors.black),
                    ("BACKGROUND", (0, 0), (8, 0), colors.gray),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ]
            )


        table = Table(DATA, style=style) 
        pdf.build([title, table])
    else:
        Label(window, text="please enter invoice number", fg="red", justify= CENTER).place(x=210, y=100)

#Insert record in MySQL Table 
def dbinsert():
    date = dt.datetime.now()
    format_date = f"{date:%Y-%m-%d}"

    L=[]
    c_inv_no=int(input("Enter the Invoice Number(int) : ")) 
    L.append(c_inv_no)
    L.append(format_date) 
    c_cust_name=input("Enter the Customer Name: ") 
    L.append(c_cust_name)
    c_mobile=input("Enter customer phone number : ") 
    L.append(c_mobile)
    c_prod_name=input("Enter Product name: ") 
    L.append(c_prod_name) 
    c_prod_qty=int(input("Enter product qty(int) : ")) 
    L.append(c_prod_qty)
    c_rate=float(input("Enter rate(int) :")) 
    L.append(c_rate) 
    price=float(c_prod_qty*c_rate) 
    L.append(price)
    SGST=0 
    CGST=0 
    IGST=0
    c_gst=int(input("Is Local sales (Enter 1) or Inter State (Enter 2) : ")) 
    c_gst_per=int(input("Enter GST percentage : "))
    if (c_gst==1): 
        SGST=price*((c_gst_per/100)/2) 
        CGST = price * ((c_gst_per / 100) / 2)
    elif (c_gst==2): 
        IGST=price*(c_gst_per/100)

    L.append(SGST) 
    L.append(CGST) 
    L.append(IGST) 
    invoice=(L) 
    print(invoice)
    connection = pymysql.connect(host='localhost', user='root', password= 'Ritanya@2021', database='sys')
    mycursor = connection.cursor()
    sql="INSERT INTO sales.Invoice (inv_no, inv_date, cust_name, cust_mobile, prod_name, prod_qty, prod_rate, price, CGST_Amount, SGST_Amount, \ IGST_Amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    mycursor.execute(sql,invoice) 
    connection.commit() 
    print("Saved Successfully")

    mycursor.close() 
    connection.close()

#Object declaration 
window = Tk()
window.geometry("580x130+10+20") 
window.title('Invoice')

date_ = StringVar() 
date_.set(f"{dt.datetime.now():%d-%m-%Y}")

invno = IntVar()
Label(window, text="Invoice Number ").place(x=50, y=30) 
Entry(window, textvariable=invno, justify=LEFT).place(x=145, y=30)

Label(window, text="Date ").place(x=295, y=30)
Entry(window, justify=LEFT, textvariable=date_).place(x=330, y=30) 
Button(window, text="Insert Invoice detail", command=dbinsert).place(x=145, y=70) 
Button(window, text="Print", command=invprint).place(x=300, y=70) 
window.mainloop()



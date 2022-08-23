#   project name    : inventory management system
#   made by         : Mrunmayee Shiledar

import mysql.connector
from datetime import date
from prettytable import PrettyTable


def clear():
  for _ in range(65):
     print()

def item_status(idr):
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    sql = 'select * from items where id ='+idr
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[3]

def add_item():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()

    name = input('Enter Item Name :')
    qty = input('Enter Quantity : ')
    price = input('Enter Price :')
    today = date.today()
    reorder = input('Enter Reorder Level :')
    sql = 'insert into items(name,price,qty,reorder) values ( "' + \
        name + '",' + price+','+qty+','+reorder+' );'
    #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
    #print(sql)
    cursor.execute(sql)
    #cursor.execute(sql2)
    conn.close()
    print('\n\nNew Item added successfully')
    wait = input('\n\n\n Press any key to continue....')

def sell_item():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    today = date.today()
    item_no = input('Enter Item ID :')
    qty = input('Enter sold Quantity : ')
    
    sql = 'update items set qty = qty-'+ qty +' where id='+item_no+';'
    sql2 = 'insert into transaction(dot,qty,type,item_id) values ("' + \
        str(today)+'",'+qty+',"sold" , '+item_no+');'

    #print(sql)
    result = item_status(item_no)
    #print(type(result))
    #print(result)
    
    if result >= int(qty):
      cursor.execute(sql)
      cursor.execute(sql2)
      print('\n\nItem upated successfully')
    else:
      print('We do not have this much of Quantity in our Stock')
    
    conn.close()
    
    wait = input('\n\n\n Press any key to continue....')


def received_item():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    today = date.today()
    item_no = input('Enter Item ID :')
    qty = input('Enter sold Quantity : ')
    sql = 'update items set qty = qty+' + qty + ' where id='+item_no+';'
    sql2 = 'insert into transaction(dot,qty,type,item_id) values ("' + \
        str(today)+'",'+qty+',"purchase",'+item_no+');'
    #print(sql)
    cursor.execute(sql)
    conn.close()
    print('\n\nItem upated successfully')
    wait = input('\n\n\n Press any key to continue....')

def search_item():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    clear()
    print('Search Screen ')
    print('-'*80)
    name = input('Enter Item Name :')
    sql ="select * from items where name like '%"+name+"%';"
    cursor.execute(sql)
    records = cursor.fetchall()
    t = PrettyTable(['ID', 'Item Name', 'Price', 'Quantity', 'Reorder Level'])
    for idr, name, price, qty, reorder in records:
      t.add_row([idr, name, price, qty, reorder])
   
    
    clear()
    print('Search Result for :',name)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_menu():
    while True:
      clear()
      print(' Search Menu')
      print("\n1.  Name wise")
      print('\n2.  back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        search_item()
      if choice == 2:
        break


def report_items():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    name = input('Enter Item Name :')
    sql = "select * from items;"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Item List')
    t = PrettyTable(['ID', 'Item Name', 'Price', 'Quantity', 'Reorder Level'])

    for idr, name, price, qty, reorder in records:
      t.add_row([idr,name,price,qty,reorder])
    # print(idr,name,fname,add,phone,email)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def report_qty_greater_reorder():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    sql = "select * from items where qty > reorder;"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Item List')
    t = PrettyTable(['ID', 'Item Name', 'Price', 'Quantity', 'Reorder Level'])

    for idr, name, price, qty, reorder in records:
      t.add_row([idr, name, price, qty, reorder])
    # print(idr,name,fname,add,phone,email)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def report_qty_lesser_reorder():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    sql = "select * from items where qty < reorder;"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Item List')
    t = PrettyTable(['ID', 'Item Name', 'Price', 'Quantity', 'Reorder Level'])

    for idr, name, price, qty, reorder in records:
      t.add_row([idr, name, price, qty, reorder])
    # print(idr,name,fname,add,phone,email)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def report_sold_items():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    today = date.today()
    sql = "select id, name,dot,t.qty,price from items,transaction t where id=tid and type='sold' and dot='"+str(today)+"';"
    cursor.execute(sql)
    records = cursor.fetchall()
    
    t = PrettyTable(['ID', 'Item Name', 'DOT', 'Quantity', 'Price'])
    for idr, name, dot, qty, price in records:
      t.add_row([idr, name, dot,qty,price])
    # print(idr,name,fname,add,phone,email)
    clear()
    print('Items Sold Today :', today)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def report_received_item():
    conn = mysql.connector.connect(
        host='localhost', database='stock', user='root', password='')
    cursor = conn.cursor()
    today = date.today()
    sql = "select id, name,dot,t.qty,price from items,transaction t where id=tid and type='purchase' and dot='" + \
        str(today)+"';"
    cursor.execute(sql)
    records = cursor.fetchall()

    t = PrettyTable(['ID', 'Item Name', 'DOT', 'Quantity', 'Price'])
    for idr, name, dot, qty, price in records:
      t.add_row([idr, name, dot, qty, price])
    # print(idr,name,fname,add,phone,email)
    clear()
    print('Items Received Today :',today)
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def report_menu():
    while True:
      clear()
      print(' Report Menu')
      print("\n1.  Item List")
      print('\n2.  sold Items - Today')
      print('\n3.  Received Items- Today')
      print('\n4.  Item Qty > Reorder')
      print('\n5.  Item Qty < Reorder')
      print('\n6.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        report_items()
      if choice == 2:
        report_sold_items()
      if choice == 3:
        report_received_item()
      if choice == 4:
        report_qty_greater_reorder()
      if choice == 5:
        report_qty_lesser_reorder()
      if choice == 6:
        break

def main_menu():
    while True:
      clear()
      print(' Main Menu')
      print("\n1.  Add Items")
      print('\n2.  sell Items')
      print('\n3.  Received Items')
      print('\n4.  Search Menu')
      print('\n5.  Report Menu')
      print('\n6.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      
      if choice == 1:
        add_item()
      if choice == 2:
        sell_item()
      if choice == 3:
        received_item()
      if choice == 4:
        search_menu()
      if choice == 5:
        report_menu()
      if choice == 6:
        break

if __name__ == "__main__":
    main_menu()

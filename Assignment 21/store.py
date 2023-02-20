
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="store_python"
)
mycursor = mydb.cursor()

def show_menue():
    print("1_ Add")
    print("2_ Edit")
    print("3_ Remove")
    print("4_ Search")
    print("5_ Show List")
    print("6_ Buy")
   

def add():
    name=input("enter name : ")
    price=input("enter price : ")
    count=input("enter count : ")
    
    sql = "INSERT INTO products (name, price, count) VALUES (%s, %s, %s)"
    val = (name, price, count)
    mycursor.execute(sql, val)

    mydb.commit()

def edit():
    id=input("Enter Your id Product: ")
    mycursor.execute(f"SELECT * FROM products WHERE id ='{id}'")
    myresult = mycursor.fetchone()    
    if myresult != None:

        name = input("enter name product :")
        if name =="":
           name= myresult[1]
        price = input("enter price product :")
        if price == "":
            price =  myresult[2]
        count = input("enter count product :")
        if count == "" :
            count=  myresult[3]
        sql = f"UPDATE products SET name = '{name}', price = {price}, count = '{count}' WHERE id = '{id}'"

        mycursor.execute(sql)
        mydb.commit()
    else:
        print("The desired product was NOT found")     
      
def remove():
    id=input("Enter Your id product : ")
    sql = f"DELETE FROM products WHERE id = '{id}'"
    mycursor.execute(sql)
    mydb.commit() 

def search():
    Keyword=input("Enter Your Keyword : ")
    mycursor.execute(f"SELECT * FROM products WHERE id ='{Keyword}' OR name = '{Keyword}' OR price = '{Keyword}' ")
    myresult = mycursor.fetchall()
    if myresult != []:
        for x in myresult:
             print(x)  
    else:
        print("The desired product was NOT found")       
   

def show_list():
    mycursor.execute("SELECT * FROM products")

    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)

def buy():
        id=input("Enter id Product : ")   
        mycursor.execute(f"SELECT * FROM products WHERE id ='{id}' ")    
        myresult = mycursor.fetchone()    
        if myresult != None:
              myresult = [*myresult]  # ‌تبدیل تاپل به لیست
              count_buy = input("Enter the number of products you want to Buy : ")
              if myresult[3] >= int(count_buy) :
                  print("The number of purchases : ", int(count_buy),"price product : " , myresult[2], "Total price : " , myresult[2]*int(count_buy) )
                  myresult[3] -= int(count_buy)
                  sql = f"UPDATE products SET count = '{myresult[3]}' WHERE id = '{id}'"
                  mycursor.execute(sql)
                  mydb.commit()
              else:
                  print("We do not have stock of your selected product")   
        else:
            print("The desired product was not found")       
    

while True:
    show_menue()
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
      remove()
    elif choice==4:
        search()
    elif choice==5:
      show_list()
    elif choice==6:
        buy()
    else:
        print("Choose Correctly !!!")    





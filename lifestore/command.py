import mysql.connector
#TO CONNECT TO MY DATABASE
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "product"
)

mycursor = db.cursor()



#TO CREAT A DATABASE

# mycursor.execute("CREATE DATABASE product")




#TO CREATE A TABLE IN THE DATABASE

# mycursor.execute("CREATE TABLE Productdata (name VARCHAR(50), description VARCHAR(255), sku VARCHAR(100), price int UNSIGNED, image VARCHAR(255), itemID int PRIMARY KEY AUTO_INCREMENT)")




#TO QUERY OUT ALL THE TABLE

# mycursor.execute("DESCRIBE Productdata")

# for x in mycursor:
#    print(x)




#TO ADD VALUES TO THE TABLE

# sql = "INSERT INTO Productdata (name, description, sku, price, image) VALUES(%s,%s,%s,%s,%s)"
# val = [
#         ("Paracetamol", "Paracetamol (acetaminophen) is a pain reliever and a fever reducer", "8HE902", 300, "https://www.m-medix.com/2759-large_default/emzor-paracetamol-tablets.jpg"),
#         ("Prednisolone", "Prednisolone is a corticosteroid (cortisone-like medicine or steroid). It works on the immune system to help relieve swelling, redness, itching, and allergic reactions", "8HE809", 600, "https://5.imimg.com/data5/RU/SX/JJ/SELLER-109604861/prednisolone-tablet-500x500.jpg"),
#         ("Lumefantrine", "Lumefantrine is an antimalarial agent used to treat acute uncomplicated malaria.", "8HE809", 1200, "https://i1.wp.com/nimedhealth.com.ng/wp-content/uploads/2020/09/IMG_20200920_082326-1.jpg?fit=2487%2C1599&ssl=1"),
#         ("Coflin", "Coflin Is Used To Treat Coughs And Congestion Caused By The Common Cold, Bronchitis, And Other Breathing Illnesses.", "8HE809", 1200, "https://www.m-medix.com/2677-large_default/dr-meyers-coflin-expectorant-100ml.jpg")
# ]

# mycursor.executemany(sql,val)
# db.commit()





#TO BRING OUT ALL THE DATA FROM THE TABLE.

# mycursor.execute("SELECT * FROM Productdata")

# for x in mycursor:
#     print(x)
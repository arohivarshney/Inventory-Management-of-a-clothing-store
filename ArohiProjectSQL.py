
import mysql.connector


# Entering SQL info
host = 'localhost'
user = 'root'
password = 'Amit$1609'
database = 'myclothingdatabase'
continueloop = "Y"

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL database")
    if connection.is_connected():
        print("Connected to MySQL database: {database}")

        # Interacting with database
        #SQuery = "SELECT * FROM inventory"
        #   cursor = connection.cursor()
        
        while (continueloop =="Y" or continueloop =="y"):
            # Interacting with database
            SQuery = "SELECT * FROM inventory"
            cursor = connection.cursor()
            inputmenu = input("Please select from the Menu (S - Search the inventory, A - Add to cart, R - Remove from cart, C - Checkout, AI - Add to Inventory, RI - Remove from Inventory) ")       
            if (inputmenu == "S" or inputmenu == "s"):
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"            
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"            
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"            
                    
                # SELECT QUERY
                cursor.execute(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==0):
                    print("No match found for the given search")
                # Printing the result
                else:
                    from texttable import Texttable
                    t = Texttable()
                    t.add_row(["Product Code","Sub Product Code","Category","Brand","Color","Size","Quantity","Cart"])
                    for row in results:
                        t.add_row(row)
                    print(t.draw())
                   
            elif (inputmenu == "A" or inputmenu == "a"):
                SQuery = "SELECT * FROM inventory"
                UQuery = "UPDATE inventory SET cart = cart + 1, Quantity = Quantity - 1"
                cursor = connection.cursor()
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"
                    UQuery = UQuery + " WHERE Size='"+isize+"'"
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"
                    UQuery = UQuery + " AND Color='"+icolour+"'"
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"
                    UQuery = UQuery + " AND Brand='"+ibrand+"'"
                    
                # SELECT QUERY
                cursor.execute(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==1):
                    for row in results:
                        quantity = row[6]
                        cart = row[7]
                        if (quantity > cart):
                            cursor.execute(UQuery)
                            connection.commit()
                            print ("Item added to cart")
                            # Printing the result
                            cursor.execute(SQuery)
                            results = cursor.fetchall()
                            from texttable import Texttable
                            t = Texttable()
                            t.add_row(["Product Code","Sub Product Code","Category","Brand","Color","Size","Quantity","Cart"])
                            for row in results:
                                t.add_row(row)
                            print(t.draw())
                            
                        else:
                            print ("No available quantity to add to cart !!")
                else:
                    print("Multiple/No matches found. No action taken !!")

            elif (inputmenu == "R" or inputmenu == "r"):
                SQuery = "SELECT * FROM inventory"
                UQuery = "UPDATE inventory SET cart = cart - 1, Quantity = Quantity + 1"
                cursor = connection.cursor()
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"
                    UQuery = UQuery + " WHERE Size='"+isize+"'"
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"
                    UQuery = UQuery + " AND Color='"+icolour+"'"
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"
                    UQuery = UQuery + " AND Brand='"+ibrand+"'"
                    
                # SELECT QUERY
                cursor.execute(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==1):
                    print("Item removed from cart")
                    cursor.execute(UQuery)
                    connection.commit()
                    # Printing the result
                    cursor.execute(SQuery)
                    results = cursor.fetchall()
                    from texttable import Texttable
                    t = Texttable()
                    t.add_row(["Product Code","Sub Product Code","Category","Brand","Color","Size","Quantity","Cart"])
                    for row in results:
                        t.add_row(row)
                        print(t.draw())
                else:
                    print("Multiple/No matches found")

            elif (inputmenu == "C" or inputmenu == "c"):
                SQuery = "SELECT * FROM inventory"
                UQuery = "UPDATE inventory SET cart = cart - 1"
                cursor = connection.cursor()
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"
                    UQuery = UQuery + " WHERE Size='"+isize+"'"
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"
                    UQuery = UQuery + " AND Color='"+icolour+"'"
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"
                    UQuery = UQuery + " AND Brand='"+ibrand+"'"
                    
                # SELECT QUERY
                cursor.execute(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==1):
                    print("Item checked out. Thank you for shopping !!")
                    cursor.execute(UQuery)
                    connection.commit()
                else:
                    print("Multiple/No matches found")

            elif (inputmenu == "AI" or inputmenu == "ai"):
                SQuery = "SELECT * FROM inventory"
                
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                inputqty = input("Enter Quantity to be added: ")

                UQuery = "UPDATE inventory SET Quantity = Quantity + "+inputqty
                cursor = connection.cursor()
                
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"
                    UQuery = UQuery + " WHERE Size='"+isize+"'"
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"
                    UQuery = UQuery + " AND Color='"+icolour+"'"
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"
                    UQuery = UQuery + " AND Brand='"+ibrand+"'"
                    
                # SELECT QUERY
                cursor.execute(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==1):
                    for row in results:
                        cursor.execute(UQuery)
                        connection.commit()
                        print ("Quantity added")
                       
                else:
                    print("Multiple/No matches found. No action taken !!")

            elif (inputmenu == "RI" or inputmenu == "ri"):
                SQuery = "SELECT * FROM inventory"
                
                inputsize = input("Enter Size (S/M/L, providing size is mandatory): ")
                inputcolour = input("Enter Colour (Blue(B), Black (Bl), Grey (G), Pink (P), Purple (Pr), Beige (Be),Green(Gr) blank for no colour search): ")
                inputbrand = input("Enter Brand (Levis (L), H&M (H), Zara (Z), Mango(M), blank for no brand search): ")
                inputqty = input("Enter Quantity to be removed: ")

                UQuery = "UPDATE inventory SET Quantity = Quantity - "+inputqty
                cursor = connection.cursor()
                
                #size
                if (inputsize =="S" or inputsize =="s"):
                    isize = "Small"
                elif (inputsize=="M" or inputsize =="m"):
                    isize="Medium"
                elif (inputsize=="L" or inputsize =="l"):
                    isize="Large"
                elif (inputsize==""):
                    isize=""
            
                #colour
                if (inputcolour=="B" or inputcolour=="b"):
                    icolour="Blue"
                elif (inputcolour=="Bl" or inputcolour=="b1"):
                    icolour="Black"
                elif (inputcolour=="G" or inputcolour=="g"):
                    icolour="Grey"
                elif (inputcolour=="P" or inputcolour=="p"):
                    icolour="Pink"
                elif (inputcolour=="Pr" or inputcolour=="pr"):
                    icolour="Purple"
                elif (inputcolour=="Be" or inputcolour=="be"):
                    icolour="Beige"
                elif (inputcolour=="Gr" or inputcolour=="gr"):
                    icolour="Green"
                elif inputcolour=="":
                    icolour=""

                # Brand
                if (inputbrand=="L" or inputbrand=="l"):
                    ibrand="Levis"
                elif (inputbrand=="H" or inputbrand=="h"):
                    ibrand="H&M"
                elif (inputbrand=="Z" or inputbrand=="z"):
                    ibrand="Zara"
                elif (inputbrand=="M" or inputbrand=="m"):
                    ibrand=="Mango"
                elif inputbrand=="":
                    ibrand=""
                
                if (isize!=""):
                    SQuery = SQuery + " WHERE Size='"+isize+"'"
                    UQuery = UQuery + " WHERE Size='"+isize+"'"
                if (icolour!=""):
                    SQuery = SQuery + " AND Color='"+icolour+"'"
                    UQuery = UQuery + " AND Color='"+icolour+"'"
                if (ibrand!=""):
                    SQuery = SQuery + " AND Brand='"+ibrand+"'"
                    UQuery = UQuery + " AND Brand='"+ibrand+"'"
                    
                # SELECT QUERY
                cursor.execute(SQuery)
                print(SQuery)

                # Fetching all the rows
                results = cursor.fetchall()
                if (len(results)==1):
                    for row in results:
                        cursor.execute(UQuery)
                        connection.commit()
                        print ("Quantity removed")
                       
                else:
                    print("Multiple/No matches found. No action taken !!")                
            continueloop = input("Do you want to continue (Y/N): ")
        print("Thank you for using Inventory Management. Good Bye !!")
       
except mysql.connector.Error as err:
    print(f"Error: {err}")


finally:
    # Closing the connection in the end
    if 'connection' in locals() and connection.is_connected():
        connection.close()

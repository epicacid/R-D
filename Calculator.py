import sys
 
if len(sys.argv) < 2:
    sys.exit("Error: no arguments")
    
method = sys.argv[1]
 
while (True):
    var1 = raw_input("Enter value 1 ")
    var2 = raw_input("Enter value 2 ")

    try:
        var2 = int(var2)
        var1 = int(var1)
        
        print ("Your result is: ")
        if method == "Add" or method == "add":
            print (var1 + var2)
        elif method == "Mul" or method == "mul":
            print (var1 * var2)
        else:
            continue
        print ("Want to make another calculation?")
        
        var3 = raw_input()
        
        if var3 == "N" or var3 == "n":
            break
    except ValueError:
        print("You entere a string or a float try again")
    print "user_input " , var1, " and" , var2
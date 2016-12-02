choice = 0
while choice >= 0:
    print "[======================]"
    print "1. Returning Customer"
    print "2. New Customer"
    print "3. Guest"
    print "[======================]\n"

    choice = int(raw_input("Please select your choice: "))
    try:
        if choice < 1 or choice > 3:
            choice = int(raw_input("Please select your choice. \n Enter a number between 1 and 3: "))
        elif choice == 1:
            print "Returning Customer"
            choice = -1
        elif choice == 2:
            print "New Customer"
            choice = -1
        elif choice == 3:
            print "Guest"
            choice = -1
        else:
            print "\n\nplease enter a number\n"
    except ValueError:
        print "please enter a number"

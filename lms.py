import librec
while True:
    print("""###### LIBRARY RECORD ######\n\n""")
    print(""" 1. New Member """)
    print(""" 2. Books Available """)
    print(""" 3. Book Lended """)
    print(""" 4. Book Returned """)
    print(""" 5. Late Fine """)
    print(""" ###### END ######\n\n""")
    x=input("Choose Your Option:")
    if x=="1":
        print("###### Enter Member Details ######")
        librec.take_data()
        print("###### END ######\n")
    elif x=="2":
        print("###### Available Books ######")
        librec.book_avl()
        print("###### END ######\n")
    elif x=="3":
        print("###### Book Lended ######")
        librec.book_lend()
        print("###### END ######\n")
    elif x=="4":
        print("###### Book Returned ######")
        librec.book_return()
        print("###### END ######\n")
    elif x=="5":
        print("###### Late Fine ######")
        print("Maximum number of days one can keep a book is 20,if number od days exceed 20 then a fine of Rs2/day have to be paid")
        librec.fine()
        print("###### END ######\n")
    else:
        print("Please Enter A Valid Choice:")

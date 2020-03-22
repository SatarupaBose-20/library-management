member_details=[]
books=["C","Java","Python","MATLAB","Logo","Basic","HTML","Bootstrap","SQL","JavaScript"]
bookdata={}
def take_data():
    global bookdata
    global books
    file1=open("library.txt","a")
    x=input("Enter Student's name:")
    y=input("Enter Student's Year:")
    z=input("Enter Student's Contact Number:")
    d=input("Enter Student's Department:")
    print("\t Name:"+x)
    print("\t Year:"+y,"\t Contact:"+z)
    print("\t Department:"+d)
    l=len(z)
    if l==10 and int(y)<=5:
        print("\t New Member Successfully Registered!")
        member_details=[x,y,z,d]
        book_taken=books.pop(0)
        bookdata={book_taken:member_details}
        print(bookdata)
        file1.write("-> Book name:\n\t "+str(book_taken)+"\nDetails about book borrower:\n\t "+x+"\n\t "+y+"\n\t "+z+"\n\t "+d+"\n")
        file1.close()
    else:
        print("Something Went Wrong!")
def book_avl():
    global bookdata
    for q in range(len(books)):
         print(books[q])
    b=input("Enter the book name:")
    try:
        if b in books:
                        print(f'{b} Book is available')
        else:
            print(f'{b} Book is Not Available')
    except:
        print("Sorry! Book mentioned is not in Stock")
def book_lend():
    global bookdata
    try:
        c=eval(input("Enter Book name:"))
        print(bookdata[c])
    except:
        print("This Book is not lended to anyone!")
def book_return():
    global bookdata
    try:
        a=eval(input("Enter Book Name:"))
        g=bookdata.pop(a)
        print("Book is Returned and its details are:",g)
        h=books.append(a)
        print(h)
    except:
        print("No returning pending!")
def fine():
    p=20
    k=input("Enter the number of days the book was kept by borrower:")
    if int(k)>p:
        print("Has to give fine of Rs 2 per day")
    else:
        print("No Fine Needed")
    

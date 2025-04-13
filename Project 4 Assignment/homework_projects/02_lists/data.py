def add_three_copies(myist,data):
    for i in range(3):
        myist.append(data)

def main():
    message=input("Enter a message to copy:")
    mylist=[]
    print(f"List Before {mylist}")
    add_three_copies(mylist,message)
    print(f"After Before {mylist}")

if __name__=="__main__":  
 main()  


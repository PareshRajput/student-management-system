# add data
# :name,city,percentage,coursename
# update data
# delete data
# display the data
# filter the data
# search the data

db1={101:{"name":"paresh","city":"pune","per":89,"coursename":"pyhton"}}

print("-"*100)
print("Student Management System".center(110))
print("-"*100)
while True:
    print("""
                Dashboard 
            1.Add Student Info
            2.Display Student Details
            3.Update the details
            4. Delete the record
            5.Filter the record
        """)

    ch=int(input("Enter The Your choice :"))
    if ch==1:
        reg=eval(input("Enter The Registration Number :"))
        name=str(input("Enter The Name :"))
        city=str(input("Enter the city :"))
        per=eval(input("Enter The per :"))
        coursename=str(input("Enter the course name :"))
        db1[reg]={"name":name,"city":city,"per":per,"coursename":coursename}
        print("Added Succesfuuly")
    elif ch==2:
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Registraion_No","Name","City","Per","CourseName"))
        print("-"*105)
        for i in db1:
             print("-"*105)
             print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"],db1[i]["coursename"]))
             print("-"*105)
            # db1[key]=val
            # print(db1)
    elif ch==3:
        reg=eval(input("Enter regno :"))
        print("""
                    Update the record
            1.Update the name
            2.Update the city
            3.Update the per
            4.Update the CourseName
        
        """)
        upch=int(input("Enter The Your choice for update:"))
        if upch==1:
            uname=str(input("Enter The Name :"))
            db1[reg]["name"]=uname
            print("update succesfuuly ..")
        elif upch==2:
            ucity=str(input("Enter The city :"))
            db1[reg]["city"]=ucity
            print("update succesfuuly ..")
        elif upch==3:
            uper=str(input("Enter The per :"))
            db1[reg]["per"]=uper
            print("update succesfuuly ..")
        elif upch==4:
            co=str(input("Enter The coursename :"))
            db1[reg]["coursename"]=co
            print("update succesfuuly ..")
        else:
            print("Invalid Input")

    elif ch==4:
        reg=eval(input("Enter The delete record"))
        db1.pop(reg)
        print("Deleted Succefully")
    elif ch==5:
        print("""
              1.name
              2.city
              3.course
              """)
        ch=int(input("Enter the your choice"))
        if ch==1:
            name=(input("Enter the name :"))
            print("-"*105)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Registraion_No","Name","City","Per","CourseName"))
            print("-"*105)
            for i in db1:
                if db1[i]["name"]==name:
                    print("-"*105)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"],db1[i]["coursename"]))
                    print("-"*105)
            
        elif ch==2:
            city=(input("Enter the city :"))
            print("-"*105)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Registraion_No","Name","City","Per","CourseName"))
            print("-"*105)
            for i in db1:
                if db1[i]["city"]==city:
                    print("-"*105)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"],db1[i]["coursename"]))
                    print("-"*105)
           
        elif ch==3:
            coursename=(input("Enter the coursename :"))
            print("-"*105)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Registraion_No","Name","City","Per","CourseName"))
            print("-"*105)
            for i in db1:
                if db1[i]["coursename"]==coursename:
                    print("-"*105)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"],db1[i]["coursename"]))
                    print("-"*105)
        else:
            print("Invalid the ")
    else:
        print("You Enter wrong Number")
        
        
        
        
        
# 2 full table    
        
        
        
        
       
        # update=eval(input("Enter the update value"))
        # name=str(input("Enter The Name :"))
        # city=str(input("Enter the city :"))
        # per=eval(input("Enter The per :"))
        # coursename=str(input("Enter the course name :"))
        # db1[update]={"name":name,"city":city,"per":per,"coursename":coursename}
        # print(db1)
        
        
        
# Interviwe question
# create projetc
# > Employee M S
# > ATM 
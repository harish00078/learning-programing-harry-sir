sub1 = int(input("enter first subject marks\n"))
sub2 = int(input("enter second subject marks\n"))
sub3 = int(input("enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print('you are fail beacuse you have less than 33% in one of the subject')
    
    
elif(sub1+sub2+sub3)/3<40:
    print("you are fail due to total percentage less than 40")
else:
    print("congratualtion! you pass the exam")

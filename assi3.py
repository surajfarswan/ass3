#ques1
list0=[1,2,3]
print(list0)
#ques2
list7=[]
list1=['google','apple','facebook','microsoft','tesla']
list7=list1+list0
print(list7)
#ques3
list2=[1,2,3,4,5,1,1]
print(list2.count(1))
#ques4
list3=[2,5,4,7,6]
list3.sort()
print(list3)
#ques5
list6=[]
list4=[2,3,4,50]
list5=[8,9,10,30]
list6=list4+list5
list6.sort()
print(list6)
#ques6
stack=['adi','abhi','akash']
stack.pop()
print(stack)
queue=['adi','abhi','akash']
queue.remove('adi')
print(queue)
#ques optional
list7=[2,3,4,5,6,7,8,9]
even=0;
odd=0;
for i in list7:
    if(i%2==0):
        even=even+1;
    else:
        odd=odd+1;
print("no. of even",even)
print("no. of odd",odd)

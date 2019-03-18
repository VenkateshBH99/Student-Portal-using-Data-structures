
import os.path
from os import path
from Q2 import Queues

S=[None for i in range(10)]

class ListNode:
    def __init__(self,Roll=None,pas=None,next=None):
        self.roll=Roll
        self.password=pas
        self.next=next

class arrayNode:
    def __init__(self,r=None,marks=None,sub=None,next=None,pre=None):
        self.r=r
        self.marks=marks
        self.sub=sub
        self.next=next
        self.pre=pre



class array:
    def __init__(self):
        self.arr=[]

    def setarr(self,n):
        for i in self.arr:
            if i.sub==n:
                return
        self.arr.append(arrayNode(None,None,n,None,None))

    def arrinsert(self,r,m,s):
        for i in range(len(self.arr)):
            if self.arr[i].sub==s:
                if self.arr[i].next==None:
                    temp=arrayNode(r,m,s,None,self.arr[i])
                    self.arr[i].next=temp
                    return
                """l=self.arr[i].next
                while l.next!=None:
                    l=l.next
                temp=arrayNode(r,m,s,None,l)
                l.next=temp"""
                temp=arrayNode(r,m,s,self.arr[i].next,self.arr[i])
                self.arr[i].next=temp
                temp.next.pre=temp

    def insertSort(self,s):
        for i in range(len(self.arr)):
            if self.arr[i].sub==s:
                t=self.arr[i].next
                if t==None:
                    return False
                while t.next!=None:
                    key=int(t.next.marks)
                    rol=t.next.r
                    subject=t.next.sub
                    j=t
                    while j!=self.arr[i] and int(j.marks)<key:
                        j.next.marks=j.marks
                        j.next.r=j.r
                        j.next.sub=j.sub
                        j=j.pre
                    j.next.marks=key
                    j.next.r=rol
                    j.next.sub=subject
                    t=t.next
                """t=self.arr[i].next
                j=1
                while t!=None:
                    print(j,".",end=' ')
                    print('roll no-',t.r,', marks-',t.marks)
                    t=t.next
                    j=j+1"""

    def prin(self,s):
        for i in range(len(self.arr)):
            if self.arr[i].sub==s:
                t=self.arr[i].next
                if t==None:
                    return False
                j=1
                while t!=None:
                    print(j,".",end=' ')
                    print('roll no-',t.r,', marks-',t.marks)
                    t=t.next
                    j=j+1

    def checkMar(self,s):
        for i in range(len(self.arr)):
            if self.arr[i].sub==s:
                t=self.arr[i].next
                if t==None:
                    return False
                else:
                    return True

def ascii(val):
    l=len(val)
    i=0
    sum=0
    while i!=l:
        sum=sum+ord(val[i])
        i=i+1
    return sum

def insert(x,p):
    k=ascii(x)%len(S)
    n=x+".txt"
    na="StdList/"+n
    pas=p+'\n'
    roll=x+'\n'
    f=open(na,"w+")
    path="Student/Student.lst"
    std=open(path,"a+")
    name=input("Enter name of the Student: ")
    name=name+'\n'
    cgpa=input("Enter current CGPA of the student: ")
    cgpa=cgpa+'\n'
    f.write(pas+"Roll no-"+roll+"Name-"+name+"CGPA-"+cgpa)
    std.write(n+"\n")

    f.close()
    std.close()
    t=x
    Q=Queues()
    fac=check(Q)
    fl=len(fac)

    if fl!=0:
        i=0
        while i<fl:
            f1=fac[i]

            a=t+f1+".atd"
            f2="Attd/"+a
            f=open(f2,"w+")
            f.close()
            i=i+1

    if S[k]==None:
        S[k]=ListNode()
        t=ListNode(x,p,S[k].next)
        S[k].next=t
        return

    l=S[k].next
    while l.next!=None:
        l=l.next

    t=ListNode(x,p,l.next)
    l.next=t
    return

def search(x,p):
    k=ascii(x)%len(S)
    if S[k]==None:
        return None
    l=S[k].next
    while l!=None:
       if l.roll==x:
           if l.password==p:
               return l
           else:
               return False
       l=l.next
    return None

def Sear(x):
    k=ascii(x)%len(S)
    if S[k]==None:
        return False
    l=S[k].next
    while l!=None:
       if l.roll==x:
           return True

       l=l.next
    return False

def display(x):
    n="StdList/"+x+".txt"
    f=open(n,"r")
    ld=f.readlines()
    for i in ld:
        print(i)
    f.close()

def addData(A,s):
    sub="Marks/"+s+"marks.txt"
    fh=open(sub,"w+")
    i=0
    t=True
    while i!=len(S):
        if S[i]!=None:
            t=False
            l=S[i].next
            while l!=None:
                n="StdList/"+l.roll+".txt"
                f=open(n,"a+")
                print('Enter the marks for roll no-',l.roll,' :',end='')
                marks=input()
                A.arrinsert(l.roll,marks,s)
                marks=marks+'\n'
                fh.write(l.roll+" "+marks)
                f.write(s+" marks= "+marks)
                f.close()
                l=l.next

        i=i+1
    if t:
        return print('Please add Students then add marks')
    fh.close()
    A.insertSort(s)
    return

def viewall():
    i=0
    while i!=len(S):
        if S[i]!=None:
            l=S[i].next
            while l!=None:
                display(l.roll)
                print('----------------')
                l=l.next

        i=i+1
    return


def Attend(sub):
    Q=Queues()
    stud=StudBST()
    path="Student/Student.lst"
    std=open(path,"r+")
    s=std.readlines()
    l=len(s)
    i=0
    stud.Studinsert(200)
    while i<l:
        c=s[i]
        a=int(c[4]+c[5]+c[6])
        stud.Studinsert(a)
        i=i+1

    while True:
        ch=int(input("---BATCHS AVAILABLE----\n  1.For Batch:1\n  2.For Batch:2\n  3.Exit\nEnter Choice:"))
        if ch==1:
            r=input("Enter Absenties roll no.(s)[last 2 digits only] : ")
            r=r.split()
            l=len(r)
            i=0
            if l is not 0:
                while i<l:
                    b="1"+r[i]
                    b=int(b)
                    Q.enqueue(b)
                    i=i+1

        elif ch==2:
            r=input("Enter Absenties roll no.(s)[last 2 digits only] : ")
            r=r.split()
            l=len(r)
            i=0
            if l is not 0:
                while i<l:
                    b="2"+r[i]
                    b=int(b)
                    Q.enqueue(b)
                    i=i+1

        elif ch==3:
            break

        else:
            print("Invalid Choce")

    ch=input("For Any changes [press y]/ For NO[press any key]:")
    if ch=="y" or ch=="Y":
        i=input("Enter roll no.(s) with batch number[Last 3 digits]:")
        i=i.split()
        l=len(i)
        j=0
        while j<l:

            a=int(i[j])
            Q.Remove(a)

            j=j+1

    StudAtt(stud.root,Q,sub)



def StudAtt(parent,Q,sub):
    if parent:
        StudAtt(parent.left,Q,sub)
        f="17IT"+str(parent.roll)+sub+".atd"
        f="Attd/"+f
        file=open(f,"a+")
        if parent.roll==Q.Front() and Q.isEmpty()!=True:
            file.write("0"+"\n")
            Q.dequeue()


        else:
            file.write("1"+"\n")
        file.close()
        StudAtt(parent.right,Q,sub)



def attendStatus(code,sub):
    f="17IT"+code+sub+".atd"
    f="Attd/"+f
    file=open(f,"r+")
    r=file.readlines()
    l=len(r)

    if l==0:
        print("Attendance not taken")
        return None
    i=0
    sum=0
    while i!=l:
        R=int(r[i].strip())
        sum=sum+R
        i=i+1
    perc=sum/l
    perc=perc*100
    return perc


class StudNode:
    def __init__(self,r=None,left=None,right=None):
        self.roll=r
        self.left=left
        self.right=right


class StudBST:
    def __init__(self):
        self.root=None


    def Studinsert(self,x):
        if self.root==None:
            self.root=StudNode(x,None,None)
            return
        current=self.root
        while True:
            if x<=current.roll:
                if current.left:
                    current=current.left
                else:
                    current.left=StudNode(x,None,None)
                    return

            else:
                if current.right:
                    current=current.right
                else:
                    current.right=StudNode(x,None,None)
                    return

def check(L):
    temp=[]
    pat='Faculty/Faculty.lst'
    f=open(pat,"r+")
    fac=f.readlines()
    g=len(fac)
    i=0
    while i<g:
        k=fac[i]
        a=k.strip()
        L.enqueue(a)

        temp.append(a)
        i=i+1
    f.close()
    return temp

class Pascode:
    def __init__(self,fac=None,admin=None):
        self.fac=fac
        self.admin=admin


def main():

    L=Queues()
    A=array()
    P1=Pascode()
    pat='Faculty/Password'
    if os.path.exists(pat):
        f=open(pat,"r+")
        r=f.readlines()
        r0=r[0].strip()
        r1=r[1].strip()
        P1.admin=r0
        P1.fac=r1
        f.close()
    else:
        f=open(pat,"w+")
        P1.admin="admin"
        P1.fac="Fac"
        a1="admin"+"\n"
        f1="Fac"+"\n"
        f.write(a1+f1)
        f.close()



    admin_pass="admin"
    Facutlypass="f"
    print('WELCOME TO PORTAL')
    pat="Student/Student.lst"
    f=open(pat,"r+")
    file=f.readlines()
    le=len(file)
    i=0

    while i<le:
        st=file[i]
        stud=st[0]+st[1]+st[2]+st[3]+st[4]+st[5]+st[6]
        st=st.strip()
        st="StdList/"+st
        fite=open(st,"r+")
        fite0=fite.readlines()
        p=fite0[0]
        p=p.strip()
        k=ascii(stud)%len(S)
        if S[k]==None:
            S[k]=ListNode()
            t=ListNode(stud,p,S[k].next)
            S[k].next=t
        else:
            N=S[k].next
            while N.next!=None:
                N=N.next
            t=ListNode(stud,p,N.next)
            N.next=t
        i=i+1

    pat='Faculty/Faculty.lst'
    f=open(pat,"r+")
    fac=f.readlines()
    g=len(fac)
    i=0
    while i<g:
        k=fac[i]
        a=k.strip()
        A.setarr(a)
        L.enqueue(a)
        bi="Marks/"+a+"marks.txt"

        if path.exists(bi):
            fr=open(bi,"r+")
            mar=fr.readlines()
            j=0
            while j<len(mar):
                ma=mar[j].strip()
                ro=ma[0]+ma[1]+ma[2]+ma[3]+ma[4]+ma[5]+ma[6]
                if len(ma)==11:
                    m1=ma[8]+ma[9]+ma[10]
                elif len(ma)==10:
                    m1=ma[8]+ma[9]
                elif len(ma)==8:
                    m1=ma[8]
                elif len(ma)==7:
                    m1=0
                A.arrinsert(ro,int(m1),a)
                A.insertSort(a)
                j=j+1
            fr.close()

        i=i+1
    f.close()
    L.pr()


    while True:
        print('---------------------------------')
        ch=int(input("****MENU****\n1.Add New Students\n2.Add New Faculty Subject code\n3.Faculty login\n4.Student Login\n5.Admin View\n6.feedback form\n7.View marks list of each subject according to Rank\n8.Exit\nEnter your choice:"))
        if ch==1:
            ad=input("Enter admin password:")
            if ad==P1.admin:
                n=int(input('Enter the number of students to be added:'))
                for i in range(n):
                    val=input("Enter roll no:")
                    pa=input("Create Password:")
                    insert(val,pa)
                    print('---------------------')

            else:
                print('Worng password!!')
        elif ch==2:
            ad=input("Enter admin password:")
            if ad==P1.admin:
                n=int(input("Enter the number of subjects to be added:"))
                #A.setarr(n)
                for i in range(n):
                    print(i+1,end=' ')
                    pat='Faculty/Faculty.lst'
                    pa="Student/Student.lst"
                    pa1=open(pa,"r+")
                    std=pa1.readlines()
                    l=len(std)
                    fi=open(pat,"a+")
                    val=input("Enter subject code:")
                    v="Sub/"+val
                    t=val+"\n"
                    fi.write(t)
                    if l is not 0:
                        i=0
                        while i<l:
                            s=std[i]
                            s=s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]

                            D="Attd/"+s+val+".atd"
                            fi1=open(D,"w+")
                            fi1.close()
                            i=i+1
                    fi.close()
                    A.setarr(val)
                    f=open(v,"w+")
                    f.close()
            else:
                print('Worng password!!')

        elif ch==3:
            fp=input("Enter Faculty password:")
            if fp==P1.fac:
                temp=check(L)
                if L.isEmpty():
                    print('Please Add Faculty Subject code')
                    continue

                print('Available subject code:')
                L.print()
                s=input("Enter your subject code:")
                if s in temp:
                    c=int(input("   -----Available operations----\n  1.Add Final Marks for present Students\n  2.Take Attendance\n  3.Get Attendance Status of a student\n  4.view feedback\nEnter your option:"))
                    if c==1:
                        a=A.checkMar(s)
                        if a==False:
                            print('ADD MARKS FOR: ',s)
                            addData(A,s)
                        else:
                            print('Marks has been already added for this subject!!!')
                    elif c==4:
                        s="Sub/"+s
                        f=open(s,"r")
                        h=f.readlines()
                        if h==[]:
                            print('---there is no feedback entered by students---')
                            continue
                        for i in h:
                            print(i)
                        f.close()
                    elif c==2:
                        Attend(s)
                    elif c==3:
                        t=input("Enter student roll no with batch number [last 3 digits]: ")
                        B="17IT"+t
                        if Sear(B):
                            if attendStatus(t,s)!=None:
                                print("Attendance Status is ",attendStatus(t,s))
                        else:
                            print("Invalid Roll number")
                    else:
                        print('Invalid option')
                else:
                    print('Entered Subject code not available!!')
            else:
                print('Wrong password!!')


        elif ch==4:
            val=input("Enter your ROLL NO:")
            pa=input("Enter password:")
            E=search(val,pa)
            if E!=None and E!=False:
                c=int(input("  ----Available operations----\n  1.View information\n  2.Check attendence status\n  3.Change password\nEnter your option:"))

                if c==1:
                    display(E.roll)
                elif c==2:
                    print("---Available Subject Codes---")
                    check(L)
                    L.print()
                    Course=input("Enter subject Code:")
                    t=val[4]+val[5]+val[6]
                    if attendStatus(t,Course)!=None:
                        print("Attendance Status is ",attendStatus(t,Course))
                elif c==3:
                    new=input("Enter New password:")
                    E.password=new
                    val=val+".txt"
                    val1="StdList/"+val
                    pat=open(val1,"r+")
                    line=pat.readlines()
                    pat.truncate(0)
                    pat.close()
                    new=new+"\n"
                    line[0]=new
                    pat=open(val1,"a+")
                    for i in line:
                        pat.write(i)
                    pat.close()


                else:
                    print("Invalid option")
            elif E==None:
                print('There is no student with this roll no')
            elif E==False:
                print('Wrong password!!!')

        elif ch==5:
            p=input('Enter the admin password:')
            if p==P1.admin:
                cho=int(input(" ----Available operations----\n  1.View all Students details\n  2.View specific student details\n  3.Change admin password\n  4.Change Faculty password\nEnter your choice:"))
                if cho==1:
                    viewall()
                elif cho==2:
                    rol=input("Enter Roll No:")
                    if Sear(rol):
                        display(rol)
                    else:
                        print('Invaild roll no!!!')
                elif cho==3:
                    Anew=input("Enter New admin password:")
                    P1.admin=Anew
                    pat="Faculty/Password"
                    f=open(pat,"r+")
                    line=f.readlines()
                    f.truncate(0)
                    f.close()
                    Anew=Anew+"\n"
                    line[0]=Anew
                    f=open(pat,"a+")
                    for i in line:
                        f.write(i)
                    f.close()
                elif cho==4:
                    Fnew=input("Enter New Faculty password:")
                    P1.fac=Fnew
                    pat="Faculty/Password"
                    f=open(pat,"r+")
                    line=f.readlines()
                    f.truncate(0)
                    f.close()
                    Fnew=Fnew+"\n"
                    line[1]=Fnew
                    f=open(pat,"a+")
                    for i in line:
                        f.write(i)
                    f.close()

                else:
                    print('Invalid choice:')

            else:
                print('Wrong password!!!')


        elif ch==6:

            roll=input("Enter your Roll No:")
            pa=input("Enter password:")
            E=search(roll,pa)
            if E!=None and E!=False:
                te=check(L)
                if L.isEmpty():
                    print('There are no subject code to enter feedback form!!')
                    continue
                print("--Available subject code---")
                L.print()
                print('feedback form:')
                c=int(input(" ----Available operation----\n  1.Enter for all\n  2.Enter for specific subject\nEnter your choice:"))
                if c==1:
                    length=len(te)
                    t=0
                    #print(te[t])
                    while t<length:
                        subj="Sub/"+te[t]
                        f=open(subj,"a+")
                        print('feedback for ',te[t],' Faculty in one line:')
                        feed=input()
                        feed=feed+"\n"
                        f.write(feed)
                        f.close()
                        t=t+1
                elif c==2:
                    en=input("Enter Subject code:")
                    if en in te:
                        subj="Sub/"+en
                        f=open(subj,"a+")
                        print('feedback for ',en,' Faculty in one line:')
                        feed=input()
                        feed=feed+"\n"
                        f.write(feed)
                        f.close()
                    else:
                        print('Entered Subject code not available!!!')

            elif E==None:
                print('There is no student with this roll no')
            elif E==False:
                print('Wrong password!!!')


        elif ch==7:
            fact=check(L)
            if L.isEmpty():
                print('Please add faculty and marks!!')
                continue
            print('Available subject code:')
            L.print()
            s=input("Enter the subject code:")
            sub=s
            if s in fact:
                a=A.prin(sub)
                if a==False:
                    print('Marks did not added for this subject!!')
            else:
                print('Entered subject code not available ')
        elif ch==8:
             break
        else:
            print('Invalid choice')



if __name__ == '__main__':

    main()


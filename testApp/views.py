from datetime import datetime
from pyexpat import model
from django.shortcuts import render,redirect
from .models import SaveBookData,MycustomUser,Bookissue
from django.http import HttpResponseRedirect
from testApp.forms import modelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
# Create your views here.
#python manage.py migrate --run-syncdb 
def index_view(request):
    if request.method == 'POST':
        subject = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        send_mail(
        subject,
        message,
        'chouhanyuvrajsingh83@gmail.com',
        [email],
        fail_silently=False,)
        messages.success(request, 'Massege Send Successfully')
        return redirect('/alldata')
    else:
        messages.error(request, 'Massege Not Send ')   
        return render(request, 'mainfolder/base.html')

def index_view1(request):
    return render(request, 'mainfolder/base1.html')

def showbook_view(request):
    book_list = SaveBookData.objects.all()
    return render(request,'mainfolder/showbooks.html',{'book_list':book_list})
# def showbook_view(request):
#     return render(request, 'mainfolder/showbooks.html')=['id','bookname','auther_name','total_book','date_time']

def AddBook_view(request):
    if request.method == 'POST':
        bookname= request.POST.get('BookName')
        auther_name= request.POST.get('auther_name')
        total_book= request.POST.get('total_books')
        print("hiiiiiiiiiiiiiiiiiiiii  ",total_book)
        obj = SaveBookData.objects.filter(bookname=bookname)
        if obj.exists():
            obj1 = SaveBookData.objects.get(bookname=bookname)
            total = obj1.total_book+int(total_book)
            obj1.total_book = total
            print(total)
            obj1.save()
        else:
            data=SaveBookData(bookname=bookname,auther_name=auther_name,total_book=total_book )
            data.save()
            return HttpResponseRedirect('/showbooks')
    return render(request, 'mainfolder/addbooks.html')  
    # return render(request, 'mainfolder/addbooks.html')  

def delete_view(request,id):
    data=SaveBookData.objects.get(pk=id)
    tb = data.total_book
    tb1 =  tb-1
    if tb1==0:
        data.delete()
    else:
        data.total_book = tb1
        data.save()
    return HttpResponseRedirect('/showbooks')



def signup_view(request):
    form=modelForm()
    print()
    if request.method == 'POST':  
        name = request.POST['studentname']
        email = request.POST['email']
        Date = datetime.now()
        message = 'Hello {} your library account is open on {} date Thanks for being a part of us And Now you can parchese any 3 books from this library '.format(name,Date)
        form=modelForm(request.POST) 
        if form.is_valid():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            form=modelForm(request.POST) 
            user=form.save()
            user.set_password(user.password)
            user.save()
            send_mail('LibraryAccount', message, 'chouhanyuvrajsingh83@gmail.com', [email], fail_silently=False,)
            return redirect('/alldata')
    return render(request, 'mainfolder/signup1.html',{"form":form})



def showStudent_view(request):
    book_list = MycustomUser.objects.exclude(email = 'yuvraj@gmail.com')
    if request.method == 'GET':
        st = request.GET.get("q")
        if st==None:
            pass
        print("record",st)
        if st!=None:               
            book_list = MycustomUser.objects.filter(Q(studentname__icontains =st) | Q(email__icontains= st) | Q(classname__icontains= st) | Q(branch__icontains= st) | Q(mobile_no__icontains= st) | Q(address__icontains= st)).exclude(studentname='yuvraj')
            print("back data",book_list)
        
    return render(request,'mainfolder/Allstudent.html',{'book_list':book_list})


# def Search_Student_view(request):
#     if "q" in request.GET:
#         mysearch = request.GET["q"]
#         book_list = MycustomUser.objects.filter(studentname = mysearch)
#     else:
#         book_list = MycustomUser.objects.exclude(email = 'yuvraj@gmail.com')
#     return render(request,'mainfolder/Allstudent.html',{'book_list':book_list}) 


def delete_view1(request,id):
    data=MycustomUser.objects.get(pk=id)
    data1 = data.email
    name = data.studentname
    date = datetime.now()
    message = 'Hello {} your library account is closed on {} date Thanks for being a part of us '.format(name,date)
    data2 = Bookissue.objects.filter(email=data1)
    print(data2)
    data2.delete()
    data.delete()
    send_mail('LibraryAccount', message, 'chouhanyuvrajsingh83@gmail.com', [data1], fail_silently=False,)
    return HttpResponseRedirect('/alldata')



def Book_issue_view(request): 
    if request.method == 'POST':
        email= request.POST.get('email')
        bookname= request.POST.get('bookname')
        auther_name= request.POST.get('auther_name')
        total_book= request.POST.get('total_books')
        date= request.POST.get('date')
        obj = MycustomUser.objects.filter(email=email)
        if obj.exists():
            obj1 = Bookissue.objects.filter(email=email).count()
            name = MycustomUser.objects.get(email=email)
            myname = name.studentname
            message = 'Hello {} We are inform you that we assigned {} {} book on your library account on this {} date And we hope that you will use this book very effectively, and  You can keep the book for 15 days, after that you may have to pay fine at Rs 5 per day. but  You can again purchase book after 15 days again  '.format(myname,total_book,bookname,date)
            if obj1==3:
                messages.error(request, '3 Books Already Given To You ')
                return redirect('/issuebook')
            elif obj1!=3:
                obj4 = SaveBookData.objects.filter(bookname=bookname)
                if obj4.exists():
                    obj3 = SaveBookData.objects.get(bookname=bookname)
                    tb = obj3.total_book-int(total_book)
                    if tb>0:
                        obj3.total_book = tb
                        obj3.save()
                        data=Bookissue(email=email,bookname=bookname,auther_name=auther_name,total_book=total_book,date=date )
                        data.save()
                        send_mail('Book Issue', message, 'chouhanyuvrajsingh83@gmail.com', [email], fail_silently=False,)
                        return redirect('/alldata')
                    else:
                        messages.error(request, 'Minimum Books Are Available')
                        return redirect('/issuebook')  
                else:
                    messages.error(request, 'Books Are Not Available in Library ')
                    return redirect('/issuebook')             
        else:
            messages.error(request, 'This Email is not exists ')
            return redirect('/issuebook')
    return render(request,'mainfolder/assignbook.html')

# book_list
def showAloteBooks_view(request,id):
    data=MycustomUser.objects.get(pk=id)
    data1 = data.email
    print(data1)
    book_list = Bookissue.objects.filter(email=data1)
    print(book_list)
    return render(request,'mainfolder/bookalotedata.html', {'book_list':book_list})

def delete_view2(request,id):
    data=Bookissue.objects.get(pk=id)
    pemail = data.email
    print(data.id)
    tb = data.total_book
    tb1 =  tb-1
    bn = data.bookname
    print(bn)
    data1=SaveBookData.objects.get(bookname=bn)
    stb = data1.total_book+1
    data1.total_book = stb
    data1.save()
    if tb1==0:
        data.delete()
        return HttpResponseRedirect('/alldata')
    else:
        data.total_book = tb1
        data.save()
    pdata=MycustomUser.objects.get(email=pemail)
    preid = pdata.id
    return HttpResponseRedirect('/showissuebook/{}'.format(preid))
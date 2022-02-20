from django import forms
from testApp.models import MycustomUser,Bookissue
from django.forms import   TextInput, EmailInput


# class BookForm(forms.ModelForm):
#     class Meta:
#         model=Bookissue
#         fields = ['email','bookname','auther_name','total_book','date']
#         widgets = {
#             'email': EmailInput(attrs={
#                 'class': "form-control",
#                 'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
#                 'placeholder': 'Email'
#                 }),
#             'bookname': TextInput(attrs={
#                 'class': "form-control", 
#                 'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
#                 'placeholder': 'Book Name'
#                 }),
#             'auther_name': TextInput(attrs={
#                 'class': "form-control", 
#                 'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
#                 'placeholder': 'Auther Name'
#                 }),
#             'total_book': TextInput(attrs={
#                 'class': "form-control", 
#                 'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
#                 'placeholder': 'Total_book',
#                 'type': 'number'
#                 }),
#             'date': TextInput(attrs={
#                 'class': "form-control", 
#                 'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
#                 'placeholder': 'Date',
#                 'type': 'date'
#                 }),
#         }


class modelForm(forms.ModelForm):
    class Meta:
        model=MycustomUser
        fields = ['studentname','email','password','classname','branch','mobile_no','date_of_birth','address']
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Email'
                }),
            'password': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Password',
                'type':'password',
                'id': 'myInput'
                }),
            'studentname': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Student Name'
                }),
            'date_of_birth': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'date_of_birth',
                'type': 'date'
                }),
            'mobile_no': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Mobile Number',
                'type': 'tel',
                'maxlength': '10',
                'minlength': '10'

                }),
            'classname': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Class Name'
                }),
            'branch': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Branch '
                }),    
            'address': TextInput(attrs={
                'class': "form-control", 
                'style': 'width:100%; border-radius:10px; border: solid black 2px; float:left; margin-top:0px; height: 45px;',
                'placeholder': 'Address '
                }), 
        } 
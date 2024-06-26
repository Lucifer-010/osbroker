from django import forms
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ModelForm , TextInput,EmailInput , PasswordInput,NumberInput
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError
from .models import UserDetail,TransferFund,Report
from django.forms import TextInput, Select
from phonenumber_field.formfields import SplitPhoneNumberField

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',"placeholder":"name@example.com"}))
    #firstname= forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}))
    #lastname= forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last Name"}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    def clean_email(self):
        emails=self.cleaned_data["email"]
        if User.objects.filter(email=emails).exists():
            raise ValidationError("Email Already Exist. Try Again")
        return emails
    def __init__(self,*arg,**kwarg):
        super(RegisterUserForm,self).__init__(*arg,**kwarg)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter username'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='name@example.com'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password '
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        
        for fieldname in ['username']:
            self.fields[fieldname].help_text = ""
        for fieldname in ['password1']:
            self.fields[fieldname].help_text = ""

class PasswordForm(SetPasswordForm):
    class meta:
        model = get_user_model()
        fields = ['password1','password2']
    def __init__(self,*arg,**kwarg):
        super(PasswordForm,self).__init__(*arg,**kwarg)
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='New Passworld'
        self.fields['new_password2'].widget.attrs['placeholder']='Confirm Password'

#
class StaffForm(ModelForm):
    class Meta:
        model =    UserDetail
        fields = ("firstname","lastname","othername","birth","gender",
                  "contact","emergency_name","emergency_contact","nationality","address","license_image","pin","verify_pin",)
        #contact = PhoneNumberField(widget=PhoneNumberPrefixWidget(widgets=[Select,TextInput],attrs=None))
        contact = SplitPhoneNumberField()
        emergency_contact = SplitPhoneNumberField()
    def __init__(self,*arg,**kwarg):
        super(StaffForm,self).__init__(*arg,**kwarg)
        self.fields["firstname"].widget.attrs['placeholder']='Firstname'
        self.fields["firstname"].widget.attrs['class']='form-control'
        self.fields["lastname"].widget.attrs['placeholder']='Lastname'
        self.fields["lastname"].widget.attrs['class']='form-control'
        self.fields["othername"].widget.attrs['placeholder']='Othername'
        self.fields["othername"].widget.attrs['class']='form-control'
        self.fields['birth'].widget = forms.widgets.DateInput(attrs={"type":"date","min":"1910-01-01","placeholder":"yyyy-mm-dd (DOB)","class":"form-control butpad"})
        self.fields["gender"].widget.attrs['placeholder']='Gender'
        self.fields["gender"].widget.attrs['class']='form-control'
        #self.fields["contact"].widget.attrs['class']='menu form-control'
        #self.fields["contact"].widget.attrs['placeholder']='(555) 555-1234'
        
        #self.fields["emergency_contact"].widget.attrs['class']='menu form-control'
        #self.fields["emergency_contact"].widget.attrs['placeholder']='(555) 555-1234'
        self.fields["emergency_name"].widget.attrs['placeholder']='Emergency Name'
        self.fields["emergency_name"].widget.attrs['class']='form-control'
        
        self.fields["nationality"].widget.attrs['placeholder']='Nationality'
        self.fields["nationality"].widget.attrs['class']='form-control'
        self.fields["address"].widget.attrs['placeholder']='Address'
        self.fields["address"].widget.attrs['class']='form-control'
        #self.fields["license_image"].widget.attrs['label']='Driver License Upload'
        self.fields["license_image"].widget.attrs['class']='form-control input input-box custom-file-input'
        self.fields["pin"].widget = forms.widgets.PasswordInput(attrs={"type":"password","pattern":"[0-9]{4}","maxlength":4,"class":"form-control","data-bs-toggle":"password"})
        self.fields["verify_pin"].widget = forms.widgets.PasswordInput(attrs={"type":"password","pattern":"[0-9]{4}","maxlength":4,"class":"form-control","data-bs-toggle":"password"})
        
class TransferForm(ModelForm):
    class Meta:
        model =    TransferFund
        fields = ("account_name","bank_name","account_number","ammount","swift_code","description","pin",)
    def __init__(self,*arg,**kwarg):
        super(TransferForm,self).__init__(*arg,**kwarg)
        self.fields["account_name"].widget.attrs['placeholder']='Account Name'
        self.fields["account_name"].widget.attrs['class']='form-control'
        self.fields["bank_name"].widget.attrs['placeholder']='Select Bank'
        self.fields["bank_name"].widget.attrs['class']='form-control'
        self.fields["swift_code"].widget.attrs['placeholder']='Swift code/Routing number'
        self.fields["swift_code"].widget.attrs['class']='form-control'
        self.fields["account_number"].widget.attrs['placeholder']='Enter Account Number'
        self.fields["account_number"].widget.attrs['class']='form-control'
        self.fields["ammount"].widget.attrs['placeholder']='$0.0'
        self.fields["ammount"].widget.attrs['class']='form-control'
        self.fields["ammount"].widget.attrs['id']='myNumberInput'
        self.fields["description"].widget.attrs['placeholder']='Payment Description'
        self.fields["description"].widget.attrs['class']='form-control'
        self.fields["pin"].widget = forms.widgets.PasswordInput(attrs={"type":"password","pattern":"[0-9]{4}","maxlength":4,"id":"transfer_number","class":"form-control","data-bs-toggle":"password"})

class ReportForm(ModelForm):
    class Meta:
        model =    Report
        fields = ("title","subject","ref",)
    def __init__(self,*arg,**kwarg):
        super(ReportForm,self).__init__(*arg,**kwarg)
        self.fields["title"].widget.attrs['placeholder']='Title'
        self.fields["title"].widget.attrs['class']='form-control'
        self.fields["subject"].widget.attrs['placeholder']='Subject'
        self.fields["subject"].widget.attrs['class']='form-control'
        self.fields["ref"].widget.attrs['placeholder']='Ref'
        self.fields["ref"].widget.attrs['class']='form-control'


class editStaffForm(ModelForm):
    class Meta:
        model =    UserDetail
        fields = ("firstname","lastname","othername","birth","gender","email",
                  "contact","emergency_name","emergency_contact","nationality","address","license_image","pin","verify_pin",)
        contact = SplitPhoneNumberField()
        emergency_contact = SplitPhoneNumberField()
    def __init__(self,*arg,**kwarg):
        super(editStaffForm,self).__init__(*arg,**kwarg)
        
        self.fields["firstname"].widget.attrs['placeholder']='Firstname'
        self.fields["firstname"].widget.attrs['class']='form-control'
        self.fields["lastname"].widget.attrs['placeholder']='Lastname'
        self.fields["lastname"].widget.attrs['class']='form-control'
        self.fields["othername"].widget.attrs['placeholder']='Othername'
        self.fields["othername"].widget.attrs['class']='form-control'
        
        self.fields['birth'].widget = forms.widgets.DateInput(attrs={"type":"date","min":"1910-01-01","placeholder":"yyyy-mm-dd (DOB)","class":"form-control butpad"})
        self.fields["gender"].widget.attrs['placeholder']='Gender'
        self.fields["gender"].widget.attrs['class']='form-control'
        
        self.fields["email"].widget.attrs['placeholder']='Enter email'
        self.fields["email"].widget.attrs['class']='form-control'
        #self.fields["contact"].widget.attrs['class']='menu form-control'
        #self.fields["contact"].widget.attrs['placeholder']='(555) 555-1234'
        #self.fields["emergency_contact"].widget.attrs['class']='menu form-control'
        #self.fields["emergency_contact"].widget.attrs['placeholder']='(555) 555-1234'
        
        self.fields["emergency_name"].widget.attrs['placeholder']='Emergency Name'
        self.fields["emergency_name"].widget.attrs['class']='form-control'
        
        self.fields["nationality"].widget.attrs['placeholder']='Nationality'
        self.fields["nationality"].widget.attrs['class']='form-control'
        self.fields["address"].widget.attrs['placeholder']='Address'
        self.fields["address"].widget.attrs['class']='form-control'
        #self.fields["license_image"].widget.attrs['label']='Driver License Upload'
        self.fields["license_image"].widget.attrs['class']='form-control input input-box custom-file-input'
        self.fields["pin"].widget = forms.widgets.PasswordInput(attrs={"type":"password","pattern":"[0-9]{4}","maxlength":4,"class":"form-control","data-bs-toggle":"password"})
        self.fields["verify_pin"].widget = forms.widgets.PasswordInput(attrs={"type":"password","pattern":"[0-9]{4}","maxlength":4,"class":"form-control","data-bs-toggle":"password"})
        

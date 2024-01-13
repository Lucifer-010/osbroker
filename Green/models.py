from ast import mod
from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
import secrets
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta

import random
import string
from .email_otp import text,otptext
User    = settings.AUTH_USER_MODEL
password = 'ghcz jcpi zqbk olay'
sender_email = 'clovercooporative@gmail.com'

MARKET_TYPE =(
    ("CRYPTO","CRYPTO"),("STOCKS","STOCKS"),("CURRENCIES","CURRENCIES"),("INDICES","INDICES"),
)

def validate_age(value):
    min_age = 7
    today = date.today()
    min_birth_date = today - timedelta(days=(min_age * 365.25))  # Account for leap years

    if value > today:
        raise ValidationError(
            _('%(value)s is a future date. Please enter a date in the past.'),
            params={'value': value},
        )
    elif value > min_birth_date:
        raise ValidationError(
            _('%(value)s is less than %(min_age)d years ago. You must be at least %(min_age)d years old.'),
            params={'value': value, 'min_age': min_age},
        )

class WalletBalance(models.Model):
    trading_balance = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    bitcoin_mining = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    ethereum_mining = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    dogecoin_mining = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    binance_coin_mining = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    cosmos_mining = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    verified = models.BooleanField(default=False)
    user   = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.user}"
    
class CopyTrader(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    win_rate = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    profit_share = models.PositiveIntegerField(blank=False,null=False)
    asset_under_management = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    days = models.PositiveIntegerField(blank=False,null=False)
    profile_image = models.URLField(blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.name}"
    
class CopiedTrade(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    win_rate = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    profit_share = models.PositiveIntegerField(blank=False,null=False,default=40)
    profile_image = models.URLField(blank=False,null=False,default="https://ww.gffjd.com")
    date = models.DateTimeField(auto_now_add=True)
    user   = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.user}"

class Coin(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    value = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    mine_rate = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    image = models.URLField(blank=False,null=False,default="https://ww.gffjd.com")
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.name}"
    
class Market(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    symbol = models.CharField(max_length=200,null=False,blank=False)
    form = models.CharField(max_length=200,null=False,blank=False,choices=MARKET_TYPE)
    value = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=6)
    image = models.URLField(blank=False,null=False,default="https://ww.gffjd.com")
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.name}"

class WatchList(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    symbol = models.CharField(max_length=200,null=False,blank=False)
    form = models.CharField(max_length=200,null=False,blank=False,choices=MARKET_TYPE)
    image = models.URLField(blank=False,null=False,default="https://ww.gffjd.com")
    date = models.DateTimeField(auto_now_add=True)
    user   = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-date",)

    def __str__(self) -> str:
        return f"User: {self.name}"

CURRENCY=(
    ("USD","USD"),("EUR","EUR"),("CAD","CAD"),("AUD","AUD"),("GBP","GBP"),
    )  
class UserInfo(models.Model):
    firstname       = models.CharField(max_length=50 , blank=False)
    lastname       = models.CharField(max_length=50 , blank=False)
    birth = models.DateField(blank=False,null=False,validators=[validate_age])
    currency       = models.CharField(max_length=50 ,choices= CURRENCY, blank=False)
    email         = models.EmailField(blank=True,null=True ,default="test@gmail.com")
    contact       = PhoneNumberField(blank=False)
    nationality = CountryField(blank=False,null=False)
    address  = models.CharField(max_length=70, null=False,blank=False,help_text="describe your location")
    date_created = models.DateTimeField(auto_now_add=True)
    user          = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-date_created",)
    def __str__(self):
        return f"{self.user}"
    
class Otp(models.Model):
    time = models.TimeField(auto_now_add=True)
    otp = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    user   = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-time",)

    def __str__(self) -> str:
        return f"otp: {self.time}"
    def save(self , *args,**kwargs) -> None:
        while not self.otp :
            otp = random.randrange(10001,50005,2)
            object_with_similar_ref  = Otp.objects.filter(otp=otp)
            if not object_with_similar_ref:
                self.otp = otp
                receiver_email =f"{self.email}"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Account Activity"
                message["From"] = sender_email
                message["To"] = receiver_email
                try:
                    html = otptext.format(self.time,self.user,self.otp)
                    part1 = MIMEText(text, "plain")
                    part2 = MIMEText(html, "html")

                    message.attach(part1)
                    message.attach(part2)

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(
                            sender_email, receiver_email, message.as_string()
                        )
                    super(Otp, self).save(*args, **kwargs)
                except:
                    pass

DEPOSIT_TO =(
    ("TRADING BALANCE","TRADING BALANCE"),("BITCOIN MINIG","BITCOIN MINIG"),
    ("DOGECOIN MINING","DOGECOIN MINING"),("ETHEREUM MINING","ETHEREUM MINING"),
    ("BINANCE COIN MINING","BINANCE COIN MINING"),("COSMO (ATOM) MINING","COSMO (ATOM) MINING"),
)

def limit_value(value):
    val=int(value)
    if val >= 500:
        return value
    else:
        raise ValidationError("Deposit above 500(USD)")

PAYMETHOD =  (
    ("BITCOIN","BITCOIN"),("ETHEREUM","ETHEREUM"),
)  
class Deposit(models.Model):
    ammount = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2,validators=[MinValueValidator(500.00)])
    fund = models.CharField(max_length=100,blank=False,null=False,choices=DEPOSIT_TO,default=1) # type: ignore
    pay_in = models.CharField(max_length = 200,blank=False,null=False,choices=PAYMETHOD,default=1) # type: ignore
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user          = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-date_created",)
    def __str__(self):
        return f"{self.user}"

class Withdraw(models.Model):
    ammount = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2,validators=[MinValueValidator(500.00)])
    fromacc = models.CharField(max_length=100,blank=False,null=False,choices=DEPOSIT_TO,default=1) # type: ignore
    wallet = models.CharField(max_length = 200,blank=False,null=False,choices=PAYMETHOD,default=1) # type: ignore
    address = models.CharField(max_length=500,blank=False,null=False)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user          = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=("-date_created",)
    def __str__(self):
        return f"{self.user}"
    
STATES =   (
    ("OPEN TRADE","OPEN TRADE"),("CLOSED TRADE","CLOSED TRADE"),
)  

class OpenClosedTrade(models.Model):
    ammount = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    up = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    down = models.DecimalField(max_digits=999,blank=False,null=False,decimal_places=2)
    name = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    trade_type = models.CharField(max_length=500,blank=False,null=False,default=1,choices=STATES)
    pair = models.CharField(max_length=500,blank=False,null=False,default="BTCUSD")
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_created",)
    def __str__(self):
        return f"{self.name}"

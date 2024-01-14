import profile
import re
from urllib import request
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import random,datetime
from django.http import JsonResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .forms import DepositForm, RegisterUserForm,WithdrawForm,UserForm



# Create your views here.
from .models import WalletBalance,CopyTrader,CopiedTrade,Coin,Market,WatchList,Otp,Deposit,Withdraw,OpenClosedTrade,DepositCoin
import datetime,time,requests
import yfinance as yf

def log_out(request):
    logout(request)
    return redirect('login')

def loginuser(request):
    user = "ADMIN"
    if request.method=="POST":
        user_email=request.POST['email']
        password=request.POST['password']
        try:
            usernames = User.objects.get(email=user_email)
            user=authenticate(request,username=usernames.username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
                return redirect('login')
        except User.DoesNotExist:
            messages.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
            return redirect('login')
    else:
        return render(request,'login.html',{"user":user})   

def signup(request):
    if request.method == "POST":
        register = RegisterUserForm(request.POST)
        info = UserForm(request.POST)
        if register.is_valid() and info.is_valid():
            register.save()
            username = register.cleaned_data['username']
            password = register.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            edith = info.save(commit=False)
            edith.email = request.user.email
            edith.user = request.user
            edith.save()
            verification = Otp.objects.create(user=request.user,email=register.cleaned_data['email'])
            verification.save()
            return redirect("otp")
        else:
            #messages.success(request,"Invalid Credential")
            #return redirect("signup")
            pass
    else:
        register = RegisterUserForm()
        info = UserForm()
    return render(request,"signup.html",{"form":register,"form2":info})

def SendOtp(request):
    if request.method=="POST":
        user_email=request.POST['otp']
        try:
            verification = Otp.objects.get(otp=user_email)
            name = type(request.user)
            print(f"nahim be this {name}")
            if request.user == verification.user:
                get_acc = WalletBalance.objects.create(user=request.user,cosmos_mining=0.00000,trading_balance=0.00,binance_coin_mining=0.00000,dogecoin_mining=0.00000,ethereum_mining=0.0000,bitcoin_mining=0.00000)
                get_acc.save()
                resave = WalletBalance.objects.get(user = request.user)
                resave.verified= True
                resave.save()
                verification.delete()
                return redirect("dashboard")
            else:
                messages.success(request,"invalid OTP")
                return redirect("otp")
        except Otp.DoesNotExist:
            messages.success(request,"invalid OTP")
            return redirect("otp")
    else:
        return render(request,'otp.html',{})
    
def homeview(request):
    return render(request,"index.html",{})
def about(request):
    return render(request,"about.html",{})
def cookies(request):
    return render(request,"cookie.html",{})
def faq(request):
    return render(request,"faq.html",{})
def privacy(request):
    return render(request,"privacy.html",{})
def terms(request):
    return render(request,"terms.html",{})
def copytrading(request):
    return render(request,"copytrading.html",{})
def cryptotrading(request):
    return render(request,"cryptotrading.html",{})
def forextrading(request):
    return render(request,"forextrading.html",{})

def dashboard(request):
    if request.user.is_authenticated:
        listall = []
        open = []
        close = []
        tradess = OpenClosedTrade.objects.filter(name = request.user)
        bal = WalletBalance.objects.get(user=request.user)
        check = CopiedTrade.objects.all()
        for obj in check:
            listall.append(obj.name)
        for obj in tradess:
            if obj.trade_type == "OPEN TRADE":
                open.append(obj.pk)
            else:
              if obj.trade_type == "CLOSED TRADE":
                close.append(obj.pk)  
        return render(request,"dashboard.html",{"total":len(listall),"bal":bal,"trade":tradess,"op":len(open),"cl":len(close)})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")


def copytrade(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            trade =request.POST['name']
            if trade != "yrfgur":
                print(trade,"\ntestttt\n\n\n\n\n\n\n\n\n")
                pass
        title = CopyTrader.objects.get(name="Ansem")
        
        trades = CopyTrader.objects.all()
        listall = []
        check = CopiedTrade.objects.all()
        for obj in check:
            if obj.user == request.user:
                listall.append(obj.name)
        return render(request,"traders.html",{"trade":trades,"list":listall})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

def trader_info(request,id):
    if request.user.is_authenticated:
        trades = CopyTrader.objects.all()
        listall = []
        check = CopiedTrade.objects.all()
        for obj in check:
            if obj.user == request.user:
                listall.append(obj.name)
            else:
                pass
        name = CopyTrader.objects.get(pk=id)
        interest = int(int(name.asset_under_management)*0.1)
        rate = round(random.uniform(20.11,50.44),2)
        return render(request,"traderinfo.html",{"name":name,"interest":interest,"rate":rate,"trade":trades,"list":listall})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def mining(request):
    if request.user.is_authenticated:
        bal = WalletBalance.objects.get(user=request.user)
        coins = Coin.objects.all()
        return render(request,"mining.html",{"coins":coins,"bal":bal})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

def market(request,id):
    if request.user.is_authenticated:
        name=id
        mylist = WatchList.objects.all()
        listall = []
        for obj in mylist:
            if obj.user == request.user:
                listall.append(obj.name)
            else:
                pass
        crypto = Market.objects.filter(form="CRYPTO")
        stock = Market.objects.filter(form="STOCKS")
        currency = Market.objects.filter(form="CURRENCIES")
        total_stock = []
        total_crypto = []
        total_currency = []
        for s,c,cr in zip(stock,currency,crypto):
            total_stock.append(s)
            total_currency.append(c)
            total_crypto.append(cr)
        market_data = Market.objects.all()
        data = {"total_stock":len(total_stock),"total_currency":len(total_currency),"total_crypto":len(total_crypto),
                "data":market_data,"name":name,"list":listall,
                }
        return render(request,"market.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

@csrf_exempt
def like_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name= request.POST["name"]
            if name.isnumeric() == True:
                trade = CopyTrader.objects.get(pk=name)
                try:
                    dele =CopiedTrade.objects.get(user=request.user,name=trade.name)
                    dele.delete()
                    print(name,"\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
                    return JsonResponse({'likes': "jhff"})
                except CopiedTrade.DoesNotExist:
                    addnew = CopiedTrade.objects.create(user=request.user,name=trade.name,profile_image=trade.profile_image,profit_share=trade.profit_share,win_rate=trade.win_rate)
                    addnew.save()
                    print(name,"\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
                    return JsonResponse({'likes': "jhff"})
            else:
                trades = Market.objects.get(name=name)
                delet = WatchList.objects.all()
                print(trades.name,"fjbj\n\n\n\n\n\n\n\n\n\n")
                for obj in delet:
                    print(name,"jjjj\n")
                    if obj.name == trades.name and obj.user == request.user:
                        obj.delete()
                        print(name,"fjbj\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
                        return JsonResponse({'likes': "jhff"})
                print(name,"jjjj\n")
                addnews = WatchList.objects.create(user=request.user,name=trades.name,image=trades.image,symbol=trades.symbol,form=trades.form)
                addnews.save()
                print(name,"ddde\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
                return JsonResponse({'likes': "jhff"})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
            
            
                
        
@csrf_exempt
def addwishlist(request):
    if request.method == "POST":
        name= request.POST["name"]
        trade = Market.objects.get(pk=name)
        try:
            dele = WatchList.objects.get(name=trade.name)
            dele.delete()
            print(name,"\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
            return JsonResponse({'likes': "jhff"})
        except CopiedTrade.DoesNotExist:
            addnew = WatchList.objects.create(user=request.user,name=trade.name,image=trade.image,symbol=trade.symbol,form=trade.form)
            addnew.save()
            print(name,"\n\n\nn\\nn\\n\n\n\n\n\n\n\n")
            return JsonResponse({'sent': "done"})

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        return current_price
    except Exception as e:
        #print(f"Error fetching forex price: {e}")
        return (0.00)

def get_forex_price(symbol):
    try:
        forex_pair = yf.Ticker(symbol)
        current_price = forex_pair.history(period='1d')['Close'].iloc[-1]
        return current_price
    except Exception as e:
        #print(f"Error fetching forex price: {e}")
        return (0.00) 
       


def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if symbol in data:
            return data[symbol]['usd']
        else:
            return (0.00)

    except requests.exceptions.RequestException as e:
        #print(f"Error: {e}")
        return (0.00)




def loaddata(request):
    if request.user.is_authenticated:
        crypto = Market.objects.filter(form="CRYPTO")
        stock = Market.objects.filter(form="STOCKS")
        currency = Market.objects.filter(form="CURRENCIES")
        for obj in stock:
            symbols = obj.symbol
            price = get_stock_price(symbols)
            save_stock = Market.objects.get(symbol = obj.symbol)
            save_stock.value = price # type: ignore
            save_stock.save()
            #print("\n\n\n\n\n\n\n",symbols,"\n\n",crypto,"\n\n",currency)
        for obj in currency:
            symbols = f"{obj.symbol}=X"
            price = get_forex_price(symbols)
            save_currency = Market.objects.get(symbol = obj.symbol)
            save_currency.value = price # type: ignore
            save_currency.save()
        for obk in crypto:
            symbols = obk.name.lower()
            price = get_crypto_price(symbols)
            save_crypto = Market.objects.get(symbol = obk.symbol)
            save_crypto.value = price # type: ignore
            save_crypto.save()
        return redirect("dashboard")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def traderoom(request,id):
    if request.user.is_authenticated:
        name =id
        crypto = Market.objects.filter(form="CRYPTO")
        stock = Market.objects.filter(form="STOCKS")
        currency = Market.objects.filter(form="CURRENCIES")
        balance = WalletBalance.objects.get(user=request.user)
        getid  = Market.objects.get(id=name)
        total_stock = []
        total_crypto = []
        total_currency = []
        for s,c,cr in zip(stock,currency,crypto):
            total_stock.append(s)
            total_currency.append(c)
            total_crypto.append(cr)
        data={"crypto":crypto,"stock":stock,"currenct":currency,"balance":balance,
              "total_stock":len(total_stock),"total_currency":len(total_currency),"total_crypto":len(total_crypto),
              "current":getid,
              }
        return render(request,"traderoom.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def deposit(request):
    if request.user.is_authenticated:
        depositform = DepositForm(request.POST)
        if request.method == "POST":
            if depositform.is_valid():
                step= depositform.save(commit=False)
                step.user = request.user
                n=depositform.save()
                return redirect("makepayment",id=n.pk)
            else:
                pass
        else:
            depositform = DepositForm(request.POST)
        total=[]
        deposits = Deposit.objects.all()
        for obj in deposits:
            if obj.user == request.user:
                total.append(obj)
        data={"form":depositform,"total":len(total),"deposits":deposits}
        return render(request,"deposit.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def withdraw(request):
    if request.user.is_authenticated:
        withdrawform = WithdrawForm(request.POST)
        if request.method == "POST":
            if withdrawform.is_valid()==True:
                setuser = withdrawform.save(commit=False)
                setuser.user = request.user
                setuser.save()
                return redirect("dashboard")
            else:
                pass
        else:
            withdrawform = WithdrawForm(request.POST)
        total=[]
        withdraws = Withdraw.objects.all()
        for obj in withdraws:
            if obj.user == request.user:
                total.append(obj)
        checkbal = Deposit.objects.all()
        sums = []
        for obj in checkbal:
            if obj.user == request.user:
                sums.append(obj.ammount)
        data={"form":withdrawform,"total":len(total),"deposits":withdraws,"bal":sum(sums)}
        return render(request,"withdraw.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

def makepayment(request,id):
    if request.user.is_authenticated:
        check = Deposit.objects.get(pk=id)
        coin = DepositCoin.objects.get(Coin=check.pay_in)
        price = round((check.ammount/(get_crypto_price("bitcoin"))),6)
        adress=coin.pair

        data ={"address":adress,"price":price,"type":check,"coin":coin}
        return render(request,"deposit2.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
 
def upgrade(request):
    if request.user.is_authenticated:
        return render(request,"upgrade.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def referals(request):
    if request.user.is_authenticated:
        return render(request,"referrals.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

def upgrademm(request):
    if request.user.is_authenticated:
        return render(request,"mining_plan.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def contracts(request):
    if request.user.is_authenticated:
        return render(request,"contracts.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

def account(request):
    if request.user.is_authenticated:
        return render(request,"account.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def refferal(request):
    if request.user.is_authenticated:
        return render(request,"referrals.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,"profile.html")
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    

def fund(request):
    if request.user.is_authenticated:
        depositform = DepositForm(request.POST)
        if request.method == "POST":
            if depositform.is_valid():
                step= depositform.save(commit=False)
                step.user = request.user
                n=depositform.save()
                return redirect("makepayment",id=n.pk)
            else:
                pass
        else:
            depositform = DepositForm(request.POST)
        total=[]
        deposits = Deposit.objects.all()
        for obj in deposits:
            if obj.user == request.user:
                total.append(obj)
        data={"form":depositform,"total":len(total),"deposits":deposits}
        return render(request,"fund.html",data)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")       

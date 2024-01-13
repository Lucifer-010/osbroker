from django.contrib import admin
from .models import CopyTrader,CopiedTrade,WalletBalance,Coin,Market,WatchList,UserInfo,Deposit,Withdraw,OpenClosedTrade
# Register your models here.

admin.site.register(WalletBalance)
admin.site.register(CopyTrader)
admin.site.register(CopiedTrade)
admin.site.register(Coin)
admin.site.register(UserInfo)
admin.site.register(Market)
admin.site.register(Deposit)
admin.site.register(WatchList)
admin.site.register(Withdraw)
admin.site.register(OpenClosedTrade)

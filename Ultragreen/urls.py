"""
URL configuration for Ultragreen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Green import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', views.dashboard,name="dashboard"),
    path('logout', views.log_out,name="logout"),
    path('', views.homeview,name="home"),
    path('terms/', views.terms,name="terms"),
    path('faq/', views.faq,name="faq"),
    path('forextrading', views.forextrading,name="forextrading"),
    path('cryptotrading', views.cryptotrading,name="cryptotrading"),
    path('copytrading', views.copytrading,name="copytrading"),
    path('privacy', views.privacy,name="privacy"),
    path('cookies', views.cookies,name="cookies"),
    path('account', views.account,name="account"),
    path('about', views.about,name="about"),
    path('complete/transaction/<int:id>', views.makepayment,name="makepayment"),
    path('deposit', views.deposit,name="deposit"), # type: ignore
    path('accounts/login/', views.loginuser, name="loginn" ),
    path('traderoom/<int:id>', views.traderoom,name="traderoom"),
    path('login/', views.loginuser,name="login"),
    path('signup', views.signup,name="signup"),
    path('load', views.loaddata,name="load"),
    path('contracts', views.contracts,name="contracts"),
    path('withdraw', views.withdraw,name="withdraw"),
    path('mining', views.mining,name="mining"),
    path('market/<str:id>', views.market,name="market"),
    path('addwishlist/', views.addwishlist,name="addwish"),# type: ignore
    path('trader/info/<int:id>', views.trader_info,name="traderInfo"),
    path('like_post/',views.like_post,name='like_post'), # type: ignore
    path('copytrade/', views.copytrade,name="copytrade"),
    path('upgrade', views.upgrade, name="upgrade" ),
    path('upgrade/mining', views.upgrademm, name="miningup" ),
    path('referrals', views.referals, name="referrals" ),
    path('account/verification', views.SendOtp, name="otp" ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

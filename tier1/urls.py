from django.contrib import admin
from django.urls import path
from tier1.views import create_transaction_one,getTransactions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('createtierone/', create_transaction_one, name="create-tier-one") ,
    path('transactions/',getTransactions, name="transactions") ,
 

]

from django.contrib import admin
from.models import Currency, Customer,Wallet,Account,Transaction,Card,Thirdparty,Notification,Loan,Reward,Receipt
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address",)
    search_fields=("fist_name","last_name")
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Receipt)
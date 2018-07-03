from django import forms
from .models import Order

# Create your models here.

class OrderForm(forms.ModelForm):
	def __init__(self, shop, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		# 해당 시점의 상품목록만 보이도록 Filter
		self.fields['item_set'].queryset = self.fields['item_set'].queryset.filter(shop=shop)

	class Meta:
		model = Order
		fields = ('item_set',)
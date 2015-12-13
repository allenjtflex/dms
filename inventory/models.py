from django.db import models

# Create your models here.
class Category(models.Model):
	classify = models.CharField(max_length=4, null=False) #分類碼
	itemcode = models.CharField(max_length=8, null=False) #
	description = models.CharField(max_length=60)
	is_effective = models.BooleanField(default=True) #有效

	class Meta:
		unique_together = (("classify", "itemcode"),)

	def __str__(self):
		return self.description


class Vender(models.Model):
	title = models.CharField(max_length=60, null=False)
	is_effective = models.BooleanField(default=True) #有效


class Equipment(models.Model):
	category = models.ForeignKey(Category, limit_choices_to = { 'classify': 'EC'})
	vender = models.ForeignKey(Vender)
	brand_model = models.CharField(max_length=60, null=False) #廠牌與型號
	spec_description = models.TextField() #規格說明
	purchase_at = models.DateField(auto_now_add=True) #購買日期
	is_special =  models.BooleanField(default=False) #特殊規格
	warranty_month = models.IntegerField(default=1) #保固月數

	is_effective = models.BooleanField(default=True) #有效
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False )
	update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.brand_model
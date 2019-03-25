from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Disease1(models.Model):
	record_id=models.AutoField(primary_key=True)
	gene_name=models.CharField(max_length=50, null=False)
	logFC=models.FloatField(null=True, blank=True, default=None)
	AveExpr=models.FloatField(null=True, blank=True, default=None)
	t=models.FloatField(null=True, blank=True, default=None)
	P_Value=models.FloatField(null=True, blank=True, default=None)
	adj_P_Val=models.FloatField(null=True, blank=True, default=None)
	B=models.FloatField(null=True, blank=True, default=None)
	dataset=models.CharField(max_length=50, null=False)
	category=models.IntegerField()
	def __str__(self):
		return '%d %s %d %d %d %d %d %d %s %d' % (self.record_id, self.gene_name, self.logFC, self.AveExpr, self.t, self.P_Value, self.adj_P_Val, self.B, self.dataset, self.category)



class Disease2(models.Model):
	record_id=models.AutoField(primary_key=True)
	gene_name=models.CharField(max_length=50, null=False)
	logFC=models.FloatField(null=True, blank=True, default=None)
	AveExpr=models.FloatField(null=True, blank=True, default=None)
	t=models.FloatField(null=True, blank=True, default=None)
	P_Value=models.FloatField(null=True, blank=True, default=None)
	adj_P_Val=models.FloatField(null=True, blank=True, default=None)
	B=models.FloatField(null=True, blank=True, default=None)
	dataset=models.CharField(max_length=50, null=False)
	category=models.IntegerField()
	def __str__(self):
		return '%d %s %d %d %d %d %d %d %s %d' % (self.record_id, self.gene_name, self.logFC, self.AveExpr, self.t, self.P_Value, self.adj_P_Val, self.B, self.dataset, self.category)
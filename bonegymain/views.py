from django.shortcuts import render
from bonegymain.models import Disease1, Disease2
import json
from django.contrib.staticfiles.templatetags.staticfiles import static
import pandas as pd
from django.conf import settings



def index(request):
	
	return render(request, 'bonegymain/index.html')

def result(request):
	if request.method=='POST':
		gene_name=request.POST.get('GeneName')
		request.session['gene_name']=gene_name
		'''disease1'''
		d1_cate_1_result=list(Disease1.objects.all().filter(gene_name=gene_name).filter(category=1).values_list('dataset', flat=True))
		request.session['datasets_1_1']=d1_cate_1_result
		d1_cate_2_result=list(Disease1.objects.all().filter(gene_name=gene_name).filter(category=2).values_list('dataset', flat=True))
		request.session['datasets_1_2']=d1_cate_2_result
		d1_cate_3_result=list(Disease1.objects.all().filter(gene_name=gene_name).filter(category=3).values_list('dataset', flat=True))
		request.session['datasets_1_3']=d1_cate_3_result
		d1_cate_4_result=list(Disease1.objects.all().filter(gene_name=gene_name).filter(category=4).values_list('dataset', flat=True))
		request.session['datasets_1_4']=d1_cate_4_result
		d1_cate_5_result=list(Disease1.objects.all().filter(gene_name=gene_name).filter(category=5).values_list('dataset', flat=True))
		request.session['datasets_1_5']=d1_cate_5_result
		d1_cate_1_count=len(d1_cate_1_result)
		d1_cate_2_count=len(d1_cate_2_result)
		d1_cate_3_count=len(d1_cate_3_result)
		d1_cate_4_count=len(d1_cate_4_result)
		d1_cate_5_count=len(d1_cate_5_result)
		'''disease2'''
		d2_cate_1_result=list(Disease2.objects.all().filter(gene_name=gene_name).filter(category=1).values_list('dataset', flat=True))
		request.session['datasets_2_1']=d2_cate_1_result
		d2_cate_2_result=list(Disease2.objects.all().filter(gene_name=gene_name).filter(category=2).values_list('dataset', flat=True))
		request.session['datasets_2_2']=d2_cate_2_result
		d2_cate_3_result=list(Disease2.objects.all().filter(gene_name=gene_name).filter(category=3).values_list('dataset', flat=True))
		request.session['datasets_2_3']=d2_cate_3_result
		d2_cate_4_result=list(Disease2.objects.all().filter(gene_name=gene_name).filter(category=4).values_list('dataset', flat=True))
		request.session['datasets_2_4']=d2_cate_4_result
		d2_cate_5_result=list(Disease2.objects.all().filter(gene_name=gene_name).filter(category=5).values_list('dataset', flat=True))
		request.session['datasets_2_5']=d2_cate_5_result
		d2_cate_1_count=len(d2_cate_1_result)
		d2_cate_2_count=len(d2_cate_2_result)
		d2_cate_3_count=len(d2_cate_3_result)
		d2_cate_4_count=len(d2_cate_4_result)
		d2_cate_5_count=len(d2_cate_5_result)
	return render(request, 'bonegymain/result.html', {'gene_name':gene_name,
													'd1_cate_1_count': d1_cate_1_count, 
													'd1_cate_2_count': d1_cate_2_count, 
													'd1_cate_3_count': d1_cate_3_count, 
													'd1_cate_4_count': d1_cate_4_count, 
													'd1_cate_5_count': d1_cate_5_count, 
													'd2_cate_1_count': d2_cate_1_count, 
													'd2_cate_2_count': d2_cate_2_count, 
													'd2_cate_3_count': d2_cate_3_count, 
													'd2_cate_4_count': d2_cate_4_count, 
													'd2_cate_5_count': d2_cate_5_count})
def simple(request, group, gene_name):
	try_to_get='datasets_'+group
	dataset_names=request.session.get(try_to_get)
	final_out=[]
	range=[]
	for i in dataset_names:
		file_path=settings.STATIC_ROOT+'\\exp_data\\'+i+'.txt'
		data=pd.read_csv(file_path, index_col=0, header=0, sep='\t')
		column_name='Dataset_'+i
		values=list(data.loc[[gene_name]].values[0])
		range=range+values
		current_dict={'column_name':column_name, 'values':values}
		final_out.append(dict(current_dict))
	max_num=max(range)
	max_num=json.dumps(max_num)
	min_num=min(range)
	min_num=json.dumps(min_num)
	final_out=json.dumps(final_out)
	return final_out, max_num, min_num
	
	
	
	
def plot(request, group):
	group=group
	gene_name=request.session.get('gene_name')
	final_out, max_num, min_num=simple(request, group, gene_name)
	return render(request, 'bonegymain/plot.html', {'group': group, 'final_out': final_out, 'min_num':min_num, 'max_num':max_num, 'gene_name':gene_name})


	
	
	
	
	
	
	
	
	
	
	
	
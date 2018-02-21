from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from getregi.models import Laboratory, Personnel, Rizivcode, Genetictest, Disease, TestDisease, Purpose, TestPurpose, Volume, TestVolume, Gene, Genepanel, GenepanelGene, GenepanelDisease, TestGenepanel, TestGene, DiseaseGene, TestMethod, MethodCategory, MethodTechnique, MethodPlatform
from django.template import Context, loader, RequestContext
from django.db.models import Count, Q, Sum, Avg
import operator

# Create your views here.

def index(request):
	laboratory_list = Laboratory.objects.all().order_by('lab_name')
	genetictest_list = Genetictest.objects.all().order_by('test_name')
	return render_to_response('getregi/index.html', {'laboratory_list': laboratory_list, 'genetictest_list': genetictest_list},
		context_instance=RequestContext(request))

def index_search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		qset_test = (
			Q(test_name__icontains=q) |
			Q(test_shortname__icontains=q) |
			Q(test_commercialname__icontains=q) |
			Q(test_loinc__icontains=q) |
			Q(test_category__icontains=q) |
			Q(test_lab__lab_name__icontains=q) |
			Q(test_lab__lab_shortname__icontains=q) |
			Q(test_lab__lab_cityname__icontains=q) |
			Q(test_lab__lab_countryname__icontains=q) |
			Q(test_personnelcontact__pers_firstname__icontains=q) |
			Q(test_personnelcontact__pers_lastname__icontains=q) |
			Q(test_rizivcode__riziv_code__icontains=q) |
			Q(testdisease__disease__disease_name__icontains=q) |
			Q(testdisease__disease__disease_shortname__icontains=q) |
			Q(testdisease__disease__disease_synonym__icontains=q) |
			Q(testgene__gene__gene_name__icontains=q) |
			Q(testgene__gene__gene_shortname__icontains=q) |
			Q(testgene__gene__gene_synonym__icontains=q)
		)
		qset_gene = (
			Q(gene_name__icontains=q) |
			Q(gene_shortname__icontains=q) |
			Q(gene_synonym__icontains=q) |
			Q(gene_xrefomim__icontains=q) |
			Q(gene_xrefhgnc__icontains=q)
		)
		qset_disease = (
			Q(disease_name__icontains=q) |
			Q(disease_shortname__icontains=q) |
			Q(disease_synonym__icontains=q) |
			Q(disease_xrefomim__icontains=q) |
			Q(disease_xreforphanet__icontains=q)
		)
		qset_laboratory = (
			Q(lab_name__icontains=q) |
			Q(lab_shortname__icontains=q) |
			Q(lab_cityname__icontains=q) |
			Q(lab_countryname__icontains=q) |
			Q(personnel__pers_firstname__icontains=q) |
			Q(personnel__pers_lastname__icontains=q)
		)
		if not q:
			errors.append('Please submit a search term !')
		elif len(q) > 24:
			errors.append('Please enter at most 24 characters !')
		else:
			genetictests = Genetictest.objects.filter(qset_test).distinct()
			genes = Gene.objects.filter(qset_gene).distinct()
			diseases = Disease.objects.filter(qset_disease).distinct()
			laboratories = Laboratory.objects.filter(qset_laboratory).distinct()
			return render(request, 'getregi/search_results.html',
				{'genetictests': genetictests, 'genes': genes, 'diseases': diseases, 'laboratories': laboratories, 'q': q})
	return render(request, 'getregi/index_search.html',
		{'errors': errors})

def index_browse(request):
	laboratory_list = Laboratory.objects.all().order_by('lab_name')
	return render_to_response('getregi/index_browse.html', {'laboratory_list': laboratory_list},
		context_instance=RequestContext(request))
		
def index_laboratory(request):
	laboratory_list = Laboratory.objects.all().order_by('lab_name')
	return render_to_response('getregi/index_laboratory.html', {'laboratory_list': laboratory_list},
		context_instance=RequestContext(request))
		
def index_personnel(request):
	personnel_list = Personnel.objects.all().order_by('pers_lastname')
	return render_to_response('getregi/index_personnel.html', {'personnel_list': personnel_list},
		context_instance=RequestContext(request))

def index_rizivcode(request):
	rizivcode_list = Rizivcode.objects.all().order_by('riziv_code')
	return render_to_response('getregi/index_rizivcode.html', {'rizivcode_list': rizivcode_list},
		context_instance=RequestContext(request))

def index_genetictest(request):
	genetictest_list = Genetictest.objects.all().order_by('test_name')
	return render_to_response('getregi/index_genetictest.html', {'genetictest_list': genetictest_list},
		context_instance=RequestContext(request))

def index_disease(request):
	disease_list = Disease.objects.all().order_by('disease_name')
	return render_to_response('getregi/index_disease.html', {'disease_list': disease_list},
		context_instance=RequestContext(request))

def index_gene(request):
	gene_list = Gene.objects.all().order_by('gene_name')
	genepanel_list = Genepanel.objects.all().order_by('genepanel_name')
	return render_to_response('getregi/index_gene.html', {'gene_list': gene_list, 'genepanel_list': genepanel_list},
		context_instance=RequestContext(request))
		
#def index_genepanel(request):
#	genepanel_list = Genepanel.objects.all().order_by('genepanel_name')
#	return render_to_response('getregi/index_genepanel.html', {'genepanel_list': genepanel_list},
#		context_instance=RequestContext(request))

def index_methodology(request):
	methodcategory_list = MethodCategory.objects.all().order_by('method_category')
	methodtechnique_list = MethodTechnique.objects.all().order_by('method_technique')
	methodplatform_list = MethodPlatform.objects.all().order_by('method_platform')
	return render_to_response('getregi/index_methodology.html', {'methodcategory_list': methodcategory_list, 'methodtechnique_list': methodtechnique_list, 'methodplatform_list': methodplatform_list},
		context_instance=RequestContext(request))

def detail_laboratory(request, laboratory_id):
	p = get_object_or_404(Laboratory, pk=laboratory_id)
	personnel_list = Laboratory.objects.prefetch_related('personnel_set').all()
	genetictest_list = Laboratory.objects.prefetch_related('genetictest_set').all()
	return render_to_response('getregi/detail_laboratory.html', {'laboratory': p, 'personnel_list': personnel_list, 'genetictest_list': genetictest_list},
		context_instance=RequestContext(request))

def detail_personnel(request, personnel_id):
	p = get_object_or_404(Personnel, pk=personnel_id)
	genetictest_list = Personnel.objects.prefetch_related('genetictest_set').all()
	return render_to_response('getregi/detail_personnel.html', {'personnel': p, 'genetictest_list': genetictest_list},
		context_instance=RequestContext(request))

def detail_methodcategory(request, methodcategory_id):
	p = get_object_or_404(MethodCategory, pk=methodcategory_id)
#	test_list = p.testmethod_set.all().order_by('test__test_name')
#	test_list = p.testmethod_set.all().values('test__test_name','test__test_lab__lab_name').distinct()
#	test_list = MethodCategory.objects.prefetch_related('testmethod_set').all().order_by('testmethod')
#	test_list = Genetictest.objects.filter(testmethod__methodcategory=1).distinct()
	test_list = p.testmethod_set.order_by('test__test_name').distinct()
#	test_list = MethodCategory.objects.prefetch_related('testmethod_set').all()
	return render_to_response('getregi/detail_methodcategory.html', {'methodcategory': p, 'test_list': test_list},
		context_instance=RequestContext(request))

def detail_methodtechnique(request, methodtechnique_id):
	p = get_object_or_404(MethodTechnique, pk=methodtechnique_id)
#	test_list = MethodTechnique.objects.prefetch_related('testmethod_set').all().order_by('test')
#	test_list = Genetictest.objects.filter(testmethod__methodtechnique=1).distinct()
#	test_list = Genetictest.objects.prefetch_related('testmethod_set').all().order_by('test_name').distinct()
	test_list = p.testmethod_set.order_by('test__test_name').distinct()	
	return render_to_response('getregi/detail_methodtechnique.html', {'methodtechnique': p, 'test_list': test_list},
		context_instance=RequestContext(request))
		
def detail_methodplatform(request, methodplatform_id):
	p = get_object_or_404(MethodPlatform, pk=methodplatform_id)
#	test_list = MethodPlatform.objects.prefetch_related('testmethod_set').all().order_by('test')
#	test_list = Genetictest.objects.filter(testmethod__methodplatform=1).distinct()
#	test_list = Genetictest.objects.prefetch_related('testmethod_set').all().order_by('test_name').distinct()
	test_list = p.testmethod_set.order_by('test__test_name').distinct()
	return render_to_response('getregi/detail_methodplatform.html', {'methodplatform': p, 'test_list': test_list},
		context_instance=RequestContext(request))

def detail_genetictest(request, genetictest_id):
	p = get_object_or_404(Genetictest, pk=genetictest_id)
	g1 = Genetictest.objects.filter(id=1)
	year_volume = p.testvolume_set.all().values('volume__vol_year').annotate(count=Count('volume__vol_year'), sum_total=Sum('volume__vol_total'), sum_positive=Sum('volume__vol_positive'), sum_negative=Sum('volume__vol_negative'), sum_carrier=Sum('volume__vol_carrier'), sum_unclassified=Sum('volume__vol_unclassified'))
	symptom_volume = p.testvolume_set.all().values('volume__vol_symptom').annotate(count=Count('volume__vol_symptom'), sum_total=Sum('volume__vol_total'), sum_positive=Sum('volume__vol_positive'), sum_negative=Sum('volume__vol_negative'), sum_carrier=Sum('volume__vol_carrier'), sum_unclassified=Sum('volume__vol_unclassified'))
#	year_volume = g1.values('testvolume__volume__vol_year').annotate(count=Count('testvolume__volume__vol_year'), sum_total=Sum('testvolume__volume__vol_total'), sum_positive=Sum('testvolume__volume__vol_positive'), sum_negative=Sum('testvolume__volume__vol_negative'), sum_carrier=Sum('testvolume__volume__vol_carrier'), sum_unclassified=Sum('testvolume__volume__vol_unclassified'))
#	symptom_volume = g1.values('testvolume__volume__vol_symptom').annotate(count=Count('testvolume__volume__vol_symptom'), sum_total=Sum('testvolume__volume__vol_total'), sum_positive=Sum('testvolume__volume__vol_positive'), sum_negative=Sum('testvolume__volume__vol_negative'), sum_carrier=Sum('testvolume__volume__vol_carrier'), sum_unclassified=Sum('testvolume__volume__vol_unclassified'))
	Sums = {}
	Sums['total'] = sum(i.volume.vol_total for i in p.testvolume_set.all())
	Sums['positive'] = sum(i.volume.vol_positive for i in p.testvolume_set.all())
	Sums['negative'] = sum(i.volume.vol_negative for i in p.testvolume_set.all())
	Sums['unclassified'] = sum(i.volume.vol_unclassified for i in p.testvolume_set.all())
	Sums['carrier'] = sum(i.volume.vol_carrier for i in p.testvolume_set.all())
#	disease_list = Genetictest.objects.prefetch_related('testdisease_set').all().order_by('test_name')
	disease_list = p.testdisease_set.all().order_by('disease__disease_name')
#	gene_list = Genetictest.objects.prefetch_related('testgene_set').all().order_by('test_name')
	gene_list = p.testgene_set.all().order_by('gene__gene_shortname')
	genepanel_list = p.testgenepanel_set.all().order_by('genepanel__genepanel_name') 
#	purpose_list = Genetictest.objects.prefetch_related('testpurpose_set').all().order_by('test_name')
	purpose_list = p.testpurpose_set.all().order_by('purpose__purp_name') 
#	volume_list = Genetictest.objects.prefetch_related('testvolume_set').all().order_by('test_name')
	volume_list = p.testvolume_set.all().order_by('volume__vol_year', 'volume__vol_symptom')
#	method_list = Genetictest.objects.prefetch_related('testmethod_set').all().order_by('test_name')
	method_list = p.testmethod_set.all().order_by('methodcategory__method_category', 'methodtechnique__method_technique', 'methodplatform__method_platform')
#	eqa_list = Genetictest.objects.prefetch_related('testeqa_set').all().order_by('test_name')
	eqa_list = p.testeqa_set.all().order_by('eqa__eqa_name', 'year', 'eqa__eqa_organizer')
#	accreditation_list = Genetictest.objects.prefetch_related('testaccreditation_set').all().order_by('test_name')
	accreditation_list = p.testaccreditation_set.all().order_by('accreditation__accreditation_name', 'year', 'accreditation__accreditation_organizer')
	return render_to_response('getregi/detail_genetictest.html', {'genetictest': p, 'disease_list': disease_list, 'purpose_list': purpose_list, 'volume_list': volume_list, 'gene_list': gene_list, 'genepanel_list': genepanel_list, 'method_list': method_list, 'eqa_list': eqa_list, 'accreditation_list': accreditation_list, 'Sums': Sums, 'g1': g1, 'year_volume': year_volume, 'symptom_volume': symptom_volume},
		context_instance=RequestContext(request))

def detail_disease(request, disease_id):
	p = get_object_or_404(Disease, pk=disease_id)
	test_list = Disease.objects.prefetch_related('testdisease_set').all().order_by('test')
	gene_list = Disease.objects.prefetch_related('diseasegene_set').all().order_by('gene')
	return render_to_response('getregi/detail_disease.html', {'disease': p, 'test_list': test_list, 'gene_list': gene_list},
		context_instance=RequestContext(request))

def detail_gene(request, gene_id):
	p = get_object_or_404(Gene, pk=gene_id)
	test_list = Gene.objects.prefetch_related('testgene_set').all().order_by('test')
	disease_list = Gene.objects.prefetch_related('diseasegene_set').all().order_by('disease')
	return render_to_response('getregi/detail_gene.html', {'gene': p, 'test_list': test_list, 'disease_list': disease_list},
		context_instance=RequestContext(request))

def detail_genepanel(request, genepanel_id):
	p = get_object_or_404(Genepanel, pk=genepanel_id)
	gene_list = Genepanel.objects.prefetch_related('genepanelgene_set').all().order_by('gene')
	test_list = Genepanel.objects.prefetch_related('testgenepanel_set').all().order_by('test')
	disease_list = Genepanel.objects.prefetch_related('genepaneldisease_set').all().order_by('disease')
	return render_to_response('getregi/detail_genepanel.html', {'genepanel': p, 'gene_list': gene_list, 'test_list': test_list, 'disease_list': disease_list},
		context_instance=RequestContext(request))

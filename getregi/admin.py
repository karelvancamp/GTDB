from django.contrib import admin

# Register your models here.

from getregi.models import Laboratory
from getregi.models import Personnel
from getregi.models import Rizivcode
from getregi.models import Genetictest
from getregi.models import Disease
from getregi.models import TestDisease
from getregi.models import Purpose
from getregi.models import TestPurpose
from getregi.models import Volume
from getregi.models import TestVolume
from getregi.models import Gene
from getregi.models import Genepanel
from getregi.models import GenepanelGene
from getregi.models import TestGene
from getregi.models import TestGenepanel
from getregi.models import DiseaseGene
from getregi.models import GenepanelDisease
from getregi.models import MethodCategory
from getregi.models import MethodTechnique
from getregi.models import MethodPlatform
from getregi.models import TestMethod
from getregi.models import Eqa
from getregi.models import TestEqa
from getregi.models import Accreditation
from getregi.models import TestAccreditation

class LaboratoryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Laboratory name/institute', {'fields': ['lab_name', 'lab_shortname', 'lab_institutename', 'lab_instituteshortname', 'lab_departmentname']}),
		('Address', {'fields': ['lab_streetname', 'lab_streetnumber', 'lab_cityname', 'lab_citycode', 'lab_statename', 'lab_countryname', 'lab_addresspublic']}),
		('Contact', {'fields': ['lab_phone', 'lab_fax', 'lab_email', 'lab_url']}),
	]
	list_display = ('id', 'lab_name', 'lab_cityname')
	list_display_links = ('id', 'lab_name', 'lab_cityname')
	search_fields = ['lab_name', 'lab_cityname', 'lab_countryname']

class PersonnelAdmin(admin.ModelAdmin):
	fieldsets = [
		('Laboratory', {'fields': ['pers_lab', 'pers_persdirector', 'pers_perspublic']}),
		('Name', {'fields': ['pers_firstname', 'pers_lastname', 'pers_middlename']}),
		('Qualifications', {'fields': ['pers_title', 'pers_jobtitle', 'pers_degree']}),
		('Contact', {'fields': ['pers_phone', 'pers_fax', 'pers_email']}),
	]
	list_display = ('id', 'pers_firstname', 'pers_lastname')
	list_display_links = ('id', 'pers_firstname', 'pers_lastname')
	search_fields = ['pers_firstname', 'pers_lastname']
	
class RizivcodeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Riziv code', {'fields': ['riziv_code', 'riziv_description']}),
		('Financial', {'fields': ['riziv_honorarium', 'riziv_ambulantreimbursement', 'riziv_hospitalizedreimbursement']}),
	]
	list_display = ('id', 'riziv_code')
	list_display_links = ('id', 'riziv_code')
	search_fields = ['riziv_code', 'riziv_description']

class GenetictestAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test_name', 'test_loinc', 'test_shortname', 'test_commercialname']}),
		('Test contact', {'fields': ['test_lab', 'test_location', 'test_outsidelab', 'test_personnelcontact', 'test_url']}),
		('Test details', {'fields': ['test_category', 'test_target', 'test_tat', 'test_cost', 'test_rizivcode']}),
		('Test performance', {'fields': ['test_analyticalsensitivity', 'test_analyticalspecificity', 'test_analyticalprecision', 'test_clinicalvalidity', 'test_clinicalutility']}),
	]
	list_display = ('id', 'test_name', 'test_lab')
	list_display_links = ('id', 'test_name', 'test_lab')
	search_fields = ['test_name', 'test_lab']

class DiseaseAdmin(admin.ModelAdmin):
	fieldsets = [
		('Disease', {'fields': ['disease_name', 'disease_shortname', 'disease_synonym', 'disease_description']}),
		('Cross references', {'fields': ['disease_xref', 'disease_xrefomim', 'disease_xreforphanet']}),
	]
	list_display = ('id', 'disease_name', 'disease_shortname')
	list_display_links = ('id', 'disease_name', 'disease_shortname')
	search_fields = ['disease_name', 'disease_shortname', 'disease_synonym']

class TestDiseaseAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Disease', {'fields': ['disease']}),
	]
	list_display = ('id', 'test', 'disease')
	list_display_links = ('id', 'test', 'disease')
	search_fields = ['test', 'disease']

class PurposeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Purpose', {'fields': ['purp_name', 'purp_description']}),
	]
	list_display = ('id', 'purp_name')
	list_display_links = ('id', 'purp_name')
	search_fields = ['purp_name']

class TestPurposeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Purpose', {'fields': ['purpose']}),
	]
	list_display = ('id', 'test', 'purpose')
	list_display_links = ('id', 'test', 'purpose')
	search_fields = ['test', 'purpose']

class VolumeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Year', {'fields': ['vol_year']}),
		('Indication/symptom', {'fields': ['vol_symptom']}),
		('Volumes', {'fields': ['vol_total', 'vol_positive', 'vol_negative', 'vol_unclassified', 'vol_carrier', 'vol_failed']}),
	]
	list_display = ('id', 'vol_year', 'vol_symptom', 'vol_total')
	list_display_links = ('id', 'vol_year', 'vol_symptom', 'vol_total')
	search_fields = ['vol_year', 'vol_symptom']

class TestVolumeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Volume', {'fields': ['volume']}),
	]
	list_display = ('id', 'test', 'volume')
	list_display_links = ('id', 'test', 'volume')
	search_fields = ['test', 'purpose']

class GeneAdmin(admin.ModelAdmin):
	fieldsets = [
		('Gene', {'fields': ['gene_name', 'gene_shortname', 'gene_synonym', 'gene_description']}),
		('Cross references', {'fields': ['gene_xref', 'gene_xrefomim', 'gene_xrefhgnc']}),
	]
	list_display = ('id', 'gene_name', 'gene_shortname')
	list_display_links = ('id', 'gene_name', 'gene_shortname')
	search_fields = ['gene_name', 'gene_shortname', 'gene_synonym']
	
class GenepanelAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genepanel', {'fields': ['genepanel_name', 'genepanel_shortname', 'genepanel_synonym', 'genepanel_description']}),
		('Provider', {'fields': ['genepanel_provider']}),
	]
	list_display = ('id', 'genepanel_name', 'genepanel_shortname')
	list_display_links = ('id', 'genepanel_name', 'genepanel_shortname')
	search_fields = ['genepanel_name', 'genepanel_shortname', 'genepanel_synonym', 'genepanel_provider']

class GenepanelGeneAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genepanel', {'fields': ['genepanel']}),
		('Gene', {'fields': ['gene']}),
	]
	list_display = ('id', 'genepanel', 'gene')
	list_display_links = ('id', 'genepanel', 'gene')
	search_fields = ['genepanel', 'gene']

class TestGeneAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Gene', {'fields': ['gene']}),
	]
	list_display = ('id', 'test', 'gene')
	list_display_links = ('id', 'test', 'gene')
	search_fields = ['test', 'gene']

class TestGenepanelAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Genepanel', {'fields': ['genepanel']}),
	]
	list_display = ('id', 'test', 'genepanel')
	list_display_links = ('id', 'test', 'genepanel')
	search_fields = ['test', 'genepanel']

class DiseaseGeneAdmin(admin.ModelAdmin):
	fieldsets = [
		('Disease', {'fields': ['disease']}),
		('Gene', {'fields': ['gene']}),
	]
	list_display = ('id', 'disease', 'gene')
	list_display_links = ('id', 'disease', 'gene')
	search_fields = ['disease', 'gene']

class GenepanelDiseaseAdmin(admin.ModelAdmin):
	fieldsets = [
		('Disease', {'fields': ['disease']}),
		('Genepanel', {'fields': ['genepanel']}),
	]
	list_display = ('id', 'disease', 'genepanel')
	list_display_links = ('id', 'disease', 'genepanel')
	search_fields = ['disease', 'genepanel']

class MethodCategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Method category', {'fields': ['method_category']}),
		('Category description', {'fields': ['method_categorydescription']}),
	]
	list_display = ('id', 'method_category')
	list_display_links = ('id', 'method_category')
	search_fields = ['method_category']

class MethodTechniqueAdmin(admin.ModelAdmin):
	fieldsets = [
		('Method technique', {'fields': ['method_technique']}),
		('Technique description', {'fields': ['method_techniquedescription']}),
	]
	list_display = ('id', 'method_technique')
	list_display_links = ('id', 'method_technique')
	search_fields = ['method_technique']

class MethodPlatformAdmin(admin.ModelAdmin):
	fieldsets = [
		('Method platform', {'fields': ['method_platform']}),
		('Platform description', {'fields': ['method_platformdescription']}),
	]
	list_display = ('id', 'method_platform')
	list_display_links = ('id', 'method_platform')
	search_fields = ['method_platform']

class TestMethodAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Method category', {'fields': ['methodcategory']}),
		('Method technique', {'fields': ['methodtechnique']}),
		('Method platfom', {'fields': ['methodplatform']}),
	]
	list_display = ('id', 'test', 'methodcategory', 'methodtechnique', 'methodplatform')
	list_display_links = ('id', 'test', 'methodcategory', 'methodtechnique', 'methodplatform')
	search_fields = ['test', 'methodcategory', 'methodtechnique', 'methodplatform']

class EqaAdmin(admin.ModelAdmin):
	fieldsets = [
		('EQA name', {'fields': ['eqa_name']}),
		('EQA organizer', {'fields': ['eqa_organizer']}),
	]
	list_display = ('id', 'eqa_name', 'eqa_organizer')
	list_display_links = ('id', 'eqa_name', 'eqa_organizer')
	search_fields = ['eqa_name', 'eqa_organizer']

class AccreditationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Accreditation name', {'fields': ['accreditation_name']}),
		('Accreditation organizer', {'fields': ['accreditation_organizer']}),
	]
	list_display = ('id', 'accreditation_name', 'accreditation_organizer')
	list_display_links = ('id', 'accreditation_name', 'accreditation_organizer')
	search_fields = ['accreditation_name', 'accreditation_organizer']

class TestEqaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('EQA', {'fields': ['eqa']}),
		('Year', {'fields': ['year']}),
		('Score', {'fields': ['scoremax', 'scorelab']}),
	]
	list_display = ('id', 'test', 'eqa', 'year', 'scoremax', 'scorelab')
	list_display_links = ('id', 'test', 'eqa', 'year', 'scoremax', 'scorelab')
	search_fields = ['test', 'eqa', 'year', 'scoremax', 'scorelab']

class TestAccreditationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Genetic test', {'fields': ['test']}),
		('Accreditation', {'fields': ['accreditation']}),
		('Year', {'fields': ['year']}),
	]
	list_display = ('id', 'test', 'accreditation', 'year')
	list_display_links = ('id', 'test', 'accreditation', 'year')
	search_fields = ['test', 'accreditation', 'year']


admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Rizivcode, RizivcodeAdmin)
admin.site.register(Genetictest, GenetictestAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(TestDisease, TestDiseaseAdmin)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(TestPurpose, TestPurposeAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(TestVolume, TestVolumeAdmin)
admin.site.register(Gene, GeneAdmin)
admin.site.register(Genepanel, GenepanelAdmin)
admin.site.register(GenepanelGene, GenepanelGeneAdmin)
admin.site.register(TestGene, TestGeneAdmin)
admin.site.register(TestGenepanel, TestGenepanelAdmin)
admin.site.register(DiseaseGene, DiseaseGeneAdmin)
admin.site.register(GenepanelDisease, GenepanelDiseaseAdmin)
admin.site.register(MethodCategory, MethodCategoryAdmin)
admin.site.register(MethodTechnique, MethodTechniqueAdmin)
admin.site.register(MethodPlatform, MethodPlatformAdmin)
admin.site.register(TestMethod, TestMethodAdmin)
admin.site.register(Eqa, EqaAdmin)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(TestEqa, TestEqaAdmin)
admin.site.register(TestAccreditation, TestAccreditationAdmin)
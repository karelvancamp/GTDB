from django.db import models
import datetime

# Create your models here.

class Laboratory(models.Model):
	CITY_CHOICES = (
		('Antwerpen', 'Antwerpen'),
		('Brussel', 'Brussel'),
		('Gent', 'Gent'),
		('Gosselies', 'Gosselies'),
		('Leuven', 'Leuven'),
		('Louvain-La-Neuve', 'Louvain-La-Neuve'),
		('Luik', 'Luik'),
		('Other', 'Other')
	)
	STATE_CHOICES = (
		('Antwerpen', 'Antwerpen'),
		('Brussel', 'Brussel'),
		('Henegouwen', 'Henegouwen'),
		('Namen', 'Namen'),
		('Oost-Vlaanderen', 'Oost-Vlaanderen'),
		('Luik', 'Luik'),
		('Luxemburg', 'Luxemburg'),
		('Vlaams-Brabant', 'Vlaams-Brabant'),
		('Waals-Brabant', 'Waals-Brabant'),
		('West-Vlaanderen', 'West-Vlaanderen'),
		('Other', 'Other')
	)
	COUNTRY_CHOICES = (
		('Austria', 'Austria'),
		('Belgium', 'Belgium'),
		('Croatia', 'Croatia'),
		('Czech Republic', 'Czech Republic'),
		('Denmark', 'Denmark'),
		('Estonia', 'Estonia'),
		('Finland', 'Finland'),
		('France', 'France'),
		('Germany', 'Germany'),
		('Greece', 'Greece'),
		('Hungary', 'Hungary'),
		('Italy', 'Italy'),
		('Latvia', 'Latvia'),
		('Lithuania', 'Lithuania'),
		('Norway', 'Norway'),
		('Poland', 'Poland'),
		('Portugal', 'Portugal'),
		('Romania', 'Romania'),
		('Slovakia', 'Slovakia'),
		('Slovenia', 'Slovenia'),
		('Spain', 'Spain'),
		('Sweden', 'Sweden'),
		('Switzerland', 'Switzerland'),
		('The Netherlands', 'The Netherlands'),
		('United Kingdom', 'United Kingdom')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	lab_name = models.CharField(unique=True, max_length=128)
	lab_shortname = models.CharField(max_length=32, blank=True)
	lab_institutename = models.CharField(max_length=128, blank=True)
	lab_instituteshortname = models.CharField(max_length=32, blank=True)
	lab_departmentname = models.CharField(max_length=128, blank=True)
	lab_streetname = models.CharField(max_length=128, blank=True)
	lab_streetnumber = models.CharField(max_length=32, blank=True)
	lab_cityname = models.CharField(max_length=128, choices=CITY_CHOICES)
	lab_citycode = models.CharField(max_length=32)
	lab_statename = models.CharField(max_length=128, choices=STATE_CHOICES)
	lab_countryname = models.CharField(max_length=128, choices=COUNTRY_CHOICES)
	lab_addresspublic = models.BooleanField()
	lab_phone = models.CharField(max_length=32)
	lab_fax = models.CharField(max_length=32, blank=True)
	lab_email = models.CharField(max_length=32)
	lab_url = models.CharField(max_length=128)
	def __unicode__(self):
		return unicode(self.lab_name)
	class Meta:
		verbose_name = 'Laboratory'
		verbose_name_plural = 'Laboratories'
		ordering = ('lab_name',)
		db_table = u'laboratories'

class Personnel(models.Model):
	TITLE_CHOICES = (
		('Ms.', 'Ms.'),
		('Mrs.', 'Mrs.'),
		('Mr.', 'Mr.'),
		('Dr.', 'Dr.'),
		('Prof.', 'Prof.')
	)
	JOBTITLE_CHOICES = (
		('Administrator', 'Administrator'),
		('Nurse', 'Nurse'),
		('Lab Director', 'Lab Director'),
		('Scientific Director', 'Scientific Director'),
		('Medical Director', 'Medical Director'),
		('Staff', 'Staff'),
		('Other', 'Other')
	)
	DEGREE_CHOICES = (
		('BASc', 'BASc'),
		('BA', 'BA'),
		('MSc', 'MSc'),
		('Ph.D.', 'Ph.D.'),
		('M.D.', 'M.D.')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	pers_lab = models.ForeignKey(Laboratory)
	pers_perspublic = models.BooleanField()
	pers_persdirector = models.BooleanField()
	pers_firstname = models.CharField(max_length=128)
	pers_lastname = models.CharField(max_length=128)
	pers_middlename = models.CharField(max_length=128, blank=True)
	pers_title = models.CharField(max_length=32, choices=TITLE_CHOICES, blank=True)
	pers_jobtitle = models.CharField(max_length=32, choices=JOBTITLE_CHOICES, blank=True)
	pers_degree = models.CharField(max_length=32, choices=DEGREE_CHOICES, blank=True)
	pers_phone = models.CharField(max_length=32)
	pers_fax = models.CharField(max_length=32, blank=True)
	pers_email = models.CharField(max_length=32)
	def __unicode__(self):
		return unicode("%s %s %s" % (self.pers_lastname, self.pers_firstname, self.pers_lab.lab_name))
	class Meta:
		verbose_name = 'Personnel'
		verbose_name_plural = 'Personnel'
		ordering = ('pers_lastname', 'pers_firstname',)
		db_table = u'personnel'

class Rizivcode(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	riziv_code = models.CharField(unique=True, max_length=32)
	riziv_description = models.CharField(max_length=256)
	riziv_honorarium = models.CharField(max_length=128)
	riziv_ambulantreimbursement = models.CharField(max_length=128)
	riziv_hospitalizedreimbursement = models.CharField(max_length=128)
	def __unicode__(self):
		return unicode(self.riziv_code)
	class Meta:
		verbose_name = 'Riziv Code'
		verbose_name_plural = 'Riziv Codes'
		ordering = ('riziv_code',)
		db_table = u'rizivcode'
		
class Genetictest(models.Model):
	CATEGORY_CHOICES = (
		('Molecular Genetics', 'Molecular Genetics'),
		('Cytogenetics', 'Cytogenetics'),
		('Pathology', 'Pathology'),
		('Immunology', 'Immunology'),
		('Parasitology', 'Parasitology'),
		('Bacteriology', 'Bacteriology'),
		('Virology', 'Virology'),
		('Mycology', 'Mycology'),
		('Hematology', 'Hematology'),
		('Imaging', 'Imaging'),		
		('Culture', 'Culture')
	)
	CLINUTIL_CHOICES = (
		('Avoidance of invasive testing', 'Avoidance of invasive testing'),
		('Establish or confirm diagnosis', 'Establish or confirm diagnosis'),
		('Guidance for management', 'Guidance for management'),
		('Guidance for selecting a drug therapy and/or dose', 'Guidance for selecting a drug therapy and/or dose'),
		('Lifestyle planning', 'Lifestyle planning'),
		('Predicitive risk information for patient and/or family members', 'Predicitive risk information for patient and/or family members'),
		('Reproductive decision-making', 'Reproductive decision-making'),
		('Other', 'Other'),	
		('Sufficient research has not been conducted to demonstrate the utility of the test', 'Sufficient research has not been conducted to demonstrate the utility of the test')
	)
	LOCATION_CHOICES = (
		('Entire test performed in-house', 'Entire test performed in-house'),
		('Entire test performed at an outside laboratory', 'Entire test performed at an outside laboratory'),
		('Interpretation performed at an outside laboratory', 'Interpretation performed at an outside laboratory'),
		('Interpretation performed both in-house and at an outside laboratory', 'Interpretation performed both in-house and at an outside laboratory'),
		('Report generated at an outside laboratory', 'Report generated at an outside laboratory'),
		('Report generated both in-house and at an outside laboratory', 'Report generated both in-house and at an outside laboratory'),
		('Specimen preparation performed at an outside laboratory', 'Specimen preparation performed at an outside laboratory'),
		('Specimen preparation performed both in-house and at an outside laboratory', 'Specimen preparation performed both in-house and at an outside laboratory'),	
		('Wet lab work performed at an outside laboratory', 'Wet lab work performed at an outside laboratory'),
		('Wet lab work performed both in-house and at an outside laboratory', 'Wet lab work performed both in-house and at an outside laboratory')
	)
	TARGET_CHOICES = (
		('Whole genome sequencing', 'Whole genome sequencing'),
		('Whole exome sequencing', 'Whole exome sequencing'),
		('Gene panel sequencing', 'Gene panel sequencing'),
		('Gene sequencing', 'Gene sequencing'),
		('Exon sequencing', 'Exon sequencing'),
		('Chromosome rearrangements', 'Chromosome rearrangements'),
		('Copy number variations', 'Copy number variations')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test_lab = models.ForeignKey(Laboratory, related_name='testlab')
	test_location = models.CharField(max_length=128, choices=LOCATION_CHOICES)
	test_outsidelab = models.ForeignKey(Laboratory, related_name='outsidelab', null=True)
	test_loinc = models.CharField(max_length=128, blank=True)
	test_name = models.CharField(max_length=256)
	test_shortname = models.CharField(max_length=32, blank=True)
	test_commercialname = models.CharField(max_length=256, blank=True)
	test_personnelcontact = models.ForeignKey(Personnel)
	test_url = models.CharField(max_length=128, blank=True)
	test_category = models.CharField(max_length=128, choices=CATEGORY_CHOICES)
	test_target = models.CharField(max_length=128, choices=TARGET_CHOICES)
	test_tat = models.CharField(max_length=128, blank=True)
	test_cost = models.CharField(max_length=128, blank=True)
	test_rizivcode = models.ForeignKey(Rizivcode)
	test_analyticalsensitivity = models.CharField(max_length=128, blank=True)
	test_analyticalspecificity = models.CharField(max_length=128, blank=True)
	test_analyticalprecision = models.CharField(max_length=128, blank=True)
	test_clinicalvalidity = models.CharField(max_length=128, blank=True)
	test_clinicalutility = models.CharField(max_length=128, choices=CLINUTIL_CHOICES, blank=True)
#	test_order = models.ForeignKey(Order)
	def __unicode__(self):
		return unicode("%s %s" % (self.test_name, self.test_lab.lab_name))
	class Meta:
		verbose_name = 'Genetic test'
		verbose_name_plural = 'Genetic tests'
		ordering = ('test_name',)
		db_table = u'genetictests'
		
class Disease(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	disease_name = models.CharField(unique=True, max_length=128)
	disease_shortname = models.CharField(max_length=32)
	disease_synonym = models.CharField(max_length=128)
	disease_xref = models.CharField(max_length=128, blank=True)
	disease_xrefomim = models.CharField(max_length=128)
	disease_xreforphanet = models.CharField(max_length=128)
	disease_description = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.disease_name)
	class Meta:
		verbose_name = 'Disease'
		verbose_name_plural = 'Diseases'
		ordering = ('disease_name',)
		db_table = u'diseases'
		
class TestDisease(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	disease = models.ForeignKey(Disease)
	def __unicode__(self):
		return unicode("%s %s" % (self.test, self.disease))
	class Meta:
		verbose_name = 'Test Disease'
		verbose_name_plural = 'Test Diseases'
		order_with_respect_to = ('disease')
		db_table = u'testdiseases'
		
class Purpose(models.Model):
	PURPOSE_CHOICES = (
		('Diagnostic', 'Diagnostic'),
		('Mutation confirmation', 'Mutation confirmation'),
		('Presomatic', 'Presomatic'),
		('Carrier', 'Carrier'),
		('Newborn screening', 'Newborn screening'),
		('Prenatal', 'Prenatal'),
		('Preimplantation diagnosis', 'Preimplantation diagnosis'),
		('Dosage', 'Dosage'),
		('Monitoring', 'Monitoring')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	purp_name = models.CharField(max_length=128, choices=PURPOSE_CHOICES)
	purp_description = models.CharField(max_length=2048, blank=True)
	def __unicode__(self):
		return unicode(self.purp_name)
	class Meta:
		verbose_name = 'Purpose'
		verbose_name_plural = 'Purpose'
		ordering = ('purp_name',)
		db_table = u'purpose'

class TestPurpose(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	purpose = models.ForeignKey(Purpose)
	def __unicode__(self):
		return unicode("%s %s %s" % (self.test.test_name, self.test.test_lab.lab_name, self.purpose))
	class Meta:
		verbose_name = 'Test Purpose'
		verbose_name_plural = 'Test Purpose'
		order_with_respect_to = ('purpose')
		db_table = u'testpurpose'

class Volume(models.Model):
	SYMPTOM_CHOICES = (
		('thrombocytopenia', 'thrombocytopenia'),
		('spinal hemangioblastoma', 'spinal hemangioblastoma'),
		('cerebellar hemangioblastoma', 'cerebellar hemangioblastoma'),
		('retinal hemangioblastoma', 'retinal hemangioblastoma'),
		('some other symptom', 'some other symptom'),
		('yet another symptom', 'yet another symptom'),
		('the worst symptom', 'the worst symptom')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	vol_year = models.IntegerField()
	vol_symptom = models.CharField(max_length=256, choices=SYMPTOM_CHOICES)
	vol_total = models.IntegerField()
	vol_positive = models.IntegerField()
	vol_negative = models.IntegerField()
	vol_unclassified = models.IntegerField()
	vol_carrier = models.IntegerField()
	vol_failed = models.IntegerField()
	def __unicode__(self):
		return unicode("%s %s %s" % (self.vol_symptom, self.vol_year, self.vol_total))
	class Meta:
		verbose_name = 'Volume'
		verbose_name_plural = 'Volumes'
		ordering = ('vol_year', 'vol_symptom')
		db_table = u'volume'

class TestVolume(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	volume = models.ForeignKey(Volume)
	def __unicode__(self):
		return unicode("%s %s %s %s" % (self.test.test_name, self.test.test_lab.lab_name, self.volume.vol_year, self.volume.vol_total))
	class Meta:
		verbose_name = 'Test Volume'
		verbose_name_plural = 'Test Volume'
		order_with_respect_to = ('volume')
		db_table = u'testvolume'
		
class Gene(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	gene_name = models.CharField(unique=True, max_length=128)
	gene_shortname = models.CharField(max_length=32)
	gene_synonym = models.CharField(max_length=128)
	gene_xref = models.CharField(max_length=128, blank=True)
	gene_xrefomim = models.CharField(max_length=128)
	gene_xrefhgnc = models.CharField(max_length=128)
	gene_description = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode("%s %s" % (self.gene_name, self.gene_shortname))
	class Meta:
		verbose_name = 'Gene'
		verbose_name_plural = 'Genes'
		ordering = ('gene_name',)
		db_table = u'genes'
		
class TestGene(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	gene = models.ForeignKey(Gene)
	def __unicode__(self):
		return unicode("%s %s" % (self.test, self.gene))
	class Meta:
		verbose_name = 'Test Gene'
		verbose_name_plural = 'Test Genes'
		order_with_respect_to = ('gene')
		db_table = u'testgenes'

class Genepanel(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	genepanel_name = models.CharField(unique=True, max_length=128)
	genepanel_shortname = models.CharField(max_length=32)
	genepanel_synonym = models.CharField(max_length=128, blank=True)
	genepanel_description = models.CharField(max_length=2048, blank=True)
	genepanel_provider = models.CharField(max_length=2048, blank=True)
	def __unicode__(self):
		return unicode("%s %s" % (self.genepanel_name, self.genepanel_shortname))
	class Meta:
		verbose_name = 'Genepanel'
		verbose_name_plural = 'Genepanels'
		ordering = ('genepanel_name',)
		db_table = u'genepanels'

class GenepanelGene(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	gene = models.ForeignKey(Gene)
	genepanel = models.ForeignKey(Genepanel)
	def __unicode__(self):
		return unicode("%s %s" % (self.gene, self.genepanel))
	class Meta:
		verbose_name = 'Genepanel Gene'
		verbose_name_plural = 'Genepanelgenes'
		order_with_respect_to = ('gene')
		db_table = u'genepanelgenes'

class TestGenepanel(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	genepanel = models.ForeignKey(Genepanel)
	def __unicode__(self):
		return unicode("%s %s" % (self.test, self.genepanel))
	class Meta:
		verbose_name = 'Test Genepanel'
		verbose_name_plural = 'Test Genepanels'
		order_with_respect_to = ('genepanel')
		db_table = u'testgenepanels'

class DiseaseGene(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	disease = models.ForeignKey(Disease)
	gene = models.ForeignKey(Gene)
	def __unicode__(self):
		return unicode("%s %s" % (self.gene, self.disease))
	class Meta:
		verbose_name = 'Disease Gene'
		verbose_name_plural = 'Disease Genes'
		order_with_respect_to = ('disease')
		db_table = u'diseasegenes'

class GenepanelDisease(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	disease = models.ForeignKey(Disease)
	genepanel = models.ForeignKey(Genepanel)
	def __unicode__(self):
		return unicode("%s %s" % (self.disease, self.genepanel))
	class Meta:
		verbose_name = 'Genepanel Disease'
		verbose_name_plural = 'Genepaneldiseases'
		order_with_respect_to = ('disease')
		db_table = u'genepaneldiseases'

class MethodCategory(models.Model):
	CATEGORY_CHOICES = (
		('Analyte assay', 'Analyte assay'),
		('Copy number variations', 'Copy number variations'),
		('Chromosomal instability', 'Chromosomal instability'),
		('Deletion/duplication analysis', 'Deletion/duplication analysis'),
		('Detection of chromosome alterations large in size', 'Detection of chromosome alterations large in size'),
		('Detection of microdeletions/microduplications', 'Detection of microdeletions/microduplications'),
		('Enzyme assay', 'Enzyme assay'),
		('Karyotyping', 'Karyotyping'),
		('Linkage analysis', 'Linkage analysis'),
		('Methylation analysis', 'Methylation analysis'),
		('Mutation scanning/screening of entire coding region', 'Mutation scanning/screening of entire coding region'),
		('Mutation scanning/screening of selected exons', 'Mutation scanning/screening of selected exons'),
		('Protein expression', 'Protein expression'),
		('RNA analysis', 'RNA analysis'),
		('Sequence analysis: entire coding region', 'Sequence analysis: entire coding region'),
		('Sequence analysis: mitochondrial genome', 'Sequence analysis: mitochondrial genome'),
		('Sequence analysis: selected exons', 'Sequence analysis: selected exons'),
		('Sequence analysis: whole exome', 'Sequence analysis: whole exome'),
		('Sequence analysis: whole genome', 'Sequence analysis: whole genome'),
		('Targeted mutation analysis', 'Targeted mutation analysis'),
		('Uniparental disomy study', 'Uniparental disomy study')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	method_category = models.CharField(max_length=128, choices=CATEGORY_CHOICES)
	method_categorydescription = models.CharField(max_length=2048, blank=True)
	def __unicode__(self):
		return unicode(self.method_category)
	class Meta:
		verbose_name = 'Method Category'
		verbose_name_plural = 'Method Categories'
		ordering = ('method_category',)
		db_table = u'methodcategories'

class MethodTechnique(models.Model):
	TECHNIQUE_CHOICES = (
		('Array based techniques', 'Array based techniques'),
		('BS-Pyrosequencing', 'BS-Pyrosequencing'),
		('Chromosome breakage studies', 'Chromosome breakage studies'),
		('FISH', 'FISH'),
		('Immunohistochemistry', 'Immunohistochemistry'),
		('Karyotyping', 'Karyotyping'),		
		('MLPA based techniques', 'MLPA based techniques'),
		('Microsatellite analysis', 'Microsatellite analysis'),
		('Multicolor FISH', 'Multicolor FISH'),
		('NGS sequencing', 'NGS sequencing'),
		('PCR based techniques', 'PCR based techniques'),
		('Sanger sequencing', 'Sanger sequencing'),
		('Uniparental disomy study', 'Uniparental disomy study'),
		('Western Blot', 'Western Blot')		
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	method_technique = models.CharField(max_length=128, choices=TECHNIQUE_CHOICES)
	method_techniquedescription = models.CharField(max_length=2048, blank=True)
	def __unicode__(self):
		return unicode(self.method_technique)
	class Meta:
		verbose_name = 'Method Technique'
		verbose_name_plural = 'Method Techniques'
		ordering = ('method_technique',)
		db_table = u'methodtechniques'

class MethodPlatform(models.Model):
	PLATFORM_CHOICES = (
		('Affymetrix CytoScan HD Array', 'Affymetrix CytoScan HD Array'),
		('Affymetrix Genome-Wide Human SNP Array 6.0', 'Affymetrix Genome-Wide Human SNP Array 6.0'),
		('Agilent Human CpG Island Microarray Kit, 1x244K', 'Agilent Human CpG Island Microarray Kit, 1x244K'),
		('Agilent Human ENCODE ChIP-on-chip Microarray', 'Agilent Human ENCODE ChIP-on-chip Microarray'),
		('Amerscham CodeLink UniSet Human I Bioarray', 'Amerscham CodeLink UniSet Human I Bioarray'),
		('Illumina Infinium HD HumanCytoSNP-12', 'Illumina Infinium HD HumanCytoSNP-12'),		
		('Life Technologies TaqMan OpenArray MicroRNA Panels', 'Life Technologies TaqMan OpenArray MicroRNA Panels'),
		('Other', 'Other'),
		('None/not applicable', 'None/not applicable')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	method_platform = models.CharField(max_length=128, choices=PLATFORM_CHOICES)
	method_platformdescription = models.CharField(max_length=2048, blank=True)
	def __unicode__(self):
		return unicode(self.method_platform)
	class Meta:
		verbose_name = 'Method Platform'
		verbose_name_plural = 'Method Platforms'
		ordering = ('method_platform',)
		db_table = u'methodplatforms'

class TestMethod(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	methodcategory = models.ForeignKey(MethodCategory)
	methodtechnique = models.ForeignKey(MethodTechnique)
	methodplatform = models.ForeignKey(MethodPlatform)
	def __unicode__(self):
		return unicode("%s %s %s %s" % (self.test, self.methodcategory, self.methodtechnique, self.methodplatform))
	class Meta:
		verbose_name = 'Test Method'
		verbose_name_plural = 'Test Methods'
		order_with_respect_to = ('test')
		db_table = u'testmethods'
		
	
class Eqa(models.Model):
	ORGANIZER_CHOICES = (
		('CEQAS', 'CEQAS'),
		('CF Network', 'CF Network'),
		('EMQN', 'EMQN'),
		('UKNEQAS', 'UKNEQAS')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	eqa_name = models.CharField(max_length=128)
	eqa_organizer = models.CharField(max_length=256, choices=ORGANIZER_CHOICES)
	def __unicode__(self):
		return unicode("%s %s" % (self.eqa_name, self.eqa_organizer))
	class Meta:
		verbose_name = 'Eqa'
		verbose_name_plural = 'Eqas'
		ordering = ('eqa_name',)
		db_table = u'eqas'

class Accreditation(models.Model):
	ORGANIZER_CHOICES = (
		('BELAC', 'BELAC'),
		('DAKKS/DAR-DACH', 'DAKKS/DAR-DACH'),
		('Other', 'Other')
	)
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	accreditation_name = models.CharField(max_length=128)
	accreditation_organizer = models.CharField(max_length=256, choices=ORGANIZER_CHOICES)
	def __unicode__(self):
		return unicode("%s %s" % (self.accreditation_name, self.accreditation_organizer))
	class Meta:
		verbose_name = 'Accreditation'
		verbose_name_plural = 'Accreditations'
		ordering = ('accreditation_name',)
		db_table = u'accreditations'

class TestEqa(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	eqa = models.ForeignKey(Eqa)
	year = models.IntegerField()
	scoremax = models.DecimalField(max_digits=8, decimal_places=5)
	scorelab = models.DecimalField(max_digits=8, decimal_places=5)
	def __unicode__(self):
		return unicode("%s %s %s" % (self.test, self.eqa, self.year))
	class Meta:
		verbose_name = 'Test Eqa'
		verbose_name_plural = 'Test Eqas'
		order_with_respect_to = ('test')
		db_table = u'testeqas'

class TestAccreditation(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	test = models.ForeignKey(Genetictest)
	accreditation = models.ForeignKey(Accreditation)
	year = models.IntegerField()
	def __unicode__(self):
		return unicode("%s %s %s" % (self.test, self.accreditation, self.year))
	class Meta:
		verbose_name = 'Test Accreditation'
		verbose_name_plural = 'Test Accreditations'
		order_with_respect_to = ('test')
		db_table = u'testaccreditations'

class SimpleTax:
	def __init__(self, annual, taxdata):
		self.annual = annual
		self.prov_brk1 = taxdata['province']['brk1']
		self.prov_brk2 = taxdata['province']['brk2']
		self.prov_brk3 = taxdata['province']['brk3']
		self.prov_brk4 = taxdata['province']['brk4']
		self.prov_brk5 = taxdata['province']['brk5']
		self.prov_PersonalAmount = taxdata['province']['PersonalAmount']

		self.federal_brk1 = taxdata['federal']['brk1']
		self.federal_brk2 = taxdata['federal']['brk2']
		self.federal_brk3 = taxdata['federal']['brk3']
		self.federal_brk4 = taxdata['federal']['brk4']
		self.federal_brk5 = taxdata['federal']['brk5']
		self.federal_PersonalAmount = taxdata['federal']['PersonalAmount']

		self.maxei = taxdata['employeeInsurance']['maxei']
		self.maxcppContrib = taxdata['cpp']['maxcppContrib']
		self.cppExempt = taxdata['cpp']['cppExempt']

	def clamp(self, x, cmin, cmax):
		clamped = 0 if x < cmin else max(cmin, min(x, cmax))
		return clamped

	def canadaPensionPlan(self, maxcppContrib, cppExempt):
		cppContrib = min(maxcppContrib[0], self.annual)
		cpp = (cppContrib-cppExempt)*(maxcppContrib[1]*0.01)
		return cpp

	def emplymentInsurance(self, maxei):
		eiContrib = min(maxei[0], self.annual)
		ei = (eiContrib*(maxei[1]*0.01))
		return ei

	def bracketTax(self, personal, bracket1, bracket2, bracket3, bracket4, bracket5):
		ernBrk1 = max(0, self.clamp(self.annual, bracket1[0], bracket1[1]))
		ernBrk1Due = ernBrk1*(bracket1[2]*0.01)
		ernBrk2 = max(0, self.clamp(self.annual, bracket2[0], bracket2[1])-ernBrk1)
		ernBrk2Due = ernBrk2*(bracket2[2]*0.01)
		ernBrk3 = max(0, self.clamp(self.annual, bracket3[0], bracket3[1])-ernBrk2-ernBrk1)
		ernBrk3Due = ernBrk3*(bracket3[2]*0.01)
		ernBrk4 = max(0, self.clamp(self.annual, bracket4[0], bracket4[1])-ernBrk3-ernBrk2-ernBrk1)
		ernBrk4Due = ernBrk4*(bracket4[2]*0.01)
		ernBrk5 = max(0, self.clamp(self.annual, bracket5[0], bracket5[1])-ernBrk4-ernBrk3-ernBrk2-ernBrk1)
		ernBrk5Due = ernBrk5*(bracket5[2]*0.01)
		bracketTaxDue = (ernBrk1Due+ernBrk2Due+ernBrk3Due+ernBrk4Due+ernBrk5Due)-(personal[0]*(personal[1]*0.01))
		return bracketTaxDue

	def afterTax(self):
		after = self.annual \
		- self.canadaPensionPlan(self.maxcppContrib, self.cppExempt) \
		- self.emplymentInsurance(self.maxei) \
		- self.bracketTax(self.prov_PersonalAmount, self.prov_brk1, self.prov_brk2, self.prov_brk3, self.prov_brk4, self.prov_brk5) \
		- self.bracketTax(self.federal_PersonalAmount, self.federal_brk1, self.federal_brk2, self.federal_brk3, self.federal_brk4, self.federal_brk5)
		return after

	def taxDue(self):
		due = self.annual - self.afterTax()
		return due

###################################
#  TESTS
if __name__ == '__main__':
	from jsonParser import jsonFile

	taxfile = jsonFile("BCtax2017.json")
	taxdata = taxfile.load()

	ann = 180000
	testCalc = SimpleTax(ann, taxdata).afterTax() 
	print(testCalc)
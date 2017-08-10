
class SimpleTax:
	def __init__(self, annual):
		self.annual = annual
		# 2017 data http://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates
		self.prov_BC_brk1 = [0, 38898, 5.06]
		self.prov_BC_brk2 = [38898, 77797, 7.70]
		self.prov_BC_brk3 = [77797.01, 89320, 10.5]
		self.prov_BC_brk4 = [89320.01, 108460, 12.29]
		self.prov_BC_brk5 = [108460, 150000, 14.70]
		self.prov_BC_PersonalAmount = [10208, 5.06]
		# 2017 data https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
		self.federal_brk1 = [0, 45916, 15]
		self.federal_brk2 = [45916, 91831, 20.5]
		self.federal_brk3 = [91831, 142353, 26]
		self.federal_brk4 = [142353, 202800, 29]
		self.federal_brk5 = [202800, 999000, 33]
		self.federal_PersonalAmount = [11635, 15]
		# maximum Employer Insurance for 2017
		self.maxei = [51300, 1.63]
		# maximum CPP Contribution for 2017 adn General contribution rate %
		self.maxcppContrib = [55300, 4.95]
		self.cppExempt = 3500 # Basic exemption amount (unchanged since at least 1997)

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
		after = self.annual - self.canadaPensionPlan(self.maxcppContrib, self.cppExempt) - self.emplymentInsurance(self.maxei) - self.bracketTax(self.prov_BC_PersonalAmount, self.prov_BC_brk1, self.prov_BC_brk2, self.prov_BC_brk3, self.prov_BC_brk4, self.prov_BC_brk5) - self.bracketTax(self.federal_PersonalAmount, self.federal_brk1, self.federal_brk2, self.federal_brk3, self.federal_brk4, self.federal_brk5)
		return after

	def taxDue(self):
		due = self.annual - self.afterTax()
		return due

###################################
#  TESTS
if __name__ == '__main__':
	ann = 180000
	print(SimpleTax(ann).afterTax())


class SimpleTax(object):
	def __init__(self):
		self.getData = 1
		#2017 data http://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates
		prov_BC_brk1 = [0, 38898, 5.06]
		prov_BC_brk2 = [38898, 77797, 7.70]
		prov_BC_brk3 = [77797.01, 89320, 10.5]
		prov_BC_brk4 = [89320.01, 108460, 12.29]
		prov_BC_brk5 = [108460, 150000, 14.70]
		prov_BC_PersonalAmount = [10208, 5.06]
		#2017 data https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
		federal_brk1 = [0, 45916, 15]
		federal_brk2 = [45916, 91831, 20.5]
		federal_brk3 = [91831, 142353, 26]
		federal_brk4 = [142353, 202800, 29]
		federal_brk5 = [202800, 999000, 33]
		federal_PersonalAmount = [11635, 15]

	def clamp(self, x, cmin, cmax):
		clamped = 0 if x < cmin else max(cmin, min(x, cmax))
		return clamped

	def canadaPensionPlan(self, annual):
		maxcppContrib = [55300, 4.95] #maximum CPP Contribution for 2017 adn General contribution rate %
		cppExempt = 3500 # Basic exemption amount (unchanged since at least 1997)
		cppContrib = min(maxcppContrib[0], annual)
		cpp = (cppContrib-cppExempt)*(maxcppContrib[1]*0.01) #CPP rate for 2017
		return cpp

	def emplymentInsurance(self, annual):
		maxei = [51300, 1.63] #maximum Employer Insurance for 2017
		eiContrib = min(maxei[0], annual)
		ei = (eiContrib*(maxei[1]*0.01)) #EI rate for 2017
		return ei

	def bracketTax(self, annual, personal, bracket1, bracket2, bracket3, bracket4, bracket5):
		ernBrk1 = max(0, self.clamp(annual, bracket1[0], bracket1[1]))
		ernBrk1Due = ernBrk1*(bracket1[2]*0.01)
		ernBrk2 = max(0, self.clamp(annual, bracket2[0], bracket2[1])-ernBrk1)
		ernBrk2Due = ernBrk2*(bracket2[2]*0.01)
		ernBrk3 = max(0, self.clamp(annual, bracket3[0], bracket3[1])-ernBrk2-ernBrk1)
		ernBrk3Due = ernBrk3*(bracket3[2]*0.01)
		ernBrk4 = max(0, self.clamp(annual, bracket4[0], bracket4[1])-ernBrk3-ernBrk2-ernBrk1)
		ernBrk4Due = ernBrk4*(bracket4[2]*0.01)
		ernBrk5 = max(0, self.clamp(annual, bracket5[0], bracket5[1])-ernBrk4-ernBrk3-ernBrk2-ernBrk1)
		ernBrk5Due = ernBrk5*(bracket5[2]*0.01)
		bracketTaxDue = (ernBrk1Due+ernBrk2Due+ernBrk3Due+ernBrk4Due+ernBrk5Due)-(personal[0]*(personal[1]*0.01))
		return bracketTaxDue

	def ProvincialTax(self, annual):
		#2017 data http://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates
		brk1 = [0, 38898, 5.06]
		brk2 = [38898, 77797, 7.70]
		brk3 = [77797.01, 89320, 10.5]
		brk4 = [89320.01, 108460, 12.29]
		brk5 = [108460, 150000, 14.70]
		PersonalAmount = [10208, 5.06]
		#############################################
		ernBrk1 = max(0, self.clamp(annual, brk1[0], brk1[1]))
		ernBrk1Due = ernBrk1*(brk1[2]*0.01)
		ernBrk2 = max(0, self.clamp(annual, brk2[0], brk2[1])-ernBrk1)
		ernBrk2Due = ernBrk2*(brk2[2]*0.01)
		ernBrk3 = max(0, self.clamp(annual, brk3[0], brk3[1])-ernBrk2-ernBrk1)
		ernBrk3Due = ernBrk3*(brk3[2]*0.01)
		ernBrk4 = max(0, self.clamp(annual, brk4[0], brk4[1])-ernBrk3-ernBrk2-ernBrk1)
		ernBrk4Due = ernBrk4*(brk4[2]*0.01)
		ernBrk5 = max(0, self.clamp(annual, brk5[0], brk5[1])-ernBrk4-ernBrk3-ernBrk2-ernBrk1)
		ernBrk5Due = ernBrk5*(brk5[2]*0.01)
		PTDue = (ernBrk1Due+ernBrk2Due+ernBrk3Due+ernBrk4Due+ernBrk5Due)-(PersonalAmount[0]*(PersonalAmount[1]*0.01))
		return PTDue

	def FederalTax(self, annual):
		#2017 data https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
		brk1 = [0, 45916, 15]
		brk2 = [45916, 91831, 20.5]
		brk3 = [91831, 142353, 26]
		brk4 = [142353, 202800, 29]
		brk5 = [202800, 999000, 33]
		PersonalAmount = [11635, 15]
		#############################################
		ernBrk1 = max(0, self.clamp(annual, brk1[0], brk1[1]))
		ernBrk1Due = ernBrk1*(brk1[2]*0.01)
		ernBrk2 = max(0, self.clamp(annual, brk2[0], brk2[1])-ernBrk1)
		ernBrk2Due = ernBrk2*(brk2[2]*0.01)
		ernBrk3 = max(0, self.clamp(annual, brk3[0], brk3[1])-ernBrk2-ernBrk1)
		ernBrk3Due = ernBrk3*(brk3[2]*0.01)
		ernBrk4 = max(0, self.clamp(annual, brk4[0], brk4[1])-ernBrk3-ernBrk2-ernBrk1)
		ernBrk4Due = ernBrk4*(brk4[2]*0.01)
		ernBrk5 = max(0, self.clamp(annual, brk5[0], brk5[1])-ernBrk4-ernBrk3-ernBrk2-ernBrk1)
		ernBrk5Due = ernBrk5*(brk5[2]*0.01)
		FTDue = (ernBrk1Due+ernBrk2Due+ernBrk3Due+ernBrk4Due+ernBrk5Due)-(PersonalAmount[0]*(PersonalAmount[1]*0.01))
		return FTDue

	def afterTax(self, annual):
		after = annual - self.canadaPensionPlan(annual) - self.emplymentInsurance(annual) - self.ProvincialTax(annual) - self.FederalTax(annual)
		return after

	def taxDue(self, annual):
		due = annual - self.afterTax(annual)
		return due

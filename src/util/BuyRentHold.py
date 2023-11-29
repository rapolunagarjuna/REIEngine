class BuyRentHold:
    def __init__(self, offer_price_USD, units, insurance_USD, property_tax_USD, defaults):
        
        

        if not isinstance(units, int):
            UNITS = 1
        else:
            UNITS = units

        
        self.property_info = PropertyInfo(offer_price_USD, UNITS, defaults)
        self.purchase_info = PurchaseInfo(offer_price_USD, defaults)
        self.income_info = IncomeInfo(defaults["incomeInfo"]["grossRents"], defaults)
        self.operating_expenses = OperatingExpenses(
            property_tax_USD, 
            insurance_USD, 
            defaults["incomeInfo"]["grossRents"], 
            self.property_info.management_rate_percent,
            self.property_info.num_of_units, 
            self.property_info.advertising_cost_per_vacancy_USD, 
            self.property_info.vacancy_rate_percent,
            defaults
            )
        self.financing = Financing(offer_price_USD, self.purchase_info.real_purchase_price_USD, defaults)
        self.cash_requirements = CashRequirements(self.financing.cash_required_to_close_USD, defaults)


        #summary statistics
        self.net_operating_income_USD = self.income_info.effective_income_USD - self.operating_expenses.total_expenses_USD
        self.debt_servicing_cost_USD = (self.financing.first_mtg_monthly_payment_USD + self.financing.second_mtg_monthly_payment_USD + self.financing.interest_only_total_monthly_payment_USD + self.financing.other_monthly_financing_costs_USD)*12
        
        self.annual_profit_USD = self.net_operating_income_USD - self.debt_servicing_cost_USD
        self.monthly_profit_USD = self.annual_profit_USD / 12
        self.cashflow_per_unit_per_month_USD = self.monthly_profit_USD / self.property_info.num_of_units  

        self.first_mortgage_LTV_percent = 100 * self.financing.first_mtg_principle_borrowed_USD / self.property_info.fair_market_value_USD
        self.first_mortgage_LTPP_percent = 100 * self.financing.first_mtg_principle_borrowed_USD / self.purchase_info.offer_price_USD
        self.second_mortgage_LTV_percent = 100 * self.financing.second_mtg_principle_borrowed_USD / self.property_info.fair_market_value_USD
        self.second_mortgage_LTPP_percent = 100 * self.financing.second_mtg_principle_borrowed_USD / self.purchase_info.offer_price_USD

        self.cap_rate_on_PP_percent = 100*(self.net_operating_income_USD/ self.purchase_info.offer_price_USD)
        self.cap_rate_on_FMV_percent = 100*(self.net_operating_income_USD/ self.property_info.fair_market_value_USD)
        self.average_rent_USD = self.income_info.annual_rent_USD / (self.property_info.num_of_units * 12)
        self.GRM = self.purchase_info.offer_price_USD / self.income_info.annual_rent_USD
        
        self.cash_on_cash_ROI_percent = float('inf') if self.cash_requirements.total_cash_required_USD <= 0 else 100*self.annual_profit_USD/self.cash_requirements.total_cash_required_USD
        self.equity_ROI_percent = float('inf') if self.cash_requirements.total_cash_required_USD <= 0 else 100* (self.financing.first_mtg_principle_borrowed_USD + self.financing.second_mtg_principle_borrowed_USD) / self.cash_requirements.total_cash_required_USD
        self.appreciation_ROI_percent = float('inf') if self.cash_requirements.total_cash_required_USD <= 0 else 100 *(self.property_info.fair_market_value_USD*(1 + (self.property_info.annual_appreciation_rate_percent/100)) - self.property_info.fair_market_value_USD ) / abs(self.cash_requirements.total_cash_required_USD)
        self.total_ROI_percent = float('inf') if self.cash_requirements.total_cash_required_USD <= 0 else self.cash_on_cash_ROI_percent + self.equity_ROI_percent + self.appreciation_ROI_percent
        self.forced_app_ROI_percent = float('inf') if self.cash_requirements.total_cash_required_USD <= 0 else 100*(self.property_info.fair_market_value_USD - self.purchase_info.real_purchase_price_USD) / abs(self.cash_requirements.total_cash_required_USD)
        self.expense_to_income_ratio = 100*(self.operating_expenses.total_expenses_USD / self.income_info.total_income_USD)



class CashRequirements:
    def __init__(self, cash_required_to_close_USD, defaults):
        self.deposits_made_with_offer_USD = 0	
        self.less_pro_ration_of_rents_USD = 0	
        self.cash_required_to_close_USD = cash_required_to_close_USD - self.deposits_made_with_offer_USD 
        self.total_cash_required_USD = cash_required_to_close_USD - self.less_pro_ration_of_rents_USD

class Financing:
    def __init__(self, offer_price_USD, real_purchase_price_USD, defaults):
        self.offer_price_USD = offer_price_USD
        self.real_purchase_price_USD = real_purchase_price_USD


        self.first_mtg_principle_borrowed_USD = defaults["financing"]["firstMtgPrincipleAmount"]
        self.first_mtg_interest_rate_percent = defaults["financing"]["firstMtgInterestRate"]
        self.first_mtg_amortization_period_years = defaults["financing"]["firstMtgAmortizationPeriod"]
        self.first_mtg_CHMC_fee_percent = defaults["financing"]["firstMtgCMHCFee"]
        self.first_mtg_total_principle_USD = self.first_mtg_principle_borrowed_USD*(1 + (self.first_mtg_CHMC_fee_percent/100))
        self.first_mtg_monthly_payment_USD = self.first_mtg_total_principle_USD*((((1+(self.first_mtg_interest_rate_percent/200))**(1/6))-1)/(1-(((1+(self.first_mtg_interest_rate_percent/200))**(1/6))**(self.first_mtg_amortization_period_years*-12))))

        self.second_mtg_principle_borrowed_USD = defaults["financing"]["secondMtgPrincipleAmount"]
        self.second_mtg_interest_rate_percent = defaults["financing"]["secondMtgInterestRate"]
        self.second_mtg_amortization_period_years = defaults["financing"]["secondMtgAmortizationPeriod"]
        self.second_mtg_monthly_payment_USD = self.second_mtg_principle_borrowed_USD*((((1+(self.second_mtg_interest_rate_percent/200))**(1/6))-1)/(1-(((1+(self.second_mtg_interest_rate_percent/200))**(1/6))**(self.second_mtg_amortization_period_years*-12))))

        self.interest_only_principle_amount_USD = 0
        self.interest_only_interest_rate_percent = 0
        self.interest_only_total_monthly_payment_USD = self.interest_only_principle_amount_USD*self.interest_only_interest_rate_percent / 1200

        self.other_monthly_financing_costs_USD = 350
        self.cash_required_to_close_USD = self.real_purchase_price_USD - self.first_mtg_principle_borrowed_USD - self.second_mtg_principle_borrowed_USD - self.interest_only_principle_amount_USD

class OperatingExpenses:
    def __init__(self, property_tax_USD, insurance_USD, annual_rent_USD, management_rate_percent, units, advertising_cost_per_vacancy_USD, vacancy_rate_percent, defaults):
        #storing arguments

        self.repairs_percent = defaults["operating"]["repairsRate"]
        self.management_rate_percent = management_rate_percent
        self.annual_rent_USD = annual_rent_USD
        self.units = units
        self.advertising_cost_per_vacancy_USD = advertising_cost_per_vacancy_USD
        self.vacancy_rate_percent = vacancy_rate_percent

        #individual elements of operating expenses
        self.property_tax_USD = property_tax_USD
        self.insurance_USD =  insurance_USD
        self.repairs_USD = self.repairs_percent * annual_rent_USD / 100
        self.electricity_USD = defaults["operating"]["electricity"]
        self.gas_USD = defaults["operating"]["gas"]
        self.lawn_snow_maintenance_USD = defaults["operating"]["lawn"]
        self.water_sewer_USD = defaults["operating"]["water"]
        self.cable_USD = defaults["operating"]["cable"]
        self.management_USD = self.management_rate_percent * self.annual_rent_USD / 100
        self.caretaking_USD = defaults["operating"]["caretaking"]
        self.advertizing_USD = 12 * self.units * self.vacancy_rate_percent * self.advertising_cost_per_vacancy_USD / 200  
        self.association_fees_USD = defaults["operating"]["associationFees"]
        self.pest_control_USD = self.units*140 if self.units < 2 else self.units * 70
        self.security_USD = (self.vacancy_rate_percent/ 100) * self.units * 12 /1.5 * 50
        self.trash_removal_USD = defaults["operating"]["trashRemoval"]
        self.misc_USD = defaults["operating"]["miscellaneous"]
        self.common_area_maintenance_USD = defaults["operating"]["commonAreaMaintenance"] 
        self.capital_improvements_USD = defaults["operating"]["capitalImprovements"] 
        self.accounting_USD = defaults["operating"]["accounting"] 
        self.legal_USD = defaults["operating"]["legal"]
        self.bad_debts_USD = defaults["operating"]["badDebts"] 
        self.other_USD = defaults["operating"]["other"] 
        self.evictions_USD = (((units * 12 * vacancy_rate_percent/100)/2)/10)*1000

        self.total_expenses_USD = (
            self.property_tax_USD +
            self.insurance_USD +
            self.repairs_USD +
            self.electricity_USD + 
            self.gas_USD +
            self.lawn_snow_maintenance_USD +
            self.water_sewer_USD +
            self.cable_USD +
            self.management_USD +
            self.caretaking_USD +
            self.advertizing_USD +
            self.association_fees_USD +
            self.pest_control_USD +
            self.security_USD +
            self.trash_removal_USD +
            self.misc_USD +
            self.common_area_maintenance_USD +
            self.capital_improvements_USD +
            self.accounting_USD +	
            self.legal_USD +	
            self.bad_debts_USD +
            self.other_USD +
            self.evictions_USD
        )

class PropertyInfo:
    def __init__(self, offer_price_USD, units, defaults):
        self.fair_market_value_USD = offer_price_USD
        self.vacancy_rate_percent = defaults["propertyInfo"]["vacancyRate"]
        self.management_rate_percent = defaults["propertyInfo"]["managementRate"]
        self.advertising_cost_per_vacancy_USD = defaults["propertyInfo"]["advertizingCost"]
        self.num_of_units = units
        self.annual_appreciation_rate_percent = defaults["propertyInfo"]["annualAppreciationRate"]

class PurchaseInfo:
    def __init__(self, offer_price_USD, defaults):

        self.offer_price_USD = offer_price_USD
        self.repairs_USD = defaults["purchaseInfo"]["repairs"]
        self.repairs_contingency_USD = defaults["purchaseInfo"]["repairsContingency"]
        self.lender_fee_USD = defaults["purchaseInfo"]["lenderFee"]
        self.broker_fee_USD = -1 * defaults["purchaseInfo"]["brokerFee"]
        self.environmentals_USD = defaults["purchaseInfo"]["environmentals"]
        self.inspections_USD = defaults["purchaseInfo"]["inspections"]
        self.appraisals_USD = defaults["purchaseInfo"]["appraisals"]
        self.misc_USD = defaults["purchaseInfo"]["misc"]
        self.transfer_tax_USD = defaults["purchaseInfo"]["transferTax"]
        self.legal_USD = defaults["purchaseInfo"]["legal"]

        self.real_purchase_price_USD = (
            self.offer_price_USD + 
            self.repairs_USD + 
            self.repairs_contingency_USD + 
            self.lender_fee_USD + 
            self.broker_fee_USD + 
            self.environmentals_USD + 
            self.inspections_USD + 
            self.appraisals_USD +
            self.misc_USD + 
            self.transfer_tax_USD + 
            self.legal_USD
        )

class IncomeInfo:
    def __init__(self, annual_rent_USD, defaults):

        self.annual_rent_USD = defaults["incomeInfo"]["grossRents"]
        self.parking_USD = defaults["incomeInfo"]["parking"]
        self.storage_USD = defaults["incomeInfo"]["storage"]
        self.laundry_USD = defaults["incomeInfo"]["laundry"]
        self.other_USD = defaults["incomeInfo"]["other"]
        self.total_income_USD = (
            self.annual_rent_USD + self.parking_USD + self.storage_USD
            + self.laundry_USD + self.other_USD
        )
        self.vacancy_rate_percent = 5
        self.vacancy_loss_USD = (
            self.total_income_USD * self.vacancy_rate_percent / 100
        )
        self.effective_income_USD = self.total_income_USD - self.vacancy_loss_USD



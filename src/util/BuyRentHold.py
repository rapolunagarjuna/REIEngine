class BuyRentHold:
    def __init__(self, offer_price_USD, units, annual_rent_USD, insurance_USD, property_tax_USD):
        # if offer_price_USD is None or units is None or annual_rent_USD is None:
        #     raise Exception("Arguments are missing")
        # print(type(offer_price_USD))
        # if (not isinstance(offer_price_USD, float) )or (not isinstance(offer_price_USD, int)):
        #     raise Exception("Offer price is not a float/ integer")
        # if not isinstance(units, int):
        #     raise Exception("Units are not an integer")
        
        self.property_info = PropertyInfo(offer_price_USD, units)
        self.purchase_info = PurchaseInfo(offer_price_USD)
        self.income_info = IncomeInfo(annual_rent_USD)
        self.operating_expenses = OperatingExpenses(
            property_tax_USD, 
            insurance_USD, 
            annual_rent_USD, 
            self.property_info.management_rate_percent,
            self.property_info.num_of_units, 
            self.property_info.advertising_cost_per_vacancy_USD, 
            self.property_info.vacancy_rate_percent
            )
        self.financing = Financing(offer_price_USD, self.purchase_info.real_purchase_price_USD)
        self.cash_requirements = CashRequirements(self.financing.cash_required_to_close_USD)


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
    def __init__(self, cash_required_to_close_USD):
        self.deposits_made_with_offer_USD = 0	
        self.less_pro_ration_of_rents_USD = 0	
        self.cash_required_to_close_USD = cash_required_to_close_USD - self.deposits_made_with_offer_USD 
        self.total_cash_required_USD = cash_required_to_close_USD - self.less_pro_ration_of_rents_USD
        

class Financing:
    def __init__(self, offer_price_USD, real_purchase_price_USD):
        self.offer_price_USD = offer_price_USD
        self.real_purchase_price_USD = real_purchase_price_USD


        self.first_mtg_principle_borrowed_USD = offer_price_USD*0.95 
        self.first_mtg_interest_rate_percent = 8
        self.first_mtg_amortization_period_years = 30
        self.first_mtg_CHMC_fee_percent = 0
        self.first_mtg_total_principle_USD = self.first_mtg_principle_borrowed_USD*(1 + (self.first_mtg_CHMC_fee_percent/100))
        self.first_mtg_monthly_payment_USD = self.first_mtg_total_principle_USD*((((1+(self.first_mtg_interest_rate_percent/200))**(1/6))-1)/(1-(((1+(self.first_mtg_interest_rate_percent/200))**(1/6))**(self.first_mtg_amortization_period_years*-12))))

        self.second_mtg_principle_borrowed_USD = 0
        self.second_mtg_interest_rate_percent = 12
        self.second_mtg_amortization_period_years = 99999
        self.second_mtg_monthly_payment_USD = self.second_mtg_principle_borrowed_USD*((((1+(self.second_mtg_interest_rate_percent/200))**(1/6))-1)/(1-(((1+(self.second_mtg_interest_rate_percent/200))**(1/6))**(self.second_mtg_amortization_period_years*-12))))

        self.interest_only_principle_amount_USD = 0
        self.interest_only_interest_rate_percent = 0
        self.interest_only_total_monthly_payment_USD = self.interest_only_principle_amount_USD*self.interest_only_interest_rate_percent / 1200

        self.other_monthly_financing_costs_USD = 350
        self.cash_required_to_close_USD = self.real_purchase_price_USD - self.first_mtg_principle_borrowed_USD - self.second_mtg_principle_borrowed_USD - self.interest_only_principle_amount_USD





class OperatingExpenses:
    def __init__(self, property_tax_USD, insurance_USD, annual_rent_USD, management_rate_percent, units, advertising_cost_per_vacancy_USD, vacancy_rate_percent,  repairs_percent = 5):
        #storing arguments
        self.repairs_percent = repairs_percent
        self.management_rate_percent = management_rate_percent
        self.annual_rent_USD = annual_rent_USD
        self.units = units
        self.advertising_cost_per_vacancy_USD = advertising_cost_per_vacancy_USD
        self.vacancy_rate_percent = vacancy_rate_percent

        #individual elements of operating expenses
        self.property_tax_USD = property_tax_USD
        self.insurance_USD =  insurance_USD
        self.repairs_USD = self.repairs_percent * annual_rent_USD / 100
        self.electricity_USD = 0   
        self.gas_USD = 0
        self.lawn_snow_maintenance_USD = 0
        self.water_sewer_USD = 1200
        self.cable_USD = 1200
        self.management_USD = self.management_rate_percent * self.annual_rent_USD / 100
        self.caretaking_USD = 2880
        self.advertizing_USD = 12 * self.units * self.vacancy_rate_percent * self.advertising_cost_per_vacancy_USD / 200  
        self.association_fees_USD = 0
        self.pest_control_USD = self.units*140 if self.units < 2 else self.units * 70
        self.security_USD = (self.vacancy_rate_percent/ 100) * self.units * 12 * 50 / 1.5
        self.trash_removal_USD = 0
        self.misc_USD = 0
        self.common_area_maintenance_USD = 0   
        self.capital_improvements_USD = 0   
        self.accounting_USD = 0		
        self.legal_USD = 0		
        self.bad_debts_USD = 0
        self.other_USD = 0	
        self.evictions_USD = 180

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
    def __init__(self, offer_price_USD, units, vacancy_rate_percent = 5, management_rate_percent = 5, advertising_cost_per_vacancy_USD = 100, annual_appreciation_rate_percent = 3):
        self.fair_market_value_USD = offer_price_USD
        self.vacancy_rate_percent = vacancy_rate_percent
        self.management_rate_percent = management_rate_percent
        self.advertising_cost_per_vacancy_USD = advertising_cost_per_vacancy_USD
        self.num_of_units = units
        self.annual_appreciation_rate_percent = annual_appreciation_rate_percent


class PurchaseInfo:
    def __init__(self, offer_price_USD, repairs_USD = 5000, repairs_contingency_USD = 1000, lender_fee_USD = 1500, broker_fee_USD = -5000, environmentals_USD = 0, inspections_USD = 700, appraisals_USD = 700, misc_USD = 500, transfer_tax_USD = 0, legal_USD = 500):
        self.offer_price_USD = offer_price_USD
        self.repairs_USD = repairs_USD
        self.repairs_contingency_USD = repairs_contingency_USD
        self.lender_fee_USD = lender_fee_USD
        self.broker_fee_USD = broker_fee_USD
        self.environmentals_USD = environmentals_USD
        self.inspections_USD = inspections_USD
        self.appraisals_USD = appraisals_USD
        self.misc_USD = misc_USD
        self.transfer_tax_USD = transfer_tax_USD
        self.legal_USD = legal_USD

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
    def __init__(self, annual_rent_USD, parking_USD = 0, storage_USD = 0, laundry_USD = 0, other_USD = 0):

        self.annual_rent_USD = annual_rent_USD
        self.parking_USD = parking_USD
        self.storage_USD = storage_USD
        self.laundry_USD = laundry_USD
        self.other_USD = other_USD
        self.total_income_USD = (
            self.annual_rent_USD + self.parking_USD + self.storage_USD
            + self.laundry_USD + self.other_USD
        )
        self.vacancy_rate_percent = 5
        self.vacancy_loss_USD = (
            self.total_income_USD * self.vacancy_rate_percent / 100
        )
        self.effective_income_USD = self.total_income_USD - self.vacancy_loss_USD



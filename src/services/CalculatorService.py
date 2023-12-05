from src.services.PropertyService import PropertyService
from src.util.BuyRentHold import BuyRentHold
from src.services.PropertyRentEstimateService import PropertyRentEstimateService


class CalculatorService:

    @staticmethod
    def getCalculator(params):
        response = PropertyService.getPropertyDetails(params)
        
        if not hasattr(response, 'success'):

            offer_price = response['data']['home']['list_price']
            units = response['data']['home']['description']['units']
            insurance_rate = response['data']['home']['mortgage']['insurance_rate']
            property_tax_rate = response['data']['home']['mortgage']['property_tax_rate']

            address = response['data']['home']['location']['address']['line'] + ", " + response['data']['home']['location']['address']['city'] + \
                ", " + response['data']['home']['location']['address']['state'] + \
                ", " + response['data']['home']['location']['address']['postal_code']
            
            bedrooms = response['data']['home']['description']['beds']
            bathrooms = response['data']['home']['description']['baths']
            propertyType = response['data']['home']['description']['type']
            squareFootage = response['data']['home']['description']["sqft"]
            compCount = 15
            
            rental_reponse_call = PropertyRentEstimateService.getPropertyRentEstimate(
                address, propertyType, bedrooms, bathrooms, squareFootage, compCount)
            print(rental_reponse_call)
            # some problem with the rental estimation api call
            if hasattr(rental_reponse_call, 'success'):
                return rental_reponse_call
            
            print(rental_reponse_call)
            annual_rent = rental_reponse_call['rent'] * 12
            insurance = offer_price * insurance_rate
            property_tax = offer_price * property_tax_rate

            defaults = {
                "propertyInfo": {
                    "vacancyRate": 5,
                    "managementRate": 5,
                    "advertizingCost": 100,
                    "annualAppreciationRate": 3,
                },
                "purchaseInfo": {
                    "repairs": 5000,
                    "repairsContingency": 1000,
                    "lenderFee": 1500,
                    "brokerFee": 5000,
                    "environmentals":0,
                    "inspections": 700,
                    "appraisals": 700,
                    "misc": 500,
                    "transferTax": 0,
                    "legal": 500,
                },
                "incomeInfo": {
                    "grossRents": 58800,
                    "parking": 0,
                    "storage": 0,
                    "laundry": 0,
                    "other": 0,
                },
                "financing": {
                    "firstMtgPrincipleAmount": 355300,
                    "firstMtgInterestRate": 8,
                    "firstMtgAmortizationPeriod": 30,
                    "firstMtgCMHCFee": 0,
                    "secondMtgPrincipleAmount": 0,
                    "secondMtgInterestRate": 12,
                    "secondMtgAmortizationPeriod": 9999,
                },
                "operating": {
                    "repairsRate": 5,
                    "electricity":0,
                    "gas": 0,
                    "lawn": 0,
                    "water": 1200,
                    "cable": 1200,
                    "caretaking": 2880,
                    "associationFees": 0,
                    "trashRemoval": 0,
                    "miscellaneous": 0,
                    "commonAreaMaintenance": 0,
                    "capitalImprovements":0,
                    "accounting": 0,
                    "legal": 0,
                    "badDebts": 0,
                    "other": 0,
                }
            }


            defaults["incomeInfo"]["grossRents"] = annual_rent
            defaults["financing"]["firstMtgPrincipleAmount"] = offer_price * 0.95

            summary = BuyRentHold(offer_price, units,
                                 insurance, property_tax, defaults)
            
            response = {
                "Expense to Income Ratio %" : summary.expense_to_income_ratio, 
                "Total Expenses $" : summary.operating_expenses.total_expenses_USD, 
                "Total Monthly Profit or Loss $" : summary.monthly_profit_USD ,
                "Cashflow per Unit per Month $" : summary.cashflow_per_unit_per_month_USD ,
                "Net Operating Income $" : summary.net_operating_income_USD,
                "Effective Gross Income	$" : summary.income_info.effective_income_USD ,
                "Real Purchase Price (RPP) $" : summary.purchase_info.real_purchase_price_USD,
                "Cash Required to Close (After Financing) $": summary.financing.cash_required_to_close_USD,
                "Total Cash Required $" : summary.cash_requirements.total_cash_required_USD ,
                "Cash on Cash ROI %" : summary.cash_on_cash_ROI_percent,
                "Equity ROI (After 1 Year) %" : summary.equity_ROI_percent ,
                "Appreciation ROI (After 1 Year) %"	: summary.appreciation_ROI_percent,
                "Debt servicing costs $": summary.debt_servicing_cost_USD,
                "Annual Profit $": summary.annual_profit_USD,

                "defaults": defaults
            }

        return response

    @staticmethod
    def getTrial(params):
        response = PropertyService.getPropertyDetails(params)
        defaults = {
                "propertyInfo": {
                    "vacancyRate": 5,
                    "managementRate": 5,
                    "advertizingCost": 100,
                    "annualAppreciationRate": 3,
                },
                "purchaseInfo": {
                    "repairs": 5000,
                    "repairsContingency": 1000,
                    "lenderFee": 1500,
                    "brokerFee": 5000,
                    "environmentals":0,
                    "inspections": 700,
                    "appraisals": 700,
                    "misc": 500,
                    "transferTax": 0,
                    "legal": 500,
                },
                "incomeInfo": {
                    "grossRents": 58800,
                    "parking": 0,
                    "storage": 0,
                    "laundry": 0,
                    "other": 0,
                },
                "financing": {
                    "firstMtgPrincipleAmount": 355300,
                    "firstMtgInterestRate": 8,
                    "firstMtgAmortizationPeriod": 30,
                    "firstMtgCMHCFee": 0,
                    "secondMtgPrincipleAmount": 0,
                    "secondMtgInterestRate": 12,
                    "secondMtgAmortizationPeriod": 9999,
                },
                "operating": {
                    "repairsRate": 5,
                    "electricity":0,
                    "gas": 0,
                    "lawn": 0,
                    "water": 1200,
                    "cable": 1200,
                    "caretaking": 2880,
                    "associationFees": 0,
                    "trashRemoval": 0,
                    "miscellaneous": 0,
                    "commonAreaMaintenance": 0,
                    "capitalImprovements":0,
                    "accounting": 0,
                    "legal": 0,
                    "badDebts": 0,
                    "other": 0,
                }
            }
        
        defaults["financing"]["firstMtgPrincipleAmount"] = 374000 * 0.95

        if not hasattr(response, 'success'):
            summary = BuyRentHold(374000, 6, 1800, 5400, defaults)
            
            response = {
                "Expense to Income Ratio %" : summary.expense_to_income_ratio, 
                "Total Expenses $" : summary.operating_expenses.total_expenses_USD, 
                "Total Monthly Profit or Loss $" : summary.monthly_profit_USD ,
                "Cashflow per Unit per Month $" : summary.cashflow_per_unit_per_month_USD ,
                "Net Operating Income $" : summary.net_operating_income_USD,
                "Effective Gross Income	$" : summary.income_info.effective_income_USD ,
                "Real Purchase Price (RPP) $" : summary.purchase_info.real_purchase_price_USD,
                "Cash Required to Close (After Financing) $": summary.financing.cash_required_to_close_USD,
                "Total Cash Required $" : summary.cash_requirements.total_cash_required_USD ,
                "Cash on Cash ROI %" : summary.cash_on_cash_ROI_percent,
                "Equity ROI (After 1 Year) %" : summary.equity_ROI_percent ,
                "Appreciation ROI (After 1 Year) %"	: summary.appreciation_ROI_percent,
                "Debt servicing costs $": summary.debt_servicing_cost_USD,
                "Annual Profit $": summary.annual_profit_USD,
                "defaults": defaults,
            }

        return response


    @staticmethod
    def setCalculator(params , defaults):
        response = PropertyService.getPropertyDetails(params)

        if not hasattr(response, 'success'):

            offer_price = response['data']['home']['list_price']
            units = response['data']['home']['description']['units']
            insurance_rate = response['data']['home']['mortgage']['insurance_rate']
            property_tax_rate = response['data']['home']['mortgage']['property_tax_rate']

            address = response['data']['home']['location']['address']['line'] + ", " + response['data']['home']['location']['address']['city'] + \
                ", " + response['data']['home']['location']['address']['state'] + \
                ", " + response['data']['home']['location']['address']['postal_code']
            
            bedrooms = response['data']['home']['description']['beds']
            bathrooms = response['data']['home']['description']['baths']
            propertyType = response['data']['home']['description']['type']
            squareFootage = response['data']['home']['description']["sqft"]
            compCount = 15
            
            # rental_reponse_call = PropertyRentEstimateService.getPropertyRentEstimate(
            #     address, propertyType, bedrooms, bathrooms, squareFootage, compCount)
            
            # # some problem with the rental estimation api call
            # if hasattr(rental_reponse_call, 'success'):
            #     return rental_reponse_call
            
            
            # annual_rent = rental_reponse_call['rent'] * 12
            insurance = offer_price * insurance_rate
            property_tax = offer_price * property_tax_rate

            summary = BuyRentHold(offer_price, units,
                                  insurance, property_tax, defaults)
            
            response = {
                "Expense to Income Ratio %" : summary.expense_to_income_ratio, 
                "Total Expenses $" : summary.operating_expenses.total_expenses_USD, 
                "Total Monthly Profit or Loss $" : summary.monthly_profit_USD ,
                "Cashflow per Unit per Month $" : summary.cashflow_per_unit_per_month_USD ,
                "Net Operating Income $" : summary.net_operating_income_USD,
                "Effective Gross Income	$" : summary.income_info.effective_income_USD ,
                "Real Purchase Price (RPP) $" : summary.purchase_info.real_purchase_price_USD,
                "Cash Required to Close (After Financing) $": summary.financing.cash_required_to_close_USD,
                "Total Cash Required $" : summary.cash_requirements.total_cash_required_USD ,
                "Cash on Cash ROI %" : summary.cash_on_cash_ROI_percent,
                "Equity ROI (After 1 Year) %" : summary.equity_ROI_percent ,
                "Appreciation ROI (After 1 Year) %"	: summary.appreciation_ROI_percent,
                "Debt servicing costs $": summary.debt_servicing_cost_USD,
                "Annual Profit $": summary.annual_profit_USD,

                "defaults": defaults
            }

        return response
    
    @staticmethod
    def get_Calculator_temporary(params, annual_rent):
        response = PropertyService.getPropertyDetails(params)
        
        if not hasattr(response, 'success'):

            offer_price = response['data']['home']['list_price']
            units = response['data']['home']['description']['units']
            insurance_rate = response['data']['home']['mortgage']['insurance_rate']
            property_tax_rate = response['data']['home']['mortgage']['property_tax_rate']
    

            insurance = offer_price * insurance_rate
            property_tax = offer_price * property_tax_rate

            defaults = {
                "propertyInfo": {
                    "vacancyRate": 5,
                    "managementRate": 5,
                    "advertizingCost": 100,
                    "annualAppreciationRate": 3,
                },
                "purchaseInfo": {
                    "repairs": 5000,
                    "repairsContingency": 1000,
                    "lenderFee": 1500,
                    "brokerFee": 5000,
                    "environmentals":0,
                    "inspections": 700,
                    "appraisals": 700,
                    "misc": 500,
                    "transferTax": 0,
                    "legal": 500,
                },
                "incomeInfo": {
                    "grossRents": 58800,
                    "parking": 0,
                    "storage": 0,
                    "laundry": 0,
                    "other": 0,
                },
                "financing": {
                    "firstMtgPrincipleAmount": 355300,
                    "firstMtgInterestRate": 8,
                    "firstMtgAmortizationPeriod": 30,
                    "firstMtgCMHCFee": 0,
                    "secondMtgPrincipleAmount": 0,
                    "secondMtgInterestRate": 12,
                    "secondMtgAmortizationPeriod": 9999,
                },
                "operating": {
                    "repairsRate": 5,
                    "electricity":0,
                    "gas": 0,
                    "lawn": 0,
                    "water": 1200,
                    "cable": 1200,
                    "caretaking": 2880,
                    "associationFees": 0,
                    "trashRemoval": 0,
                    "miscellaneous": 0,
                    "commonAreaMaintenance": 0,
                    "capitalImprovements":0,
                    "accounting": 0,
                    "legal": 0,
                    "badDebts": 0,
                    "other": 0,
                }
            }


            defaults["incomeInfo"]["grossRents"] = annual_rent
            defaults["financing"]["firstMtgPrincipleAmount"] = offer_price * 0.95

            summary = BuyRentHold(offer_price, units,
                                 insurance, property_tax, defaults)
            
            response = {
                "Expense to Income Ratio %" : summary.expense_to_income_ratio, 
                "Total Expenses $" : summary.operating_expenses.total_expenses_USD, 
                "Total Monthly Profit or Loss $" : summary.monthly_profit_USD ,
                "Cashflow per Unit per Month $" : summary.cashflow_per_unit_per_month_USD ,
                "Net Operating Income $" : summary.net_operating_income_USD,
                "Effective Gross Income	$" : summary.income_info.effective_income_USD ,
                "Real Purchase Price (RPP) $" : summary.purchase_info.real_purchase_price_USD,
                "Cash Required to Close (After Financing) $": summary.financing.cash_required_to_close_USD,
                "Total Cash Required $" : summary.cash_requirements.total_cash_required_USD ,
                "Cash on Cash ROI %" : summary.cash_on_cash_ROI_percent,
                "Equity ROI (After 1 Year) %" : summary.equity_ROI_percent ,
                "Appreciation ROI (After 1 Year) %"	: summary.appreciation_ROI_percent,
                "Debt servicing costs $": summary.debt_servicing_cost_USD,
                "Annual Profit $": summary.annual_profit_USD,

                "defaults": defaults
            }

        return response

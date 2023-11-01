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
            
            # some problem with the rental estimation api call
            if hasattr(rental_reponse_call, 'success'):
                return rental_reponse_call
            
            
            annual_rent = rental_reponse_call['rent'] * 12
            insurance = offer_price * insurance_rate
            property_tax = offer_price * property_tax_rate

            summary = BuyRentHold(offer_price, units,
                                  annual_rent, insurance, property_tax)
            
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
            }

        return response

    @staticmethod
    def getTrial(params):
        response = PropertyService.getPropertyDetails(params)
        if not hasattr(response, 'success'):
            summary = BuyRentHold(374000, 6, 58800, 1800, 5400)
            
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
            }

        return response

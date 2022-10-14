from fiscalsim_us.model_api import *


class va_age_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA age deduction https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2021-760-instructions.pdf for information"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA


    def formula(tax_unit,period,parameters):


        age_of_head = tax_unit("age_head", period)

        age_of_spouse = tax_unit("age_spouse", period)

        filing_status = tax_unit("filing_status", period)

        federal_agi = tax_unit("adjusted_gross_income", period)

        spouse_agi = tax_unit("spouse_separate_adjusted_gross_income", period)


        if age_of_head > 65: 

            if filing_status == 1:

                age_deduction_count = 1

            if filing_status == 2 & age_of_spouse > 65: 

                age_deduction_count = 2

        
        if filing_status == 1: 

            total_agi = federal_agi 

        else:

            total_agi


                




            





        
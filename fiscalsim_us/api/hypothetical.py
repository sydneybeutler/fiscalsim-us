from openfisca_tools import IndividualSim as GeneralIndividualSim
from fiscalsim_us import CountryTaxBenefitSystem
from fiscalsim_us.entities import entities
from fiscalsim_us.data import CPS


class IndividualSim(GeneralIndividualSim):
    tax_benefit_system = CountryTaxBenefitSystem
    entities = {entity.key: entity for entity in entities}
    default_dataset = CPS

    default_roles = dict(
        tax_unit="member",
        spm_unit="member",
        household="member",
        family="member",
    )
    required_entities = [
        "tax_unit",
        "spm_unit",
        "household",
        "family",
    ]
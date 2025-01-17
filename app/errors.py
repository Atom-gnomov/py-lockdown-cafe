class VaccineError(Exception):
    def __str__(self) -> str:
        return "Access denied: Visitor is not vaccinated."


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Access denied: Visitor do not have mask"

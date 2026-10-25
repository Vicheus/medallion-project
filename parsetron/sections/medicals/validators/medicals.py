from typing import Optional, Dict, Union
from .date_injury import validate_date_injury
from .date_hospital import validate_date_hospital
from .date_evacuation import validate_date_evacuation
from .severity import validate_severity
from parsetron.sections.base.validators.base import base_validation


def medicals(
    diagnosis: str = None,
    date_injury: str = None,
    place_injury: str = None,
    date_hospital: str = None,
    severity: int = None,
    medical_org: str = None,
    evacuation_route: str = None,
    date_evacuation: str = None,
    primary_documents: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    diagnosis = base_validation(diagnosis)
    date_injury = validate_date_injury(date_injury, date_format)
    place_injury = base_validation(place_injury)
    date_hospital = validate_date_hospital(date_hospital, date_format)
    severity = validate_severity(severity)
    medical_org = base_validation(medical_org)
    evacuation_route = base_validation(evacuation_route)
    date_evacuation = validate_date_evacuation(date_evacuation, date_format)
    primary_documents = base_validation(primary_documents)
    comment = base_validation(comment)

    return {
        "diagnosis": diagnosis,
        "date_injury": date_injury,
        "place_injury": place_injury,
        "date_hospital": date_hospital,
        "severity": severity,
        "medical_org": medical_org,
        "evacuation_route": evacuation_route,
        "date_evacuation": date_evacuation,
        "primary_documents": primary_documents,
    }

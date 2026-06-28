import re
import spacy

# Load spaCy model only once
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):

    doc = nlp(text)

    entities = {
        "equipment": [],
        "components": [],
        "failures": [],
        "procedures": [],
        "locations": [],
        "engineers": [],
        "dates": [],
        "organizations": [],
        "measurements": [],
        "standards": [],
        "risk_levels": [],
        "materials": [],
        "chemicals": [],
        "keywords": []
    
    }

    # -----------------------
    # spaCy Named Entities
    # -----------------------

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            entities["engineers"].append(ent.text)

        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)

        elif ent.label_ == "LOC":
            entities["locations"].append(ent.text)

        elif ent.label_ == "DATE":
            entities["dates"].append(ent.text)

        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)

    # -----------------------
    # Equipment Detection
    # -----------------------

    equipment_pattern = (
        r"\b(?:Pump|Motor|Valve|Pipe|Tank|Boiler|Generator|Compressor|Turbine)"
        r"\s*[A-Z]?\d+\b"
    )

    equipments = re.findall(equipment_pattern, text)

    entities["equipment"].extend(equipments)

    # -----------------------
    # Component Detection
    # -----------------------

    component_keywords = [
        "bearing",
        "valve",
        "motor",
        "shaft",
        "gear",
        "compressor",
        "pump",
        "turbine",
        "pipe",
        "sensor"
    ]

    lower_text = text.lower()

    for component in component_keywords:

        if component in lower_text:

            entities["components"].append(component.title())

    # -----------------------
    # Failure Detection
    # -----------------------

    failure_keywords = [
        "failure",
        "crack",
        "leak",
        "wear",
        "overheating",
        "corrosion",
        "damage",
        "fault"
    ]

    for failure in failure_keywords:

        if failure in lower_text:

            entities["failures"].append(failure.title())

    # -----------------------
    # Procedure Detection
    # -----------------------

    procedure_keywords = [
        "maintenance",
        "inspection",
        "replacement",
        "installation",
        "shutdown",
        "startup",
        "repair"
    ]

    for procedure in procedure_keywords:

        if procedure in lower_text:

            entities["procedures"].append(procedure.title())


    # -----------------------
    # Measurement Detection
    # -----------------------

    measurement_pattern = (
        r"\b\d+(?:\.\d+)?\s?"
        r"(?:°C|°F|psi|bar|rpm|RPM|V|kV|A|mA|Hz|kHz|kg|g|mg|mm|cm|m|km|L|ml|%)\b"
    )

    measurements = re.findall(
        measurement_pattern,
        text
    )

    entities["measurements"].extend(measurements)


    # -----------------------
    # Standards Detection
    # -----------------------

    standard_pattern = (
        r"\b(?:ISO|IEC|API|ASME|ASTM|ANSI|IEEE|NFPA)"
        r"\s?[A-Za-z0-9.\-]+\b"
    )

    standards = re.findall(
        standard_pattern,
        text
    )

    entities["standards"].extend(standards)


    # -----------------------
    # Risk Level Detection
    # -----------------------

    risk_keywords = [

        "high",
        "medium",
        "low",
        "critical",
        "warning",
        "hazard",
        "emergency",
        "severe"

    ]

    for risk in risk_keywords:

        if risk in lower_text:

            entities["risk_levels"].append(
                risk.title()
            )


    # -----------------------
    # Keyword Extraction
    # -----------------------

    for token in doc:

        if (
            token.is_alpha
            and not token.is_stop
            and not token.is_punct
            and len(token.text) > 2
        ):

            entities["keywords"].append(
                token.lemma_.title()
            )

    # Remove duplicates

    for key in entities:

        entities[key] = list(set(entities[key]))

    return entities
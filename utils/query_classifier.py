def is_maintenance_query(query):

    query = query.lower()

    maintenance_keywords = [

        "maintenance",

        "repair",

        "failure",

        "fault",

        "inspection",

        "breakdown",

        "overheating",

        "vibration",

        "bearing",

        "pump",

        "motor",

        "compressor",

        "valve",

        "shutdown",

        "lubrication"

    ]

    return any(
        keyword in query
        for keyword in maintenance_keywords
    )
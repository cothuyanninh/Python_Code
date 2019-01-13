DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    ]

list_code_country = {country : code for code, country in DIAL_CODES}
print(list_code_country)
print({code : country.upper() for country, code in list_code_country.items() if code < 66})

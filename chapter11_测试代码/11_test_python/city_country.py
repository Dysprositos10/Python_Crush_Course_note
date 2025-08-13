def citycountry(city,country,population=''):
    if population:
        city_full_name = f"{city},{country}-{population}"
    else:
        city_full_name = f"{city},{country}"
    return city_full_name
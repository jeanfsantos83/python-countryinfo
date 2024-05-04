from countryinfo import CountryInfo

country = CountryInfo(input('Enter the name of the country: '))

print(f'Country: {country.name()}')
print(f'Country Capital: {country.capital()}')
print(f'Currencies: {country.currencies}')
print(f'Languages: {country.languages()}')
print(f'Borders: {country.borders()}')
print(f'Calling Codes: {country.calling_codes()}')
print(f'Population: {country.population()}')
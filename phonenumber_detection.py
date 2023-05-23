
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import (region_code_for_country_code, region_code_for_number,)
import pycountry

print('X' * 70 )

entered_number = input('Enter your number with + country code : ')

pn = phonenumbers.parse(entered_number, None)
print(pn)

Region_Code = region_code_for_country_code(pn.country_code)
Country_name = pycountry.countries.get(alpha_2=region_code_for_number(pn))
Carrier_Name = carrier.name_for_number(pn, "en")
print(Region_Code + ',' + Country_name.name)
print(Carrier_Name)
# mobile_info_tracker.py

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_number(number):
    try:
        # Parse the number
        parsed_number = phonenumbers.parse(number)
        
        # Get region (country)
        region = geocoder.description_for_number(parsed_number, 'en')
        
        # Get carrier
        phone_carrier = carrier.name_for_number(parsed_number, 'en')
        
        # Get timezone
        phone_timezone = timezone.time_zones_for_number(parsed_number)
        
        # Display info
        print(f"Number: {number}")
        print(f"Region: {region}")
        print(f"Carrier: {phone_carrier}")
        print(f"Timezone(s): {phone_timezone}")
        
    except phonenumbers.NumberParseException:
        print("Invalid phone number!")

if __name__ == "__main__":
    number = input("Enter mobile number with country code (e.g., +14155552671): ")
    track_number(number)

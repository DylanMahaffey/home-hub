from ..models.business_models import BusinessProfile, Address, BusinessHours

# This method is currently returning mock data. 
# Will eventually webscrape to get the data
def get_business_locations(query: str, zip: str):
    return [
        get_mock_business(query, zip)
    ]
    
def get_mock_business(query, zip):
    mock_business = BusinessProfile()
    mock_business._id = "123456"
    mock_business.name = query
    mock_business.yellow_pages_url = "https://www.yellowpages.com/fresno-ca/mip/costco-768540"
    mock_business.url = "https://www.costco.com/warehouse-locations/fresno-CA-657.html"
    
    address = Address()
    address.street = "265 W. Menlo"
    address.city = "Fresno"
    address.state = "Ca"
    address.zip = zip
    mock_business.address = address
    
    hours = BusinessHours()
    hours.sunday = "11am - 8pm"
    hours.monday = "11am - 8pm"
    hours.tuesday = "11am - 8pm"
    hours.wednesday = "11am - 8pm"
    hours.thursday = "11am - 8pm"
    hours.friday = "11am - 8pm"
    hours.saturday = "11am - 8pm"
    mock_business.hours = hours
    
    return mock_business
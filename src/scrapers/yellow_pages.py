from ..models.business_models import BusinessProfile, Address, BusinessHours
from playwright.async_api import async_playwright

# This method is currently returning mock data. 
# Will eventually webscrape to get the data
async def get_business_locations(query: str, zip: str):
    async with async_playwright() as p:
        base_url = "https://www.yellowpages.com"
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"{base_url}/search?search_terms={query}&geo_location_terms={zip}")
        context = page.locator(".result")
        content = []
        for el in await context.all():
            b = BusinessProfile()
            b.ypid = await el.get_attribute("data-ypid")
            b.name = query
            b.yellow_pages_url = base_url + await el.locator("a.business-name").get_attribute("href")
            address = Address()
            address.street = await el.locator(".street-address").inner_text()
            local = await el.locator(".locality").inner_text()
            split = local.split(",")
            address.city = split[0]
            state_zip = split[1].split(" ")
            address.state = state_zip[1]
            address.zip = state_zip[2]
            b.address = address
            content.append(b)
            
        await browser.close()
        return content
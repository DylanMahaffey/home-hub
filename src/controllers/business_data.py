from playwright.async_api import async_playwright

class BusinessData:
    async def get_business_data():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto("http://playwright.dev")
            print(await page.title())
            await browser.close()
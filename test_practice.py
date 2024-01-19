from playwright.sync_api import Page, expect

class Test_playwright:
    def test_first(self,page:Page):
        page.goto("https://www.mystoriesmatter.com/")
        page.get_by_role("link", name="Login").click()
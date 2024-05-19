from base import BaseCase
from ui.pages.company_page import CompanyPage

class TestCompany(BaseCase):
    def test_chose_site_company_targer(self, company_page: CompanyPage):
        company_page.create_company()
        company_page.select_site_target()

        assert "Рекламируемый сайт" in company_page.driver.page_source
        
        company_page.clear_companies()

    def test_company_settings_no_region(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.create_company()
        company_page.select_site_target()
        company_page.fill_site_url('https://prinesy-poday.ru/')
        company_page.apply_target()
        company_page.apply_groups()
        company_page.assert_no_region_message()
        company_page.clear_companies()

    def test_interests(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.create_company()
        company_page.select_site_target()
        company_page.fill_site_url('https://prinesy-poday.ru/')
        company_page.apply_target()
        company_page.open_interests()
        company_page.assert_interests_dropdown()
        company_page.assert_interests_dropdown()

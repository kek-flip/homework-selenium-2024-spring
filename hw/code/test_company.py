import pytest
from base import BaseCase
from ui.pages.company_page import CompanyPage, CompanyTarget

@pytest.fixture()
def clear_companies(company_page: CompanyPage):
    yield
    company_page.clear_companies()

class TestCompany(BaseCase):
    def test_create_site_company(self, company_page: CompanyPage, clear_companies):
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)
        assert "Рекламируемый сайт" in company_page.driver.page_source

        site_url = 'https://prinesy-poday.ru/'

        company_page.set_site_url(site_url)
        assert site_url in company_page.driver.page_source
        assert 'Целевое действие' in company_page.driver.page_source
        assert 'Стратегия ставок' in company_page.driver.page_source
        assert 'Бюджет' in company_page.driver.page_source
        assert 'Дата проведения' in company_page.driver.page_source
        company_page.unfocus()
        company_page.apply_target()

        company_page.set_region()
        assert 'Россия' in company_page.driver.page_source
        company_page.apply_groups()

        ad_header = 'AD'
        ad_desc = 'DESC'

        company_page.set_ad_header(ad_header)
        company_page.set_ad_short_desc(ad_desc)
        assert ad_header in company_page.driver.page_source
        assert ad_desc in company_page.driver.page_source
        assert "1/30" in company_page.driver.page_source
        
        company_page.save_company()

        company_page.open_companies_list()
        company_page.open_companies_drafts()
        companies_drafts = company_page.get_companies_drafts()

        assert len(companies_drafts) == 1

    def test_company_settings_no_region(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)

        site_url = 'https://prinesy-poday.ru/'

        company_page.set_site_url(site_url)

        company_page.apply_target()
        company_page.apply_groups()

        assert company_page.is_no_region_message_visible()

    def test_interests_dropdown(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)

        site_url = 'https://prinesy-poday.ru/'

        company_page.set_site_url(site_url)
        company_page.apply_target()
        company_page.open_interests()
        assert company_page.is_interests_dropdown_visible()

    def test_ad_without_header_and_desc(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)

        site_url = 'https://prinesy-poday.ru/'

        company_page.set_site_url(site_url)
        company_page.apply_target()
        company_page.set_region()
        company_page.apply_groups()
        company_page.save_company()

        assert "Обязательное поле" in company_page.driver.page_source

    def test_create_catalog_company(self, company_page: CompanyPage, clear_companies):
            company_page.open_company_creation()
            company_page.select_target(CompanyTarget.CATALOG)
            assert "Сайт" in company_page.driver.page_source

            site_url = 'https://prinesy-poday.ru/'

            company_page.set_site_url(site_url)
            assert site_url in company_page.driver.page_source
            company_page.open_catalogs_dropdown()
            company_page.select_catalog("Каталог 2024-05-28")
            assert 'Целевое действие' in company_page.driver.page_source
            assert 'Стратегия ставок' in company_page.driver.page_source
            assert 'Бюджет' in company_page.driver.page_source
            assert 'Дата проведения' in company_page.driver.page_source
            company_page.unfocus()
            company_page.apply_target()

            company_page.set_region()
            assert 'Россия' in company_page.driver.page_source
            company_page.apply_groups()

            ad_header = 'AD'
            ad_desc = 'DESC'
            ad_carousel = 'CAROUSEL'
            ad_card = 'CARD'

            company_page.set_ad_header(ad_header)
            company_page.set_ad_short_desc(ad_desc)
            company_page.set_ad_carousel_desc(ad_carousel)
            company_page.set_ad_card_desc(ad_card)
            assert ad_header in company_page.driver.page_source
            assert ad_desc in company_page.driver.page_source
            assert ad_carousel in company_page.driver.page_source

            company_page.public_company()
            company_page.wait_for_company_load()

            assert 'Клики по рекламе' in company_page.driver.page_source
            assert 'Каталог товаров' in company_page.driver.page_source
    
    def test_create_public_company(self, company_page: CompanyPage, clear_companies):
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.PUBLIC)
        assert "Рекламируемый объект" in company_page.driver.page_source

        site_url = 'Артемий Лебедев'

        company_page.set_site_url(site_url)
        assert site_url in company_page.driver.page_source
        assert 'Целевое действие' in company_page.driver.page_source
        assert 'Стратегия ставок' in company_page.driver.page_source
        assert 'Бюджет' in company_page.driver.page_source
        assert 'Дата проведения' in company_page.driver.page_source
        company_page.unfocus()
        company_page.apply_target()

        company_page.set_region()
        assert 'Россия' in company_page.driver.page_source
        company_page.apply_groups()

        ad_header = 'AD'
        ad_desc = 'DESC'

        company_page.set_ad_header(ad_header)
        company_page.set_ad_short_desc(ad_desc)
        assert ad_header in company_page.driver.page_source
        assert ad_desc in company_page.driver.page_source

        company_page.public_company()
        company_page.wait_for_company_load()

        assert 'Подписка на сообщество' in company_page.driver.page_source
        assert 'Сообщество ВКонтакте' in company_page.driver.page_source
    
    def test_create_odkl_company(self, company_page: CompanyPage, clear_companies):
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.ODKL)
        assert "Рекламируемый объект" in company_page.driver.page_source

        site_url = 'O'

        company_page.set_site_url(site_url)
        assert site_url in company_page.driver.page_source
        assert 'Целевое действие' in company_page.driver.page_source
        assert 'Стратегия ставок' in company_page.driver.page_source
        assert 'Бюджет' in company_page.driver.page_source
        assert 'Дата проведения' in company_page.driver.page_source
        company_page.unfocus()
        company_page.apply_target()

        company_page.set_region()
        assert 'Россия' in company_page.driver.page_source
        company_page.apply_groups()

        ad_header = 'AD'
        ad_desc = 'DESC'

        company_page.set_ad_header(ad_header)
        company_page.set_ad_short_desc(ad_desc)
        assert ad_header in company_page.driver.page_source
        assert ad_desc in company_page.driver.page_source

        company_page.public_company()
        company_page.wait_for_company_load()

        assert 'Подписка на сообщество' in company_page.driver.page_source
        assert 'Одноклассники' in company_page.driver.page_source
    
    # def test_high_limit_price(self, company_page: CompanyPage, clear_companies):
    #     company_page.open_company_creation()
    #     company_page.select_target(CompanyTarget.PUBLIC)
    #     assert "Рекламируемый объект" in company_page.driver.page_source
        
    #     company_page.open_public_dropdown()
    #     company_page.open_public_another_btn()
    #     company_page.set_add_public_modal('temalebedev')
    #     company_page.click_add_public_btn()
    
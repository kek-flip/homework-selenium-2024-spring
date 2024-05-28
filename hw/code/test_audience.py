import pytest
from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource

@pytest.fixture()
def create_audiences(audience_page: AudiencePage, config):
    audience_page.open_audience_creation()

    audience_name = 'EXISTING_AUDIENCE'
    audience_page.set_audience_name(audience_name)
    audience_page.open_sources_list()
    audience_page.select_audience_source(AudienceSource.USERS_LIST)

    users_list_name = "USER LIST"
    users_list_type = "Email"
    users_list_path = config['users_list_path']

    audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
    audience_page.submit_audience_source()
    audience_page.wait_for_success_notify()
    audience_page.submit_audience_source()
    yield

@pytest.fixture()
def clear_audiences(audience_page: AudiencePage):
    yield
    audience_page.clear_audiences()

class TestAudience(BaseCase):
    def test_audience_from_users_list(self, audience_page: AudiencePage, clear_audiences):
        audience_page.open_audience_creation()

        audience_name = 'AUDIENCE'
        audience_page.set_audience_name(audience_name)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.USERS_LIST)

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config['users_list_path']

        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
        assert users_list_name in audience_page.driver.page_source
        assert users_list_type in audience_page.driver.page_source
        audience_page.submit_audience_source()
        audience_page.wait_for_success_notify()
        assert "Список пользователей" in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert audience_name in audiences

    def test_audience_from_existing_audience(self, audience_page: AudiencePage, create_audiences, clear_audiences):
        audience_page.open_audience_creation()

        audience_name = 'AUDIENCE'
        audience_page.set_audience_name(audience_name)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.EXISTING)
        
        audience_page.add_existing_audience("EXISTING_AUDIENCE")
        assert "EXISTING_AUDIENCE" in audience_page.driver.page_source
        audience_page.submit_audience_source()
        assert "Существующая аудитория" in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 2
        assert audience_name in audiences

    def test_audience_from_keywords(self, audience_page: AudiencePage, clear_audiences):
        audience_page.open_audience_creation()

        audience_name = 'AUDIENCE'
        audience_page.set_audience_name(audience_name)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.KEYWORDS)

        keywords_name = 'KEYWORDS'

        with open(self.config['keywords_path'], 'r') as keywords_file:
            with open(self.config['breakwords_path'], 'r') as breakwords_file:
                keywords = keywords_file.readlines()
                breakwords = breakwords_file.readlines()
                audience_page.add_key_words(keywords_name, keywords, breakwords)

                for keyword, breakword in zip(keywords, breakwords):
                    assert keyword in audience_page.driver.page_source
                    assert breakword in audience_page.driver.page_source
        
        audience_page.submit_audience_source()
        assert keywords_name in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert audience_name in audiences

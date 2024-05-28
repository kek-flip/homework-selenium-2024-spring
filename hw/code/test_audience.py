import pytest
from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource

@pytest.fixture()
def create_users_list(audience_page: AudiencePage, config):
    audience_page.open_users_list_list()
    audience_page.open_users_list_creation()

    users_list_name = "EXISTING USER LIST"
    users_list_type = "Email"
    users_list_path = config['users_list_path']

    audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
    audience_page.submit_users_list_creation()
    audience_page.wait_for_success_notify()

@pytest.fixture()
def clear_users_list(audience_page: AudiencePage):
    yield
    audience_page.clear_users_lists()

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
    audience_page.open_users_list_list()
    audience_page.clear_users_lists()

@pytest.fixture()
def clear_audiences(audience_page: AudiencePage):
    yield
    audience_page.open_audiences_list()
    audience_page.clear_audiences()

class TestAudience(BaseCase):
    def test_create_users_list(self, audience_page: AudiencePage, clear_users_list):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config['users_list_path']

        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
        assert users_list_name in audience_page.driver.page_source
        assert users_list_type in audience_page.driver.page_source
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        users_lists = audience_page.get_users_lists()
        assert len(users_lists) == 1
        assert users_list_name in users_lists

    def test_create_users_list_from_audience(self, audience_page: AudiencePage, clear_audiences, clear_users_list):
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
        audience_page.submit_audience_creation()

        audience_page.open_users_list_list()
        users_lists = audience_page.get_users_lists()
        assert len(users_lists) == 1
        assert users_list_name in users_lists

    def test_audience_from_uploading_users_list(self, audience_page: AudiencePage, clear_audiences, clear_users_list):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config['users_list_path']

        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
        audience_page.create_audience_from_list()
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        audience_page.open_audiences_list()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert f'[auto] Список пользователей / {users_list_name}' in audiences

    def test_audience_from_new_users_list(self, audience_page: AudiencePage, clear_audiences, clear_users_list):
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

    def test_audience_from_existing_users_list(self, audience_page: AudiencePage, create_users_list, clear_audiences):
        audience_page.open_audience_creation()

        audience_name = 'AUDIENCE'
        audience_page.set_audience_name(audience_name)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.USERS_LIST)

        audience_page.add_existing_users_list("EXISTING USER LIST")
        assert "EXISTING USER LIST" in audience_page.driver.page_source
        audience_page.submit_audience_source()
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

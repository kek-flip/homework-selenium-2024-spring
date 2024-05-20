from base import BaseCase
from ui.pages.user_lists_page import UserListsPage


class TestUserListsPage(BaseCase):
    WRONG_KEY = "888"
    SEARCH_TEXT = "реклама"

    def test_open_add_modal(self, user_lists_page: UserListsPage):
        user_lists_page.click_add_lists()
        assert user_lists_page.is_add_list_modal_visible()

    def test_load_invalid_id(self, user_lists_page: UserListsPage):
        user_lists_page.click_load_list()
        user_lists_page.click_activate_list()
        user_lists_page.fill_key(self.WRONG_KEY)
        user_lists_page.click_activate()
        assert user_lists_page.is_alert_visible()

    def test_search_nothing(self, user_lists_page: UserListsPage):
        user_lists_page.click_search()
        user_lists_page.fill_search(self.SEARCH_TEXT)
        assert user_lists_page.is_nothing_found_visible()

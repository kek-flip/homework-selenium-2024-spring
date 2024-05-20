import pytest
from base import UnauthorizedCase
from ui.pages.forum_page import ForumPage

idea_themes = [("Сайты", 5), ("Сообщества", 8)]

idea_statuses = [("Уже в работе", 12), ("Реализована", 7)]


class TestNewsPage(UnauthorizedCase):
    SEARCH_BY_TITLE = "реклама"
    SEARCH_BY_TITLE_IDEAS_COUNT = 3
    SEARCH_BY_ID = "3"
    SEARCH_BY_ID_IDEAS_COUNT = 1

    def test_ideas_search_by_title(self, forum_page: ForumPage):
        forum_page.fill_search(self.SEARCH_BY_TITLE)
        forum_page.wait_for_count_of_ideas(self.SEARCH_BY_TITLE_IDEAS_COUNT)
        assert forum_page.get_ideas_count() == self.SEARCH_BY_TITLE_IDEAS_COUNT

    def test_upvote_search_by_id(self, forum_page: ForumPage):
        forum_page.fill_search(self.SEARCH_BY_ID)
        forum_page.wait_for_count_of_ideas(self.SEARCH_BY_ID_IDEAS_COUNT)
        assert forum_page.get_ideas_count() == self.SEARCH_BY_ID_IDEAS_COUNT

    @pytest.mark.parametrize("theme_name,ideas_count", idea_themes)
    def test_upvote_select_theme(self, forum_page: ForumPage, theme_name: str, ideas_count: int):
        forum_page.select_idea_theme(theme_name)
        forum_page.wait_for_count_of_ideas(ideas_count)
        assert forum_page.get_ideas_count() == ideas_count

    @pytest.mark.parametrize("status_name,ideas_count", idea_statuses)
    def test_upvote_select_status(self, forum_page: ForumPage, status_name: str, ideas_count: int):
        forum_page.select_idea_status(status_name)
        forum_page.wait_for_count_of_ideas(ideas_count)
        assert forum_page.get_ideas_count() == ideas_count






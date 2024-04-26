from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage

import time
class TestCommerceCenter(BaseCase):
    def test_test(self, commerce_center_page: CommerceCenterPage):
        assert commerce_center_page.is_opened()

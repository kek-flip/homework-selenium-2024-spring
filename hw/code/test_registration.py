from base import NoCabinetCase
from ui.pages.registration_page import RegistrationPage
import pytest


class TestRegistration(NoCabinetCase):
    NO_FIELD_ERROR = 'Обязательное поле'
    MIN_LENGTH = 'Минимальная длина 12'
    MAX_LENGTH = 'Максимальная длина 12 символов'
    INVALID_EMAIL_ERROR = 'Некорректный email адрес'

    def test_go_to_create_cabinet(self, registration_page: RegistrationPage):
        registration_page.click_create()
        assert self.is_url_open('https://ads.vk.com/hq/registration/new')

    currency_test_args = [
        ('Беларусь', ('Доллар США (USD)', 'Евро (EUR)')),
        ('Россия', ('Российский рубль (RUB)',)),
    ]

    @pytest.mark.parametrize('country,currencies', currency_test_args)
    def test_currency_select(self, registration_page, country, currencies):
        registration_page.click_create()
        registration_page.select_country(country)
        assert registration_page.available_currencies_after_country_change(
            currencies[0]) == currencies

    def test_create_cabinet_without_email(self, registration_page: RegistrationPage):
        registration_page.click_create()
        registration_page.fill_in_form('')
        assert registration_page.email_error(self.NO_FIELD_ERROR) is not None

    def test_small_inn(self, registration_page: RegistrationPage):
        registration_page.click_create()
        registration_page.fill_inn("1234")
        registration_page.click_create_account()
        assert registration_page.inn_error(self.MIN_LENGTH) is not None

    def test_small_inn(self, registration_page: RegistrationPage):
        registration_page.click_create()
        registration_page.fill_inn("123456789101112131415")
        registration_page.click_create_account()
        assert registration_page.inn_error(self.MAX_LENGTH) is not None

    def test_no_terms(self, registration_page):
        example_mail = 'example@mail.ru'
        registration_page.click_create()
        registration_page.fill_in_form(example_mail, terms_accepted=False)
        assert registration_page.terms_not_accepted_error(self.NO_FIELD_ERROR) is not None

    bad_emails = [
        'abcmail.ru',
        'example@mailr',
        'кккк@mail.ru'
    ]

    @pytest.mark.parametrize('email', bad_emails)
    def test_bad_email_format(self, registration_page, email):
        registration_page.click_create()
        registration_page.fill_in_form(email)
        assert registration_page.email_error(
            error=self.INVALID_EMAIL_ERROR) is not None

    def test_create_cabinet(self, registration_page: RegistrationPage):
        registration_page.click_create()
        registration_page.fill_in_form('fanaty_elki_selenium_no_cabinet@mail.ru')
        registration_page.click_create_account()
        assert self.is_url_open('https://ads.vk.com/hq/overview')
        registration_page.delete_account()


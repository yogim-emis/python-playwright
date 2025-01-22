import pytest
import pyotp
from playwright.sync_api import Page


class EMISXTOTPPage:


    def __init__(self, page: Page):
        self.page = page
        self.totp_input = page.get_by_placeholder("Enter your code")
        self.signin_totp_button = page.get_by_label("Verify")


    def SubmitTOTPCode(self, secret):
        otp = pyotp.TOTP(secret)
        otp_code = otp.now()
        print("EMISX OTP: ",otp_code)
        self.totp_input.fill(otp_code)
        self.signin_totp_button.click()

    def PickOrganisation(self, organisationid):
        print("INI: OrganisationId: " + organisationid)
        xpath = 'xpath=//*[@data-testid="ern:emis:org:org:' + organisationid + '-button"]'
        self.page.locator(xpath).click()

		
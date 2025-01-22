import re
import pyotp
from playwright.sync_api import Page, expect


class TOTPPage:


    def __init__(self, page: Page):
        self.page = page
        self.totp_input = page.get_by_label("authentication code")
        self.signin_button = page.get_by_role("button", name="Sign in")


    def SubmitTOTPCode(self, secret):
        otp = pyotp.TOTP(secret)
        otp_code = otp.now()
        print("OTP: ",otp_code)
        self.totp_input.fill(otp_code)
        self.signin_button.click()

		
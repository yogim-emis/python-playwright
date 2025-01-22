from playwright.sync_api import Page


class LoginPage:


    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signin_button = page.get_by_role("button", name="submit")
        self.error_in_authentication = page.get_by_text("Error in authentication,").nth(1)

        self.totp_input = page.get_by_label("authentication code")
        self.signin_totp_button = page.get_by_role("button", name="Sign in")


    def goto(self, targeturl):
        print ("PathwayUrl: " + targeturl)    
        self.page.goto(targeturl)
        self.username_input.wait_for()


    def SubmitLogonCredentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signin_button.click()

		
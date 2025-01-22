from playwright.sync_api import Page


class EMISXLoginPage:


    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Email address", exact=True)
        self.password_input = page.get_by_label("Password", exact=True)
        self.signin_button = page.get_by_role("button", name="Sign in")
        self.error_in_authentication = page.get_by_text("Email and password don't")


    def goto(self, targeturl):
        print ("EMISXUrl: " + targeturl)
        self.page.goto(targeturl)
        self.username_input.wait_for()


    def SubmitLogonCredentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signin_button.click()

		
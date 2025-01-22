from playwright.sync_api import Page


class CreatePathwayPage:


    def __init__(self, page: Page):
        self.page = page


        self.page_hdr = page.locator('xpath=//*[@id="__next"]/div/div/div/div/div/div[3]/div/h1')
        self.page_back_btn = page.get_by_role("button", name="Back")
        self.editpathway_btn = page.get_by_role("button", name="Edit Pathway Icon Edit pathway")

        self.description_section_hdr = page.get_by_role("heading", name="Pathway description")
        self.datasharingpermission_section_hdr =  page.get_by_role("heading", name="Data sharing permission")
        self.supportingdocs_section_hdr = page.get_by_role("heading", name="Supporting documents")

        self.description_section_txt = page.locator('xpath=//*[@id="__next"]/div/div/div/div/div/div[4]/div/div/div[1]/div[1]/span')
        self.datasharingpermission_section_txt = page.get_by_role("paragraph")
        self.supportingdocs_section_txt = page.locator('xpath=//*[@id="__next"]/div/div/div/div/div/div[4]/div/div/div[1]/div[2]/div')

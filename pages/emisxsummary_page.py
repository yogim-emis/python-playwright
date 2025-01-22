from playwright.sync_api import Page


class EMISXSummaryPage:


    def __init__(self, page: Page):
        self.page = page
        self.page_hdr = page.locator('xpath=//*[@data-testid="pathway-name"]/span')
        self.pathwaydescription_lbl = page.get_by_test_id("pathway-description-section")
        self.pathwaydescriptions_inf = page.get_by_test_id("pathway-description-content")
        self.supportingdocuments_lbl = page.get_by_test_id("supporting-documents-section")
        self.yourpatients_lbl = page.get_by_text("Your patients")
        self.yourpatients_patientsdatasharing_lbl = page.get_by_text("Patient data sharing:")
        self.yourpatients_patientsdatasharing_inf = page.get_by_text("Available", exact=True)
        self.yourpatients_permissions_inf = page.get_by_text("Permissions")
        self.yourpatients_agree_btn = page.get_by_test_id("data-sharing-toggle")
        self.yourpatients_viewpatients_btn = page.get_by_test_id("see-patients-button")
        self.pathway_settings_lbl = page.get_by_text("Settings")
        self.pathway_configuresettings_lnk = page.get_by_role("link", name="Configure variables")

        self.agreementdialog_hdr = page.get_by_text("CO_Ordinator_No_Patients_shared_testing permissions")
        self.agreementdialog_tandc_lbl = page.get_by_test_id("dialog-content").get_by_text("Terms and conditions")
        self.agreementdialog_datasharing_lbl = page.get_by_test_id("dialog-content").get_by_text("Data sharing")
        self.agreementdialog_agree_btn = page.get_by_test_id("dataSharingDialogOkButton")
        self.agreementdialog_cancel_btn = page.get_by_test_id("dataSharingDialogCancelButton")
        self.agreementdialog_close_btn = page.get_by_test_id("dialog-header-close-button")
        


    def goto(self, targeturl):
        print ("EMISPathwaySummaryXUrl: " + targeturl)
        self.page.goto(targeturl)
        self.page.wait_for_load_state()


		
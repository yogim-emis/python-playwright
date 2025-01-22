from playwright.sync_api import Page


class PathwaysPage:


    def __init__(self, page: Page):
        self.page = page
        self.addnewpathway_button = page.get_by_test_id("dialog-trigger")
        self.search = page.get_by_placeholder("Search")
        ## Create New Pathway Dialog
        self.dialog_header = page.get_by_role("heading", name="Create New Pathway")
        self.dialog_pathwayname_lbl = page.get_by_test_id("dialog-content").get_by_text("Pathway Name")
        self.dialog_description_lbl = page.get_by_test_id("dialog-content").get_by_text("Description")
        self.dialog_patientdatasharing_lbl = page.get_by_test_id("dialog-content").get_by_text("Patient data sharing")
        self.dialog_enabledatasharing_checkbox_lbl = page.get_by_text("Enable Data Sharing with")
        self.dialog_pathwaytype_lbl = page.get_by_test_id("dialog-content").get_by_text("Pathway Type")

        self.dialog_title_txt = page.get_by_test_id("title")
        self.dialog_description_txt = page.get_by_test_id("description")
        self.dialog_enabledatasharing_chk = page.get_by_test_id("sharing-allowed")
        self.dialog_pathwaytype_cbx = page.get_by_role("combobox")
        self.dialog_pathwaytype_standard_opt = page.get_by_test_id("standard")        
        self.dialog_pathwaytype_dataout_opt = page.get_by_test_id("data_out")
        self.dialog_pathwaytype_cohortin_opt = page.get_by_test_id("cohort_in")
        self.dialog_pathwaytype_cohortscoring_opt = page.get_by_test_id("cohort_scoring")       

        self.dialog_createpathway_btn = page.get_by_test_id("createbtn")
        self.dialog_cancel_btn = page.get_by_test_id("cancelbtn")
        self.dialog_close = page.get_by_test_id("dialog-header-close-button")

    def SubmitCreateNewPathway(self, pathway_name, description, sharing_enabled, pathwaytype_option):
        self.dialog_title_txt.fill(pathway_name)
        self.dialog_description_txt.fill(description)

        if sharing_enabled == True and not self.dialog_enabledatasharing_chk.is_checked:
            self.dialog_enabledatasharing_chk.click()
        elif sharing_enabled == False and self.dialog_enabledatasharing_chk.is_checked:
            self.dialog_enabledatasharing_chk.click()

        self.dialog_pathwaytype_cbx.click()
        if pathwaytype_option.lower() == "data out": 
            self.dialog_pathwaytype_dataout_opt.click()
        elif  pathwaytype_option.lower() == "cohort in": 
            self.dialog_pathwaytype_cohortin_opt.click()
        elif  pathwaytype_option.lower() == "cohort scoring": 
            self.dialog_pathwaytype_cohortscoring_opt.click()
        else:
            self.dialog_pathwaytype_standard_opt.click() 
        self.dialog_createpathway_btn.click()     

    def SearchForPathway(self, pathway_name):
        self.search.type(pathway_name)
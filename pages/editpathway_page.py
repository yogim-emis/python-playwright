from playwright.sync_api import Page


class EditPathwayPage:


    def __init__(self, page: Page):
        self.page = page

        # Pathway Details Tab
        self.page_hdr = page.locator('xpath=//*[@id="__next"]/div/div/div/div/div[1]/div[1]/div/span[2]')
        self.page_back_btn = page.get_by_role("button", name="Back")
        self.viewpathway_btn = page.get_by_test_id("viewpathwaybutton")
        self.update_btn = page.get_by_test_id("update")
        self.pathwaydetails_tab = page.get_by_test_id("pathwayDetailTab")
        self.pathwaydetailstab_hdr = page.get_by_role("heading", name="Pathway details")
        self.pathwaydetailstab_pathwayname_lbl = page.get_by_text("Pathway Name")
        self.pathwaydetailstab_pathwayname_txt = page.get_by_test_id("title")
        self.pathwaydetailstab_description_lbl = page.get_by_text("Description") 
        self.pathwaydetailstab_descriptiuon_txt = page.locator('xpath=//*[@id="description"]/div[2]/div/p/span')
        self.pathwaydetailstab_supportedvariables_lbl = page.get_by_text("Supported variables:")
        self.pathwaydetailstab_supvar_patientfullname_lbl = page.get_by_text("[Patient-FullName]")
        self.pathwaydetailstab_supvar_patientfirstname_lbl = page.get_by_text("[Patient-FirstName]")
        self.pathwaydetailstab_supvar_patientlastname_lbl = page.get_by_text("[Patient-LastName]")              
        self.pathwaydetailstab_supvar_gpname_lbl = page.get_by_text("[GP-Name]")
        self.pathwaydetailstab_supvar_gppractice_lbl = page.get_by_text("[GP-Practice]")
        self.pathwaydetailstab_supvar_messagesender_lbl = page.get_by_text("[Message-Sender]")    
        self.pathwaydetailstab_supvar_patientnhsnumber_lbl = page.get_by_text("[Patient-NHS-Number]")
        self.pathwaydetailstab_supvar_medicationtable_lbl = page.get_by_text("[Medication-Table]")
        self.pathwaydetailstab_supvar_practiceaddress_lbl = page.get_by_text("[Practice-Address]")
        self.pathwaydetailstab_supvar_clinicaltable_lbl = page.get_by_text("[Clinical-Table]")
        self.pathwaydetailstab_supvar_detailstable_lbl = page.get_by_text("[Details-Table]")
        self.pathwaydetailstab_supvar_sharinggroupname_lbl = page.get_by_text("[Sharing-Group-Name]")
        self.pathwaydetailstab_supvar_patienthomeaddress_lbl = page.get_by_text("[Patient-Home-Address]")
        self.pathwaydetailstab_supvar_variablegpphonenumber_lbl = page.get_by_text("[Variable-GP-Phone-Number]")
        self.pathwaydetailstab_supvar_variablegpurl_lbl = page.get_by_text("[Variable-GP-URL]")                                                      
        self.pathwaydetailstab_supportedvariables_moredetails_btn = page.get_by_role("button", name="More details")
        self.pathwaydetailstab_patientdatasharing_lbl = page.get_by_text("Patient data sharing")
        self.pathwaydetailstab_sharingallowed_chk = page.get_by_test_id("sharing-allowed")
        self.pathwaydetailstab_sharingallowed_chk_lbl = page.get_by_text("Enable Data Sharing with")
        self.pathwaydetailstab_pathwaytype_lbl = page.get_by_text("Pathway type")    
        self.pathwaydetailstab_pathwaytype_txt = page.get_by_test_id("pathway-type")      


        self.supportingdocs_tab = page.get_by_test_id("supportingDocTab")

        # Cohort Deinition Tab
        self.cohortdefinition_tab = page.get_by_test_id("cohortDefTab")
        self.cohortdefinitiontab_hdr = page.get_by_role("heading", name="Cohort definition")
        self.cohortdefinitiontab_sqlquery_inf = page.get_by_text("SQL query will be executed")
        self.cohortdefinitiontab_sqlquery_lbl = page.get_by_text("SQL query", exact=True)
        self.cohortdefinitiontab_sqlquery_txt = page.get_by_test_id("sqlquery")
        self.cohortdefinitiontab_sqlcolumnmap_lbl = page.get_by_text("SQL Column Map")
        self.cohortdefinitiontab_sqlcolumnmap_inf = page.get_by_text("Maps SQL query column name to")
        self.cohortdefinitiontab_sqlcolumnmap_txt = page.get_by_test_id("columnmap")

        # Permission Working Tab
        self.permissionwording_tab = page.get_by_test_id("permissionWordingTab")
        self.permissionwordingtab_hdr = page.get_by_role("heading", name="Permission wording")
        self.permissionwordingtab_termsandconditions_lbl = page.get_by_text("Terms and conditions for GPs")
        self.permissionwordingtab_termsandconditions_txt = page.get_by_test_id("terms-inner").get_by_label("Rich text editor")
        self.permissionwordingtab_suportedvariable_lbl = page.get_by_text("Supported variables:")
        self.permissionwordingtab_supvar_patientfullname_lbl = page.get_by_text("[Patient-FullName]")
        self.permissionwordingtab_supvar_patientfirstname_lbl = page.get_by_text("[Patient-FirstName]")
        self.permissionwordingtab_supvar_patientlastname_lbl = page.get_by_text("[Patient-LastName]")              
        self.permissionwordingtab_supvar_gpname_lbl = page.get_by_text("[GP-Name]")
        self.permissionwordingtab_supvar_gppractice_lbl = page.get_by_text("[GP-Practice]")
        self.permissionwordingtab_supvar_messagesender_lbl = page.get_by_text("[Message-Sender]")    
        self.permissionwordingtab_supvar_patientnhsnumber_lbl = page.get_by_text("[Patient-NHS-Number]")
        self.permissionwordingtab_supvar_medicationtable_lbl = page.get_by_text("[Medication-Table]")
        self.permissionwordingtab_supvar_practiceaddress_lbl = page.get_by_text("[Practice-Address]")
        self.permissionwordingtab_supvar_clinicaltable_lbl = page.get_by_text("[Clinical-Table]")
        self.permissionwordingtab_supvar_detailstable_lbl = page.get_by_text("[Details-Table]")
        self.permissionwordingtab_supvar_sharinggroupname_lbl = page.get_by_text("[Sharing-Group-Name]")
        self.permissionwordingtab_supvar_patienthomeaddress_lbl = page.get_by_text("[Patient-Home-Address]")
        self.permissionwordingtab_supvar_variablegpphonenumber_lbl = page.get_by_text("[Variable-GP-Phone-Number]")
        self.permissionwordingtab_supvar_variablegpurl_lbl = page.get_by_text("[Variable-GP-URL]")                                                      
        self.permissionwordingtab_supportedvariables_moredetails_btn = page.get_by_role("button", name="More details")
        self.permissionwordingtab_datasharingcopy_chk = page.get_by_test_id("data-copy")
        self.permissionwordingtab_datasharingcopy_lbl = page.get_by_text("Include data sharing copy")
        self.permissionwordingtab_gpdatasharingwording_lbl = page.get_by_text("Data sharing wording for GPs")
        self.permissionwordingtab_gpdatasharingwording_txt = page.get_by_test_id("wording-inner").get_by_label("Rich text editor")


        # Data Sharing Groups
        self.datasharinggroups_tab = page.get_by_test_id("dsgTab")
        self.datasharinggroups_hdr = page.get_by_role("heading", name="Data sharing groups")
        self.datasharinggroups_inf = page.get_by_label("Data sharing groups")
        self.datasharinggroups_add_btn = page.get_by_test_id("addGrpsBtn")

        # Data Sharing Groups Dialog
        self.datasharinggroupsdialog_hdr = page.get_by_role("heading", name="Data sharing group")
        self.datasharinggroupsdialog_name_lbl = page.get_by_text("Name", exact=True)
        self.datasharinggroupsdialog_name_txt = page.get_by_label("Name", exact=True)
        self.datasharinggroupsdialog_organisationids_lbl = page.get_by_text("Organisation IDs", exact=True)
        self.datasharinggroupsdialog_organisationids_txt = page.get_by_label("Organisations Search Input")
        self.datasharinggroupsdialog_addorg_btn = page.get_by_test_id("addOrgBtn")
        self.datasharinggroupsdialog_organisationids_inf =  page.get_by_text("Comma separate Organisation")
        self.datasharinggroupsdialog_nopractices_inf = page.get_by_text("No practices added")
        self.datasharinggroupsdialog_orgsexadatalakevalidated_inf = page.get_by_text("Added organisations are") 
        self.datasharinggroupsdialog_dismiss_btn = page.get_by_test_id("addDefaultBtn")
        self.datasharinggroupsdialog_displayname_lbl = page.get_by_text("Display name")
        self.datasharinggroupsdialog_displayname_txt = page.get_by_label("Display name")
        self.datasharinggroupsdialog_add_btn = page.get_by_test_id("updateBtn")
        self.datasharinggroupsdialog_cancel_btn = page.get_by_test_id("cancelBtn")       
        self.datasharinggroupsdialog_close_btn = page.get_by_test_id("dialog-header-close-button")



        self.messageconfig_tab = page.get_by_test_id("msgConfigTab")
        self.exportconfig_tab = page.get_by_test_id("exportConfigTab")


        self.publish_tab = page.get_by_test_id("publishTab")
        self.publishtab_hdr = page.get_by_role("heading",name="Publish")
        self.publishtab_cantpublish_msg = page.get_by_text("You can't currently publish")
        self.publishtab_pathwaystatus_lbl = page.get_by_text("Pathway status")
        self.publishtab_draftoption_rdo = page.get_by_test_id("draftRadio-draft-input")
        self.publishtab_publishedoption_rdo = page.get_by_test_id("publishRadio-published-input")
        self.update_btn = page.get_by_test_id("update")


    def SubmitCohortDefinition(self, sqlquery, sqlcolumnmap):
        self.cohortdefinitiontab_sqlquery_txt.fill(sqlquery)
        self.cohortdefinitiontab_sqlcolumnmap_txt.fill(sqlcolumnmap)
        self.update_btn.click()

    def SubmitPermissionWording(self, termsandcondition, gpdatasharingwording):
        self.permissionwordingtab_termsandconditions_txt.fill(termsandcondition)
        self.permissionwordingtab_gpdatasharingwording_txt.fill(gpdatasharingwording)
        self.update_btn.click()

    def SubmitDataSharingGroups(self, name, orgids, displayname):
        self.datasharinggroups_add_btn.click()
        self.datasharinggroupsdialog_name_txt.fill(name)
        self.datasharinggroupsdialog_organisationids_txt.fill(orgids)
        self.datasharinggroupsdialog_addorg_btn.click()
        self.datasharinggroupsdialog_displayname_txt.fill(displayname)
        self.datasharinggroupsdialog_add_btn.click()

    def SubmitPublish(self, publish):
        if (self.publishtab_draftoption_rdo.is_checked() and publish == True):
            self.publishtab_publishedoption_rdo.click()
        if (self.publishtab_publishedoption_rdo.is_checked() and publish == False):
            self.publishtab_draftoption_rdo.click()
        self.update_btn.click()


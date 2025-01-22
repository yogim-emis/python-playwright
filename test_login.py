import re
import pytest
from playwright.sync_api import Browser, expect
from pages.pathways_page import PathwaysPage
from pages.createpathway_page import CreatePathwayPage
from pages.editpathway_page import EditPathwayPage
from pages.emisxsummary_page import EMISXSummaryPage
from module import Module
from pathwaytestdata import PATHWAYTESTDATA
import time

@pytest.mark.author
#@pytest.mark.skip(reason="Unfinished test or temporarily disabled")
def test_CreatePathwayDialogDefaults(browser: Browser):
    ## Synopsis: Validate that create pathway page that expected page/dialog attributes are
    ##           available, headers and labels spelt correctly and input fields are defaulted
    ##           as expected
    #    
    if pytest.gLogonFailure==False:
        ## Navigate to Pathways home page using initial browser context
        page = browser.contexts[0].pages[0]
        page.bring_to_front()
        page.goto(pytest.gAUTAuthorUrl)

        # Open up the new Create pathway dialog
        pathways_page = PathwaysPage(page)
        pathways_page.addnewpathway_button.click()

        # Inspect the Create New Pathway dialog page
        
        # Assert expected field label names
        expect(pathways_page.dialog_header).to_have_text('Create New Pathway')
        expect(pathways_page.dialog_pathwayname_lbl).to_have_text('Pathway Name')
        expect(pathways_page.dialog_description_lbl).to_have_text('Description')
        expect(pathways_page.dialog_patientdatasharing_lbl).to_have_text("Patient data sharing")
        expect(pathways_page.dialog_enabledatasharing_checkbox_lbl).to_have_text("Enable Data Sharing with Coordinator user")
        expect(pathways_page.dialog_pathwaytype_lbl).to_have_text("Pathway Type")

        # Assert expected field default values
        expect(pathways_page.dialog_title_txt).to_be_empty()
        expect(pathways_page.dialog_description_txt).to_be_empty()
        expect(pathways_page.dialog_enabledatasharing_chk).to_be_checked()
        expect(pathways_page.dialog_pathwaytype_cbx).to_have_text("Standard")

        # Assert dialog button are enabled
        expect(pathways_page.dialog_createpathway_btn).to_be_enabled()
        expect(pathways_page.dialog_cancel_btn).to_be_enabled()
        expect(pathways_page.dialog_close).to_be_enabled()


@pytest.mark.author
#@pytest.mark.skip(reason="Unfinished test or temporarily disabled")
##@pytest.mark.skipif(pytest.gLogonFailure==True, reason = "Abandoning tests due to logon authentication failure")
def test_CancelFromCreateNewPathwayDialog(browser: Browser):
    ## Synopsis: As author can cancel out from creating a draft pathway

    ## Navigate to Pathways home page using initial browser context    
    page = browser.contexts[0].pages[0]
    page.goto(pytest.gAUTAuthorUrl)

    # Open up the new Create pathway dialog
    pathways_page = PathwaysPage(page)
    pathways_page.addnewpathway_button.click()

    # Assert that we have opened up the dialog
    expect(pathways_page.dialog_header).to_have_text('Create New Pathway')

    # Exit dialog via the Cancel button
    pathways_page.dialog_cancel_btn.click()

    # Retry and exit via the dialog header close [X]
    pathways_page.addnewpathway_button.click()

    # Assert that we have opened up the dialog
    expect(pathways_page.dialog_header).to_have_text('Create New Pathway') 

    pathways_page.dialog_close.click()

@pytest.mark.author
#@pytest.mark.skip(reason="Unfinished test or temporarily disabled")
@pytest.mark.skipif(pytest.gLogonFailure==True, reason = "Abandoning tests due to logon authentication failure")
def test_CanCreatePathwayAsAuthor_DFTSTDENS(browser: Browser):
    ## Synopsis: As author can create a DraFT STandarD with ENabled Sharing pathway (DFTSTDENS)
    ## Additional Test Validation: 
    ##  1. Checks available page and dialog attributes (headers, field labels, default page/dialog field values)
    ##  2. Confirmaton of create pathway page url

    ## Navigate to Pathways home page using initial browser context    
    page = browser.contexts[0].pages[0]
    page.bring_to_front()
    page.goto(pytest.gAUTAuthorUrl)

    # Open up the new Create pathway dialog
    pathways_page = PathwaysPage(page)
    pathways_page.addnewpathway_button.click()

    # Assert that we have opened up the dialog
    expect(pathways_page.dialog_header).to_have_text('Create New Pathway')

    # Fill and submit create new pathway form
    pathway_name = "AUTO-Pathway-" + Module.getnow_yyyymmddhhmmss() 
    pathways_page.SubmitCreateNewPathway(pathway_name, "Standard Data sharing enabled pathway created by automated test", True, "Standard")

    # Assert that we have created the draft pathway and landed on create pathway page with correct input details
    createpathway_page = CreatePathwayPage(page)
    expect(page).to_have_url(re.compile(r".*/create-pathway.*"))

    expect(createpathway_page.page_hdr).to_have_text(pathway_name)
    expect(createpathway_page.description_section_hdr).to_have_text("Pathway description")
    expect(createpathway_page.datasharingpermission_section_hdr).to_have_text("Data sharing permission")
    expect(createpathway_page.supportingdocs_section_hdr).to_have_text("Supporting documents")

    expect(createpathway_page.description_section_txt).to_have_text("Standard Data sharing enabled pathway created by automated test")
    expect(createpathway_page.datasharingpermission_section_txt).to_have_text("Missing")
    expect(createpathway_page.supportingdocs_section_txt).to_have_text("Missing")

    # Extract the newly created draft pathway id and record in runsettings ini file for future test re-use
    pathwayid = page.url[page.url.index("=")+1:]
    print ("DFTSTDENS PathwayId: " + pathwayid)
    Module.setrunsettings(pytest.gAUTEnvName,"PathwayTestData", "PathwayId-DFTSTDENS",pathwayid)

@pytest.mark.author
#@pytest.mark.skip(reason="Unfinished test or temporarily disabled")
@pytest.mark.skipif(pytest.gLogonFailure==True, reason = "Abandoning tests due to logon authentication failure")
def test_CanPublishPathway_NGPENSSTD(browser: Browser):
    ## Synopsis: As author can publish a No Granted Permission STandarD with ENabled Sharing pathway (NGPSTDENS) 
    ##           having filled in mandatory Corhort definition, Permission wording and Data sharing group section

    ## Navigate to Pathways home page using initial browser context    
    page = browser.contexts[0].pages[0]
    page.bring_to_front()
    page.goto(pytest.gAUTAuthorUrl)

    # Open up the new Create pathway dialog
    pathways_page = PathwaysPage(page)
    pathways_page.addnewpathway_button.click()

    # Assert that we have opened up the dialog
    expect(pathways_page.dialog_header).to_have_text('Create New Pathway')

    # Fill and submit create new pathway form
    pathway_name = "AUTO-Pathway-" + Module.getnow_yyyymmddhhmmss() 
    pathways_page.SubmitCreateNewPathway(pathway_name, "A published standard data sharing enabled pathway created by automated test", True, "Standard")

    # Assert that we have created the draft pathway and landed on create pathway page with correct input details
    createpathway_page = CreatePathwayPage(page)
    expect(page).to_have_url(re.compile(r".*/create-pathway.*"))

    # Extract the newly created draft pathway id and record in runsettings ini file for further test re-use
    pathwayid = page.url[page.url.index("=")+1:]
    print ("Published pathway standard/enabled sharing/no comms/permission not granted PathwayId: " + pathwayid)

    # Edit draft pathway
    createpathway_page.editpathway_btn.click()
    expect(page).to_have_url(re.compile(r".*/PathwayEdit.*"))

    editpathway_page = EditPathwayPage(page)

    editpathway_page.cohortdefinition_tab.click()
    expect(editpathway_page.cohortdefinitiontab_hdr).to_have_text("Cohort definition")
    editpathway_page.SubmitCohortDefinition(PATHWAYTESTDATA.scenario_001.sql, PATHWAYTESTDATA.scenario_001.colmap)

    editpathway_page.permissionwording_tab.click()
    expect(editpathway_page.permissionwordingtab_hdr).to_have_text("Permission wording")
    editpathway_page.SubmitPermissionWording(PATHWAYTESTDATA.scenario_001.wordingtandc, PATHWAYTESTDATA.scenario_001.wordinggpsharing)

    editpathway_page.datasharinggroups_tab.click()
    expect(editpathway_page.datasharinggroups_hdr).to_have_text("Data sharing groups")   
    editpathway_page.SubmitDataSharingGroups(PATHWAYTESTDATA.scenario_001.dsgname,PATHWAYTESTDATA.scenario_001.dsgorganisationids, PATHWAYTESTDATA.scenario_001.dsgdisplayname)

    editpathway_page.publish_tab.click()
    expect(editpathway_page.publishtab_hdr).to_have_text("Publish")
    editpathway_page.SubmitPublish(True)  

    Module.setrunsettings(pytest.gAUTEnvName,"PathwayTestData", "PathwayId-NGPSTDENS",pathwayid)


@pytest.mark.controller
#@pytest.mark.skip(reason="Unfinished test or temporarily disabled")
@pytest.mark.skipif(pytest.gLogonFailure==True, reason = "Abandoning tests due to logon authentication failure")
def test_CanAgreeToDataSharingPatientData_PERENSSTD(browser: Browser):
    ## Synopsis: As controller can agree by granting PERMission to share patient data for pathway PERENSSTD 

    ## Navigate to Pathways home page using initial browser context    
    page = browser.contexts[0].pages[0]
    page.bring_to_front()
    page.goto(pytest.gAUTAuthorUrl)

    # Open up the new Create pathway dialog
    pathways_page = PathwaysPage(page)
    pathways_page.addnewpathway_button.click()

    # Assert that we have opened up the dialog
    expect(pathways_page.dialog_header).to_have_text('Create New Pathway')

    # Fill and submit create new pathway form
    pathway_name = "AUTO-Pathway-" + Module.getnow_yyyymmddhhmmss() 
    pathways_page.SubmitCreateNewPathway(pathway_name, "A published standard data sharing enabled pathway created by automated test", True, "Standard")

    # Assert that we have created the draft pathway and landed on create pathway page with correct input details
    createpathway_page = CreatePathwayPage(page)
    expect(page).to_have_url(re.compile(r".*/create-pathway.*"))

    # Extract the newly created draft pathway id and record in runsettings ini file for further test re-use
    pathwayid = page.url[page.url.index("=")+1:]
    print ("Published pathway standard/enabled sharing/no comms/permission not granted PathwayId: " + pathwayid)

    # Edit draft pathway
    createpathway_page.editpathway_btn.click()
    expect(page).to_have_url(re.compile(r".*/PathwayEdit.*"))

    editpathway_page = EditPathwayPage(page)

    editpathway_page.cohortdefinition_tab.click()
    expect(editpathway_page.cohortdefinitiontab_hdr).to_have_text("Cohort definition")
    editpathway_page.SubmitCohortDefinition(PATHWAYTESTDATA.scenario_001.sql, PATHWAYTESTDATA.scenario_001.colmap)

    editpathway_page.permissionwording_tab.click()
    expect(editpathway_page.permissionwordingtab_hdr).to_have_text("Permission wording")
    editpathway_page.SubmitPermissionWording(PATHWAYTESTDATA.scenario_001.wordingtandc, PATHWAYTESTDATA.scenario_001.wordinggpsharing)

    editpathway_page.datasharinggroups_tab.click()
    expect(editpathway_page.datasharinggroups_hdr).to_have_text("Data sharing groups")   
    editpathway_page.SubmitDataSharingGroups(PATHWAYTESTDATA.scenario_001.dsgname,PATHWAYTESTDATA.scenario_001.dsgorganisationids, PATHWAYTESTDATA.scenario_001.dsgdisplayname)

    editpathway_page.publish_tab.click()
    expect(editpathway_page.publishtab_hdr).to_have_text("Publish")
    editpathway_page.SubmitPublish(True) 

    ## Switch browser context to EMISX and goto published pathway summary page
    page = browser.contexts[1].pages[0]  
    page.bring_to_front()

    # Open up the new Create pathway dialog
    emisxsummary_page = EMISXSummaryPage(page)
    emisxsummary_page.goto(pytest.gAUTControllerUrl + "pathways/summarypage/" + pathwayid)
    time.sleep(10)

    #expect(emisxsummary_page.page_hdr).to_have_text(pathway_name)
    expect(emisxsummary_page.yourpatients_patientsdatasharing_inf).to_have_text("Available")
    expect(emisxsummary_page.yourpatients_agree_btn).to_be_enabled()
    expect(emisxsummary_page.yourpatients_viewpatients_btn).to_be_disabled()

    emisxsummary_page.yourpatients_agree_btn.click()
    expect(emisxsummary_page.agreementdialog_agree_btn).to_be_enabled()
    emisxsummary_page.agreementdialog_agree_btn.click()

    expect(emisxsummary_page.yourpatients_agree_btn).to_have_text("Review")
    expect(emisxsummary_page.yourpatients_viewpatients_btn).to_be_enabled()

    Module.setrunsettings(pytest.gAUTEnvName,"PathwayTestData", "PathwayId-PERENSSTD",pathwayid)


@pytest.mark.controller
def test_yogi(browser: Browser):
    
    page = browser.contexts[1].pages[0]
    page.bring_to_front()
    page.goto("https://host.int.emishealthsolutions.com/pathways/summarypage/0538e085-4eef-4dd3-b798-40942828dfc9")
 

    # Open up the new Create pathway dialog
    emisxsummary_page = EMISXSummaryPage(page)
    time.sleep(10)
    #expect(emisxsummary_page.page_hdr).to_have_text(pathway_name)
    expect(emisxsummary_page.yourpatients_agree_btn).to_have_text("Review")
    expect(emisxsummary_page.yourpatients_agree_btn).to_be_enabled()
    expect(emisxsummary_page.yourpatients_viewpatients_btn).to_be_enabled()

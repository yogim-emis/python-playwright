import pytest
import configparser
import os
from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.totp_page import TOTPPage
from pages.emisxlogin_page import EMISXLoginPage
from pages.emisxtotp_page import EMISXTOTPPage
from aut import AUT
from defaultuser import USERS
from module import Module

pytest.gAUTEnvName=""
pytest.gLogonFailure=False
pytest.gAUTUrl=""
pytest.gAUTAuthorUrl=""
pytest.gAUTCoordinatorUrl=""
pytest.gAUTControllerUrl=""
pytest.gAUTUserId=""
pytest.gAUTPwd=""
pytest.gAUTSecret=""
pytest.gAUTEMISXUserId=""
pytest.gAUTEMISXPwd=""
pytest.gAUTEMISXSecret=""


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="default")
    ##parser.addoption("--usr", action="store", default=USERS.default.username)
    ##parser.addoption("--pwd", action="store", default=USERS.default.password)
    ##parser.addoption("--secret", action="store", default=USERS.default.secret)
    ##parser.addoption("--xusr", action="store", default=USERS.emisxint.username)
    ##parser.addoption("--xpwd", action="store", default=USERS.emisxint.password)
    ##parser.addoption("--xsecret", action="store", default=USERS.emisxint.secret)    
 

@pytest.fixture(scope='session', autouse=True)
def env_name(request):
    return request.config.getoption("--env")


#@pytest.fixture(scope='session', autouse=True)
#def logonuserid(request):
#    return request.config.getoption("--usr")


#@pytest.fixture(scope='session', autouse=True)
#def logonpassword(request):
#    return request.config.getoption("--pwd")


#@pytest.fixture(scope='session', autouse=True)
#def logonsecret(request):
#    return request.config.getoption("--secret")

#@pytest.fixture(scope='session', autouse=True)
#def emisxuserid(request):
#    return request.config.getoption("--xusr")


#@pytest.fixture(scope='session', autouse=True)
#def xlogonpassword(request):
#    return request.config.getoption("--xpwd")


#@pytest.fixture(scope='session', autouse=True)
#def xlogonsecret(request):
#    return request.config.getoption("--xsecret")


@pytest.fixture(scope="session", autouse=True)
#def browser(playwright: Playwright, env_name, logonuserid,logonpassword,logonsecret):
def browser(playwright: Playwright, env_name):

    pytest.gAUTEnvName = env_name
    config = configparser.ConfigParser(allow_no_value=True)
    ini_path = os.path.join(os.getcwd(),'runsettings' + '_' + env_name + '.ini')
    config.read(ini_path)
    sBrowser = config.get('Playwright','Browser').lower()
    print("\nINI:Browser:",sBrowser)  
    bHeadless = config.getboolean('Playwright','Headless')
    print("\nINI:Headless:",bHeadless)
    sBrowserChannel = config.get('Playwright','BrowserChannel').lower()
    print("\nINI:BrowserChannel:",sBrowserChannel)
    iSlowMo = config.getint('Playwright','SlowMo')
    print("\nINI:SlowMo:",iSlowMo)
    bVideo = config.getboolean('Playwright','Video')

    if env_name == 'staging':
        pytest.gAUTUrl = AUT.staging.weburl
        pytest.gAUTAuthorUrl = AUT.staging.authorurl
        pytest.gAUTCoordinatorUrl = AUT.staging.coordinatorurl
        pytest.gAUTControllerUrl = AUT.emisx_gp_staging.weburl.replace("?emisweb=false","") 
        pytest.gAUTUserId = USERS.staging.username
        pytest.gAUTPwd = USERS.staging.password
        pytest.gAUTSecret = USERS.staging.secret
        pytest.gAUTEMISXUserId = USERS.emisxstaging.username
        pytest.gAUTEMISXPwd = USERS.emisxstaging.password
        pytest.gAUTEMISXSecret = USERS.emisxstaging.secret
    else :
        pytest.gAUTUrl = AUT.int.weburl
        pytest.gAUTAuthorUrl = AUT.int.authorurl
        pytest.gAUTCoordinatorUrl = AUT.int.coordinatorurl 
        pytest.gAUTControllerUrl = AUT.emisx_gp_int.weburl.replace("?emisweb=false","") 
        pytest.gAUTLogonUserId = USERS.int.username
        pytest.gAUTLogonPwd = USERS.int.password
        pytest.gAUTLogonSecret = USERS.int.secret
        pytest.gAUTEMISXLogonUserId = USERS.emisxint.username
        pytest.gAUTEMISXLogonPwd = USERS.emisxint.password
        pytest.gAUTEMISXLogonSecret = USERS.emisxint.secret   

    if sBrowser == 'firefox' :
        browser = playwright.firefox.launch(headless=bHeadless, channel=sBrowserChannel, slow_mo=iSlowMo)
    elif sBrowser == 'webkit' :
        browser = playwright.webkit.launch(headless=bHeadless, channel=sBrowserChannel, slow_mo=iSlowMo)
    else :
        browser = playwright.chromium.launch(headless=bHeadless, channel=sBrowserChannel, slow_mo=iSlowMo)
    

    # Cleardown any captured previous run videos
    Module.cleardown_videos()

    # Login with new browser context with user operating as both author and data controller
    if bVideo :
        context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 640, "height": 480})
    else :
        context = browser.new_context()

    page = context.new_page()
    login_page = LoginPage(page)

    login_page.goto(pytest.gAUTUrl)
    login_page.SubmitLogonCredentials(pytest.gAUTLogonUserId,pytest.gAUTLogonPwd)

    totp_page = TOTPPage(page)
 
    #if "mfa?" in totp_page.page.url:
    #   pytest.gLoginFailure=False

    totp_page.SubmitTOTPCode(pytest.gAUTLogonSecret)

    ## Login with new browser context with user operating as data controller

    if bVideo :
        context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 640, "height": 480})
    else :
        context = browser.new_context()

    page = context.new_page()
    EMISXlogin_page = EMISXLoginPage(page)
    EMISXlogin_page.goto(pytest.gAUTControllerUrl)
    EMISXlogin_page.SubmitLogonCredentials(pytest.gAUTEMISXLogonUserId,pytest.gAUTEMISXLogonPwd)

    EMISXtotp_page = EMISXTOTPPage(page)
    EMISXtotp_page.SubmitTOTPCode(pytest.gAUTEMISXLogonSecret)
    EMISXtotp_page.PickOrganisation(config.get('DataController','OrganisationId'))
    page.wait_for_url(pytest.gAUTControllerUrl)

    yield browser
    context.clear_cookies()
    context.close()
    browser.close()

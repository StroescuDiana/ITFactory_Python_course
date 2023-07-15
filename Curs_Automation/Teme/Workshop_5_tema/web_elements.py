class WebElements:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    url = "https://www.elefant.ro/"
    cookies_accept_bttn_id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
    search_box_xpath = "//input[@class='form-control searchTerm js-has-overlay']"
    search_button_xpath = "//button[@class='btn-search btn btn-primary']"
    item = "iphone 14"
    product_title_xpath = "//a[@class='product-title']"
    product_price_xpath = "//div[@class='current-price ']"
    expected_title = "Cauti iphone 14? - Vino pe Elefant.ro!"
    cont_icon_xpath = "//span[contains(text(), 'Cont')]/preceding-sibling::i"
    conectare_bttn_homepage_xpath = "//a[@class='my-account-login btn btn-primary btn-block']"
    log_in_url = "https://www.elefant.ro/login"
    log_in_successful_url = "https://www.elefant.ro/my-account?TrackingDataContainerID=#__sMDExNjY4MjE"
    email_field_xpath = "//input[@class='form-control' and @name='ShopLoginForm_Login']"
    wrong_email_address = "fake_account@yahoo.com"
    invalid_email_address = "fake_account.com"
    password_box_xpath = "//input[@class='form-control' and @type='password']"
    wrong_password = "ksjfbs1232@!"
    conectare_button_login_xpath = "//button[contains(text(), 'Conectare')]"
    error_alert_text_xpath = "//div[@class='alert alert-danger']"
    expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."

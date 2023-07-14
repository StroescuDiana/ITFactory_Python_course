
class WebElements:
    RED = '\033[91m'
    RED1 = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    url = "https://www.elefant.ro/"
    cookies_accept_bttn_id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
    search_box_xpath = "//input[@class='form-control searchTerm js-has-overlay']"
    search_button = "//button[@class='btn-search btn btn-primary']"
    item = "iphone 14"
    product_title_xpath = "//a[@class='product-title']"
    product_price_xpath = "//div[@class='current-price ']"
    expected_title = "Cauti iphone 14? - Vino pe Elefant.ro!"
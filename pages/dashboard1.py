from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//*[@id='__next']//ul/div"
    players_button_xpath = "//*[@id='__next']//ul/div[2]"
    lang_button_xpath = "//*[@id='__next']//ul[2]/div"
    sign_out_button_xpath = "//*[@id='__next']//ul[2]/div[2]"
    addlang_button_xpath = "//*[@id='__next']//div[2]//div[2]//div[15]/button"
    addlink_button_xpath = "//*[@id='__next']//div[2]//div[2]//div[19]/button"
    submit_button_xpath = "//*[@id='__next']//div[2]//div[3]/button"
    clear_button_xpath = "//*[@id='__next']//div[2]//div[3]/button[2]"
    email_field_xpath = "//*[@id='__next']//div[2]//div[2]//input"
    name_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[2]//input"
    surname_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[3]//input"
    phone_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[4]//input"
    weight_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[5]//input"
    height_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[6]//input"
    age_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[7]//input"
    leg_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[8]//input"
    club_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[9]//input"
    level_field_xpath = "//*[@id='__next']//div[2]//div[2]//div[10]//input"








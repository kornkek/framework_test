from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//*[@id='__next']//ul/div"
    players_button_xpath = "//*[@id='__next']//ul/div[2]"
    lang_button_xpath = "//*[@id='__next']//ul[2]/div"
    sign_out_button_xpath = "//*[@id='__next']//ul[2]/div[2]"
    dev_team_button_xpath = "//*[@id='__next']//div[3]//div/div[3]/a"
    add_player_button_xpath = "//*[@id='__next']//div[3]/div[2]/div//a/button"
    players_count_table_xpath = "//*[@id='__next']//div[2]/div/div"
    matches_count_table_xpath = "//*[@id='__next']//div[2]/div[2]/div"
    reports_count_table_xpath = "//*[@id='__next']//div[2]/div[2]/div"
    events_count_table_xpath = "//*[@id='__next']//div[2]/div[4]/div"



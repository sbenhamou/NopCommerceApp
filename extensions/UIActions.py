
class Actions:


    def click_element(self, web_element):
        web_element.click()

    def fill_element(self, web_element, text):
        web_element.send_keys(text)

    def submit_form(self, web_element):
        web_element.submit()

    def clear_field(self, web_element):
        web_element.clear()

    def get_txt(self, web_element):
        return web_element.text

    def click_mouseHover(self, web_element):
        self.action.move_to_element(web_element).click().perform()


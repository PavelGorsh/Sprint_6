from locators.base_page_locators import LocatorsBasePageScooter as LocatorsBP
from locators.order_page_locators import LocatorsOrderPageScooter as LocatorsOP


class DataListsForTests:
    locators_ob = LocatorsBP()
    locators_op = LocatorsOP()

    def locators_questions_answeres_list(self):
        question_answer_list = [
            [self.locators_ob.QUESTION_1, self.locators_ob.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
            [self.locators_ob.QUESTION_2, self.locators_ob.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
            [self.locators_ob.QUESTION_3, self.locators_ob.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
            [self.locators_ob.QUESTION_4, self.locators_ob.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
            [self.locators_ob.QUESTION_5, self.locators_ob.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
            [self.locators_ob.QUESTION_6, self.locators_ob.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
            [self.locators_ob.QUESTION_7, self.locators_ob.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
            [self.locators_ob.QUESTION_8, self.locators_ob.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."],
        ]
        return question_answer_list
    
    def data_for_order(self):
        order_button_list = [self.locators_ob.ORDER_BTN_HEADER, self.locators_ob.ORDER_BTN_BODY]
        data_for_order_for = [
            ["Павел", "Горшков", "Москва Антикафе Терра", self.locators_op.METRO_NAME_BAUMANSKAYA, "+79998887766"],
            ["Курьер", "Курьерыч", "Москва Электрозавод", self.locators_op.METRO_NAME_ELECTROZAVODSKAYA, "+79876543210"]
        ]
        data_for_order_about = [
            [self.locators_op.DATEPICKER_DAY_1_CURRENT_MONTH, self.locators_op.PERIOD_MENU_5_DAYS, self.locators_op.COLOR_GREY, "Покажите как ездить?"],
            [self.locators_op.DATEPICKER_DAY_2_CURRENT_MONTH, self.locators_op.PERIOD_MENU_4_DAYS, self.locators_op.COLOR_BLACK, "Я поеду сам и никому самокат не дам (^_^)"]
        ]
        data_for_order_all = [
            [order_button_list[0], *data_for_order_for[0], *data_for_order_about[0]],
            [order_button_list[1], *data_for_order_for[1], *data_for_order_about[1]]
        ]
        return data_for_order_all
    
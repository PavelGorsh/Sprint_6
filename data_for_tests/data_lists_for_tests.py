import locators.main_page_locators as BPL
import locators.order_page_locators as OPL


class DataListsForTests:

    def locators_questions_answeres_list(self):
        question_answer_list = [
            [BPL.QUESTION_1, BPL.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
            [BPL.QUESTION_2, BPL.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
            [BPL.QUESTION_3, BPL.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
            [BPL.QUESTION_4, BPL.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
            [BPL.QUESTION_5, BPL.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
            [BPL.QUESTION_6, BPL.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
            [BPL.QUESTION_7, BPL.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
            [BPL.QUESTION_8, BPL.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."],
        ]
        return question_answer_list
    
    def data_for_order(self):
        order_button_list = [BPL.ORDER_BTN_BASE_PAGE_HEADER, BPL.ORDER_BTN_BASE_PAGE_BODY]
        data_for_order_for = [
            ["Павел", "Горшков", "Москва Антикафе Терра", OPL.METRO_NAME_BAUMANSKAYA, "+79998887766"],
            ["Курьер", "Курьерыч", "Москва Электрозавод", OPL.METRO_NAME_ELECTROZAVODSKAYA, "+79876543210"]
        ]
        data_for_order_about = [
            [OPL.DATEPICKER_DAY_1_CURRENT_MONTH, OPL.PERIOD_MENU_5_DAYS, OPL.COLOR_GREY, "Покажите как ездить?"],
            [OPL.DATEPICKER_DAY_2_CURRENT_MONTH, OPL.PERIOD_MENU_4_DAYS, OPL.COLOR_BLACK, "Я поеду сам и никому самокат не дам (^_^)"]
        ]
        data_for_order_all = [
            [order_button_list[0], *data_for_order_for[0], *data_for_order_about[0]],
            [order_button_list[1], *data_for_order_for[1], *data_for_order_about[1]]
        ]
        return data_for_order_all
    
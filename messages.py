import random


class RandomMessages:

    morning_messages = [
        "Доброе утро!Как спалось?",
        "Дзынь-дзынь, пора вставать!",
        "Проснулись потянулись!",
        "Проснулись улыбнулись!",
        "Пора вкусно и красиво завтракать!"
    ]

    compliment_messages = [
        "Ты самая прекрасная девушка в этом мире!",
        "Выглядишь сегодня свежо и ярко!",
        "Ты подобрала неплохой образ на сегодня!"
    ]
    motivation_messages = [
        "У тебя все получится!",
        "У тебя все круто получается!",
        "Осталось совсем немного!"
    ]

    def get_random_morning_message(self):
        return random.choice(self.morning_messages)

    def get_random_compliment_message(self):
        return random.choice(self.compliment_messages)

    def get_random_motivation_message(self):
        return random.choice(self.motivation_messages)

class NoticeMessages:

    drink_water = "Выпей стакан воды"
    workout = "Встань и разомнись"
    close_instagram = "Закрывай инстаграм"

    def get_notice_drink_water(self):
        return self.drink_water

    def get_notice_workout(self):
        return self.workout

    def get_notice_close_insta(self):
        return self.close_instagram
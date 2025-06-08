#parameters Constructor

class Worker:
    def __init__(self, type_of_day, healthy_activities, daily_reading):
        self.__type_of_day = type_of_day
        self.healthy_activities = healthy_activities
        self.daily_reading = daily_reading

    def daily_action1(self):
        print(f'አ ዛሬ   {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ለቀኑ ንባብ {self.daily_reading}ምረጡ ። ')

    def daily_action2(self):
        print(f'በ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def daily_action3(self):
        print(f'ገ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def daily_action4(self):
        print(f'ደ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def daily_action5(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def daily_action6(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')
    def daily_action7(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ።  ')

    def special_day(self):
        print('Day has no special day')

    def get_type_of_day(self):
        return self.__type_of_day


    type_of_day: str = 'የእለቱ ግጻዌ '
    healthy_activities: int = 5
    daily_reading: int = 1



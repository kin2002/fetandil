#parameters Constructor

class Day:
    def __init__(self, type_of_day, healthy_activities, daily_reading):
        self.__type_of_day = type_of_day
        self.healthy_activities = healthy_activities
        self.daily_reading = daily_reading


    def get_type_of_day(self):
        return self.__type_of_day

    def A(self):
        print(f'አ ዛሬ   {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ለቀኑ ንባብ {self.daily_reading}ምረጡ ። ')

    def B(self):
        print(f'በ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def C(self):
        print(f'ገ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def D(self):
        print(f'ደ ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def E(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')

    def F(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ። ')
    def G(self):
        print(f'ዛሬ  {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities}እናድርግ ከቀኑ ንባብ {self.daily_reading} ምረጡ ።  ')

    type_of_day: str = 'የእለቱ ግጻዌ '
    healthy_activities: int = 5
    daily_reading: int = 1



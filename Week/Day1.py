#parameters Constructor

class Day:
    def __init__(self, month, date, year, type_of_day, healthy_activities, daily_reading, color ):
        self.__type_of_day = type_of_day
        self.type_of_day = type_of_day
        self.month = month
        self.date = date
        self.year =year
        self.healthy_activities = healthy_activities
        self.daily_reading = daily_reading
        self.color= color

    def get_type_of_day(self):
        return self.__type_of_day

    def one_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው። {self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    def two_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    def three_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    def four_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    def five_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    def six_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')
    def seven_day(self):
        print(f'ዛሬ  {self.month} {self.date},{self.year} ነው።{self.__type_of_day} ቀን ስለሆነ ይህን {self.healthy_activities} እናድርግ። ')

    month: str = '12'
    date: int = 1
    year: str = '2025'
    type_of_day: str = 'የእለቱ ግጻዌ '
    healthy_activities: int = 5
    daily_reading: int = 1
    color: str = 'Yellow'


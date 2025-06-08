from Tool import *

class Leader:
    def __init__(self, healthy_activities, daily_reading):
        self.healthy_activities = healthy_activities
        self.daily_reading = daily_reading
        self.is_tool_equipped = False
        self.tool: Tool = None

    def equip_tool(self):
        if self.tool is not None and not self.is_tool_equipped:
            self.daily_reading += self.tool.work_increase
            self.is_tool_equipped = True

    def daily_action1(self):
        print(f' Leader works for {self.daily_reading} works.')
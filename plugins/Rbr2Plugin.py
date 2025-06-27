import logging
from plugin import Plugin

class Rbr2Plugin(Plugin):
    def __init__(self):
        self.skytower_level = 0
        self.maximum_level = 0
        self.minimum_level = 0

    async def process(self, cleaned_lines):
        rbr2 = [(line[1], line[4]) for line in cleaned_lines if line[0] == "rbr2"]

        if rbr2:
            skytower_level, level = rbr2[0]

            result = skytower_level.split('.')
            self.skytower_level = int(result[0]) - 800

            result2 = level.split('.')
            self.minimum_level = result2[0]
            self.maximum_level = result2[1]

    def get_result(self):
        return (self.skytower_level, self.maximum_level, self.minimum_level)
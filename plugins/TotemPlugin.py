import logging
from plugin import Plugin

class TotemPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        totem = next((line for line in cleaned_lines if line[0] == "in" and line[1] == "2" and line[2] == "1457"), None)
        lever = next((line for line in cleaned_lines if line[0] == "in" and line[1] == "9"), None)

        if totem and lever:
            vnum = totem[2]
            x = totem[4]
            y = totem[5]
            direction = totem[6]
            
            self.lua = f"""map_1.AddNpcs({{
    MapNpc.CreateNpcWithVnum({vnum}).At({x}, {y}).Facing({direction}),
}})\n"""
            self.lua += f"""map_1.AddObjects({{
    MapObject.CreateLever().At({lever[4]}, {lever[5]}).OnTrigger({{
    }}),
}})"""

    def get_result(self):
        return (self.lua)
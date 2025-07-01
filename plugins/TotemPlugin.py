import logging
from plugin import Plugin

class TotemPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        totems = [line for line in cleaned_lines if line[0] == "in" and line[1] == "2" and line[2] == "1457"]
        lever = next((line for line in cleaned_lines if line[0] == "in" and line[1] == "9"), None)

        if totems:
            self.lua = "map_1.AddNpcs({\n"
            
            for i, totem in enumerate(totems):
                vnum = totem[2]
                x = totem[4]
                y = totem[5]
                direction = totem[6]
                
                self.lua += f"    MapNpc.CreateNpcWithVnum({vnum}).At({x}, {y}).Facing({direction})"
                
                if i < len(totems) - 1:
                    self.lua += ","
                self.lua += "\n"
            
            self.lua += "})\n"
            
            if lever:
                self.lua += f"""map_1.AddObjects({{
    MapObject.CreateLever().At({lever[4]}, {lever[5]}).OnTrigger({{
    }}),
}})"""

    def get_result(self):
        return (self.lua)
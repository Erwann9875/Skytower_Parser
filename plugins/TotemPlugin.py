import logging
from plugin import Plugin

class TotemPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        lever = next((line for line in cleaned_lines if line[0] == "in" and line[1] == "9"), None)
        consecutive_totems = []
        i = 0
        
        while i < len(cleaned_lines):
            if (cleaned_lines[i][0] == "in" and 
                cleaned_lines[i][1] == "2" and 
                cleaned_lines[i][2] == "1457"):
                current_group = [cleaned_lines[i]]
                j = i + 1
                
                while j < len(cleaned_lines):
                    if (cleaned_lines[j][0] == "in" and 
                        cleaned_lines[j][1] == "2" and 
                        cleaned_lines[j][2] == "1457"):
                        current_group.append(cleaned_lines[j])
                        j += 1
                    elif cleaned_lines[j][0] == "ctl":
                        j += 1
                    else:
                        break

                if current_group:
                    consecutive_totems = current_group
                    break
                
                i = j
            else:
                i += 1

        if consecutive_totems:
            self.lua = "map_1.AddNpcs({\n"
            
            for idx, totem in enumerate(consecutive_totems):
                vnum = totem[2]
                x = totem[4]
                y = totem[5]
                direction = totem[6]
                
                self.lua += f"    MapNpc.CreateNpcWithVnum({vnum}).At({x}, {y}).Facing({direction})"
                
                if idx < len(consecutive_totems) - 1:
                    self.lua += ","
                self.lua += "\n"
            
            self.lua += "})\n"
            
            if lever:
                self.lua += f"""
map_1.AddObjects({{
    MapObject.CreateLever().At({lever[4]}, {lever[5]}).OnTrigger({{
    }}),
}})"""

    def get_result(self):
        return self.lua
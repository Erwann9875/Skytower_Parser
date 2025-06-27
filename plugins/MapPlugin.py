import logging
from plugin import Plugin

class MapPlugin(Plugin):
    def __init__(self):
        self.map_lua = ""

    async def process(self, cleaned_lines):
        rsfp_info = next(((line[1], line[2]) for line in cleaned_lines if line[0] == "rsfp"), None)
        map_id = next((line[2] for line in cleaned_lines if line[0] == "at"), None)

        if rsfp_info and map_id:
            self.map_lua = f"local map_1 = Map.Create().WithMapId({map_id}).SetMapCoordinates({rsfp_info[0]}, {rsfp_info[1]})"

    def get_result(self):
        return (self.map_lua)
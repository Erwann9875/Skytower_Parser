import logging
from plugin import Plugin

class EndPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        at = next((line for line in cleaned_lines if line[0] == "at"), None)
        rbr2_plugin = self.input_from_other_plugins.get('Rbr2Plugin', None)

        if at and rbr2_plugin:
            floor_level = rbr2_plugin[0]
            self.lua = f"""local skyTower = SkyTower.Create({floor_level})  -- SkyTower Floor Level
    .SetMaps({{map_1}})
    .SetSpawn(Location.InMap(map_1).At({at[3]}, {at[4]}))
    .SetLives(1)
    .SetObjectives(objectives)
    .SetDurationInSeconds(1200)
    .SkyTowerDurationInSeconds(600)
    .SetBonusPointItemDropChance(5000)
return skyTower"""

    def get_result(self):
        return self.lua
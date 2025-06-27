import logging
from plugin import Plugin

class SkyTowerPlugin(Plugin):
    def __init__(self):
        pass

    async def process(self, cleaned_lines):
        basic_plugin = self.input_from_other_plugins.get('BasicPlugin', None)
        rbr2_plugin = self.input_from_other_plugins.get('Rbr2Plugin', None)
        map_plugin = self.input_from_other_plugins.get('MapPlugin', None)
        totem_plugin = self.input_from_other_plugins.get('TotemPlugin', None)
        monster_plugin = self.input_from_other_plugins.get('MonsterPlugin', None)
        end_plugin = self.input_from_other_plugins.get("EndPlugin", None)

        lua_content = basic_plugin + "\n" + map_plugin + "\n\n" + totem_plugin + "\n" + monster_plugin + "\n\n" + end_plugin

        file_name = f"output/skytower_{rbr2_plugin[0]}.lua"

        with open(file_name, 'w') as lua_file:
            lua_file.write(lua_content)

        logging.info(f"Lua file generated at {file_name}")

    def get_result(self):
        return None
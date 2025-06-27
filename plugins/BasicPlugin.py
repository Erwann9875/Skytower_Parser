import logging
from plugin import Plugin

class BasicPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        rbr2_plugin = self.input_from_other_plugins.get('Rbr2Plugin', None)

        if rbr2_plugin and rbr2_plugin[0] > 0:
            self.lua = f"-- SkyTower Script Floor {rbr2_plugin[0]}"
        else:
            self.lua = "-- SkyTower Script"

        self.lua += """
local Map = require('Map')
local Monster = require('Monster')
local Event = require('Event')
local MapObject = require('MapObject')
local MapNpc = require('MapNpc')
local MonsterWave = require('MonsterWave')
local Portal = require('Portal')
local Location = require('Location')
local SkyTower = require('SkyTower')
local PortalType = require("PortalType")
local PortalMinimapOrientation = require('PortalMinimapOrientation')
local SkyTowerObjective = require('SkyTowerObjective')
local SkyTowerTaskType = require('SkyTowerTaskType')
local SkyTowerTask = require('SkyTowerTask')
local SkyTowerFinishType = require('SkyTowerFinishType')

local objectives = SkyTowerObjective.Create()
    .WithProtectNPC()
        """

    def get_result(self):
        return self.lua
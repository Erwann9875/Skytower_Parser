-- SkyTower Script Floor 5
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
        
local map_1 = Map.Create().WithMapId(5440).SetMapCoordinates(6, 4)

map_1.AddNpcs({
    MapNpc.CreateNpcWithVnum(1457).At(38, 39).Facing(0),
})
map_1.AddObjects({
    MapObject.CreateLever().At(39, 39).OnTrigger({
    }),
})
map_1.AddMonsterWaves({
    MonsterWave.CreateWithDelay(0).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(6),
        Monster.CreateWithVnum(700).At(39, 6).Facing(6),
        Monster.CreateWithVnum(700).At(39, 74).Facing(6),
        Monster.CreateWithVnum(691).At(40, 73).Facing(5),
        Monster.CreateWithVnum(700).At(25, 10).Facing(0),
    }),
    MonsterWave.CreateWithDelay(30).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(0),
        Monster.CreateWithVnum(700).At(39, 6).Facing(4),
        Monster.CreateWithVnum(700).At(39, 74).Facing(2),
    }),
    MonsterWave.CreateWithDelay(60).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(7),
        Monster.CreateWithVnum(776).At(38, 7).Facing(7),
        Monster.CreateWithVnum(700).At(39, 6).Facing(1),
        Monster.CreateWithVnum(700).At(39, 74).Facing(7),
        Monster.CreateWithVnum(691).At(41, 7).Facing(4),
        Monster.CreateWithVnum(694).At(72, 40).Facing(7),
    }),
    MonsterWave.CreateWithDelay(90).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(2),
        Monster.CreateWithVnum(700).At(39, 6).Facing(2),
        Monster.CreateWithVnum(700).At(39, 74).Facing(7),
        Monster.CreateWithVnum(694).At(72, 40).Facing(7),
    }),
    MonsterWave.CreateWithDelay(120).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(1),
        Monster.CreateWithVnum(721).At(6, 40).Facing(2),
        Monster.CreateWithVnum(700).At(39, 6).Facing(6),
        Monster.CreateWithVnum(700).At(39, 74).Facing(0),
        Monster.CreateWithVnum(721).At(40, 74).Facing(1),
        Monster.CreateWithVnum(721).At(33, 31).Facing(1),
        Monster.CreateWithVnum(691).At(41, 73).Facing(0),
        Monster.CreateWithVnum(700).At(43, 6).Facing(5),
        Monster.CreateWithVnum(694).At(72, 40).Facing(1),
        Monster.CreateWithVnum(721).At(73, 42).Facing(3),
    }),
    MonsterWave.CreateWithDelay(150).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(1),
        Monster.CreateWithVnum(721).At(6, 40).Facing(2),
        Monster.CreateWithVnum(700).At(39, 6).Facing(2),
        Monster.CreateWithVnum(700).At(39, 74).Facing(1),
        Monster.CreateWithVnum(721).At(40, 74).Facing(4),
        Monster.CreateWithVnum(721).At(32, 38).Facing(6),
        Monster.CreateWithVnum(694).At(72, 40).Facing(3),
        Monster.CreateWithVnum(721).At(73, 42).Facing(2),
    }),
    MonsterWave.CreateWithDelay(180).WithMonsters({
        Monster.CreateWithVnum(694).At(6, 39).Facing(1),
        Monster.CreateWithVnum(721).At(6, 40).Facing(7),
        Monster.CreateWithVnum(691).At(37, 6).Facing(5),
        Monster.CreateWithVnum(700).At(39, 6).Facing(3),
        Monster.CreateWithVnum(700).At(39, 74).Facing(3),
        Monster.CreateWithVnum(721).At(40, 74).Facing(4),
        Monster.CreateWithVnum(721).At(6, 38).Facing(2),
        Monster.CreateWithVnum(776).At(42, 74).Facing(2),
        Monster.CreateWithVnum(694).At(72, 40).Facing(7),
        Monster.CreateWithVnum(721).At(73, 42).Facing(1),
    }),
})

local skyTower = SkyTower.Create(5)  -- SkyTower Floor Level
    .SetMaps({map_1})
    .SetSpawn(Location.InMap(map_1).At(38, 36))
    .SetLives(1)
    .SetObjectives(objectives)
    .SetDurationInSeconds(1200)
    .SkyTowerDurationInSeconds(600)
    .SetBonusPointItemDropChance(5000)
return skyTower
import logging
from plugin import Plugin

class MonsterPlugin(Plugin):
    def __init__(self):
        self.lua = ""

    async def process(self, cleaned_lines):
        monster_waves = []
        current_wave_monsters = []
        wave_delay = 0
        in_wave = False
        
        i = 0
        while i < len(cleaned_lines):
            line = cleaned_lines[i]
            
            if line[0] == "msgi" and len(line) > 2 and line[2] == "679":
                if i > 0:
                    prev_line = cleaned_lines[i - 1]
                    if prev_line[0] == "in" and prev_line[1] == "3":
                        vnum = prev_line[2]
                        x = prev_line[4]
                        y = prev_line[5]
                        direction = prev_line[6]
                        
                        if not in_wave:
                            current_wave_monsters = [{
                                'vnum': vnum,
                                'x': x,
                                'y': y,
                                'direction': direction
                            }]
                            in_wave = True
                
                i += 1
                while i < len(cleaned_lines):
                    next_line = cleaned_lines[i]
                    
                    if next_line[0] == "in" and next_line[1] == "3":
                        vnum = next_line[2]
                        x = next_line[4]
                        y = next_line[5]
                        direction = next_line[6]
                        
                        current_wave_monsters.append({
                            'vnum': vnum,
                            'x': x,
                            'y': y,
                            'direction': direction
                        })
                        i += 1
                    elif next_line[0] == "msgi":
                        i += 1
                    else:
                        break
                
                if current_wave_monsters:
                    monster_waves.append({
                        'delay': wave_delay,
                        'monsters': current_wave_monsters
                    })
                    current_wave_monsters = []
                    wave_delay += 30
                    in_wave = False
                continue
            
            i += 1
        
        if monster_waves:
            self.lua = "map_1.AddMonsterWaves({\n"
            
            for wave in monster_waves:
                self.lua += f"    MonsterWave.CreateWithDelay({wave['delay']}).WithMonsters({{\n"
                
                for monster in wave['monsters']:
                    self.lua += f"        Monster.CreateWithVnum({monster['vnum']}).At({monster['x']}, {monster['y']}).Facing({monster['direction']}),\n"
                
                self.lua += "    }),\n"
            
            self.lua += "})"
            
            logging.info(f"Generated {len(monster_waves)} monster waves")

    def get_result(self):
        return self.lua
#!/usr/bin/env python3

from packet_processor import PacketProcessor
from plugin import Plugin
import asyncio
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

def load_plugins(processor, plugin_directory="plugins"):
    plugin_files = [f for f in os.listdir(plugin_directory) if f.endswith(".py")]
    for plugin_file in plugin_files:
        plugin_module = plugin_file[:-3]
        try:
            module = __import__(f"{plugin_directory}.{plugin_module}", fromlist=[plugin_directory])
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj is not Plugin:
                    processor.register_plugin(obj, obj.__name__)
        except Exception as e:
            logging.error(f"Err loading plugin: [{plugin_module}]: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python3 main.py <input_file>")
        sys.exit(84)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        logging.error(f"Error: File '{input_file}' not found.")
        sys.exit(84)

    processor = PacketProcessor()
    load_plugins(processor)
    plugin_order = ["Rbr2Plugin", "BasicPlugin", "MapPlugin", "TotemPlugin", "MonsterPlugin", "EndPlugin", "SkyTowerPlugin"]
    processor.set_plugin_order(plugin_order)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    asyncio.run(processor.process_packet(lines))
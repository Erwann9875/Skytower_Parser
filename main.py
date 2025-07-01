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

async def process_file(processor, filepath):
    logging.info(f"Processing file: {filepath}")
    
    encodings = ['utf-8', 'windows-1252', 'latin-1', 'iso-8859-1', 'cp1252']
    lines = None
    successful_encoding = None
    
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                lines = file.readlines()
            successful_encoding = encoding
            break
        except UnicodeDecodeError:
            continue
    
    if lines is None:
        logging.error(f"Error: Could not decode file '{filepath}' with any of the attempted encodings: {encodings}")
        return
    
    try:
        logging.info(f"Successfully read {filepath} with encoding: {successful_encoding}")
        await processor.process_packet(lines)
        logging.info(f"Successfully processed: {filepath}")
    except Exception as e:
        logging.error(f"Error processing file '{filepath}': {e}")

async def process_all_files(processor, input_directory):
    files_processed = 0
    
    for filename in sorted(os.listdir(input_directory)):
        filepath = os.path.join(input_directory, filename)
        
        if not os.path.isfile(filepath):
            continue
            
        await process_file(processor, filepath)
        files_processed += 1
    
    return files_processed

if __name__ == "__main__":
    input_directory = "input"
    
    if not os.path.exists(input_directory):
        logging.error(f"Error: Input directory '{input_directory}' not found.")
        sys.exit(84)
    
    if not os.listdir(input_directory):
        logging.error(f"Error: Input directory '{input_directory}' is empty.")
        sys.exit(84)

    processor = PacketProcessor()
    load_plugins(processor)
    plugin_order = ["Rbr2Plugin", "BasicPlugin", "MapPlugin", "TotemPlugin", "MonsterPlugin", "EndPlugin", "SkyTowerPlugin"]
    processor.set_plugin_order(plugin_order)

    files_count = asyncio.run(process_all_files(processor, input_directory))
    
    if files_count == 0:
        logging.warning("No files were processed.")
        sys.exit(84)
    else:
        logging.info(f"Total files processed: {files_count}")
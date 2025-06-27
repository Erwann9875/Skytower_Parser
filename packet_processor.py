import logging

class PacketProcessor:
    def __init__(self):
        self.plugins = {}
        self.plugin_order = []

    def register_plugin(self, plugin_cls, name):
        self.plugins[name] = plugin_cls()
        logging.info(f"Registered plugin: {name}")

    def set_plugin_order(self, order):
        self.plugin_order = order

    async def process_packet(self, packet):
        cleaned_lines = [line.split()[2:] for line in packet if line.split()[2:]]
        
        plugin_results = {}
        for plugin_name in self.plugin_order:
            if plugin_name in self.plugins:
                plugin = self.plugins[plugin_name]
                plugin.accept_input(plugin_results)
                await plugin.process(cleaned_lines)
                if hasattr(plugin, 'get_result'):
                    plugin_results[plugin_name] = plugin.get_result()

    def get_results(self):
        results = {}
        for plugin_name, plugin in self.plugins.items():
            if plugin_name in self.plugins and hasattr(self.plugins[plugin_name], 'get_result'):
                results[plugin_name] = plugin.get_result()
        return results
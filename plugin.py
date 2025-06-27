class Plugin:
    def __init__(self):
        self.input_from_other_plugins = {}

    def accept_input(self, input_data):
        self.input_from_other_plugins = input_data

    async def process(self, cleaned_lines):
        raise NotImplementedError("Subclasses must implement process()")
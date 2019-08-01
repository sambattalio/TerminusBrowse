#Config.py

import json, os

from debug import DEBUG

class Config():
    def __init__(self, location=None):
        if location and not os.path.isdir(location):
            self.location = location
        else:
            self.location = os.path.expanduser('~') + '/.config/commandChan/config.json'

        # load default config
        self.defaults = self._load('./src/default_config.json')
        if not self.defaults:
            DEBUG('ERROR: No default file')

        # load user config
        self.config = self._load(self.location)
        if not self.config:
            self.config = self.defaults
            self.write(self.defaults)

    def get(self, key):
        if self.config.get(key, None):
            return self.config.get(key)
        else:
            try:
                return self.defaults[key]
            except:
                DEBUG('Error: No key {} in default config'.format(key))

    def _load(self, location):
        ''' load json from config file '''
        try:
            with open(location) as cfg:
                return json.load(cfg)
        except:
            # add default config to location
            DEBUG('File {} does not exist'.format(location))
            return None

    def write(self, data):
        ''' overwrites config file with data '''
        os.makedirs(os.path.dirname(self.location), exist_ok=True)
        with open(self.location, 'w') as cfg:
            json.dump(data, cfg, indent=4)

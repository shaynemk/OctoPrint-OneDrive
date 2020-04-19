# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class OneDrivePlugin(octoprint.plugin.StartupPlugin,
                     octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

__plugin_name__ = "OneDrive for Octoprint"
__plugin_pythoncompat__ = ">=2.7,<4"
#__plugin_implementation__ = OneDrivePlugin()

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = OneDrivePlugin()
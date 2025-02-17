### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class {{ cookiecutter.plugin_title | replace(' ', '_') }}Plugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.StartupPlugin
):
    def __init__(self):
        super().__init__()

        defaults = self.get_settings_defaults()
        self._enabled = defaults["enabled"]

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            "enabled": True,
        }

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.read_settings()

    def read_settings(self):
        self._enabled = self._settings.getBoolean(["enabled"])

    def write_settings(self):
        self._settings.setBoolean(["enabled"], self._enabled)
        self._settings.save()

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return {
            "js": ["js/{{ cookiecutter.plugin_identifier }}.js"],
            "css": ["css/{{ cookiecutter.plugin_identifier }}.css"],
            "less": ["less/{{ cookiecutter.plugin_identifier }}.less"]
        }

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        return [
            {
                "type": "settings",
                "name": "{{ cookiecutter.plugin_title }} Plugin",
                "template": "{{ cookiecutter.plugin_identifier }}_settings.jinja2",
                "custom_bindings": True,
            },
            {
                "type": "tab",
                "name": "{{ cookiecutter.plugin_title }}",
                "template": "{{ cookiecutter.plugin_identifier }}_tab.jinja2",
                "custom_bindings": True,
                "icon": "fas fa-power-off",
            },
            {
                "type": "sidebar",
                "name": "{{ cookiecutter.plugin_title }}",
                "template": "{{ cookiecutter.plugin_identifier }}_sidebar.jinja2",
                "custom_bindings": True,
                "icon": "fas fa-power-off",
            },
        ]

    ##~~ StartupPlugin mixin

    def on_after_startup(self):
        self.read_settings()

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "{{ cookiecutter.plugin_identifier }}": {
                "displayName": "{{ cookiecutter.plugin_title }} Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "{{cookiecutter.github_username}}",
                "repo": "{{cookiecutter.repo_name}}",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/archive/{target_version}.zip",
            }
        }


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "{{ cookiecutter.plugin_title }} Plugin"


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = {{ cookiecutter.plugin_title | replace(' ', '_') }}Plugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

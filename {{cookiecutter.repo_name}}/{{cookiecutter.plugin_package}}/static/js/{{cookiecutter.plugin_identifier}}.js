/*
 * View model for {{ cookiecutter.plugin_name }}
 *
 * Author: {{cookiecutter.full_name}}
 * License: {{cookiecutter.plugin_license}}
 */
$(function() {
    function {{ cookiecutter.plugin_title | replace(' ', '_') }}ViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        self.settingsView = parameters[0];
        // self.loginStateViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
        self.enabled = ko.observable(false);

        self.onBeforeBinding = function () {
            self._settings = self.settingsView.settings.plugins.poweroffafterprint;
            self._updateSettings(self._settings, self);
        };

        self.onSettingsBeforeSave = function () {
            self._updateSettings(self, self._settings);
        };

        self._updateSettings = function (source, target) {
            target.enabled(source.enabled());
        };

    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: {{ cookiecutter.plugin_title | replace(' ', '_') }}ViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "settingsViewModel", /* "loginStateViewModel" */ ],
        // Elements to bind to, e.g. #settings_plugin_{{ cookiecutter.plugin_identifier }}, #tab_plugin_{{ cookiecutter.plugin_identifier }}, ...
        elements: [
            "#settings_plugin_{{ cookiecutter.plugin_identifier }}",
            "#sidebar_plugin_{{ cookiecutter.plugin_identifier }}",
            "#tab_plugin_{{ cookiecutter.plugin_identifier }}",
        ]
    });
});

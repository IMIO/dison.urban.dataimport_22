# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromImportSettings


class DisonImporterSettingsForm(ImporterSettingsForm):
    """ """

class DisonImporterSettings(ImporterSettings):
    """ """
    form = DisonImporterSettingsForm


class DisonImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = DisonImporterSettings


class DisonImporterFromImportSettings(UrbawebImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(DisonImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings

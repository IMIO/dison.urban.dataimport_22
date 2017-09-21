# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dison.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dison.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dison.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dison.urban.dataimport'))

    def test_uninstall(self):
        """Test if dison.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['dison.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('dison.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDisonUrbanDataimportLayer is registered."""
        from dison.urban.dataimport.interfaces import IDisonUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IDisonUrbanDataimportLayer in utils.registered_layers())

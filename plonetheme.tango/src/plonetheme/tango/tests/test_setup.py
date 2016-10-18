# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.tango.testing import PLONETHEME_TANGO_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.tango is properly installed."""

    layer = PLONETHEME_TANGO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.tango is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.tango'))

    def test_browserlayer(self):
        """Test that IPlonethemeTangoLayer is registered."""
        from plonetheme.tango.interfaces import (
            IPlonethemeTangoLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeTangoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_TANGO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.tango'])

    def test_product_uninstalled(self):
        """Test if plonetheme.tango is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.tango'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeTangoLayer is removed."""
        from plonetheme.tango.interfaces import \
            IPlonethemeTangoLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeTangoLayer, utils.registered_layers())

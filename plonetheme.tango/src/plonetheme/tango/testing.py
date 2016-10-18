# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.tango


class PlonethemeTangoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.tango)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.tango:default')


PLONETHEME_TANGO_FIXTURE = PlonethemeTangoLayer()


PLONETHEME_TANGO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_TANGO_FIXTURE,),
    name='PlonethemeTangoLayer:IntegrationTesting'
)


PLONETHEME_TANGO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_TANGO_FIXTURE,),
    name='PlonethemeTangoLayer:FunctionalTesting'
)


PLONETHEME_TANGO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_TANGO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeTangoLayer:AcceptanceTesting'
)

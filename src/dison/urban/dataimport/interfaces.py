# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from imio.urban.dataimport.interfaces import IUrbanDataImporter


class IDisonUrbanDataimportLayer(IDefaultPloneLayer):
    """ Marker interface that defines a Zope 3 browser layer."""


class IDisonDataImporter(IUrbanDataImporter):
    """ Marker interface for IDison urbaweb importer """

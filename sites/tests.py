# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse

from sites.models import Site

class SiteViewsBaseTests(TestCase):

    def setUp(self):
        site = Site.allSites.create(name='ABC')
        site.sitevalues_set.create(aValue=1.1, bValue=2.6)
        site.sitevalues_set.create(aValue=2.4, bValue=2.9)
        site.sitevalues_set.create(aValue=4.5, bValue=10.6)

class SiteSummationViewsTests(SiteViewsBaseTests):

    def test_summation(self):
        response = self.client.get(reverse('getSumOfSiteValues'))
        site = response.context['sitesSummary'][0]
        self.assertEqual(site.name, 'ABC')
        self.assertAlmostEqual(site.aggregateAValue, 8.0, places=2)
        self.assertAlmostEqual(site.aggregateBValue, 16.1, places=2)

    def test_average(self):
        response = self.client.get(reverse('getAverageOfSiteValues'))
        site = response.context['sitesSummary'][0]
        self.assertEqual(site.name, 'ABC')
        self.assertAlmostEqual(site.aggregateAValue, 2.666, places=2)
        self.assertAlmostEqual(site.aggregateBValue, 5.366, places=2)

class SiteAverageViewsTests(SiteViewsBaseTests):

    def test_average(self):
        response = self.client.get(reverse('getAverageOfSiteValues'))
        site = response.context['sitesSummary'][0]
        self.assertEqual(site.name, 'ABC')
        self.assertAlmostEqual(site.aggregateAValue, 2.666, places=2)
        self.assertAlmostEqual(site.aggregateBValue, 5.366, places=2)

class SiteDetailViewTests(SiteViewsBaseTests):

    def compareSiteValues(self, siteValue, aValue, bValue):
        self.assertEqual(siteValue.aValue, aValue)
        self.assertEqual(siteValue.bValue, bValue)

    def test_summation(self):
        response = self.client.get(reverse('siteDetail', kwargs={'pk':1}))
        siteValues = response.context['siteValues']
        self.compareSiteValues(siteValues[0], 1.1, 2.6)
        self.compareSiteValues(siteValues[1], 2.4, 2.9)
        self.compareSiteValues(siteValues[2], 4.5, 10.6)



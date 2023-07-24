from django.test import SimpleTestCase, override_settings
from django.apps import apps


@override_settings(INSTALLED_APPS=['django_quanttide_hr.apps.DjangoPackageConfig'])
class AppConfigTestCase(SimpleTestCase):
    def test_install_app(self):
        self.assertTrue(apps.is_installed('django_quanttide_hr'))
        app_config = apps.get_app_config('django_quanttide_hr')
        self.assertEqual('django_quanttide_hr', app_config.name)

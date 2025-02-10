import helpers

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATIC_VENDOR_DIR = getattr(settings, "STATIC_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js.map"
}


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATIC_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stderr.write(
                    self.style.ERROR(f"Failed to download {name} from {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All vendor files downloaded successfully")
            )
        else:
            self.stderr.write(
                self.style.WARNING(
                    "Some files were not downloaded successfully")
            )

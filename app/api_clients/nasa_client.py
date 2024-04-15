import requests
from django.conf import settings
from django.db.models import TextChoices
from pydantic import BaseModel


class NasaCamerasChoices(TextChoices):
    FHAZ = "Front Hazard Avoidance Camera"
    NAVCAM = "Navigation Camera"
    MAST = "Mast Camera"
    CHEMCAM = "Chemistry and Camera Complex"
    MAHLI = "Mars Hand Lens Imager"
    MARDI = "Mars Descent Imager"
    RHAZ = "Rear Hazard Avoidance Camera"


class MarsImageLink(BaseModel):
    img_src: str


class MarsImageLinkList(BaseModel):
    mars_photos: list[MarsImageLink]


class NasaClient:
    api_key = settings.NASA_API_KEY
    base_url = settings.NASA_BASE_URL

    def get_mars_photos(
        self, camera: NasaCamerasChoices, earth_date: str, page_number: int = 0
    ):
        """
        Returns a list of mars photos for a given camera and earth day.
        """
        params: dict = {
            "api_key": self.api_key,
            "cameras": camera,
            "earth_date": earth_date,
            "page": page_number,
        }
        mars_photos = requests.get(self.base_url, params=params).json()["photos"]
        return MarsImageLinkList(
            mars_photos=[
                MarsImageLink(img_src=mars_photo["img_src"])
                for mars_photo in mars_photos
            ]
        )


nasa_client = NasaClient()

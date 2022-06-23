from django.db import models
from main import models as main_models


class UserProfile(main_models.BaseModel):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="user_profile"
    )

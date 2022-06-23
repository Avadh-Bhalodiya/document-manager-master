from django.db import models
from main import models as main_models


class DocumentTemplate(main_models.BaseModel):
    name = models.CharField(max_length=200)
    document = models.FileField()
    variable_config = models.JSONField()


class GeneratedDocument(main_models.BaseModel):
    template = models.ForeignKey("document.DocumentTemplate", on_delete=models.PROTECT)
    variables = models.JSONField()
    document = models.FileField()
    generated_by = models.ForeignKey("core.UserProfile", on_delete=models.PROTECT)

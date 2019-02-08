from django.db import models
from datetime import datetime
# Create your models here.


class ApiNameSpace(models.Model):

    namespace = models.CharField(max_length=100)

    def __str__(self):
        return self.namespace


class ApiProject(models.Model):

    project_name = models.CharField(max_length=1000)
    namespace = models.ForeignKey(ApiNameSpace, on_delete=models.CASCADE, related_name="namespace_project")
    project_description = models.CharField(max_length=1000, default="", blank=True)
    project_host = models.CharField(max_length=100, default="")
    project_env = models.CharField(max_length=10, default="")
    project_creater = models.CharField(max_length=100, default="")
    project_create_date = models.DateTimeField("createTime", default=datetime.now)
    project_swagger = models.TextField(default="")
    project_swagger_one = models.TextField(default="")
    project_swagger_url = models.CharField(max_length=100, default="")
    project_document_type = models.CharField(max_length=100, default="")
    project_delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name


class ApiEnv(models.Model):

    project_name = models.ForeignKey(ApiProject, on_delete=models.CASCADE)
    env_name = models.CharField(max_length=100, default="")
    env_description = models.CharField(max_length=100, default="")
    env_delete_flag = models.BooleanField(default=False)
    env_host = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.env_name

class ApiApi(models.Model):

    project_name = models.ForeignKey(ApiProject, on_delete=models.CASCADE)
    # api_name = models.CharField(max_length=100, default="")
    path = models.CharField(max_length=100, default="")
    # api_schemes = models.CharField(max_length=100, default="http")
    api_summary = models.CharField(max_length=100, default="", null=True)
    api_operationId = models.CharField(max_length=100, default="", null=True)
    api_requset_type = models.CharField(max_length=100, default="")
    api_request_method = models.CharField(max_length=100, default="", null=True)
    api_security = models.CharField(max_length=100, default="", null=True)
    api_tags = models.CharField(max_length=100, default="", null=True)
    api_tags_description = models.CharField(max_length=100, default="", null=True)
    api_delete_flag = models.BooleanField(default=False)
    api_env = models.CharField(max_length=100, default="", null=True)

    def __str__(self):
        return self.api_summary


class ApiParameters(models.Model):

    api_id = models.ForeignKey(ApiApi, on_delete=models.CASCADE)
    param_kind = models.CharField(max_length=100, default="")
    param_name = models.CharField(max_length=100, default="")
    param_in = models.CharField(max_length=100, default="")
    param_description = models.CharField(max_length=100, default="", null=True)
    param_required = models.BooleanField(default=1)
    param_type = models.CharField(max_length=1000, default="", null=True)
    param_default = models.CharField(max_length=1000, default="", null=True)
    param_schema = models.CharField(max_length=1000, default="", null=True)
    param_ref = models.CharField(max_length=1000, default="", null=True)
    param_delete_flag = models.BooleanField(default=False)


class ApiSchemasDefine(models.Model):
    define_name = models.CharField(max_length=100, default="", null=True)
    project_name = models.ForeignKey(ApiProject, on_delete=models.CASCADE)
    define_type = models.CharField(max_length=100, default="", null=True)
    define_description = models.CharField(max_length=100, default="", null=True)
    define_delete_flag = models.BooleanField(default=False)


class ApiSchemasStructure(models.Model):
    define_name = models.ForeignKey(ApiSchemasDefine,  on_delete=models.CASCADE)
    structure_type = models.CharField(max_length=100, default="", null=True)
    structure_ref = models.CharField(max_length=100, default="", null=True)
    structure_kind = models.CharField(max_length=100, default="", null=True)
    structure_key = models.CharField(max_length=100, default="", null=True)
    structure_description = models.CharField(max_length=100, default="", null=True)
    structure_format = models.CharField(max_length=100, default="", null=True)
    structure_in = models.CharField(max_length=100, default="", null=True)
    structure_enum = models.CharField(max_length=100, default="", null=True)
    structure_items = models.CharField(max_length=100, default="", null=True)
    structure_required = models.BooleanField(default=False)
    structure_example = models.CharField(max_length=100, default="", null=True)
    structure_delete_flag = models.BooleanField(default=False)


class ApiTestResultField(models.Model):
    api_id = models.ForeignKey(ApiApi, on_delete=models.CASCADE)
    result_key = models.CharField(max_length=100, default="", null=True)
    result_type = models.CharField(max_length=100, default="", null=True)

class ApiTestCase(models.Model):
    api_id = models.ForeignKey(ApiApi, on_delete=models.CASCADE)
    case_num = models.IntegerField(null=True)
    case_header = models.TextField(null=True)
    case_path = models.TextField(null=True)
    case_param = models.TextField(null=True)
    case_body = models.TextField(null=True)
    case_response = models.TextField(null=True)
    case_description = models.CharField(max_length=1000, default="", null=True)
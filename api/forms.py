# -*- coding: utf-8 -*-
from django import forms
from django.forms import BaseFormSet
from django.forms.fields import BooleanField, IntegerField
from .models import *
from .lib import testcase_handle
from api.lib import noty

PROJECT_CREATE_TYPE = (("直接创建", "直接创建"),
                       # ("Swagger_2.0", "Swagger_2.0"),
                       # ("OpenApi_3.0", "OpenApi_3.0"),
                       )

TYPE_CHOICE = (("input", "输入"),
               ("empty", "为空"),
               ("kwags", "参数"),
               ("script", "脚本"),)

RESULT_TYPE_CHOICE = (('Str', 'Str'),
                      ('Int', 'Int'),
                      ('Bool', 'Bool'),
                      ('List', 'List'),
                      ('script', '脚本'),
                      ('Dict', 'Dict'),)

RESULT_LOGIC_CHOICE = (("no", "不判断"),
                       ('=', '等于'),
                       ('>', '大于'),
                       ('<', '小于'),
                       ('in', '包含'),)

def tmp_handle(target):
    re_data = eval(target)
    return re_data


class CreateProject(forms.Form):

    project_document_type = forms.ChoiceField(choices=PROJECT_CREATE_TYPE)
    namespace = forms.ChoiceField()
    swagger_url = forms.CharField(required=False)
    project_name = forms.CharField(max_length=1000)
    project_host = forms.CharField(max_length=1000)
    project_description = forms.CharField(required=False)


    def __init__(self, *args, **kwargs):
        super(CreateProject, self).__init__(*args, **kwargs)
        self.fields['namespace'].widget.attrs["class"] = "form-control"
        self.fields['project_document_type'].widget.attrs["class"] = "form-control"
        self.fields['swagger_url'].widget.attrs["class"] = "form-control"
        self.fields['namespace'].choices = ((x.pk, x.namespace) for x in ApiNameSpace.objects.all())
        self.fields['project_name'].widget.attrs["class"] = "form-control"
        self.fields['project_host'].widget.attrs["class"] = "form-control"
        self.fields['project_description'].widget.attrs["class"] = "form-control"


class TestCase(forms.Form):


    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        class_get_params = kwargs["initial"]["params_key"]
        testcase_objs = kwargs["initial"]["testcase_objs"]
        api_id  = kwargs["initial"]["api_id"]

        params_header_field, params_header_type = class_get_params.get_params_header_field()
        params_path_field, params_path_type = class_get_params.get_params_path_field()
        params_query_field, params_query_type = class_get_params.get_params_query_field()
        request_body_field, request_body_type = class_get_params.get_request_body_field()
        result_field, result_type = class_get_params.get_result_field()

        if testcase_objs:
            case_num = int(kwargs['prefix'][5:]) + 1
            case_obj = ApiTestCase.objects.get(api_id_id=api_id, case_num=case_num)
            header_tmp_dict = case_obj.case_header
            path_tmp_dict = case_obj.case_path
            query_tmp_dict = case_obj.case_param
            body_tmp_dict = case_obj.case_body
            result_tmp_dict = case_obj.case_response

            header_dict = tmp_handle(header_tmp_dict)
            path_dict = tmp_handle(path_tmp_dict)
            query_dict = tmp_handle(query_tmp_dict)
            body_dict = tmp_handle(body_tmp_dict)
            result_dict = tmp_handle(result_tmp_dict)

            for header in params_header_field:
                fields_name = 'header_' + header
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                try:
                    self.fields[fields_name].initial = header_dict[fields_name]
                except Exception as err:
                    print(err)

                fields_type = 'type_header_' + header
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = header_dict[fields_type]
                except Exception as err:
                    print(err)

            for path in params_path_field:
                fields_name = 'path_' + path
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                try:
                    self.fields[fields_name].initial = path_dict[fields_name]
                except Exception as err:
                    print(err)

                fields_type = 'type_path_' + path
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = path_dict[fields_type]
                except Exception as err:
                    print(err)

            for query in params_query_field:
                fields_name = 'query_' + query
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                try:
                    self.fields[fields_name].initial = query_dict[fields_name]
                except Exception as err:
                    print(err)

                fields_type = 'type_query_' + query
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = query_dict[fields_type]
                except Exception as err:
                    print(err)

            for body in request_body_field:
                fields_name = 'body_' + body
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                try:
                    self.fields[fields_name].initial = body_dict[fields_name]
                except Exception as err:
                    print(err)

                fields_type = 'type_body_' + body
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = body_dict[fields_type]
                except Exception as err:
                    print(err)

            for resulte in result_field:
                fields_name = 'result_expect_value_' + resulte
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                try:
                    self.fields[fields_name].initial = result_dict[fields_name]
                except Exception as err:
                    print(err)





                fields_type = 'type_result_' + resulte
                self.fields[fields_type] = forms.ChoiceField(choices=RESULT_TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = result_dict[fields_type]
                except Exception as err:
                    print(err)

                fields_type = 'logic_result_' + resulte
                self.fields[fields_type] = forms.ChoiceField(choices=RESULT_LOGIC_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                try:
                    self.fields[fields_type].initial = result_dict[fields_type]
                except Exception as err:
                    print(err)

                fields_name = 'result_response_value_' + resulte
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                self.fields[fields_name].widget.attrs["readonly"] = True

                try:
                    judge_result = result_dict.get("judge_result_{}".format(resulte))
                    if judge_result == "no_judge":
                        self.fields[fields_name].widget.attrs["style"] = "width:100%;  background: #9ba3af"
                    elif judge_result:
                        self.fields[fields_name].widget.attrs["style"] = "width:100%;  background: aquamarine"
                    else:
                        self.fields[fields_name].widget.attrs["style"] = "width:100%;  background: #FFE4E1"
                except Exception as err:
                    print(err)
                    judge_result = "no_judge"


                try:
                    if judge_result == "no_judge":
                        pass
                    else:
                        self.fields[fields_name].initial = result_dict[fields_name]
                except Exception as err:
                    print(err)


        else:
            for header in params_header_field:
                fields_name = 'header_' + header
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False

                fields_type = 'type_header_' + header
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"

            for path in params_path_field:
                fields_name = 'path_' + path
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False

                fields_type = 'type_path_' + path
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"

            for query in params_query_field:
                fields_name = 'query_' + query
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False

                fields_type = 'type_query_' + query
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"

            for body in request_body_field:
                fields_name = 'body_' + body
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False

                fields_type = 'type_body_' + body
                self.fields[fields_type] = forms.ChoiceField(choices=TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"

            for resulte in result_field:
                fields_name = 'result_expect_value_' + resulte
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False

                fields_type = 'type_result_' + resulte
                self.fields[fields_type] = forms.ChoiceField(choices=RESULT_TYPE_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                if fields_type == "type_result_r_status":
                    self.fields[fields_type].initial = 'Str'
                if fields_type == "type_result_r_time":
                    self.fields[fields_type].initial = 'Int'

                fields_type = 'logic_result_' + resulte
                self.fields[fields_type] = forms.ChoiceField(choices=RESULT_LOGIC_CHOICE)
                self.fields[fields_type].widget.attrs["style"] = "width:100%;"
                if fields_type == "logic_result_r_status":
                    self.fields[fields_type].initial = '='
                if fields_type == "logic_result_r_time":
                    self.fields[fields_type].initial = '>'

                fields_name = 'result_response_value_' + resulte
                self.fields[fields_name] = forms.CharField()
                self.fields[fields_name].widget.attrs["style"] = "width:100%;"
                self.fields[fields_name].required = False
                self.fields[fields_name].widget.attrs["readonly"] = True


class ORDER_FIXED(BaseFormSet):

    def add_fields(self, form, index):
        """A hook for adding extra fields on to each form instance."""
        if self.can_order:
            # Only pre-fill the ordering field for initial forms.
            if index is not None and index < self.initial_form_count():
                form.fields['ORDER'] = IntegerField(label='Order', initial=index + 1, required=False)
                form.fields['ORDER'].widget.attrs["style"] = "width:30px;"
                form.fields['ORDER'].widget.attrs["readonly"] = True
            else:
                form.fields['ORDER'] = IntegerField(label='Order', required=False, initial=1)
                form.fields['ORDER'].widget.attrs["style"] = "width:30px;"
                form.fields['ORDER'].widget.attrs["readonly"] = True
        if self.can_delete:
            form.fields['DELETE'] = BooleanField(label='DELETE', required=False)

    def save(self, request, datas, api_id):
        try:
            for data in datas:
                if data["DELETE"]:
                    pass
                else:
                    testcasehandle = testcase_handle.TestCaseHandle(data=data, api_id=api_id)
                    header_dict = testcasehandle.header_dict_handle()
                    path_dict = testcasehandle.path_dict_handle()
                    query_dict = testcasehandle.query_dict_handle()
                    body_dict = testcasehandle.body_dict_handel()
                    result_dict = testcasehandle.result_dict_handle()
                    try:
                        obj = ApiTestCase.objects.get(api_id_id=api_id, case_num=data["ORDER"])
                        obj.case_header = header_dict
                        obj.case_path = path_dict
                        obj.case_param = query_dict
                        obj.case_body = body_dict
                        obj.case_response = result_dict
                        obj.save()
                    except Exception as err:
                        ApiTestCase.objects.create(case_header=header_dict,
                                                   case_path=path_dict,
                                                   case_param=query_dict,
                                                   case_body=body_dict,
                                                   case_response=result_dict,
                                                   api_id_id=api_id,
                                                   case_num=data["ORDER"])
            noty.noty(request, "保存测试用例成功", level="info")
        except Exception as err:
            print(err)
            noty.noty(request, "保存测试用例失败", level="error")









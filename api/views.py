from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from api.lib.swagger_handle import *
from api.lib import namespace_handle, params_handle
from django.forms import formset_factory
# Create your views here.


@login_required
def api_home(request):
    username = request.session.get('username')
    namespace_list = ApiNameSpace.objects.all()
    create_project_form = CreateProject()
    project_query = ApiProject.objects.all()

    ctx = {"username": username,
           "namespace_list": namespace_list,
           "create_project_form": create_project_form,
           "project_query": project_query,
           }
    return render(request, 'api-home.html', ctx)


def api_homne_namespace(request, namespace):
    print(namespace)
    username = request.session.get('username')
    namespace_list = ApiNameSpace.objects.all()
    create_project_form = CreateProject()
    namespace_obj = ApiNameSpace.objects.get(pk=namespace)
    project_query = ApiProject.objects.filter(namespace=namespace_obj, project_delete_flag=0)

    ctx = {"username": username,
           "namespace_list": namespace_list,
           "current_namespace": namespace_obj.namespace,
           "create_project_form": create_project_form,
           "project_query": project_query,
           }
    return render(request, 'api-home-namespace.html', ctx)


def api_home_api(request, namespace, project):
    username = request.session.get('username')
    current_namespace = ApiNameSpace.objects.get(pk=namespace)
    current_project = ApiProject.objects.get(pk=project)
    api_list = ApiApi.objects.filter(project_name_id=project)
    ctx = {"username": username,
           "current_namespace": current_namespace,
           "current_project": current_project,
           "api_list": api_list,
           }
    return render(request, 'api-home-api.html', ctx)


def api_home_api_doc(request, namespace_id, project_id, api_id):
    username = request.session.get('username')
    current_namespace = ApiNameSpace.objects.get(pk=namespace_id)
    current_project = ApiProject.objects.get(pk=project_id)
    current_api = ApiApi.objects.get(pk=api_id)

    class_get_params = params_handle.params_by_api(api_id)
    params_header_list =  class_get_params.get_params_header_list()
    params_path_list = class_get_params.get_params_path_list()
    params_query_list = class_get_params.get_params_query_list()
    params_request_body_list = class_get_params.get_request_body_list()

    ctx = {"username": username,
           "current_namespace": current_namespace,
           "current_project": current_project,
           "current_api": current_api,
           "params_path_list": params_path_list,
           "params_query_list": params_query_list,
           "params_request_body_list": params_request_body_list,
           "params_header_list": params_header_list
           }
    return render(request, 'api-home-api-doc.html', ctx)


def api_home_api_test(request, namespace_id, project_id, api_id):
    username = request.session.get('username')
    current_namespace = ApiNameSpace.objects.get(pk=namespace_id)
    current_project = ApiProject.objects.get(pk=project_id)
    current_api = ApiApi.objects.get(pk=api_id)
    testcase_objs = ApiTestCase.objects.filter(api_id=api_id)

    class_get_params = params_handle.params_by_api(api_id)
    params_header_field, params_header_type = class_get_params.get_params_header_field()
    params_path_field, params_path_type= class_get_params.get_params_path_field()
    params_query_field, params_query_type = class_get_params.get_params_query_field()
    request_body_field, request_body_type = class_get_params.get_request_body_field()
    result_field, result_type = class_get_params.get_result_field()

    header_len = len(params_header_field)
    path_len = len(params_path_field)
    query_len = len(params_query_field)
    body_len = len(request_body_field)
    result_len = len(result_field)

    if testcase_objs:
        TestCaseFormSet = formset_factory(form=TestCase, formset=ORDER_FIXED, can_order=True, can_delete=True, extra=0)
        TestCaseFormSets = TestCaseFormSet(initial=testcase_objs,
                                           form_kwargs={"initial":
                                                            {"params_key": class_get_params,
                                                             "testcase_objs": testcase_objs,
                                                             "api_id": api_id,
                                                             }})
    else:
        TestCaseFormSet = formset_factory(form=TestCase, formset=ORDER_FIXED, can_order=True, can_delete=True)
        TestCaseFormSets = TestCaseFormSet(initial=testcase_objs,
                                           form_kwargs={"initial":
                                                            {"params_key": class_get_params,
                                                             "testcase_objs": testcase_objs,
                                                             "api_id": api_id,
                                                             }})
    if request.method == "POST":


        TestCaseFormSets_POST = TestCaseFormSet(request.POST, form_kwargs={"initial":
                                                            {"params_key": class_get_params,
                                                             "testcase_objs": testcase_objs,
                                                             "api_id": api_id,
                                                             }})
        if "testcasesave" in request.POST:

            if TestCaseFormSets_POST.is_valid():
                temp_data = TestCaseFormSets_POST.cleaned_data
                TestCaseFormSets_POST.save(request=request, datas=temp_data, api_id=api_id)
        if "testexec" in request.POST:
            if TestCaseFormSets_POST.is_valid():
                temp_data = TestCaseFormSets_POST.cleaned_data
                TestCaseFormSets_POST.save(request=request, datas=temp_data, api_id=api_id)
                class_exec_case = testcase_handle.TestExec(api_id=api_id)
                class_exec_case.exec_case()
        return HttpResponseRedirect("/api/home/{}/{}/{}/test".format(namespace_id, project_id, api_id))
    ctx = {"username": username,
           "current_namespace": current_namespace,
           "current_project": current_project,
           "current_api": current_api,
           "header_len": header_len,
           "path_len": path_len,
           "query_len": query_len,
           "body_len": body_len,
           "result_len": result_len,
           "params_header_field": params_header_field,
           "params_header_type": params_header_type,
           "params_path_field": params_path_field,
           "params_path_type": params_path_type,
           "params_query_field": params_query_field,
           "params_query_type": params_query_type,
           "request_body_field": request_body_field,
           "request_body_type": request_body_type,
           "result_field": result_field,
           "result_type": result_type,
           "TestCaseFormSets": TestCaseFormSets
           }
    return render(request, 'api-home-test.html', ctx)






def create_project(request):
    if "submin_create_project" in request.POST:
        create_project_form_POST = CreateProject(request.POST)
        if create_project_form_POST.is_valid():
            clean_data = create_project_form_POST.cleaned_data
            if clean_data["project_document_type"] == "直接创建":
                namespace_handle.create_project(clean_data, request)
                namespace_obj= ApiNameSpace.objects.get(pk=clean_data["namespace"])
                return HttpResponseRedirect("/api/home/{}".format(namespace_obj.id))
            else:
                class_create_project = create_project_handle(namespace=clean_data['namespace'],
                                      project_document_type=clean_data['project_document_type'], request=request)
                if clean_data['project_document_type'] == "Swagger_2.0":
                    class_create_project.create_project_swagger_url(swagger_url=clean_data['swagger_url'])
                elif clean_data['project_document_type'] == "OpenApi_3.0":
                    class_create_project.create_project_openApi(swagger_url=clean_data['swagger_url'])
    return HttpResponseRedirect("/api/home")
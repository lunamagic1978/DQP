from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
import json


@csrf_exempt
def create_namespace(request):
    if request.method == "POST":
        data = request.POST
        namespace = data["namespace"]
        try:
            ApiNameSpace.objects.get(namespace=namespace)
            return JsonResponse({"msg": "namespace已经存在",
                                 "code": 300})
        except Exception:
            ApiNameSpace.objects.create(namespace=namespace)
            return JsonResponse({"msg": "namespace创建成功",
                                 "code": 200})
    else:
        return JsonResponse({"msg": "请求方法不正确",
                             "code": 400})


def get_swagger(request):

    data = {
    "swagger": "2.0",
    "info": {
        "version": "1.0",
        "title": "京东方微服务文档",
        "termsOfService": "http://www.baidu.com/",
        "contact": {
            "name": "京东方"
        }
    },
    "host": "10.8.0.208:10005",
    "basePath": "/",
    "tags": [
        {
            "name": "LoginController",
            "description": "登录相关接口"
        },
        {
            "name": "ProjectController",
            "description": "工程"
        },
        {
            "name": "UserCenterController",
            "description": "用户中心"
        }
    ],
    "paths": {
        "/empLogin": {
            "post": {
                "tags": [
                    "LoginController"
                ],
                "summary": "员工登录",
                "operationId": "empLoginUsingPOST",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "in": "body",
                        "name": "dto",
                        "description": "dto",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/员工登录字段"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project": {
            "post": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "创建工程",
                "operationId": "createProjectUsingPOST",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "in": "body",
                        "name": "createProjectRequest",
                        "description": "createProjectRequest",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/CreateCodeProjectRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project/delete/{projectId}": {
            "delete": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "删除工程",
                "operationId": "deleteProjectUsingDELETE",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    },
                    {
                        "name": "projectType",
                        "in": "query",
                        "description": "projectType",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "204": {
                        "description": "No Content"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            }
        },
        "/project/detail/{projectId}": {
            "get": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "工程详情",
                "operationId": "projectDetailUsingGET",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    },
                    {
                        "name": "projectType",
                        "in": "query",
                        "description": "projectType",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project/list": {
            "get": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "工程列表",
                "operationId": "projectListUsingGET",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "pageNo",
                        "in": "query",
                        "description": "pageNo",
                        "required": False,
                        "type": "integer",
                        "default": 1,
                        "format": "int32"
                    },
                    {
                        "name": "pageSize",
                        "in": "query",
                        "description": "pageSize",
                        "required": False,
                        "type": "integer",
                        "default": 1000,
                        "format": "int32"
                    },
                    {
                        "name": "projectType",
                        "in": "query",
                        "description": "projectType",
                        "required": False,
                        "type": "integer",
                        "default": 0,
                        "format": "int32"
                    },
                    {
                        "name": "projectStatus",
                        "in": "query",
                        "description": "projectStatus",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    },
                    {
                        "name": "keyWord",
                        "in": "query",
                        "description": "keyWord",
                        "required": False,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project/upLoadFile": {
            "post": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "上传文件",
                "operationId": "upLoadFileUsingPOST",
                "consumes": [
                    "multipart/form-data"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "file",
                        "in": "formData",
                        "description": "file",
                        "required": True,
                        "type": "file"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project/update": {
            "put": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "更改担当人",
                "operationId": "updateProjectEmployeeUsingPUT",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "in": "body",
                        "name": "updateEmployeeRequest",
                        "description": "updateEmployeeRequest",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/UpdateEmployeeRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/project/update/{projectId}": {
            "put": {
                "tags": [
                    "ProjectController"
                ],
                "summary": "更改工程状态",
                "operationId": "updateProjectStatusUsingPUT",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "integer",
                        "format": "int32"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        },
        "/userCenter/user": {
            "get": {
                "tags": [
                    "UserCenterController"
                ],
                "summary": "获取用户（担当人）",
                "operationId": "getUserUsingGET",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "*/*"
                ],
                "parameters": [
                    {
                        "name": "dfp-auth-token",
                        "in": "header",
                        "description": "token",
                        "required": True,
                        "type": "string",
                        "default": "TQMS--item--114963--item--c6209065-6822-49a3-bc66-e9939a5fddc6"
                    },
                    {
                        "name": "keyWord",
                        "in": "query",
                        "description": "keyWord",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/ResultVO"
                        }
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                }
            }
        }
    },
    "definitions": {
        "ResultVO": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string"
                },
                "data": {
                    "type": "object"
                },
                "msg": {
                    "type": "string"
                }
            }
        },
        "Employee": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string"
                },
                "id": {
                    "type": "integer",
                    "format": "int32"
                },
                "orgPath": {
                    "type": "string"
                },
                "role": {
                    "type": "integer",
                    "format": "int32"
                },
                "userCode": {
                    "type": "string"
                },
                "userName": {
                    "type": "string"
                }
            }
        },
        "员工登录字段": {
            "type": "object",
            "required": [
                "password",
                "userName"
            ],
            "properties": {
                "password": {
                    "type": "string",
                    "description": "密码"
                },
                "userName": {
                    "type": "string",
                    "description": "工号"
                }
            }
        },
        "CreateCodeProjectRequest": {
            "type": "object",
            "properties": {
                "algEmployees": {
                    "type": "array",
                    "description": "算法担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "applyEmployees": {
                    "type": "array",
                    "description": "应用担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "bspEmployees": {
                    "type": "array",
                    "description": "BSP担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "createdTime": {
                    "type": "string",
                    "format": "date-time",
                    "description": "创建日期"
                },
                "downFac": {
                    "type": "string",
                    "description": "下游厂商"
                },
                "facTconModel": {
                    "type": "string",
                    "description": "厂商Tcon型号(code工程参数)"
                },
                "fgCode": {
                    "type": "string",
                    "description": "FG Code(code工程参数)"
                },
                "figureOutInstruction": {
                    "type": "string",
                    "description": "出图说明(mask工程参数)"
                },
                "figureOutTime": {
                    "type": "integer",
                    "format": "int64",
                    "description": "出图时间(mask工程参数)"
                },
                "instructionBeTaken": {
                    "type": "string",
                    "description": "须知会担当(mask工程参数)"
                },
                "itemNo": {
                    "type": "string",
                    "description": "项目编号"
                },
                "materialNumber": {
                    "type": "string",
                    "description": "物料号(code工程参数)"
                },
                "modifiedTime": {
                    "type": "string",
                    "format": "date-time",
                    "description": "数据更新日期"
                },
                "noticeEmployees": {
                    "type": "array",
                    "description": "须知会担当(Mask工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "orderNumber": {
                    "type": "integer",
                    "format": "int32",
                    "description": "订单号(ARVR工程参数)"
                },
                "otherEmployees": {
                    "type": "array",
                    "description": "其它担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "pm": {
                    "type": "string",
                    "description": "工程项目经理"
                },
                "projectId": {
                    "type": "integer",
                    "format": "int32",
                    "description": "工程id"
                },
                "projectName": {
                    "type": "string",
                    "description": "工程名称"
                },
                "projectStatus": {
                    "type": "integer",
                    "format": "int32",
                    "description": "工程状态"
                },
                "projectType": {
                    "type": "integer",
                    "format": "int32",
                    "description": "工程类型"
                },
                "sdkEmployees": {
                    "type": "array",
                    "description": "SDK担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "upFac": {
                    "type": "string",
                    "description": "上游厂商"
                },
                "updatedTime": {
                    "type": "string",
                    "format": "date-time",
                    "description": "更新日期"
                }
            }
        },
        "UpdateEmployeeRequest": {
            "type": "object",
            "properties": {
                "employees": {
                    "type": "array",
                    "description": "SDK担当(ARVR工程参数)",
                    "items": {
                        "$ref": "#/definitions/Employee"
                    }
                },
                "projectId": {
                    "type": "integer",
                    "format": "int32",
                    "description": "工程id"
                },
                "projectType": {
                    "type": "integer",
                    "format": "int32",
                    "description": "工程类型"
                },
                "role": {
                    "type": "integer",
                    "format": "int32",
                    "description": "担当类型"
                }
            }
        }
    }
}

    # content = json.loads(data)

    return JsonResponse(data)

def mac_openapi(request):

    data = {
    "openapi": "3.0.0",
    "info": {
        "description": "用户中心",
        "version": "1.0.0",
        "title": "用户中心API",
        "contact": {
            "email": "yann.xia@daocloud.io"
        }
    },
    "servers": [
        {
            "url": "http://mac-dev.dmptesting.xyz:9050/user-center/v1",
            "description": "测试环境"
        }
    ],
    "tags": [
        {
            "name": "user",
            "description": "用户相关"
        },
        {
            "name": "project",
            "description": "项目相关"
        },
        {
            "name": "role",
            "description": "角色相关"
        },
        {
            "name": "authority",
            "description": "权限相关"
        }
    ],
    "paths": {
        "/users/me": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "当前用户信息",
                "operationId": "CurrentUser",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Me"
                                }
                            }
                        }
                    },
                    "4XX": {
                        "description": "错误返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/responses/GeneralError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{userId}": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "根据ID获得用户信息",
                "operationId": "GetUserInfoByID",
                "parameters": [
                    {
                        "in": "path",
                        "name": "userId",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "required": True,
                        "description": "user id"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "4XX": {
                        "description": "错误返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/responses/GeneralError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "user"
                ],
                "summary": "根据ID更新用户信息",
                "operationId": "UpdateUSerById",
                "parameters": [
                    {
                        "in": "path",
                        "name": "userId",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "required": True,
                        "description": "user id"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "4XX": {
                        "description": "错误返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/responses/GeneralError"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "user"
                ],
                "summary": "根据ID删除用户信息",
                "operationId": "DeleteUserById",
                "parameters": [
                    {
                        "in": "path",
                        "name": "userId",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "required": "true",
                        "description": "user id"
                    }
                ],
                "responses": {
                    "204": {
                        "description": "成功返回"
                    }
                }
            }
        },
        "/authorities": {
            "get": {
                "tags": [
                    "authority"
                ],
                "summary": "获得所有权限列表",
                "operationId": "ListAuthority",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Authority"
                                }
                            }
                        }
                    },
                    "4XX": {
                        "description": "错误返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/responses/GeneralError"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": [
                    "authority"
                ],
                "summary": "创建新权限",
                "operationId": "CreateAuthority",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "requestBody": {
                    "required": "true",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Authority"
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Authority"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/authorities/{authorityId}": {
            "put": {
                "tags": [
                    "authority"
                ],
                "summary": "更新权限",
                "operationId": "UpdateAuthority",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "authorityId",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "required": "true",
                        "description": "authority id"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Authority"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "authority"
                ],
                "summary": "删除权限",
                "operationId": "DeleteAuthority",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "authorityId",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "required": "true",
                        "description": "authority id"
                    }
                ],
                "responses": {
                    "204": {
                        "description": "成功返回"
                    }
                }
            }
        },
        "/projects": {
            "post": {
                "tags": [
                    "project"
                ],
                "summary": "创建项目",
                "security": [
                    {
                        "OAuth2": [
                            "all"
                        ]
                    }
                ],
                "operationId": "CreateProject",
                "requestBody": {
                    "required": "true",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Project"
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "成功返回",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Project"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "User": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "username": {
                        "type": "string",
                        "description": "账号名"
                    },
                    "nick_name": {
                        "type": "string",
                        "description": "昵称"
                    },
                    "password": {
                        "type": "string",
                        "description": "密码"
                    },
                    "created_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "updated_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "更新时间"
                    },
                    "status": {
                        "type": "string",
                        "enum": [
                            "REGULAR",
                            "LOCKED"
                        ]
                    },
                    "latestUpdatePasswordTime": {
                        "type": "string",
                        "format": "date-time",
                        "description": "上次更新密码时间"
                    }
                }
            },
            "Role": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "name": {
                        "type": "string",
                        "description": "名称"
                    },
                    "description": {
                        "type": "string",
                        "description": "描述信息"
                    },
                    "created_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "updated_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "更新时间"
                    }
                }
            },
            "Authority": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "name": {
                        "type": "string",
                        "description": "名称"
                    },
                    "path": {
                        "type": "string",
                        "description": "请求路径"
                    },
                    "method": {
                        "type": "string",
                        "description": "请求方法"
                    },
                    "description": {
                        "type": "string",
                        "description": "描述信息"
                    },
                    "created_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    }
                },
                "example": {
                    "id": 1,
                    "name": "CREATE_ROLE",
                    "path": "/v1/roles",
                    "method": "POST",
                    "description": "创建角色"
                }
            },
            "Project": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "name": {
                        "type": "string",
                        "description": "名称"
                    },
                    "code": {
                        "type": "string",
                        "description": "唯一标志码"
                    },
                    "created_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "updated_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "更新时间"
                    }
                },
                "example": {
                    "id": 1,
                    "name": "test",
                    "code": "Xe2es12a",
                    "project_components": [
                        {
                            "id": 1,
                            "type": "EUREKA",
                            "eureka_url": "127.0.0.1:8761",
                            "eureka_username": "admin",
                            "eureka_password": "admin"
                        }
                    ]
                }
            },
            "Me": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "nick_name": {
                        "type": "string",
                        "description": "昵称"
                    },
                    "projects": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Project"
                        }
                    },
                    "authorises": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Authority"
                        }
                    }
                }
            }
        },
        "responses": {
            "GeneralError": {
                "description": "General Error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {
                                    "type": "string",
                                    "description": "错误信息"
                                },
                                "time": {
                                    "type": "string",
                                    "format": "date-time",
                                    "description": "响应时间"
                                }
                            }
                        }
                    }
                }
            }
        },
        "securitySchemes": {
            "OAuth2": {
                "type": "oauth2",
                "flows": {
                    "password": {
                        "tokenUrl": "http://mac-dev.dmptesting.xyz:9050/user-center/oauth/token",
                        "scopes": {
                            "all": "Grants all access"
                        }
                    }
                }
            }
        }
    }
}

    return JsonResponse(data)

def mac_gateway(request):

    data = {
  "openapi": "3.0.0",
  "info": {
    "description": "Gateway Admin 接口文档",
    "version": "1.4.0",
    "title": "Gateway Admin API",
    "contact": {
      "email": "yann.xia@daocloud.io"
    }
  },
  "servers": [
    {
      "url": "http://192.168.2.134:9030/v1",
      "description": "测试环境"
    }
  ],
  "tags": [
    {
      "name": "endpoint",
      "description": "端点相关"
    },
    {
      "name": "route",
      "description": "路由相关"
    }
  ],
  "paths": {
    "/endpoints": {
      "get": {
        "tags": [
          "endpoint"
        ],
        "summary": "查询端点规则",
        "operationId": "ListEndpoint",
        "parameters": [
          {
            "$ref": "#/components/parameters/PageParam"
          },
          {
            "$ref": "#/components/parameters/SizeParam"
          },
          {
            "$ref": "#/components/parameters/SortParam"
          },
          {
            "name": "keyword",
            "in": "query",
            "description": "关键字",
            "required": False,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "method",
            "in": "query",
            "description": "请求方式",
            "required": False,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "成功返回",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/PageResponse"
                    },
                    {
                      "type": "object",
                      "required": [
                        "data"
                      ],
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/HttpEndpoint"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "endpoint"
        ],
        "summary": "创建端点规则",
        "operationId": "CreateEndpoint",
        "requestBody": {
          "description": "新的路由规则",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/HttpEndpoint"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "成功返回",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/PageResponse"
                    },
                    {
                      "type": "object",
                      "required": [
                        "data"
                      ],
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/HttpEndpoint"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/routes": {
      "get": {
        "tags": [
          "route"
        ],
        "summary": "查询路由规则",
        "description": "查询路由规则",
        "operationId": "ListRoute",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "分页-页数 从0开始",
            "required": False,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "size",
            "in": "query",
            "description": "分页-页大小",
            "required": False,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "keyword",
            "in": "query",
            "description": "关键字",
            "required": False,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "type",
            "in": "query",
            "description": "路由类型",
            "required": False,
            "schema": {
              "type": "string",
              "enum": [
                "WEIGHT",
                "HEADER",
                "IP",
                "SERVICE_DISCOVERY"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "路由列表",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/PageResponse"
                    },
                    {
                      "type": "object",
                      "required": [
                        "data"
                      ],
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/HttpEndpoint"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "route"
        ],
        "summary": "创建一个新的路由规则",
        "description": "创建一个新的路由规则",
        "operationId": "CreateRoute",
        "requestBody": {
          "description": "新的路由规则",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRoute"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "创建路由",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EndpointRoute"
                }
              }
            }
          }
        }
      }
    },
    "/routes/{routeId}": {
      "put": {
        "tags": [
          "route"
        ],
        "summary": "更新一个路由规则",
        "description": "更新路由规则",
        "operationId": "UpdateRoute",
        "parameters": [
          {
            "in": "path",
            "name": "routeId",
            "description": "路由ID",
            "required": True,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "requestBody": {
          "description": "更新的Route规则",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRoute"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "更新路由",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EndpointRoute"
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "route"
        ],
        "summary": "删除一个路由规则",
        "operationId": "DeleteRoute",
        "parameters": [
          {
            "in": "path",
            "name": "routeId",
            "description": "路由ID",
            "required": True,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "responses": {
          "default": {
            "description": "删除成功"
          }
        }
      }
    }
  },
  "components": {
    "parameters": {
      "PageParam": {
        "in": "query",
        "name": "page",
        "required": False,
        "schema": {
          "type": "integer",
          "minimum": 0,
          "default": 0
        },
        "description": "the query page"
      },
      "SizeParam": {
        "in": "query",
        "name": "size",
        "required": False,
        "schema": {
          "type": "integer",
          "minimum": 0,
          "default": 20
        },
        "description": "query size"
      },
      "SortParam": {
        "in": "query",
        "name": "sorts",
        "required": False,
        "schema": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "example": "createTime.ASC"
        },
        "description": "sort fields"
      }
    },
    "schemas": {
      "EndpointRoute": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string",
            "description": "名称"
          },
          "description": {
            "type": "string",
            "description": "描述信息"
          },
          "route_strategy": {
            "type": "string",
            "description": "路由策略",
            "enum": [
              "WEIGHT",
              "HEADER",
              "IP",
              "SERVICE_DISCOVERY"
            ]
          },
          "header_field": {
            "type": "string",
            "description": "Http头字段"
          },
          "route_target": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RouteDestination"
            }
          }
        }
      },
      "RouteDestination": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "名称"
          },
          "urlPattern": {
            "type": "string",
            "description": "转发URL模式"
          },
          "weight": {
            "type": "integer",
            "description": "权重值"
          },
          "header": {
            "type": "string",
            "description": "头部值"
          },
          "ip": {
            "type": "string",
            "description": "IP地址，支持正则"
          },
          "server_name": {
            "type": "string",
            "description": "服务名"
          },
          "description": {
            "type": "string",
            "description": "描述"
          },
          "service_discovery_strategy": {
            "type": "string",
            "description": "服务发现策略",
            "enum": [
              "RANDOM",
              "ROUND_ROBIN",
              "WEIGHTED_RESPONSE_TIME",
              "BEST_AVAILABLE"
            ]
          }
        }
      },
      "PageResponse": {
        "type": "object",
        "properties": {
          "page": {
            "type": "integer",
            "format": "int32"
          },
          "page_size": {
            "type": "integer",
            "format": "int32"
          },
          "total": {
            "type": "integer",
            "format": "int32"
          }
        }
      },
      "HttpEndpoint": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string",
            "description": "显示名称"
          },
          "endpoint": {
            "type": "string",
            "description": "暴露出端点"
          },
          "method": {
            "type": "string",
            "enum": [
              "GET",
              "HEAD",
              "POST",
              "PUT",
              "PATCH",
              "DELETE"
            ],
            "description": "请求方式"
          },
          "routes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EndpointRoute"
            }
          },
          "description": {
            "type": "string",
            "description": "描述信息"
          },
          "auth_keys": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/BasicAuthKey"
                },
                {
                  "$ref": "#/components/schemas/TokenAuthKey"
                },
                {
                  "$ref": "#/components/schemas/ThirdPartyKey"
                }
              ]
            }
          },
          "cache_config": {
            "type": "object",
            "description": "缓存配置",
            "properties": {
              "cacheables": {
                "type": "boolean",
                "description": "缓存是否生效"
              },
              "cache_time": {
                "type": "integer",
                "description": "缓存有效期（秒）"
              }
            }
          },
          "circuit_config": {
            "type": "object",
            "description": "缓存配置",
            "properties": {
              "id": {
                "type": "integer",
                "format": "int64"
              },
              "max_failure_threshold": {
                "type": "integer",
                "description": "最大失败比例（百分比）"
              },
              "duration_in_open_state": {
                "type": "integer",
                "description": "熔断持续时间（秒）"
              },
              "ring_buffer_size_in_half_open_state": {
                "type": "integer",
                "description": "半开环大小"
              },
              "ring_buffer_size_in_closed_state": {
                "type": "integer",
                "description": "关闭环大小"
              }
            }
          }
        }
      },
      "AuthKey": {
        "type": "object",
        "discriminator": {
          "propertyName": "authKey"
        },
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string",
            "description": "名称"
          },
          "create_time": {
            "type": "string",
            "format": "date-time"
          },
          "latest_update_time": {
            "type": "string",
            "format": "date-time"
          },
          "policies": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/RateLimit"
                },
                {
                  "$ref": "#/components/schemas/QuotaLimit"
                }
              ]
            }
          }
        }
      },
      "BasicAuthKey": {
        "type": "object",
        "description": "用户名密码授权对象",
        "allOf": [
          {
            "$ref": "#/components/schemas/AuthKey"
          },
          {
            "type": "object",
            "properties": {
              "username": {
                "type": "string",
                "description": "用户名"
              },
              "password": {
                "type": "string",
                "description": "密码"
              },
              "is_active": {
                "type": "boolean",
                "description": "是否激活"
              },
              "header_key": {
                "type": "string",
                "description": "Http头部键"
              },
              "type": {
                "type": "string",
                "description": "固定标志值",
                "default": ".BasicAuthKey"
              }
            }
          }
        ]
      },
      "TokenAuthKey": {
        "type": "object",
        "description": "Token授权对象",
        "allOf": [
          {
            "$ref": "#/components/schemas/AuthKey"
          },
          {
            "type": "object",
            "properties": {
              "token": {
                "type": "string",
                "description": "token"
              },
              "expire_time": {
                "type": "string",
                "format": "date-time",
                "description": "失效时间"
              },
              "header_key": {
                "type": "string",
                "description": "Http头部键"
              },
              "type": {
                "type": "string",
                "description": "固定标志值",
                "default": ".TokenAuthKey"
              }
            }
          }
        ]
      },
      "ThirdPartyKey": {
        "type": "object",
        "description": "Token授权对象",
        "allOf": [
          {
            "$ref": "#/components/schemas/AuthKey"
          },
          {
            "type": "object",
            "properties": {
              "third_system_key_class": {
                "type": "string",
                "description": "第三方系统class"
              },
              "user_info_url": {
                "type": "string",
                "description": "用户信息路径"
              },
              "header_key": {
                "type": "string",
                "description": "Http头部键"
              },
              "type": {
                "type": "string",
                "description": "固定标志值",
                "default": ".ThirdPartyKey"
              }
            }
          }
        ]
      },
      "Policy": {
        "type": "object",
        "discriminator": {
          "propertyName": "policy"
        },
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string",
            "description": "名称"
          },
          "create_time": {
            "type": "string",
            "format": "date-time"
          },
          "latest_update_time": {
            "type": "string",
            "format": "date-time"
          },
          "description": {
            "type": "string",
            "description": "描述信息"
          }
        }
      },
      "RateLimit": {
        "type": "object",
        "description": "RateLimit对象",
        "allOf": [
          {
            "$ref": "#/components/schemas/Policy"
          },
          {
            "type": "object",
            "properties": {
              "allowance": {
                "type": "integer",
                "format": "int64",
                "description": "允许请求量"
              },
              "per": {
                "type": "integer",
                "format": "int64",
                "description": "重置时间"
              },
              "type": {
                "type": "string",
                "description": "固定标志值",
                "default": ".RateLimit"
              }
            }
          }
        ]
      },
      "QuotaLimit": {
        "type": "object",
        "description": "QuotaLimit对象",
        "allOf": [
          {
            "$ref": "#/components/schemas/Policy"
          },
          {
            "type": "object",
            "properties": {
              "quota_max": {
                "type": "integer",
                "format": "int64",
                "description": "最大值"
              },
              "quota_renewal_rate": {
                "type": "integer",
                "format": "int64",
                "description": "重置周期 秒"
              },
              "type": {
                "type": "string",
                "description": "固定标志值",
                "default": ".QuotaLimit"
              }
            }
          }
        ]
      }
    }
  }
}

    return JsonResponse(data)
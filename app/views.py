from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django Demo App</h1>")


def welcome(request):
    """
    在当前目录下的 `templates` 目录下寻找 `welcome.html`
    如果找不到再根据在 `settings.py` 文件中 `INSTALLED_APPS` 列表中的配置开始寻找
    找到则渲染模版返回，否则抛出错误。
    """
    return render(request, 'welcome.html')
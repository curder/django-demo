# Django Demo

- Django 4.0.6

## 安装 Django

```bash
# 安装 Django 框架
pip install Django 

# 初始化 Django 项目，并命名为 django_demo
django-admin startproject django_demo 
```

## 初始化项目 app
```bash
python3 manage.py startapp app # 创建一个 app 项目并初始化数据
```

## 启动项目

```bash
python manage.py runserver 
```


# Uris

| Uri        | 页面名称 | 简单说明    |
|------------|------|---------|
| `/`        | 首页   | 返回字符串响应 |
| `/welcome` | 欢迎页  | 返回页面视图  |

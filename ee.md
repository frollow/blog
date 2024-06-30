# Инструкция и примеры как добавить [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html) на сайт Django

Если пользователи из Европы просматривают ваш сайт, то вам обязательно нужно корректно обрабатывать cookie. Иначе вы можете попасть ... на большие штрафы [GDPR](https://gdpr-text.com/).

На сайте django файлы можно обрабатывать с использованием библиотеки [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html).

Инструкция, как настроить:

Установите библиотеку:

pip install django-cookie-consent

Добавьте библиотеку в INSTALLED_APPS:

```
INSTALLED_APPS= [
...
"cookie_consent",
...
]
```

В файл urls.py добавьте:

`path("cookies/", include("cookie_consent.urls")),`

Выполните миграции:

```
python mangage.py migrate
python mangage.py collectstatic
```

### Откройте административную панель и добавьте несколько записей в таблицу "Cookie Groups".

Запись1: 

* Variable name: **necessary**
* Name: **Necessary**
* Description: Some text
* Is required: False
* Is deletable?: True

Запись 2:

* Variable name: **statistic**
* Name: **Statistic**
* Description: Some text
* Is required: True
* Is deletable?: False

Перейдите в таблицу "Cookies" и добавьте несколько записей:

Запись 1:

* Cookie Group: Выберите "**Necessary**"
* Name: **cookie_consent**
* Description: Some text
* Path: /
* Domain: --пусто--
* Varname: --заполнится автоматически--

Запись 2:

* Cookie Group: Выберите "**Necessary**"
* Name: **sessionid**
* Description: Some text
* Path: /
* Domain: --пусто--
* Varname: --заполнится автоматически--

Запись 3:

* Cookie Group: Выберите "**Necessary**"
* Name: **csrftoken**
* Description: Some text
* Path: /
* Domain: --пусто--
* Varname: --заполнится автоматически--

Запись 4:

* Cookie Group: Выберите "**Statistic**"
* Name: **_ga**
* Description: Some text
* Path: /
* Domain: --пусто--
* Varname: --заполнится автоматически--

Запись 4:

* Cookie Group: Выберите "**Statistic**"
* Name: **_ga_0E0AABB0CE** *(ваш номер будет сохранен в браузере, скопируйте и вставьте его)*
* Description: Some text
* Path: /
* Domain: --пусто--
* Varname: --заполнится автоматически--

### Добавление HTML

В главный файл base.html (или main.html) добавьте сделующий код.

В теге `<head>` , ближе к началу:

```
{% load static %}
{% load cookie_consent_tags %}

{% if not request|all_cookies_accepted %}
    {% block before_close_head %}
        <link href="{% static 'cookie_consent/css/footer.css' %}" rel="stylesheet" type="text/css">
    {% endblock %}

    {% static "cookie_consent/cookiebar.module.js" as cookiebar_src %}
    {% url 'cookie_consent_status' as status_url %}
    <script type="module">
        import {showCookieBar} from '{{ cookiebar_src }}';
        showCookieBar({
        statusUrl: '{{ status_url|escapejs }}',
        templateSelector: '#cookie-consent__cookie-bar',
        cookieGroupsSelector: '#cookie-consent__cookie-groups',
        onShow: () => document.querySelector('body').classList.add('with-cookie-bar'),
        onAccept: () => document.querySelector('body').classList.remove('with-cookie-bar'),
        onDecline: () => document.querySelector('body').classList.remove('with-cookie-bar'),
        });
    </script>
    {% all_cookie_groups 'cookie-consent__cookie-groups' %}
{% endif %}
```

или создайте include и добавьте с помощью тега, например:

`{% include 'cookie_consent/base/header.html' %}` .


Перед закрывающим тегом `</body>` :

```
{% url "cookie_consent_cookie_group_list" as url_cookies %}

<template id="cookie-consent__cookie-bar">
  <div class="cookie-bar">
      <span>This site uses cookies for better performance and user experience.
      Do you agree to use these cookies?</span>
      <button type="button" class="cookie-consent__accept badge-primary small light category">Accept and Close</button>
      {% comment %} <button type="button" class="cookie-consent__decline badge-primary small light category">Decline</button> {% endcomment %}
      <a href="{{ url_cookies }}">Cookies info</a>
  </div>
</template>
```

или создайте include и добавьте с помощью тега, например:

`{% include 'cookie_consent/base/header.html' %}` .

Затем обертите все скрипты добавленные в шаблон, где используются cookie.

```
  {% if request|cookie_group_accepted:"statistic" %}
    ...
  {% endif %}
```

Здесь мы оборачиваем скрипт, для Cookie Groups - "Statistic" например обернем скрипт Google Analitycs:

```
  {% if request|cookie_group_accepted:"statistic" %}
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TGWM24RW');</script>
    <!-- End Google Tag Manager -->
  {% endif %}
```

Чтобы такая обертка сработала, обязательно добавьте в html - templatetag:

```
{% load cookie_consent_tags %}
```

Создайте файл со стилями для всплавающего попапа, в папке template/cookie_consent/css/**footer.css**

```
.cookie-bar {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: #333;
    color: #fff;
    text-align: center;
    padding: 15px;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    font-size: 14px;
    display: flex;
    align-items: center;
    grid-gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
}

.cookie-bar button {
    margin: 5px;
    padding: 10px 20px;
    background: #007BFF;
    color: #fff;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
}

.cookie-bar button:hover {
    background: #0056b3;
}

.cookie-bar a {
    color: #00aaff;
    text-decoration: none;
    margin-left: 10px;
    font-size: 14px;
}

.cookie-bar a:hover {
    text-decoration: underline;
}
```



### В итоге, должно получится примерно так:

```
{% load static %}
{% load cookie_consent_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
  {% comment %} Cookies scripts {% endcomment %}
  <link href="{% static 'cookie_consent/css/footer.css' %}" rel="stylesheet" type="text/css">
  {% if not request|all_cookies_accepted %}
    {% static "cookie_consent/cookiebar.module.js" as cookiebar_src %}
    {% url 'cookie_consent_status' as status_url %}
    <script type="module">
        import {showCookieBar} from '{{ cookiebar_src }}';
        showCookieBar({
        statusUrl: '{{ status_url|escapejs }}',
        templateSelector: '#cookie-consent__cookie-bar',
        cookieGroupsSelector: '#cookie-consent__cookie-groups',
        onShow: () => document.querySelector('body').classList.add('with-cookie-bar'),
        onAccept: () => document.querySelector('body').classList.remove('with-cookie-bar'),
        onDecline: () => document.querySelector('body').classList.remove('with-cookie-bar'),
        });
    </script>
    {% all_cookie_groups 'cookie-consent__cookie-groups' %}
  {% endif %}


  {% if request|cookie_group_accepted:"statistic" %}
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-00000000');</script>
    <!-- End Google Tag Manager -->
  {% endif %}
  
  <title>...</title>
  <meta name="description" content="...">

  ...

</head>
<body>
  {% if request|cookie_group_accepted:"statistic" %}
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-00000000"
      height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
  {% endif %}

  {% comment %} Cookies template {% endcomment %}
  {% url "cookie_consent_cookie_group_list" as url_cookies %}
  <template id="cookie-consent__cookie-bar">
    <div class="cookie-bar">
        <span>This site uses cookies for better performance and user experience.
        Do you agree to use these cookies?</span>
        <button type="button" class="cookie-consent__accept badge-primary small light category">Accept</button>
        <button type="button" class="cookie-consent__decline badge-primary small light category">Decline</button>
        <a href="{{ url_cookies }}">Cookies info</a>
    </div>
  </template>

</body>
</html>
```

Пример этого кода можете посмотреть в репозитории https://github.com/frollow/blog/blob/main/blog/templates/base.html . Создавайлся для открытого проекта 

Автор: Артем Фролов

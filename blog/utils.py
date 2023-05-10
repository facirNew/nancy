menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Добавить пост', 'url_name': 'addpage'},
        ]

login_menu = [{'title': 'Вход', 'url_name': 'signin'},
              {'title': 'Регистрация', 'url_name': 'signup'},
              {'title': 'Выход', 'url_name': 'home'},
              ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        user_login_menu = login_menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            user_login_menu.pop(2)
        else:
            user_login_menu.pop(0)
            user_login_menu.pop(0)

        context['menu'] = user_menu
        context['login_menu'] = user_login_menu

        return context

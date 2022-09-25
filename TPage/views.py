from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "page.html"
    extra_context = {"title_name": "Главная страница"}
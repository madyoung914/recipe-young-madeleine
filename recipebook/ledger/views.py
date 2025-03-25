from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RecipeForm, RecipeImageForm
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(RecipeListView, self).get_context_data(**kwargs)
        ctx['form'] = RecipeForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe_detail.html'


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = 'recipe_image_add.html'

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ledger:recipe-detail",
                            kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        ctx = super(RecipeImageCreateView, self).get_context_data(**kwargs)
        ctx['pk'] = self.kwargs["pk"]
        return ctx


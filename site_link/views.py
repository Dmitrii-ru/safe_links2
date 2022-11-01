from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Links
from django.views.generic.edit import FormMixin, DeleteView
from .forms import LinksForm
from django.shortcuts import get_object_or_404


class LinkView(ListView):
    model = Links
    form_class = LinksForm
    paginate_by = 3
    context_object_name = 'links'
    template_name = 'site_link/links_list.html'

    def get_queryset(self, **kwargs):
        if self.request.user.is_authenticated:
            return Links.objects.filter(user=self.request.user).order_by('-pk')

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated == True:
            context = super(LinkView, self).get_context_data(**kwargs)
            form = LinksForm()
            context['form'] = form
            return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = LinksForm(request.POST)
            if form.is_valid():
                try:
                    link = form.save(commit=False)
                    link.user = request.user
                    link.save()
                    return redirect(request.META.get('HTTP_REFERER'))
                except:
                    form.add_error(None, 'Что то пошло не так ')

        form = LinksForm(request.POST)
        return render(request, 'site_link/links_list.html', {'form': form})


class LinkDelete(DeleteView):
    model = Links
    success_url = '/'

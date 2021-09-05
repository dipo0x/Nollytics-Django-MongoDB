from django.shortcuts import render
from .models import SearchQuery
from core.models import Journal

# Create your views here.
def search_view(request):
	query = request.GET.get('q', None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {"query":query}
	if query is not None:		
		SearchQuery.objects.create(user=user, query=query)
		journal = Journal.objects.all().search(query=query)
		context['journal'] = journal
		template_name="search.html"
	return render(request, template_name, context)
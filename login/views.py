from django.shortcuts import render

# Create your views here.
def user_id(request):
	return render(request, 'login/start.html', {})
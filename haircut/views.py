from django.shortcuts import render

# Create your views here.
def home_page(request):

	if request.method == "POST":
		pass


	if request.method == "GET":
		return render(request, 'haircut/home_page.html')
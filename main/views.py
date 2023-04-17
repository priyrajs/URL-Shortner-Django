from django.shortcuts import render,redirect,HttpResponseRedirect
import random,string
from .models import Url_details
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.
def home(request):
	context = {}
	return render(request,'index.html',context)

def shortit(request):
	if request.method == "POST":
		input_url = request.POST.get('inp_url')
		root_url =  request.build_absolute_uri('/').strip("/")
		if not input_url.startswith("http:"):
			er_msg = "Please enter a valid URL"
			return JsonResponse({'status':'INVALIDURL','er_msg':er_msg})
		if input_url.startswith(root_url):
			er_msg = "This URL is already shortned"
			return JsonResponse({'status':'SHORTURL','er_msg':er_msg})
		# print(root_url1,FULL_URL_WITH_QUERY_STRING)
		try:
			rec = Url_details.objects.get(input_url=input_url)
			randchar = rec.output_url
		except ObjectDoesNotExist:
			# print(len(rec))
			letters = string.ascii_lowercase
			randchar =  ''.join(random.choice(letters) for i in range(10))
			URL = Url_details(input_url=input_url,output_url=randchar)
			URL.save()
		# op_url = settings.BASE_DIR+randchar
		return JsonResponse({'status':'shorted','op_url':randchar})

def handler404(request,exception):
	return render(request,'error_404.html')

def catch_all_view(request, url):
	# print(url)
	try:
		rec = Url_details.objects.get(output_url=url)
		input_url = rec.input_url
		print(input_url)
		return redirect(input_url)
		# return render(request,'error_404.html')
	except ObjectDoesNotExist:
		return render(request,'error_404.html')
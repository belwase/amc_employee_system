from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from job.models import Job

def JobList(request):
	jobs = Job.objects.all()
	data = {
		"jobs": jobs
	}
	return render(request, "job.html", data)

@csrf_exempt
def JobAdd(request):
	data = { 
		"added": False,
		"message":"",
		"job":None
		}

	if request.method == "POST":
		input_data = request.POST.copy()
		print(input_data)

		if "id" in request.GET:
			if request.GET["id"] != "":
				pass
			else:
				# Add 
				job = Job.objects.filter(
						title=input_data["title"]
						)
				if job:
					data["message"] = "The job already exists"
				else:
					input_data["experience_year"] = int(input_data["experience_year"])
					input_data["salary"] = int(input_data["salary"])
					print(input_data)
					job = Job(
							title=input_data["title"],
							description=input_data["description"],
							category=input_data["category"],
							location=input_data["location"],
							qualification=input_data["qualification"],
							experience_year=input_data["experience_year"],
							salary=input_data["salary"],
							job_type=input_data["job_type"],
							deadline=input_data["deadline"],
							skills=input_data["skills"]
						)
					job.save()
					data["added"] = True
				pass

	if "id" in request.GET:
		try:
			data["job"] = Job.objects.get(
					id=request.GET["id"]
					)
		except:
			pass
	return render(request, "job-add.html", data)
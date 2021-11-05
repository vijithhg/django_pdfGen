from django.http.response import HttpResponse
from django.shortcuts import render
from .models import StudentDetails
from pdf.utils import render_to_pdf

# Create your views here.

def Student_Details(request):
    data = StudentDetails.objects.all()
    context = {'data':data}
    return render(request, 'stu_details.html',context)

def pdf_page(request):
    data = StudentDetails.objects.all()
    context = {'data':data}
    pdf = render_to_pdf('stu_pdf.html',context)
    return HttpResponse(pdf,content_type='application/pdf')
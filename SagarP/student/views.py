from django.shortcuts import render
from student.models import Country, City, Student, Company
# from django.http import FileResponseRedirect 

# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# def venue_pdf(request):
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf,pagesize=letter, bottomup=0)
#     textob=c.beinText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFront("Helvetica ", 14) 

#     lines = [
#         "line 1",
#         "line 2"
#     ]

#     for line in lines:
#         textob.textLine(line)
    
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)

#     return FileResponse(buf , as_attachment=True, filename='venue.pdf')                 
def view_django(request):

    return render(request,'django.html',{})



def view_hello(request):

    return render(request,'hello.html',{})




def view_hello_20(request):   

    return render(request,'hello-20.html',{})



def view_record(request):

    stud_record = Student.objects.all()
    city_record = City.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'city12':city_record})


       # return render_to_response('courtcase/report_display.html', {'entry_list': q, 'entry_list1': q1,})


    # return render_to_response('hello.html', {'entry_list': q, 'entry_list1': q1,})





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# Note that once we’ve done this in all these views, we no longer need to import loader and Ht




# Create your views here.

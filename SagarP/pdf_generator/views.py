from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_pdf(request):
    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="example.pdf"'

    # Create PDF canvas
    pdf_canvas = canvas.Canvas(response)

    # Set font and size
    pdf_canvas.setFont("Helvetica", 12)

    # Add content to the PDF
    pdf_canvas.drawString(100, 750, "Generated PDF Example:")
    y_position = 730

    pdf_content = [
        "This is line 1.",
        "This is line 2.",
        "This is line 3.",
    ]

    for line in pdf_content:
        pdf_canvas.drawString(100, y_position, line)
        y_position -= 20  # Adjust the vertical position for the next line

    # Save the PDF
    pdf_canvas.save()

    return response

# Create your views here.

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

# Load curriculum data from JSON
with open("curriculum.json", "r") as json_file:
    curriculum_data = json.load(json_file)

# Create PDF document
c = canvas.Canvas("curriculum.pdf", pagesize=letter)

# Add curriculum data to the PDF
c.drawString(100, 800, "Curriculum Vitae")
c.drawString(100, 780, "Name: " + curriculum_data["name"])
c.drawString(100, 760, "Title: " + curriculum_data["title"])
# Add more information as needed

# Save the PDF
c.save()

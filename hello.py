import fitz
import os
from PIL import Image

directory = 'pdf'
output_directory = 'nightmare'
zoom = 1
mat = fitz.Matrix(zoom, zoom)
file_number = 0

# # # IMAGE GENERATION # #
for filename in os.listdir(directory):
    doc = fitz.open(directory + "\\" + filename)
    for page in doc:
        pix = page.get_pixmap(matrix = mat, dpi = 300)
        if page.number % 2 == 0:
            pix.save("{}\\front{}.jpg".format(output_directory, file_number), jpg_quality=100)
        else:
            pix.save("{}\\back{}.jpg".format(output_directory, file_number), jpg_quality=100)
    file_number += 1

# # COMPILED PDF OF FRONTS GENERATION # #
frontImages = []
backImages = []
for image in os.listdir(output_directory):
    if image.startswith("front"):
        frontImages.append(Image.open("{}\\{}".format(output_directory, image)))
    elif image.startswith("back"):
        backImages.append(Image.open("{}\\{}".format(output_directory, image)))

pixy = Image.open("{}\\{}".format(output_directory, "front0.jpg"))
margin = 36
cardWidth = 198 
cardHeight = 342 
# 1 inch = 72pt
##########################################################################################

doc = fitz.Document()
docLen = int(len(os.listdir(output_directory))/2)
pageNum = 0
for i in range(docLen):
    if i % 2 == 0:
        doc.new_page(pageNum, width = 612, height = 792)

        doc[pageNum].insert_image(fitz.Rect(margin, margin, cardWidth + margin, cardHeight + margin), filename = "{}\\front{}.jpg".format(output_directory, i))
        doc[pageNum].insert_image(fitz.Rect(cardWidth + margin, margin, cardWidth*2 + margin, cardHeight + margin), filename = "{}\\back{}.jpg".format(output_directory, i))

    else:
        doc[pageNum].insert_image(fitz.Rect(margin, cardHeight + margin, cardWidth + margin, cardHeight*2 + margin), filename = "{}\\front{}.jpg".format(output_directory, i))
        doc[pageNum].insert_image(fitz.Rect(cardWidth + margin, cardHeight + margin, cardWidth*2 + margin, cardHeight*2 + margin), filename = "{}\\back{}.jpg".format(output_directory, i))
        pageNum += 1
        
doc.save("testing2.pdf")


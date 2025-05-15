import fitz
import os
from PIL import Image
import shutil

directory = 'pdfInput'
output_directory = 'pdfBin'
zoom = 1
mat = fitz.Matrix(zoom, zoom)
card_number = 0
side_number = 0
# # # INSERT SINGLE CARD INDEXES BELOW (PAGE NUMBER MINUS 1) # # #
single_sided_index = [4,5,6,7,8,9,10]
single_side_new_card = True

# # # INSERT INDEXES OF PLENTIFUL UPGRADES AND NON-UNIQUE MODELS # # # 
# # # TO THE APPROPRIATE PLENTIFUL LIST (PAGE NUMBER MINUS 1)    # # #
# # # MAKE SURE TO INCLUDE INDEXES OF BOTH FRONT AND BACK SIDES  # # #
plentiful = []
plentiful.append([4,5,6,7,8,9,10]) #plentiful 2
plentiful.append([23,24,29,30]) #plentiful 3
plentiful.append([]) #plentiful 4
plentiful.append([]) #plentiful 5

shutil.rmtree('pdfBin') 
os.mkdir('pdfBin')

# # # IMAGE GENERATION # #
for filename in os.listdir(directory):
    doc = fitz.open(directory + "\\" + filename)
    for page in doc:
        if page.number not in single_sided_index:
            pix = page.get_pixmap(matrix = mat, dpi = 300)
            if side_number % 2 == 0: 
                pix.save("{}\\front{}.jpg".format(output_directory, card_number), jpg_quality=100)
                side_number += 1
                for i in plentiful:
                    if page.number in i:
                        for n in range(plentiful.index(i) + 1):
                            pix.save("{}\\front{}.jpg".format(output_directory, (card_number+n+1)), jpg_quality=100)

            else:
                pix.save("{}\\back{}.jpg".format(output_directory, card_number), jpg_quality=100)
                card_number += 1
                side_number += 1
                for i in plentiful:
                    if page.number in i:
                        for n in range(plentiful.index(i) + 1):
                            pix.save("{}\\back{}.jpg".format(output_directory, (card_number)), jpg_quality=100)
                            card_number += 1
            
        else:
            pix = page.get_pixmap(matrix = mat, dpi = 300)
            if single_side_new_card:
                pix.save("{}\\front{}.jpg".format(output_directory, card_number), jpg_quality=100)
                front_card_number = card_number
                single_side_new_card = False
                for i in plentiful:
                        if page.number in i:
                            for n in range(plentiful.index(i) + 1):
                                if n % 2 == 0:
                                    pix.save("{}\\back{}.jpg".format(output_directory, (card_number)), jpg_quality=100)
                                    card_number += 1
                                    single_side_new_card = True
                                else:
                                    pix.save("{}\\front{}.jpg".format(output_directory, (card_number)), jpg_quality=100)
                                    front_card_number = card_number
                                    single_side_new_card = False

                if (single_sided_index.index(page.number) == len(single_sided_index)-1 and (page.number not in plentiful[0] and page.number not in plentiful[2])) :
                    pix.save("{}\\back{}.jpg".format(output_directory, card_number), jpg_quality=100)
                    card_number += 1
                    single_side_new_card = True
            else:
                pix.save("{}\\back{}.jpg".format(output_directory, front_card_number), jpg_quality=100)
                card_number += 1
        

pixy = Image.open("{}\\{}".format(output_directory, "front0.jpg"))
# # Page Margin (set to min margin of your printer) # # 
margin = 36
# # Output Card Height and Width (in dpi) # # 
cardWidth = 198 
cardHeight = 342 
# 1 inch = 72pt
##########################################################################################

doc = fitz.Document()
# # # can probably be removed?
docLen = int(len(os.listdir(output_directory))/2)
if int(len(os.listdir(output_directory))%2) != 0:
    docLen += 1
# # # 

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
        
doc.save("output.pdf")


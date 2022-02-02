#!/usr/bin/env python3.10                                       

# Import the modules needed.
from PIL import Image, ImageDraw, ImageFont                     
import sys                                                      

# Our function which is called on line 38.
def h2o(strImg, strTxt):                               
                                                                
    # Create an Image Object from an Image.                     
    objImg = Image.open(strImg)                                 
    
    # We will need to save as a different filename.
    strFile = strImg                                            
    strFile = strFile.split('.')                                
    strFile = strFile[0] + "_h2o." + strFile[1]                 
    
    # Open the image for editing.
    width, height = objImg.size                
    draw = ImageDraw.Draw(objImg)                               
                                                                
    text = strTxt                                               
    font = ImageFont.truetype('Hind-Light.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # Calculate the x,y coordinates of the text.
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # Draw watermark in the bottom right corner.
    draw.text((x, y), text, font=font)

    # Save watermarked image.
    objImg.save(strFile)

# Call our function pass two arguments at runtime.
h2o(sys.argv[1],sys.argv[2])

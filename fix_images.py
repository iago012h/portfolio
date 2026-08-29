from PIL import Image

def process_image(filepath, crop=False):
    try:
        img = Image.open(filepath).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # If the pixel is very dark (close to black), make it transparent
            if item[0] < 30 and item[1] < 30 and item[2] < 30:
                newData.append((0, 0, 0, 0))
            else:
                newData.append(item)
                
        img.putdata(newData)
        
        if crop:
            # Crop to bounding box of non-transparent pixels
            bbox = img.getbbox()
            if bbox:
                img = img.crop(bbox)
                
        img.save(filepath, "PNG")
        print(f"Successfully processed {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Process the main logo (just remove black)
process_image("logo-iamu.png", crop=False)

# Process the favicon (remove black AND crop so it fills the tab icon better)
process_image("logo-iamu-icon.png", crop=True)

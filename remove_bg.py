import os
from rembg import remove
from PIL import Image

def process_images():
    team_dir = r"d:\z3connectwebsite-main\z3connectwebsite-main\image\team"
    images_to_process = [
        "joshan_black.png",
        "ifthikar.jpg",
        "akshan_black.png",
        "jerimoth_black.png",
        "raiyan_black.png",
        "balamurali_black.png",
        "Jenishlin.png",
        "john_Abishek.png",
        "shafeek.jpeg"
    ]
    
    for img_name in images_to_process:
        input_path = os.path.join(team_dir, img_name)
        if not os.path.exists(input_path):
            print(f"Skipping {img_name}, file not found.")
            continue
            
        print(f"Processing {img_name}...")
        try:
            input_img = Image.open(input_path)
            
            # Remove background, giving an RGBA image
            output_img = remove(input_img)
            
            # Create standard solid black background
            black_bg = Image.new('RGB', output_img.size, (0, 0, 0))
            
            # Paste the subject using its alpha channel as a mask
            black_bg.paste(output_img, mask=output_img.split()[3])
            
            # Save it back as _solid.png
            output_filename = img_name.split('.')[0] + "_solid.png"
            output_path = os.path.join(team_dir, output_filename)
            
            black_bg.save(output_path)
            print(f"Saved: {output_filename}")
        except Exception as e:
            print(f"Error processing {img_name}: {e}")

if __name__ == "__main__":
    process_images()

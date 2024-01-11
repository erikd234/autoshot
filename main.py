"""
    How it works.
    While the script is running, take a screenshot
    of the screen every 'sleep_dur' seconds.

    When the program is killed we can stop taking screenshots

    Okay so actaully we will prompt the user for the time in
    second we want to take screenshot for. This will be the length of the
    video I suppose.


    Afterwards we will do a little bit of math to figure out how many
    iterations of screenshots we will take at the 5 second interval time

    TODO Later:
    Parse the images for the number in the bottom corner, keep the latest one of
    each screen shot.
"""

import pyscreenshot as ImageGrab
import time
import os
import glob
from PIL import Image

def clean_up_pngs(folder_path):
    # Clean up the png files created.
    for file_path in glob.glob(os.path.join(folder_path, "*.png")):
        os.remove(file_path)


def combined_pngs_to_pdf(folder_path):
    # List of PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

    # Sort the files if necessary
    png_files.sort()

    # Convert each PNG image to PIL Image object and append to list
    images = []
    for png_file in png_files:
        file_path = os.path.join(folder_path, png_file)
        image = Image.open(file_path)
        images.append(image.convert("RGB"))
    # Save the images as a single PDF
    pdf_path = os.path.join(folder_path, f"{pdf_name}.pdf")
    images[0].save(pdf_path, save_all=True, append_images=images[1:])

if __name__ == "__main__":
    sleep_dur = 5  # seconds
    print("Name of folder to save screenshot.")
    folder_name = str(input("Enter Folder Name: "))
    print("Seconds to Record screenshots")
    num_secs = int(input("Enter an integer: "))
    print("What would you like the PDF file name to be?")
    pdf_name = str(input("Enter PDF file Name: "))
    num_screenshots = int(num_secs / sleep_dur)
    os.makedirs(folder_name)
    print()
    print("starting...")
    print()
    for i in range(0, num_screenshots):
        try:
            filename = f"{folder_name}/sc{i}.png"
            print(f"taking screenshot {filename} ")
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            time.sleep(5)
        except KeyboardInterrupt:
            print("Interrupted by user")
            print("combine any screenshots taken")
            folder_path = f"./{folder_name}"
            combined_pngs_to_pdf(folder_path)
            clean_up_pngs(folder_path)
            break

    folder_path = f"./{folder_name}"
    combined_pngs_to_pdf(folder_path)
    clean_up_pngs(folder_path)

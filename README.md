# Add-Text-To-Videos

Add Text-To-Videos
This project allows users to add customized text to videos with various animation effects. It uses Flask as the backend framework and Moviepy library for video editing. Users can upload a video file, specify text content, font style, text color, and choose from a variety of animation effects to apply to the text overlay.

Installation

ImageMagick is a powerful open-source software suite used for displaying, converting, and editing raster image and vector image files. In this project, ImageMagick is utilized for applying various animation effects to text overlays in videos.

To install ImageMagick on your system, follow the instructions provided on the official website.

Changing config.py
To modify configurations for the Flask application, you can make changes in the config.py file by providing paths for IMAGE_BINARY AND FFMPEG_BINARY. 

To run this project locally, follow these steps:

Clone this repository to your local machine:git clone <https://github.com/sarahanjum12/Add-Text-To-Videos.git>
pip install flask moviepy

Usage
Run the Flask application:
python app.py
Open a web browser and go to http://localhost:5000.

Upload a video file and enter the text, font, style, color, and animation details.

Click on the "Add Text" button to process the video.

Once the process is complete, the resulting video with the added text will be displayed on the screen.

System Requirements
Python 3.x
Flask
MoviePy
ImageMagick

Examples of input and output videos showcasing the text animation features will be provided in the GitHub repository's README file.

Contributors
Sarah Anjum


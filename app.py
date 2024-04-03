from flask import Flask, render_template, request,url_for
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    # Get form data
    video_file = request.files['video']
    text = request.form['text']
    font = request.form['font']
    style = request.form['style']
    color = request.form['color']
    animation = request.form['animation']
    
    # Save video file
    video_path = 'static/input_video.mp4'
    video_file.save(video_path)

    # Load video
    video_clip = VideoFileClip(video_path)

    # Create text clip
    text_clip = TextClip(text, fontsize=50, color=color, font=font, method='label').set_duration(video_clip.duration)
    if animation == 'slide_from_left':
        text_clip = text_clip.set_position(('left', 'center')).fx(resize.width, width=video_clip.w).fx(resize.height, height=video_clip.h).fx(vfx.slide_in, duration=2, side='left')

    elif animation == 'slide_from_right':
        text_clip=text_clip.set_position(('right', 'center')).fx(resize.width, width=video_clip.w).fx(resize.height, height=video_clip.h).fx(vfx.slide_in, duration=2, side='left')


    # Overlay text clip on video
    video_with_text = CompositeVideoClip([video_clip, text_clip])

    # Set output file path
    output_video_path = 'static/output_video.mp4'

    # Write the final video to file
    video_with_text.write_videofile(output_video_path, codec='libx264', fps=24)

    return render_template('result.html', output_video=output_video_path)

if __name__ == '__main__':
    app.run(debug=True)
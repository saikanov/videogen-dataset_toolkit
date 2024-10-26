from moviepy.editor import VideoFileClip
import os
import shutil
import cv2
import argparse

def split_video(input_file:str, segment_duration:int, output_dir:str ):
    """split video with moviepy"""
    os.makedirs(output_dir, exist_ok=True)
    video = VideoFileClip(input_file)
    total_duration = video.duration
    num_segments = int(total_duration // segment_duration)

    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        
        segment = video.subclip(start_time, end_time)

        base_name = os.path.splitext(os.path.basename(input_file))[0]
        
        segment.write_videofile(f"{output_dir}/{base_name}_{i+1}.mp4", codec='libx264',
                        ffmpeg_params=['-crf', '15'])  # crf kecil makin bagus, gede makin jelek
        
    if total_duration % segment_duration != 0:
        start_time = num_segments * segment_duration
        segment = video.subclip(start_time, total_duration)
        segment.write_videofile(f"{output_dir}/{base_name}_{num_segments+1}.mp4", codec='libx264',
                        ffmpeg_params=['-crf', '15']) 
    
    video.close()

def get_video_duration(file_path:str):
    """get video duration with opencv"""
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        return None
    fps = cap.get(cv2.CAP_PROP_FPS)  
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  
    duration = frame_count / fps  
    cap.release()  
    return round(duration)

def remove_img(video_dir:str):
    """sometime there is image in dataset, use this to remove them all"""
    if os.getcwd != video_dir:
        os.chdir(video_dir)

    dirlist = os.listdir()

    for i in dirlist:
        if ".png" or ".jpg" in i:
            os.remove(i)

def lessthansix(video_dir:str,output_dir:str, mvordel:str="move"):
    """Move or delete <6 second video"""
    if os.getcwd != video_dir:
        os.chdir(video_dir)
    dirlist_6s = os.listdir() 

    if mvordel =="move":
        for i in dirlist_6s:
            if get_video_duration(i) < 6:
                shutil.move(i,output_dir)
    elif mvordel =="del":
        for i in dirlist_6s:
            if get_video_duration(i) < 6:
                os.remove(i)

def main(video_dir,output_dir,lessthansix_folder):
    os.chdir(video_dir)
    
    remove_img(video_dir=video_dir)

    lessthansix(video_dir=video_dir, 
                output_dir=lessthansix_folder)
    
    for i in os.listdir():
        split_video(input_file=i,
                    segment_duration=6,
                    output_dir=output_dir)

    lessthansix(video_dir=video_dir,
                output_dir=lessthansix_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and split videos.")
    parser.add_argument("video_dir", help="Directory containing video files.")
    parser.add_argument("output_dir", help="Directory to store output segments.")
    parser.add_argument("lessthansix_folder", help="Directory for videos shorter than 6 seconds.")

    args = parser.parse_args()
    main(args.video_dir, args.output_dir, args.lessthansix_folder)

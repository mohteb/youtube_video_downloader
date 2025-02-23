# Import the YoutubeDL class from the yt_dlp library
from yt_dlp import YoutubeDL
import os

def download_video(url, quality=None):
    """
    Downloads a YouTube video using the provided URL.

    Args:
        url (str): The URL of the YouTube video to download.
        quality (str): The desired video quality (e.g., '1080', '720', '480'). If None, the best quality is selected.
    """
    # Options for yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
    }

    # Set the video quality if specified
    if quality:
        ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
    else:
        ydl_opts['format'] = 'bestvideo+bestaudio/best'  # Default to the best quality

    # Create a YoutubeDL object with the specified options
    with YoutubeDL(ydl_opts) as ydl:
        # Extract video info without downloading
        info = ydl.extract_info(url, download=False)
        
        # Prepare the filename using the video info
        filename = ydl.prepare_filename(info)
        
        # Check if the file already exists
        if os.path.exists(filename):
            # Prompt the user to overwrite or skip
            overwrite = input(f"File '{filename}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() != 'y':
                print("Download skipped.")
                return
        
        # Download the video
        ydl.download([url])

# Main entry point of the script
if __name__ == "__main__":
    try:
        # Prompt the user to enter a YouTube URL
        url = input("Enter the YouTube URL: ")
        
        # Prompt the user to choose the video quality
        quality = input("Enter video quality (e.g., 1080, 720, 480) or leave blank for best quality: ")
        
        # Call the download_video function with the provided URL and quality
        download_video(url, quality)
        
        # Notify the user that the download is complete
        print("Download complete.")
    except Exception as e:
        # Handle any errors that occur during execution
        print("An error occurred:", str(e))
# Import required libraries
from yt_dlp import YoutubeDL
import os

# Define a function to download a YouTube video
def download_video(url):
    """
    Downloads a YouTube video using the provided URL.

    Args:
        url (str): The URL of the YouTube video to download.
    """
    # Options for yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
    }

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
        
        # Call the download_video function with the provided URL
        download_video(url)
        
        # Notify the user that the download is complete
        print("Download complete.")
    except Exception as e:
        # Handle any errors that occur during execution
        print(f"An error occurred: {e}")

import os
import json
from pytube import Playlist, YouTube

def scrape_playlist_info(playlist_url, output_file):
    playlist = Playlist(playlist_url)
    videos_info = []

    print(f"Scraping playlist: {playlist.title}")
    print(f"Number of videos: {len(playlist.video_urls)}")

    for index, video_url in enumerate(playlist.video_urls, 1):
        try:
            yt = YouTube(video_url)
            video_info = {
                "title": yt.title,
                "thumbnail": yt.thumbnail_url,
                "channel": yt.author,
                "videoUrl": video_url,
                "duration": yt.length
            }
            videos_info.append(video_info)
            print(f"Scraped info for video {index}/{len(playlist.video_urls)}: {yt.title}")
        except Exception as e:
            print(f"Error scraping {video_url}: {str(e)}")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(videos_info, f, ensure_ascii=False, indent=4)

    print(f"Playlist info saved to {output_file}")

# Usage
playlist_url = input("Enter the YouTube playlist URL: ")
output_file = "playlist_info.json"

scrape_playlist_info(playlist_url, output_file)

# from pytube import Playlist, YouTube
# import os

# def scrape_and_download_playlist(playlist_url, output_dir):
#     # Create playlist object
#     playlist = Playlist(playlist_url)
    
#     # Create output directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     print(f"Playlist: {playlist.title}")
#     print(f"Number of videos: {len(playlist.video_urls)}")
    
#     # Iterate through videos in playlist
#     for index, video_url in enumerate(playlist.video_urls, 1):
#         try:
#             # Create YouTube object
#             yt = YouTube(video_url)
            
#             # Get video title
#             title = yt.title
            
#             # Get highest resolution stream
#             stream = yt.streams.get_highest_resolution()
            
#             # Download video
#             print(f"Downloading ({index}/{len(playlist.video_urls)}): {title}")
#             stream.download(output_path=output_dir)
            
#             print(f"Downloaded: {title}")
#         except Exception as e:
#             print(f"Error downloading {video_url}: {str(e)}")
    
#     print("Playlist download complete!")

# # Usage
# playlist_url = input("Enter the YouTube playlist URL: ")
# output_directory = "D:/Shimya"  # Change this to your desired directory on the D drive

# scrape_and_download_playlist(playlist_url, output_directory)
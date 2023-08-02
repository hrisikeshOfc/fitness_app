from pytube import YouTube

class YouTubeInfoExtractor:
    def __init__(self):
        self.video = None
        self.extracted_info = {}

    def extract_info(self):
        try:
            self.video = YouTube(self.url)
            self.extracted_info['id'] = self.video.video_id
            self.extracted_info['title'] = self.video.title
            self.extracted_info['channel'] = self.video.author
            self.extracted_info['view_count'] = self.video.views
            self.extracted_info['channel_id'] = self.video.channel_id
            self.extracted_info['duration'] = self.video.length
            self.extracted_info['tags'] = self.video.keywords
        except Exception as e:
            print(f"Error extracting information: {e}")

    def get_info(self, url):
        self.url = url
        if not self.extracted_info:
            self.extract_info()
        return self.extracted_info



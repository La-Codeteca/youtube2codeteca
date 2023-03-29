import json
def save_video_list(FILENAME: str, response):
    with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)

import json
from os import path, getenv
from database_manager import create_table,\
                             insert_data,\
                             exist_video

from file_manager import save_video_list
from page_manager import generate_markdown_document
from youtube_manager import get_videos
from utils import generate_name

TOKEN = getenv("YOUTUBE_TOKEN")

def main():
    print(f"Iniciando {getenv('APP_NAME')}")
    FILENAME = generate_name(extension="json")
    create_table()

    if not path.exists(FILENAME):
        respuesta = get_videos(channel_id="UCkRyPGrwHn7d6vem6BN-abg",\
                               TOKEN=TOKEN)
        
        print(json.dumps(json.loads(respuesta.text), sort_keys=True, indent=4, separators=(",", ": ")))
        if(respuesta.status_code == 200):
            save_video_list(FILENAME=FILENAME, response=respuesta)

    f = open(FILENAME)
    data = json.load(f)

    for item in data["items"]:

        id = item["id"]["videoId"]
        
        if not exist_video(id=id):

            print(f" El video {id} no ha sido procesado anteriormente")

            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            img = item["snippet"]["thumbnails"]["default"]["url"]
            content = f"{{% include video id='{id}' provider='youtube' %}}"

            generate_markdown_document(id=id,\
                                    title=title,\
                                    description=description,\
                                    img=img,\
                                    content=content)
            insert_data(id)




main()
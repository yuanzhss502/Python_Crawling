import requests
import json



url = 'https://www.ximalaya.com/revision/play/v1/show?id=237004192&sort=1&size=30&ptype=1'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

}

r = requests.get(url, headers = headers)
ret = r.text
result = json.loads(ret)

content_list = result['data']['tracksAudioPlay']

for content in content_list:
    music_name = content['trackName']
    print(music_name)
    music_id = content['trackId']

    url = 'https://www.ximalaya.com/revision/play/v1/audio?id=%d&ptype=1'%music_id
    print(url)

    mus_response = requests.get(url, headers = headers)
    mus_html = mus_response.text
    mus_result = json.loads(mus_html)

    mus_src = mus_result['data']['src']

    with open('img%s.m4a'%music_name,'wb') as f:
        mus = requests.get(mus_src, headers =headers)
        f.write(mus.content)



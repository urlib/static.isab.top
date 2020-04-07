from secrets import SystemRandom as __Random
from string import ascii_letters, digits
import os

Random = __Random()
char_set = ascii_letters + digits
char_set_len = len(char_set)


def generate_vid(length=8):
    res = Random.choices(char_set, k=length % char_set_len)
    for _ in range(length // char_set_len):
        res += Random.choices(char_set, k=char_set_len)
    return ''.join(res)


class html_template():
    def mp4(self, vid, source):
        return f"""<!DOCTYPE html>
<head><title>Playing {vid} ... | Video Player</title><meta charset="utf-8"></head>
<body>
<video id="video_{vid}" controls width="100%" src="{source}"></video>
</body>
    """

    def m3u8(self, vid, source):
        return f"""<!DOCTYPE html>
<head><title>Playing {vid} ... | Video Player</title><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script></head>
<body>
<video id="video_{vid}" controls width="100%"></video>
<script>
const source = '{source}';
const video = document.getElementById('video_{vid}'); """ + \
            """
if (Hls.isSupported()) {
let hls = new Hls();
hls.loadSource(source);
hls.attachMedia(video);
hls.on(Hls.Events.MANIFEST_PARSED, function () {
// video.play();
});
} else if (video.canPlayType('application/vnd.apple.mpegurl')) {
video.src = source;
video.addEventListener('loadedmetadata', function () {
// video.play();
});
}
</script>
</body>
"""


html_conv = html_template()


def main():
    os.chdir(os.sys.path[0])
    source = input()
    vid = generate_vid()
    source_file_name, source_file_ext = source.split('/')[-1].rsplit('.', 1)
    try:
        html = getattr(html_conv, source_file_ext)(vid, source)
    except AttributeError:
        raise Exception('ext not supported')
    file_name = f'play_video_{source_file_name}_{vid}.html'
    with open(file_name, 'w') as f:
        f.write(html)
    print(f'written to {file_name}')


# https://cdn.jsdelivr.net/gh/urlib/6UItiju5Uv5X/pfwyFZj7SrzaCokN/lover_remix/lover_remix.m3u8
if __name__ == "__main__":
    main()

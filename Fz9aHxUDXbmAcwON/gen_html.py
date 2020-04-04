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


def html_template(vid, source):
    return f"""<!DOCTYPE html>

<head>
    <meta charset="utf-8">
</head>

<body>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <video id="video_{vid}" controls class="vjs-16-9" width="100%"></video>
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


def main():
    os.chdir(os.sys.path[0])
    source = input()
    vid = generate_vid()
    html = html_template(vid, source)
    source_file_name = ''.join(source.split('/')[-1].split('.')[:-1])
    file_name = f'play_video_{source_file_name}_{vid}.html'
    with open(file_name, 'w') as f:
        f.write(html)
    print(f'written in {file_name}')


# https://cdn.jsdelivr.net/gh/urlib/6UItiju5Uv5X/pfwyFZj7SrzaCokN/lover_remix/lover_remix.m3u8
if __name__ == "__main__":
    main()

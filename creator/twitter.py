import tweepy
import time
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

image_formats = ['jpg', 'png', 'jpeg', 'jfif', 'bmp', 'tiff', 'tga']

class TwitterBot(object):
    def __init__(self):

		# Hier keys

        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_key = ""
        self.access_secret = ""

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)

        self.api = tweepy.API(self.auth)
        self.api.wait_on_rate_limit = True

        self.last_poll = time.time()

    def run(self):
        while 1:
            try:
                self.poll()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print "Failed while polling!"
		print e
            time.sleep(30)

    def poll(self):
        for msg in self.api.mentions_timeline():
            text = msg.text
            timestamp = time.mktime(msg.created_at.timetuple()) + 3600
            name = msg.author.screen_name
            img = msg.author.profile_image_url
            if timestamp > self.last_poll:
                media = None
                if 'media' in msg.entities.keys():
                    link = msg.entities['media'][0]['media_url']
                    filetype = link.split(".")[-1]
                    if filetype in image_formats:
                        os.system("wget --quiet --directory-prefix=/tmp/ %s" % link)
                        media = "/tmp/%s" % link.split("/")[-1]
                dark = False
                for word in ['dunkel', 'dark', 'nacht', 'schwarz', 'dunkelheit', 'kalt', 'angst']:
                    if word in text.lower():
                        dark = True
                self.render_tweet("@" + name, img, text, media, dark=dark)
        self.last_poll = time.time()

    def render_tweet(self, username, userimage, text, media=None, dark=False):

        ponys = ['@ennox']

        lines = textwrap.wrap(text, width=48)
        text = '\n'.join(lines)

        if username in ponys:
            userimage = "creator/data/pinkie_pie.png"
            _ = "%s (Mag Ponys sehr gerne)" % username
            username = _

        if "http://" in userimage or "https://" in userimage:
            os.system("wget --quiet --directory-prefix=/tmp/ %s" % userimage)
            userimage = "/tmp/%s" % userimage.split("/")[-1]

        image = Image.new("RGBA", (800, 600), (0, 0, 0) if dark else (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("creator/data/IndieFlower.ttf", 32)

        user_image = Image.open(userimage)
        user_image = user_image.convert("RGBA")
        user_image = user_image.resize((100, 100))

        if not media is None:
            media_image = Image.open(media)
            media_image.thumbnail((800, 340), Image.ANTIALIAS)

            width, height = media_image.size
            x = (800 / 2) - (width / 2)
            image.paste(media_image, (x, 240))

        image.paste(user_image, (10, 10))

        draw.text((120, 44), username, (255, 255, 255) if dark else (0, 0, 0), font=font)
        draw.text((10, 120), text, (255, 255, 255) if dark else (0, 0, 0), font=font)
        image.save("HERE_PATH_TO_IMAGE.jpg", "JPEG")


if __name__ == "__main__":
    TwitterBot().run()

import requests
import json
import os
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from io import BytesIO
from PIL import Image, ImageDraw, ImageOps, ImageSequence
import urllib
from wand.image import Image as Img_wand
from wand.display import display

PATH_ABS = os.path.abspath(r"../JogosBot")
PATH_DATA = os.path.join(PATH_ABS,"Data")
PATH_I = os.path.join(PATH_DATA,'Images')

class Error_image():pass

def verifica_tamanho(image):
    img = Image.open(image)

def verifica_url(url):
    var = False
    try:
        validate = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
        validate(url)
        if(url.endswith(".png") or url.endswith(".jpg") or url.endswith(".jpge")):
            return True
        else:
            return var
    except ValidationError:
        return var

def verifica_tipo_img(message):
    imagens = list()
    if message.embeds:
        if len(message.embeds) == 1:
            if(message.embeds[0].image):
                if(verifica_url(message.embeds[0].image.url) == True):
                    img = download_image(message.embeds[0].image.url)
                    imagens.append(img)
        else:
            for embed in message.embeds:
                if(embed.image):
                    if(verifica_url(embed.image.url) == True):
                        img = download_image(embed.image.url)
                        imagens.append(img)
    elif message.attachments:
        if len(message.attachments) == 1:
            if(verifica_url(message.attachments[0].url) == True):
                img = download_image(message.attachments[0].url)
                imagens.append(img)
        else:
            for a in message.attachments:
                if(verifica_url(a.url) == True):
                    img = download_image(a.url)
                    imagens.append(img)
    return imagens

async def get_image(message):
    channel = message.channel
    content = message.content
    imagens = list()
    if(message.attachments):
        imagem = message.attachments[0]
        if(verifica_url(imagem.url) == True):
            img = download_image(imagem.url)
            imagens.append(img)
    else:
        async for message in channel.history(limit=31):
            if message.content == content:
                continue
            else:
                msg = message.content.split()
                if(len(msg)==1):
                    if verifica_url(msg[0]) == True:
                        img = download_image(msg[0])
                        imagens.append(img)
                        break
                    else:
                        imagens = verifica_tipo_img(message)
                        if len(imagens)>0:
                            break
                        else:
                            continue
                else:
                    for m in msg:
                        if verifica_url(m) == True:
                            img = download_image(m)
                            imagens.append(img)
                    if len(imagens) == 0:
                        imagens = verifica_tipo_img(message)
                        if len(imagens)>0:
                            break
                    else:
                        break
    return imagens

def download_image(url):
    response = requests.get(url)
    if(response.status_code == 200):
        return BytesIO(response.content)
    else:
        return Error_image()

def func_magik(image,scale):
    scale = 1
    img = Img_wand(file=image)
    img.transform(resize='800x800>')
    img.liquid_rescale(width=int(img.width * 0.5), height=int(img.height * 0.5), delta_x=int(0.5 * scale) if scale else 1, rigidity=0)
    img.liquid_rescale(width=int(img.width * 1.5), height=int(img.height * 1.5), delta_x=scale if scale else 2, rigidity=0)
    i = BytesIO()
    img.save(file=i)
    i.seek(0)
    return i

def func_haah(image):
    i = Image.open(image)
    width, height = i.size 
    top = 0
    right = width
    bottom = height
    left = width/2
    espelhada = i.transpose(Image.FLIP_LEFT_RIGHT)
    img_crop = espelhada.crop((left, top, right, bottom))
    i.paste(img_crop,(int(width/2),0))
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_waaw(image):
    i = Image.open(image)
    width, height = i.size
    top = 0
    right = width/2
    bottom = height
    left = 0
    espelhada = i.transpose(Image.FLIP_LEFT_RIGHT)
    img_crop = espelhada.crop((left, top, right, bottom))
    i.paste(img_crop,(0,0))
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_hooh(image):
    i = Image.open(image)
    width, height = i.size
    top = 0
    right = width
    bottom = height/2
    left = 0
    espelhada = i.transpose(Image.FLIP_TOP_BOTTOM)
    espelhada.show()
    img_crop = espelhada.crop((left, top, right, bottom))
    i.paste(img_crop,(0,0))
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_woow(image):
    i = Image.open(image)
    width, height = i.size
    top = height/2
    right = width
    bottom = height
    left = 0
    espelhada = i.transpose(Image.FLIP_TOP_BOTTOM)
    img_crop = espelhada.crop((left, top, right, bottom))
    i.paste(img_crop,(0,int(height/2)))
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_rotate(image,degress):
    i = Image.open(image)
    rotated_image = i.rotate(degress)
    image_binary = BytesIO()
    rotated_image.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_ancap(image):
    i = Image.open(image)
    width, height = i.size
    ancap = Image.open(os.path.join(PATH_I,'ancap.png'))
    ancap = ancap.resize((width,height))
    i.paste(ancap, (0, 0), ancap)
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_ussr(image):
    i = Image.open(image)
    width, height = i.size
    ussr = Image.open(os.path.join(PATH_I,'ussr.png'))
    ussr = ussr.resize((width,height))
    i.paste(ussr, (0, 0), ussr)
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_nazi(image):
    i = Image.open(image)
    width, height = i.size
    nazi = Image.open(os.path.join(PATH_I,'nazi.png'))
    nazi = nazi.resize((width,height))
    i.paste(nazi, (0, 0), nazi)
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_gay(image):
    i = Image.open(image)
    width, height = i.size
    gay = Image.open(os.path.join(PATH_I,'gay.png'))
    gay = gay.resize((width,height))
    i.paste(gay, (0, 0), gay)
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_logan(image):
    i = Image.open(image)
    width, height = i.size
    logan = Image.open(os.path.join(PATH_I,'logan.png'))
    logan = logan.resize((int(width*0.75),int(height*0.75)))
    w_logan, h_logan = logan.size
    i.paste(logan, (width-w_logan, height-h_logan), logan)
    image_binary = BytesIO()
    i.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_trump(image):
    img = Image.new('RGBA',(800, 450),color=(255,255,255))
    i = Image.open(image)
    trump = Image.open(os.path.join(PATH_I,'trump.png'))
    i = i.resize((369,182))
    img.paste(i,(194,450-182))
    img.paste(trump, (0,0), trump)
    image_binary = BytesIO()
    img.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_gaben(image):
    img = Image.new('RGBA',(450, 338),color=(255,255,255))
    i = Image.open(image)
    i = i.resize((111,143))
    gaben = Image.open(os.path.join(PATH_I,'gaben.png'))
    img.paste(i,(240,163))
    img.paste(gaben, (0,0), gaben)
    image_binary = BytesIO()
    img.save(image_binary, format='PNG')
    image_binary.seek(0)
    return image_binary

def func_spin(image):
    i = Image.open(image)
    i = i.resize((175,175))
    background = Image.new(i.mode, i.size, (0,0,0))
    mask = Image.new("L", i.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, i.size[0], i.size[1]), fill=255)
    img = Image.composite(i, background, mask)
    result = img.copy()
    result.putalpha(mask)
    frames = list()
    for j in range(90,-1,-1):
        frame_binary = BytesIO()
        frame = result.rotate(j*4)
        frame.save(frame_binary,format='PNG')
        frame2 = Image.open(frame_binary)
        frames.append(frame2)
    image_binary = BytesIO()
    frames[0].save(image_binary, format='GIF', save_all=True, append_images=frames[1:], transparency=255, optimize=False, duration=2, loop=0)
    image_binary.seek(0)
    return image_binary

def upload_burn(image):
    session = requests.Session()
    params = {
        'access_key': 'e3084acf282e8323181caa61fa305b2a',
        'lang': 'en'
    }
    url = 'https://api.photofunia.com' + '/2.0/effects/burning_photo' + '?' + urllib.parse.urlencode(params)
    data = {'name': 'image','animation':'icon'}
    files = {'image': image}
    p = session.post(url, headers=None, data=data, files=files)
    return p

def func_burn(image):
    response = upload_burn(image)
    img_json = json.loads(response.content)
    return img_json['response']['images']['regular']['url']

# imagem = download_image('https://media.discordapp.net/attachments/506963931705638915/721565940264992848/magik.png')
# func_spin(imagem)
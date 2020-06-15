import discord
from discord.ext import commands


import Functions.Fun_image
from importlib import reload
reload(Functions.Fun_image)

from Functions.Fun_image import Error_image
from Functions.Fun_image import get_image,download_image,verifica_url
from Functions.Fun_image import func_magik,func_burn,func_haah,func_hooh,func_waaw,func_woow,func_spin,func_ancap,func_gay,func_gaben,func_logan,func_nazi,func_rotate,func_trump,func_ussr

class Image(commands.Cog,name= "Image"):
    def __init__ (self,bot):
            self.bot = bot
            self.emoji = '🐮'
            self.hidden = True
            self.admin = False
    
    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='magik')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def magik(self,ctx, scale: int = 1, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_magik(image,scale)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_magik(imagem,scale)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens, Escala{}'.format(scale),files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_magik(imagem,scale)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='haah')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def haah(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_haah(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_haah(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_haah(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='waaw')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def waaw(self,ctx,url=None):    
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_waaw(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_waaw(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_waaw(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='hooh')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def hooh(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_hooh(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_hooh(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_hooh(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='woow')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def woow(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_woow(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_woow(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_woow(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='gay')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def gay(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_gay(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_gay(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_gay(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='ancap')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def ancap(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_ancap(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_ancap(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_ancap(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='nazi')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def nazi(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_nazi(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_nazi(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_nazi(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='ussr')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def ussr(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_ussr(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_ussr(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_ussr(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='logan')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def logan(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_logan(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_logan(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_logan(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='spin')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def spin(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_spin(image)
                    file = discord.File(img, filename='spin.gif')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_spin(image)
                            files.append(discord.File(img,filename='spin{}.gif'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_spin(imagem)
                    file = discord.File(fp=img,filename='spin.gif')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='trump')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def trump(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_trump(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_trump(image)
                            files.append(discord.File(img,filename='trump{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_trump(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='gaben')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def gaben(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_gaben(image)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_gaben(image)
                            files.append(discord.File(img,filename='magik{}.png'.format(cont)))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(file=files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens',files=files)
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_gaben(imagem)
                    file = discord.File(img,filename='magik.png')
                    await ctx.send(file=file)
            else:
                await ctx.send('Url inválida.')

    @commands.command(name='burn')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def burn(self,ctx, url=None):
        if(url is None):
            image = await get_image(ctx.message)
            if(len(image)==1):
                image = image[0]
                if(isinstance(image,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_burn(image)
                    embed=discord.Embed()
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif(len(image)>1 and len(image)<5):
                    files = list()
                    cont=1
                    for imagem in image:
                        if(isinstance(imagem,Error_image)):
                            continue
                        else:
                            img = func_burn(image)
                            files.append('{} \n'.format(img))
                            cont+=1                
                    if(len(files)==1):
                        await ctx.send(files[0])
                    elif(len(files)>1):
                        await ctx.send('Suas imagens {}'.format(files))
                    else:
                        await ctx.send('Erro em fazer download das imagens.')
            elif(len(image)>=5):
                await ctx.send('Erro, muitas imagens.')
            else:
                await ctx.send('Imgem(s) não encontrada')
        else:
            if(verifica_url(url) == True):
                imagem = download_image(url)
                if(isinstance(imagem,Error_image)):
                    await ctx.send('Erro em fazer download da imagem.')
                else:
                    img = func_burn(imagem)
                    embed=discord.Embed()
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            else:
                await ctx.send('Url inválida.')

def setup(bot):
    bot.add_cog(Image(bot))
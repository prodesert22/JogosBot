import discord
from discord.ext import commands

import typing

import Functions.Fun_image
from importlib import reload
reload(Functions.Fun_image)

from Functions.Fun_image import Error_image
from Functions.Fun_image import get_image,download_image,verifica_url
from Functions.Fun_image import func_magik,func_burn,func_haah,func_hooh,func_waaw,func_woow,func_spin,func_ancap,func_gay,func_gaben,func_logan,func_nazi,func_rotate,func_trump,func_ussr

class Image(commands.Cog,name= "Edição de imagem"):
    def __init__ (self,bot):
            self.bot = bot
            self.emoji = '🖼️'
            self.hidden = False
            self.admin = False
    
    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='magik', aliases=['magick'], 
    usage='?magik <escala> <url1> <url2> <url3> : Opcionais',
    description='Deforma a imagem informa\nSe não for informado url, o bot irá procurar a imagem no chat.',
    brief='?magik 5 \n?magik 2 <url1>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def magik(self,ctx, scale: int = 1, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_magik(image, scale)
                file = discord.File(fp=img,filename='magik.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_magik(image, scale)
                            file = discord.File(fp=img,filename=f'magik{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')
            
    @commands.command(name='haah', aliases=['mirror'], 
    usage='?magik <url1> <url2> <url3> : Opcionais',
    description='Copia metade da imagem e cola na esquerda.',
    brief='?haah \n?haah <url1>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def haah(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_haah(image)
                file = discord.File(fp=img,filename='haah.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_haah(image)
                            file = discord.File(fp=img,filename=f'haah{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='waaw', aliases=['mirror2'], 
    usage='?waaw <url1> <url2> <url3> : Opcionais',
    description='Copia metade da imagem e cola na esquerda.',
    brief='?waaw \n?waaw <url1>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def waaw(self,ctx, *, url:typing.Optional[str] = None):    
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_waaw(image)
                file = discord.File(fp=img,filename='waaw.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_waaw(image)
                            file = discord.File(fp=img,filename=f'waaw{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='hooh', 
    usage='?hooh <url1> <url2> <url3> : Opcionais',
    description='Copia metade da imagem e cola na parte superior.',
    brief='?hooh \n?hooh <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def hooh(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_hooh(image)
                file = discord.File(fp=img,filename='hooh.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_hooh(image)
                            file = discord.File(fp=img,filename=f'hooh{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')


    @commands.command(name='woow', 
    usage='?woow <url1> <url2> <url3> : Opcionais',
    description='Copia metade da imagem e cola na parte inferior.',
    brief='?woow \n?woow <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def woow(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_woow(image)
                file = discord.File(fp=img,filename='woow.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_woow(image)
                            file = discord.File(fp=img,filename=f'woow{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='gay', 
    usage='?gay <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro gay a imagem.',
    brief='?gay \n?gay <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def gay(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_gay(image)
                file = discord.File(fp=img,filename='gay.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_gay(image)
                            file = discord.File(fp=img,filename=f'gay{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='ancap', 
    usage='?ancap <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro ancap a imagem.',
    brief='?ancap \n?gay <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def ancap(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_ancap(image)
                file = discord.File(fp=img,filename='ancap.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_ancap(image)
                            file = discord.File(fp=img,filename=f'ancap{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='nazi', 
    usage='?nazi <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro nazi a imagem.',
    brief='?nazi \n?nazi <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def nazi(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_nazi(image)
                file = discord.File(fp=img,filename='nazi.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_nazi(image)
                            file = discord.File(fp=img,filename=f'nazi{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='ussr', 
    usage='?ussr <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro ussr a imagem.',
    brief='?ussr \n?ussr <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def ussr(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_ussr(image)
                file = discord.File(fp=img,filename='ussr.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_ussr(image)
                            file = discord.File(fp=img,filename=f'ussr{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='logan', 
    usage='?logan <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro logan a imagem.',
    brief='?logan \n?logan <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def logan(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_logan(image)
                file = discord.File(fp=img,filename='logan.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_logan(image)
                            file = discord.File(fp=img,filename=f'logan{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='trump', 
    usage='?trump <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro trump a imagem.',
    brief='?trump \n?trump <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def trump(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_trump(image)
                file = discord.File(fp=img,filename='trump.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_trump(image)
                            file = discord.File(fp=img,filename=f'trump{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')


    @commands.command(name='gaben', 
    usage='?gaben <url1> <url2> <url3> : Opcionais',
    description='Adiciona o filtro gaben a imagem.',
    brief='?gaben \n?gaben <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def gaben(self,ctx, *, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_gaben(image)
                file = discord.File(fp=img,filename='gaben.png')
                await ctx.send(file=file)
        else:
            urls = url.split()
            if len(urls) <4:
                files = list()
                error_message = ''
                cont = 1
                for u in urls:
                    if verifica_url(u) == True:
                        image = download_image(u)
                        if isinstance(image,Error_image):
                            error_message += f'{image.get_message()} {cont}\n'
                        else:
                            img = func_gaben(image)
                            file = discord.File(fp=img,filename=f'gaben{cont}.png')
                            files.append(file)
                        cont+=1
                if(len(files) == 1):
                    await ctx.send(error_message,file=files[0])
                elif(len(files) == 0):
                    await ctx.send(error_message)
                else:
                    await ctx.send(error_message,files=files)
            else:
                await ctx.send('Muitas imagens o máximo são 3.')

    @commands.command(name='spin', 
    usage='?spin <url1>: Opcional',
    description='A imagem fica girando 360º.',
    brief='?spin \n?spin <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def spin(self,ctx, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_spin(image)
                file = discord.File(fp=img,filename='spin.gif')
                await ctx.send(file=file)
        else:
            if verifica_url(url) == True:
                image = download_image(url)
                if isinstance(image,Error_image):
                    await ctx.send(image.get_message())
                else:
                    img = func_spin(image)
                    file = discord.File(fp=img,filename=f'spin.gif')
                    await ctx.send(file=file)
            else:
                await ctx.send('Erro, url inválida.')


    @commands.command(name='burn', 
    usage='?burn <url1>: Opcional',
    description='Gif da imagem queimando.',
    brief='?burn \n?burn <url>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def burn(self,ctx, url:typing.Optional[str] = None):
        if(url is None):
            image = await get_image(ctx.message)
            if isinstance(image,Error_image):
                await ctx.send(image.get_message())
            else:
                img = func_burn(image)
                embed=discord.Embed()
                embed.set_image(url=img)
                await ctx.send(embed=embed)
        else:
            if verifica_url(url) == True:
                image = download_image(url)
                if isinstance(image,Error_image):
                    await ctx.send(image.get_message())
                else:
                    img = func_burn(image)
                    embed=discord.Embed()
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            else:
                await ctx.send('Erro, url inválida.')

def setup(bot):
    bot.add_cog(Image(bot))
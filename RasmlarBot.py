import asyncio
import logging
from random import randint, choice
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)
Token = "6497869440:AAFiUdZZMH9QKmWDUEEexTceIohvlWkFH_w"

bot = Bot(token=Token, parse_mode="HTML")

dp = Dispatcher()

notpics = ["https://images3.alphacoders.com/606/606500.jpg",
           "https://images6.alphacoders.com/601/601846.jpg",
           "https://images8.alphacoders.com/131/1317063.png",
           "https://images.alphacoders.com/133/1339887.png",
           "https://images3.alphacoders.com/133/1339619.png",
           "https://images6.alphacoders.com/132/1328482.png",
           "https://images8.alphacoders.com/131/1319109.jpg",
           "https://images6.alphacoders.com/133/1330647.jpeg",
           "https://images.alphacoders.com/133/1335176.jpeg",
           "https://images4.alphacoders.com/132/1329074.png",
           "https://images.alphacoders.com/133/1339894.png",
           "https://images7.alphacoders.com/133/1337527.png",
           "https://images2.alphacoders.com/132/1323443.jpg",
           "https://images5.alphacoders.com/133/1338607.png",
           "https://images2.alphacoders.com/131/1316862.png",
           "https://images.alphacoders.com/130/1301370.png",
           "https://images.alphacoders.com/133/1338574.jpeg",
           "https://images4.alphacoders.com/133/1339615.png",
           "https://images3.alphacoders.com/132/1326232.jpeg",
           "https://images3.alphacoders.com/133/1338606.png",
           "https://images6.alphacoders.com/133/1337325.jpeg",
           "https://images7.alphacoders.com/133/1333817.jpeg",
           "https://images6.alphacoders.com/132/1322261.png", ]

telpics = [
    "https://e1.pxfuel.com/desktop-wallpaper/640/957/desktop-wallpaper-amoled-black-6k-mobile-phone-dark.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/678/439/desktop-wallpaper-black-car-amoled-phone-black-car.jpg",
    "https://w0.peakpx.com/wallpaper/993/872/HD-wallpaper-color-smash-bright-colorful-colour-mix-pretty-rainbows.jpg",
    "https://w0.peakpx.com/wallpaper/739/384/HD-wallpaper-colour-2-amoled-color-colors-galaxy-mix-note-rainbow-rainbows-splash.jpg",
    "https://w0.peakpx.com/wallpaper/335/158/HD-wallpaper-flower-amoled-android-apple-black-dark-galaxy-ios-iphone-note-samsung.jpg",
    "https://w0.peakpx.com/wallpaper/465/201/HD-wallpaper-colourful-amoled-color-explosion-galaxy-mix-paint-space-splash-star.jpg",
    "https://w0.peakpx.com/wallpaper/85/389/HD-wallpaper-amoled-splash-amoled-black-fireworks-splash.jpg",
    "https://w0.peakpx.com/wallpaper/11/894/HD-wallpaper-saturn-black-amoled-amoled-galaxy-heart-premium-smoke-super-amoled-super-amoled.jpg",
    "https://w0.peakpx.com/wallpaper/603/545/HD-wallpaper-miui-12-7-colors-huawei-miui-12-mix-note-redmi-splash-xiaomi.jpg",
    "https://w0.peakpx.com/wallpaper/452/535/HD-wallpaper-colours-abstract-amoled-bright-colourfull-superamoled.jpg",
    "https://w0.peakpx.com/wallpaper/788/276/HD-wallpaper-amoled-hexagon-apple-backgrounds-black-dark-galaxy-ios-iphone-note-samsung.jpg",
    "https://w0.peakpx.com/wallpaper/55/439/HD-wallpaper-digital-flower-amoled-android-apple-black-dark-galaxy-iphone-note-samsung.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/763/358/desktop-wallpaper-black-minimalist-phone-iphone-amoled-minimalist.jpg",
    "https://e0.pxfuel.com/wallpapers/500/782/desktop-wallpaper-black-car-amoled-car.jpg",
    "https://e0.pxfuel.com/wallpapers/265/991/desktop-wallpaper-amoled-minimalist-minimalist-black-phone-top-minimalist-black-amoled-city.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/890/873/desktop-wallpaper-other-exceptional-minimalist-black-amoled-that-black-amoled.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/624/296/desktop-wallpaper-black-amoled-flower-amoled.jpg",
    "https://e0.pxfuel.com/wallpapers/148/612/desktop-wallpaper-amoled-minimal-android-black-minimalist-amoled.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/793/713/desktop-wallpaper-cool-black-amoled-for-phone-black-blue-amoled.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/945/914/desktop-wallpaper-mountains-landscape-phone-amoled-phone-mountain-amoled.jpg",
    "https://e0.pxfuel.com/wallpapers/762/609/desktop-wallpaper-amoled-background-samsung-amoled-amoled-background-and-amoled-super-amoled-display.jpg",
    "https://e0.pxfuel.com/wallpapers/741/410/desktop-wallpaper-black-phone-25-top-black-phone-black-for-mobile.jpg",
    "https://e0.pxfuel.com/wallpapers/723/613/desktop-wallpaper-border-amoled-black-and-white-edge-black-and-white-amoled.jpg",
    "https://e0.pxfuel.com/wallpapers/989/575/desktop-wallpaper-amoled-minimalist-minimalist-black-phone-top-minimalist-black-thor-amoled.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/646/196/desktop-wallpaper-black-amoled-google-plain-black-amoled.jpg",
    "https://e0.pxfuel.com/wallpapers/636/145/desktop-wallpaper-black-car-black-audi-car.jpg",
    "https://e0.pxfuel.com/wallpapers/85/150/desktop-wallpaper-minimal-amoled-black-minimal-car.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/621/498/desktop-wallpaper-amoled-anime-minimalist-phone.jpg",
    "https://e0.pxfuel.com/wallpapers/432/568/desktop-wallpaper-amoled-car-porsche-amoled.jpg",
    "https://e1.pxfuel.com/desktop-wallpaper/106/697/desktop-wallpaper-pattern-black-design-monochrome-black-iphone-amoled-black-abstract.jpg",
    "https://e0.pxfuel.com/wallpapers/833/124/desktop-wallpaper-black-amoled-google-amoled-logo.jpg",
    "https://w0.peakpx.com/wallpaper/947/996/HD-wallpaper-wave-aqua-amoled-apple-black-dark-galaxy-iphone-note-samsung-smoke.jpg",
    "https://w0.peakpx.com/wallpaper/53/119/HD-wallpaper-square-amoled-apple-black-dark-edge-galaxy-iphone-note-samsung.jpg",
    "https://w0.peakpx.com/wallpaper/254/777/HD-wallpaper-amoled-red-n-black-abstract-amoled-apple-black-dark-galaxy-iphone-samsung-wall.jpg",
    "https://w0.peakpx.com/wallpaper/112/265/HD-wallpaper-ios-14-apple-iphone.jpg",
    "https://w0.peakpx.com/wallpaper/511/713/HD-wallpaper-red-desert-abstract-android-apple-galaxy-huawei-iphone-note-samsung-wall.jpg",
    "https://w0.peakpx.com/wallpaper/343/705/HD-wallpaper-samsung-super-amoled-super-amoled-super-amoled-dark-electric-blue-flower-samsung-amoled-super-amoled-theme-herbaceous-plant-amoled-samsung-amoled-super-amoled-samsung.jpg",
    "https://w0.peakpx.com/wallpaper/202/291/HD-wallpaper-eyes-iphone-amoled-dark-samsung-anime.jpg",
    "https://w0.peakpx.com/wallpaper/621/261/HD-wallpaper-ios-15-apple-iphone.jpg",
    "https://w0.peakpx.com/wallpaper/825/359/HD-wallpaper-iphone-11-light-apple-apple-iphone-cool-honor-iphone-11-iphone-11-pro-iphone-iphone-x.jpg",
    "https://w0.peakpx.com/wallpaper/976/577/HD-wallpaper-iphone-xs-xr-x-max-apple-iphone.jpg",
    "https://w0.peakpx.com/wallpaper/484/981/HD-wallpaper-amoled-flower-galaxy-design-apple-dark-black.jpg"]

captions = ["Marhamat ☻", "Mana o'sha rasm ☺", "Siz tanlagan komandaga oid rasm.", "Mana oling!"]


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply(
        f"Salom <b>{message.from_user.first_name},</b>\nSiz quyidagi bo'limlardan birini tanlab, rasmni olishingiz mumkin ☻\nBuning uchun: /rasm kamandasini bering.",
        parse_mode="HTML")
    print(f"""
{message.from_user.first_name}
{message.from_user.last_name}
{message.from_user.username}
{message.from_user.id}""")


@dp.message(Command("ovoz"))
async def ovozla(message: types.Message):
    await message.answer("This is elon muscle")


@dp.message(Command("rasmlar"))
async def rasmlar(message: types.Message):
    await message.reply(
        f"<i>Qaysi bo'limni tanlaysiz?</i>\nTelefon uchun: <b>/ftelefon</b>\nNoutbuk uchun: <b>/fnoutbuk</b>\n\nBizda telefon uchun {len(telpics)} ta rasm mavjud,\nNoutbuklar uchun esa {len(notpics)} ta")

    @dp.message(Command("ftelefon"))
    async def ftelefon(message: types.Message):
        await message.reply("Iltimos kutib turing ⏱")
        await asyncio.sleep(5)
        for i in telpics:
            await message.answer_photo(photo=i)

    @dp.message(Command("fnoutbuk"))
    async def fnoutbuk(message: types.Message):
        await message.reply("Iltimos kutib turing ⏱")
        await asyncio.sleep(5)
        for i in notpics:
            await message.answer_photo(photo=i)


@dp.message(Command("rasm"))
async def hammasi(message: types.Message):
    await message.answer(f"""
Hurmatli foydalanuvchi, qanday qurulma uchun rasm olmoqchisiz ?\n<b>Telefon uchun: /telefon, Noutbuk uchun: /noutbuk</b>\n\nBizda telefon uchun {len(telpics)} ta rasm mavjud,\nNoutbuklar uchun esa {len(notpics)} ta""",
                         parse_mode="HTML")

    @dp.message(Command("telefon"))
    async def telefon(message: types.Message):
        await message.reply("Iltimos kutib turing ⏱")
        await asyncio.sleep(5)
        await message.answer_photo(photo=telpics[randint(0, len(telpics))], caption=captions[randint(0, len(captions))])

    @dp.message(Command("noutbuk"))
    async def noutbuk(message: types.Message):
        await message.reply("Iltimos kutib turing ⏱")
        await asyncio.sleep(5)
        await message.answer_photo(photo=notpics[randint(0, len(notpics))], caption=captions[randint(0, len(captions))])


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

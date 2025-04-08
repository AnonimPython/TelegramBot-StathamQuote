from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random

router = Router()

# Списки цитат и фото
quotes = [
    "Работа не волк. Никто не волк. Только волк — волк.",
    "Мама учила не ругаться матом, но жизнь научила не ругаться матом при маме.",
    "Если закрыть глаза, становится темно.",
    "Если тебе где-то не рады в рваных носках, то и в целых туда идти не стоит.",
    "«Жи-ши» пиши от души.",
    "Тут — это вам не там.",
    "Если ты смелый, ловкий и очень сексуальный — иди домой, ты пьян.",
    "Шаг влево, шаг вправо — два шага.",
    "Раньше я думал, что вечной любви не существует. Потом я встретил пиво.",
    "Однажды городской тип купил поселок. Теперь это поселок городского типа.",
    "Недавно я был в гостях у девушки. Хотел оставить о себе хорошее впечатление, а оставил несмываемое.",
    "Я всегда говорю правду, даже когда вру.",
    "Сниму квартиру. Порядок на районе гарантирую.",
    "Взял нож — режь, взял дошик — ешь.",
    "Если заблудился в лесу, иди домой.",
    "Запомни: всего одна ошибка — и ты ошибся.",
    "Делай, как надо. Как не надо, не делай.",
    "Кто рано встает — тому весь день спать хочется."
]

photo_urls = [
    "https://i.pinimg.com/236x/35/6f/74/356f743c8f39dad74b04249adfb9518f.jpg",
    "https://i.pinimg.com/736x/f5/c4/fc/f5c4fcc578c2c91076630f5e7e8e8fd2.jpg",
    "https://img.championat.com/i/e/c/1701171612548282247.jpg",
    "https://sevimi.by/wp-content/uploads/2023/07/stethem.webp",
    "https://twizz.ru/wp-content/uploads/2020/07/1595606788_8c7dd922ad47494fc02c388e12c00eac.jpg",
    "https://a.d-cd.net/98b2e8as-960.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG4lt25CpCAMoxTzjmTSSE32CvnYH5BdcHDg&s",
    "https://www.film.ru/sites/default/files/people/1455579-884296.jpg",
    "https://www.kinomania.ru/sites/default/files/person_images/623a1f8e55863044aa680a8fa581c36a.jpeg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXj05r8S3M70oxeD-TYFiB18e9zE4b1ZGv-w&s",
]

# Клавиатура с inline-кнопкой
quote_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Выдать цитату", callback_data="get_quote")]]
)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(
        photo="https://img.championat.com/s/732x488/news/big/y/q/dzhejson-stethem_15160383362036838957.jpg",
        caption="Привет браток, нажми на кнопку ниже",
        reply_markup=quote_kb
    )

@router.callback_query(F.data == "get_quote")
async def send_quote(callback_query):
    quote = random.choice(quotes)
    photo = random.choice(photo_urls)
    
    await callback_query.message.answer_photo(
        photo=photo,
        caption=quote,
        reply_markup=quote_kb
    )
    await callback_query.answer()
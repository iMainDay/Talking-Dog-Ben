from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, Message

import hashlib
import random
import config

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.inline_handler()
async def talking_ben_answers(q: InlineQuery):
    awailable_answers = ["yes", "no", "hohoho", "aaagh"]
    ben_choice = random.choice(awailable_answers)
    text = "Your question: *" + q.query + '*\nBen answer: *{}*'.format(ben_choice)
    content = InputTextMessageContent(text, parse_mode="markdown")
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    thumb = "https://m.media-amazon.com/images/I/91FjP7-I2NL._AC_UL960_QL65_.png"
    item = InlineQueryResultArticle(id=result_id, title=q.query or "Ben answer", description="Enter your question",
                                    input_message_content=content, thumb_url=thumb)

    await q.answer([item], is_personal=True)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


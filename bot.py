import random
import telebot

TOKEN = "7566735452:AAEzy7TCaw13GLQyu-TQUi_vLU_no_V3NtI"
bot = telebot.TeleBot(TOKEN)

# Persian Truth Questions (سوال حقیقت)
truth_questions = [
    "تا حالا به کسی دروغ بزرگی گفتی؟ چی بود؟",
    "آخرین باری که گریه کردی کی بود و چرا؟",
    "بزرگ‌ترین ترس زندگیت چیه؟",
    "آیا تا حالا شده که به کسی خیانت کنی یا بهت خیانت بشه؟",
    "اگه می‌تونستی یک نفر رو از زندگیت حذف کنی، کیو حذف می‌کردی؟",
    "بدترین سوتی عمرت چی بوده؟",
    "آیا راز بزرگی داری که هیچ‌کس ازش خبر نداره؟",
    "آخرین باری که خجالت کشیدی کی بود و چرا؟",
    "از بین همه‌ی افراد این گروه، کیو بیشتر دوست داری؟",
    "اگه مجبور بشی فقط یک نفر رو تا آخر عمرت ببینی، کیو انتخاب می‌کنی؟",
    "تا حالا به کسی حسادت کردی؟ چرا؟",
    "آیا دوست داشتی با یک نفر دیگه توی این گروه جای خودتو عوض کنی؟",
    "از بین افراد این گروه، حاضری با کی یک روز کامل رو بگذرونی؟",
    "آیا تا حالا کسی رو بدون اینکه بفهمه دوست داشتی؟",
    "اگه بخوای یه عادت بدتو ترک کنی، چی رو انتخاب می‌کنی؟",
    "بزرگ‌ترین اشتباه زندگی‌ات چی بوده؟",
    "تا حالا شده که به کسی ابراز علاقه کنی و جواب منفی بگیری؟",
    "آخرین باری که به کسی دروغ گفتی کی بود و چرا؟",
    "اگه بتونی یکی از آرزوهات رو همین الان برآورده کنی، چی می‌خوای؟",
    "چه چیزی بیشتر از همه تو رو عصبانی می‌کنه؟",
    "بدترین خاطره‌ای که توی زندگیت داشتی چی بوده؟",
    "آیا تا حالا از کسی سوءاستفاده کردی؟",
    "آیا تا حالا به کسی که دوستش داشتی دروغ گفتی؟",
    "اگه بتونی برای ۲۴ ساعت هر کاری که بخوای انجام بدی، چی‌کار می‌کنی؟",
    "آیا تا حالا کسی رو یواشکی تعقیب کردی؟",
    "تا حالا شده که دوست صمیمی‌ات بهت خیانت کنه؟",
    "از چه چیزی توی زندگی‌ات بیشتر از همه پشیمونی؟",
    "آیا تا حالا نامه عاشقانه نوشتی؟",
    "سخت‌ترین تصمیمی که تا حالا توی زندگیت گرفتی چی بوده؟",
    "آیا به کسی حسادت می‌کنی؟ چرا؟",
    "وقتی ناراحت می‌شی، معمولاً چی‌کار می‌کنی؟",
    "اگه مجبور باشی یه سال بدون اینترنت زندگی کنی، چی‌کار می‌کنی؟",
    "آیا تا حالا به کسی رشوه دادی یا رشوه گرفتی؟",
    "وقتی برای اولین بار عاشق شدی، چه احساسی داشتی؟",
    "آیا تا حالا به کسی که نباید، دل بستی؟",
    "آیا دوست داشتی یکی از افراد این گروه جای خواهر/برادرت بود؟",
    "آیا تا حالا با کسی قهر بودی و بعداً پشیمون شدی؟",
    "اولین باری که دل کسی رو شکستی، کی بود؟",
    "تا حالا شده که بخوای از کشورت مهاجرت کنی؟",
    "آیا تا حالا کسی رو با نیت بد فریب دادی؟",
    "دوست داری به گذشته برگردی و یه چیزی رو تغییر بدی؟ چی؟",
    "آیا کسی تا حالا بهت پیشنهادی داده که نتونستی ردش کنی؟",
    "اگه بتونی برای یک روز هر کسی که می‌خوای باشی، کیو انتخاب می‌کنی؟",
    "آیا تا حالا کسی رو به خاطر پول دوست داشتی؟",
    "تا حالا شده کسی رو مسخره کنی و بعداً پشیمون بشی؟",
    "بزرگ‌ترین آرزوی تو چیه که هنوز بهش نرسیدی؟",
    "آیا حاضری برای ۱ میلیون دلار عشق خودتو کنار بذاری؟",
    "آیا تا حالا به دوستت حسودی کردی؟ چرا؟",
    "اگه امروز آخرین روز زندگیت باشه، چی‌کار می‌کنی؟",
    "آیا تا حالا شده که به شدت عاشق بشی ولی طرف مقابلت بهت اهمیت نده؟"
]

# Persian Dare Challenges (سوال جرات)
dare_challenges = [
    "به اولین نفری که توی مخاطبینت هست زنگ بزن و بگو که دوستش داری!",
    "یه پیام عاشقانه به یکی از اعضای گروه بفرست.",
    "برای ۱۰ دقیقه پروفایلت رو به یه عکس خنده‌دار تغییر بده.",
    "یک پیام به شخصی که مدت‌ها باهاش حرف نزدی بفرست و بگو دلت براش تنگ شده.",
    "آخرین پیامی که توی گوشیت داری رو توی گروه بفرست!",
    "به یکی از اعضای گروه زنگ بزن و باهاش آواز بخون.",
    "برای ۵ دقیقه مثل یک ربات صحبت کن!",
    "برای ۲ دقیقه بدون اینکه بخندی یه جوک بی‌مزه تعریف کن.",
    "یکی از رازهای شخصی خودتو بگو.",
    "به یکی از افراد گروه پیام بده و بگو که عاشقش شدی.",
    "۵ دقیقه فقط با ایموجی پیام بده.",
    "یه داستان خنده‌دار از بچگی‌ات تعریف کن.",
    "برای ۱ دقیقه یه تبلیغ خیالی از خودت بساز و اجرا کن.",
    "یه پیام به یکی از دوستات بده و بگو که بهش بدهکاری!",
    "به اولین نفری که آنلاینه یه پیام عجیب بده.",
    "۱۰ تا از آخرین جستجوهای گوگلت رو بفرست!",
    "یکی از خجالت‌آورترین لحظات زندگیتو تعریف کن.",
    "برای ۳۰ ثانیه فقط با لهجه عجیب صحبت کن.",
    "یک سلفی مسخره بگیر و توی گروه بفرست.",
    "برای ۲ دقیقه ادای یکی از اعضای گروه رو در بیار.",
    "یک حقیقت خیلی عجیب درباره خودت بگو.",
    "به یکی از دوستات پیام بده و بگو که می‌خوای باهاش ازدواج کنی.",
    "یه اعتراف عجیب درباره بچگی‌ات بکن.",
    "برای ۲ دقیقه یه آهنگ بی‌معنی بخون.",
    "به مدت ۵ دقیقه اسم خودت رو عوض کن و یه اسم خنده‌دار بذار.",
    "بدون دلیل به یه نفر زنگ بزن و فقط “الو الو” بگو و قطع کن!",
    "به مدت ۲ دقیقه فقط به عقب راه برو.",
    "یکی از اعضای گروه رو تقلید کن.",
    "به اولین نفری که می‌بینی بگو که عاشقشی!",
    "۵ پیام آخر تلگرامت رو بدون دیدن، کپی کن و اینجا بفرست.",
    "یه اعتراف خنده‌دار درباره crush سابقت بکن.",
    "برای ۱ دقیقه چشماتو ببند و هر چی میگیم انجام بده.",
    "یه جمله خیلی خجالت‌آور برای کسی بفرست.",
    "آخرین عکسی که گرفتی رو بفرست.",
    "به یه نفر بگو که ازش متنفری و بعد دلیلشو توضیح بده!",
    "یه عکس از صفحه اول گوشی‌ات بفرست.",
    "به یکی از دوستات زنگ بزن و باهاش دعوا کن.",
    "اولین کلمه‌ای که الان به ذهنت میاد بفرست.",
    "برای ۳ دقیقه با کسی که اصلاً نمی‌شناسی چت کن.",
    "به مدت ۲ دقیقه ادای بچه‌ها رو دربیار.",
    "بدون دلیل به کسی پیام بده و بگو که خیلی دوستش داری.",
    "اولین نفری که آنلاین شدو صدا کن.",
    "یه سوتی خفن که دادی تعریف کن.",
    "آهنگ مورد علاقتو توی گروه بفرست.",
    "یه راز خنده‌دار از خودت بگو.",
    "از اولین نفری که می‌بینی تعریف کن!",
    "توی گروه اعتراف کن که عاشق کسی شدی.",
    "برای ۲ دقیقه یه رقص مسخره بکن.",
    "به یکی از اعضای گروه بگو که بهترین دوستته!",
    "یه جوک خنده‌دار تعریف کن."
]

# List of "بیو" responses
bio_messages = [
    """معجزه میکنه برات خدایی که صبوری هات رو دیده 💚☘️

صـبـر یـه قـدرت بــزرگـه !✨️🌱

اَندَکی‌صَبر‌؛حوادِث‌روزِگار‌میچَرخَد🖤🌱️

‌ هر آدمی خودش جایگاه خودشو مشخص میکنه! ‌️""",
    """اَندَکی‌صَبر‌؛حوادِث‌روزِگار‌میچَرخَد🖤🌱️

‌ هر آدمی خودش جایگاه خودشو مشخص میکنه! ‌️

‌  خودت خالقِ زیباترین اتفاقاتِ زندگی ات باش‌‌.🤍 ‌‌️""",
    """‌ هر آدمی خودش جایگاه خودشو مشخص میکنه! ‌️

‌  خودت خالقِ زیباترین اتفاقاتِ زندگی ات باش‌‌.🤍 ‌‌️

سـٰادِه‌اَمـٰابـٰااِصـٰالَت'🪬✨️🧿!️""",
    """  خودت خالقِ زیباترین اتفاقاتِ زندگی ات باش‌‌.🤍 ‌‌️
سـٰادِه‌اَمـٰابـٰااِصـٰالَت'🪬✨️🧿!️""",
    """‹فِـکرِ‌پَروآز‌بـاش‌حتی‌دَرسّـقوطِ🕊🤍›️

‌  خودت خالقِ زیباترین اتفاقاتِ زندگی ات باش‌‌.🤍 ‌‌️

سـٰادِه‌اَمـٰابـٰااِصـٰالَت'🪬✨️🧿!️""",
    """‹فِـکرِ‌پَروآز‌بـاش‌حتی‌دَرسّـقوطِ🕊🤍›️

_'اَزِ‌بیروِنِ‌میخَندی‌وَلیِ‌اَزِ‌دروِن‌مُردی'🖤✨️🫠!️

زیـبـایـے بــہ چـهـره نـیـسـت، بــہ نـوریـسـت کــہ از دل مـےتـابـد..!️""",
    """زیـبـایـے بــہ چـهـره نـیـسـت، بــہ نـوریـسـت کــہ از دل مـےتـابـد..!️

بزار‌لبخندت‌دنیا‌رو‌تغییر‌بده؛ولی‌نزار‌دنیا‌لبخندت‌رو‌تغییر‌بده❤️‍🩹️""",
    """زیـبـایـے بــہ چـهـره نـیـسـت، بــہ نـوریـسـت کــہ از دل مـےتـابـد..!️

بزار‌لبخندت‌دنیا‌رو‌تغییر‌بده؛ولی‌نزار‌دنیا‌لبخندت‌رو‌تغییر‌بده❤️‍🩹️

کسی که امید دارد همه چیز دارد!🌿🤍️""",
    """واخرین تصویرم از زندگی کنار جاده رو به آسمان باشد:) ️

مهم اینه که چشمات بخنده•‿•💫️

-شاخ بازی در میاری چیزی نمیگم فکر نکن میترسم، دارم به حقوق حیوانات احترام میزارم❤️️"""
]

# Handler for "بیو" messages
@bot.message_handler(func=lambda message: message.text == "بیو")
def handle_bio(message):
    response = random.choice(bio_messages)
    bot.reply_to(message, response)


# When a user sends "حقیقت", reply with a random truth question
@bot.message_handler(func=lambda message: message.text == "حقیقت")
def handle_truth(message):
    response = random.choice(truth_questions)
    bot.reply_to(message, response)

# When a user sends "جرعت" or "جرات", reply with a random dare challenge
@bot.message_handler(func=lambda message: message.text in ["جرعت", "جرات"])
def handle_dare(message):
    response = random.choice(dare_challenges)
    bot.reply_to(message, response)



@bot.message_handler(func=lambda message: "سلام" in message.text)
def handle_salam(message):
    response = "ع سلام خوش امدین به گروپ چت جهانی زیبایی های زندگی_𝐋𝐮𝐗"
    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: "سرطان کیص" in message.text)
def handle_salam(message):
    response = "سرطان بزرگترین شخص در سطح تلگرام و سازنده من است"
    bot.reply_to(message, response)

bot.polling()
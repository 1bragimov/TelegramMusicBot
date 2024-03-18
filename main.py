import telebot
from root_token import TOKEN
from buttons import keyboard

telebot.TeleBot = TOKEN

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


########################################################

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("""Assalomu alaykum! Botdan foydalanish uchun avval ro'yxatdan o'tishingizni iltimos qilamiz.

Keling, avval xizmat ko‘rsatish 🇺🇿 tilini tanlab olaylik.

________________________________

Здравствуйте! Для продолжения просим вас пройти регистрацию.

Выберите 🇷🇺 язык обслуживания.""", reply_markup=keyboard)


@bot1.message_handler(commands=["Image"])
def image(photo):
    bot1.send_photo(photo.chat.id,
                    photo="https://avatars.mds.yandex.net/i?id=1b27be8e76bd5fe7682161c16f6197ae_l-5383794-images-thumbs&n=13",
                    caption=f"For you mativation! {photo.from_user.first_name}")


@bot1.message_handler(commands=["Uzbek"])
def uzbek_music(message):
    bot1.send_message(message.chat.id, "This is bot yes all Uzbek music!")

@bot1.message_handler(commands=["1Music"])
def audio1(audio):
    bot1.send_audio(audio.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-10/doston-ergashev-toyi-bolyapti.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Toyi-Bo'lyapti.mp3")


@bot1.message_handler(commands=["2Music"])
def audio2(audi1):
    bot1.send_audio(audi1.chat.id, audio="https://musicuz.com/uploads/public_files/2023-09/doston_ergashev-tuya.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Tuya.mp3")


@bot1.message_handler(commands=["3Music"])
def audio3(audi2):
    bot1.send_audio(audi2.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-09/doston-ergashev-boravering.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Boravering.mp3")


@bot1.message_handler(commands=["4Music"])
def audio4(audi3):
    bot1.send_audio(audi3.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-10/doston-ergashev-soddaginam-remix.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Soddaginam.mp3")


@bot1.message_handler(commands=["5Music"])
def audio5(audi4):
    bot1.send_audio(audi4.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-10/doston-ergashev-soginmadingmu.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Sog'inmadingmu.mp3")


@bot1.message_handler(commands=["6Music"])
def audio6(audi5):
    bot1.send_audio(audi5.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-10/doston-ergashev-onam-qongiroq-qildi-jonli-ijro.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Onam-Qo'ng'iroq-Qildii.mp3")


@bot1.message_handler(commands=["7Music"])
def audio7(audi6):
    bot1.send_audio(audi6.chat.id, audio="https://musicuz.com/uploads/public_files/2023-12/doston-ergashev-zoya.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Zoya.mp3")


@bot1.message_handler(commands=["8Music"])
def audio8(audi7):
    bot1.send_audio(audi7.chat.id,
                    audio="https://musicuz.com/uploads/public_files/2023-12/doston_ergashev-ayt_gozalim.mp3",
                    caption="All songs are for you!"
                            "Doston Ergashev-Ayt-Guzalim.mp3")


@bot1.message_handler(commands=["9Music"])
def audio9(audi8):
    bot1.send_audio(audi8.chat.id,
                    audio="https://uzhits.net/uploads/files/2022-11/xurshid-rasulov-tulki_(uzhits.net).mp3",
                    caption="All songs are for you!"
                            "xurshid-rasulov-tulki")

@bot1.message_handler(commands=["10Music"])
def audio10(audi9):
    bot1.send_audio(audi9.chat.id, audio="https://musicuz.com/uploads/public_files/2023-12/jahongir_otajonov_biyo_biyo_zhahongir_otazhonov_bie_bie_premyera_2023.mp3",
                    caption="All songs are for you!"
                    "jahongir_otajonov_biyo_biyo_zhahongir_otazhonov_bie_bie_premyera_2023")


@bot1.message_handler(commands=["11Music"])
def audio11(audi10):
    bot1.send_audio(audi10.chat.id, audio="https://musicuz.com/uploads/public_files/2023-11/jaloliddin-ahmadaliyev-toyingizga-bormayman.mp3",
                    caption="All songs are for you!"
                            "jaloliddin-ahmadaliyev-toyingizga-bormayman")


@bot1.message_handler(commands=["12Music"])
def audio12(audi11):
    bot1.send_audio(audi11.chat.id, audio="https://musicuz.com/uploads/public_files/2023-12/olmas-olloberganov-unutma.mp3",
                    caption="All songs are for you!"
                            "olmas-olloberganov-unutma")


@bot1.message_handler(commands=["13Music"])
def audio13(audi12):
    bot1.send_audio(audi12.chat.id, audio="https://musicuz.com/uploads/public_files/2023-10/umidaxon-senga-men-kam.mp3",
                    caption="All songs are for you!"
                            "umidaxon-senga-men-kam")


@bot1.message_handler(commands=["14Music"])
def audio14(audi13):
    bot1.send_audio(audi13.chat.id, audio="https://musicuz.com/uploads/public_files/2023-11/xamdam-sobirov-va-rayhon-qizil-koylak.mp3",
                    caption="All songs are for you!"
                            "xamdam-sobirov-va-rayhon-qizil-koylak")


@bot1.message_handler(commands=["15Music"])
def audio15(audi14):
    bot1.send_audio(audi14.chat.id, audio="https://musicuz.com/uploads/public_files/2023-12/1701527336_jaloliddin-ahmadaliyev-bevafo-dil_www_musicuz_com-1.mp3",
                    caption="All songs are for you!"
                            "jaloliddin-ahmadaliyev-bevafo-dil")

####################################################################################
####################################################################################
####################################################################################


@bot1.message_handler(commands=["End"])
def end_bot(photo):
    bot1.send_photo(photo.chat.id,
                    photo="https://yandex.ru/images/search?img_url=https%3A%2F%2Fassets.website-files.com%2F629127723a265d001190e73b%2F62f15bcb23230306ae66684b_BYB_Logo_2.webp&lr=10335&pos=12&rpt=simage&source=serp&text=bye%20foto%20png",
                    caption=f"Thank you for using Pinguin bot! {photo.from_user.first_name}")


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


@bot1.message_handler(commands=["English"])
def send_message(message):
    bot1.send_message(message.chat.id, "This is bot yes all English music!"
                                       "𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙤𝙧𝙙𝙨 𝙩𝙤 𝙧𝙚𝙛𝙚𝙧 𝙩𝙤 𝙩𝙝𝙚 𝙗𝙤𝙩❕"
                                       "________________________________________________________________________"
                                       "/𝙨𝙩𝙖𝙧𝙩   <-  This word is to start the bot!"
                                       "________________________________________________________________________"
                                       "/𝙄𝙢𝙖𝙜𝙚   <-  This word is to bot's picture for you!"
                                       "________________________________________________________________________"
                                       "/𝙀𝙣𝙙     <-  This word is to audio for you to try!"
                                       "________________________________________________________________________"
                                       "/1𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/2𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/3𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/4𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/5𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/6𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/7𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/8𝙈𝙪𝙨𝙞𝙘 <- To find this word music!")


@bot1.message_handler(commands=["16Music"])
def kirish_1(sudio1):
    bot1.send_audio(sudio1.chat.id, audio="https://mp3bob.ru/download/muz/Maroon_5_-_Animals_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Maroon_5_-_Animals")


@bot1.message_handler(commands=["17Music"])
def kirish_2(sudio2):
    bot1.send_audio(sudio2.chat.id, audio="https://mp3bob.ru/download/muz/Katy_Perry_feat._TEE_-_Dark_Horse_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Katy_Perry_feat._TEE_-_Dark_Horse")


@bot1.message_handler(commands=["18Music"])
def kirish_3(sudio3):
    bot1.send_audio(sudio3.chat.id, audio="https://mp3bob.ru/download/muz/Rixton_-_Me_And_My_Broken_Heart_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Rixton_-_Me_And_My_Broken_Heart")


@bot1.message_handler(commands=["19Music"])
def kirish_4(sudio4):
    bot1.send_audio(sudio4.chat.id, audio="https://mp3bob.ru/download/muz/Otilia_-_Bilionera_(Radio_Edit)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Otilia_-_Bilionera_(Radio_Edit)")


@bot1.message_handler(commands=["20Music"])
def kirish_5(sudio5):
    bot1.send_audio(sudio5.chat.id, audio="https://mp3bob.ru/download/muz/Mohombi_-_Just_Like_That_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Mohombi_-_Just_Like_That")


@bot1.message_handler(commands=["21Music"])
def kirish_6(sudio6):
    bot1.send_audio(sudio6.chat.id, audio="https://mp3bob.ru/download/muz/Jockeyboys_feat._Nance_-_Higher_(Stephan_F_Remix_Edit)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Jockeyboys_feat._Nance_-_Higher_(Stephan_F_Remix_Edit)")


@bot1.message_handler(commands=["22Music"])
def kirish_7(sudio7):
    bot1.send_audio(sudio7.chat.id, audio="https://mp3bob.ru/download/muz/Hardwell_feat._Chris_Jones_-_Young_Again_(Radio_Edit)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Hardwell_feat._Chris_Jones_-_Young_Again_(Radio_Edit)")


@bot1.message_handler(commands=["23Music"])
def kirish_8(sudio8):
    bot1.send_audio(sudio8.chat.id, audio="https://mp3bob.ru/download/muz/Rixton_-_Wait_On_Me_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Rixton_-_Wait_On_Me")


@bot1.message_handler(commands=["24Music"])
def kirish_9(sudio9):
    bot1.send_audio(sudio9.chat.id, audio="https://mp3bob.ru/download/muz/Sean_Paul_-_Front_and_Back_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Sean_Paul_-_Front_and_Back")


@bot1.message_handler(commands=["25Music"])
def kirish_10(sudio10):
    bot1.send_audio(sudio10.chat.id, audio="https://mp3bob.ru/download/muz/Eli,_Oana_Radu_feat._Dr._Mako_-_Tu_(Radio_Edit)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Eli,_Oana_Radu_feat._Dr._Mako_-_Tu_(Radio_Edit)")


@bot1.message_handler(commands=["26Music"])
def kirish_11(sudio11):
    bot1.send_audio(sudio11.chat.id, audio="https://mp3bob.ru/download/muz/Shakira_-_Empire_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Shakira_-_Empire")


@bot1.message_handler(commands=["27Music"])
def kirish_12(sudio12):
    bot1.send_audio(sudio12.chat.id, audio="https://mp3bob.ru/download/muz/Psirico_and_Pitbull_-_Lepo_Lepo_(Radio_Edit)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Psirico_and_Pitbull_-_Lepo_Lepo_(Radio_Edit)")


@bot1.message_handler(commands=["28Music"])
def kirish_13(sudio13):
    bot1.send_audio(sudio13.chat.id, audio="https://mp3bob.ru/download/muz/Stromae_feat._Angel_Haze_-_Papaoutai_(Remix)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Stromae_feat._Angel_Haze_-_Papaoutai_(Remix)")


@bot1.message_handler(commands=["29Music"])
def kirish_14(opel14):
    bot1.send_audio(opel14.chat.id, audio="https://mp3bob.ru/download/muz/Robin_Schulz_feat._Jasmine_Thompson_-_Sun_Goes_Down_(Radio_Mix)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Robin_Schulz_feat._Jasmine_Thompson_-_Sun_Goes_Down_(Radio_Mix)")


@bot1.message_handler(commands=["30Music"])
def kirish_15(oper15):
    bot1.send_audio(oper15.chat.id, audio="https://mp3bob.ru/download/muz/Haris_-_Gold_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Haris_-_Gold")


@bot1.message_handler(commands=["End"])
def end_bot(photo):
    bot1.send_photo(photo.chat.id,
                    photo="https://yandex.ru/images/search?img_url=https%3A%2F%2Fassets.website-files.com%2F629127723a265d001190e73b%2F62f15bcb23230306ae66684b_BYB_Logo_2.webp&lr=10335&pos=12&rpt=simage&source=serp&text=bye%20foto%20png",
                    caption=f"Thank you for using Pinguin bot! {photo.from_user.first_name}")


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


# @bot1.message_handler(commands=["Russian"])
# def send_message(message):
#     bot1.send_message(message.chat.id, "This is bot yes all Russian music!"
#                                        "𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙤𝙧𝙙𝙨 𝙩𝙤 𝙧𝙚𝙛𝙚𝙧 𝙩𝙤 𝙩𝙝𝙚 𝙗𝙤𝙩❕"
#                                        "________________________________________________________________________"
#                                        "/𝙨𝙩𝙖𝙧𝙩   <-  This word is to start the bot!"
#                                        "________________________________________________________________________"
#                                        "/𝙄𝙢𝙖𝙜𝙚   <-  This word is to bot's picture for you!"
#                                        "________________________________________________________________________"
#                                        "/𝙀𝙣𝙙     <-  This word is to audio for you to try!"
#                                        "________________________________________________________________________"
#                                        "/1𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/2𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/3𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/4𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/5𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/6𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/7𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
#                                        "________________________________________________________________________"
#                                        "/8𝙈𝙪𝙨𝙞𝙘 <- To find this word music!")
#
#
# @bot1.message_handler(commands=["1Music"])
# def kirsh_1(adio1):
#     bot1.send_audio(adio1.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["2Music"])
# def kirsh_2(adio2):
#     bot1.send_audio(adio2.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["3Music"])
# def kirsh_3(adio3):
#     bot1.send_audio(adio3.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["4Music"])
# def kirsh_4(adio4):
#     bot1.send_audio(adio4.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["5Music"])
# def kirsh_5(adio5):
#     bot1.send_audio(adio5.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["6Music"])
# def kirsh_6(adio6):
#     bot1.send_audio(adio6.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["7Music"])
# def kirsh_7(adio7):
#     bot1.send_audio(adio7.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["8Music"])
# def kirsh_8(adio8):
#     bot1.send_audio(adio8.chat.id, audio="",


#######################################################################################
#######################################################################################
#######################################################################################

#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["9Music"])
# def kirsh_9(adio9):
#     bot1.send_audio(adio9.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["10Music"])
# def kirsh_10(adio10):
#     bot1.send_audio(adio10.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["11Music"])
# def kirsh_11(adio11):
#     bot1.send_audio(adio11.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["12Music"])
# def kirsh_12(adio12):
#     bot1.send_audio(adio12.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["13Music"])
# def kirsh_13(adio13):
#     bot1.send_audio(adio13.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["14Music"])
# def kirsh_14(adio14):
#     bot1.send_audio(adio14.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["15Music"])
# def kirsh_15(adio15):
#     bot1.send_audio(adio15.chat.id, audio="",
#                     caption="All songs are for you!"
#                             "")
#
#
# @bot1.message_handler(commands=["End"])
# def end_bot(photo):
#     bot1.send_photo(photo.chat.id,
#                     photo="https://yandex.ru/images/search?img_url=https%3A%2F%2Fassets.website-files.com%2F629127723a265d001190e73b%2F62f15bcb23230306ae66684b_BYB_Logo_2.webp&lr=10335&pos=12&rpt=simage&source=serp&text=bye%20foto%20png",
#                     caption=f"Thank you for using Pinguin bot! {photo.from_user.first_name}")


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


@bot1.message_handler(commands=["Turkish"])
def send_message(message):
    bot1.send_message(message.chat.id, "This is bot yes all Turk music!"
                                       "𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙤𝙧𝙙𝙨 𝙩𝙤 𝙧𝙚𝙛𝙚𝙧 𝙩𝙤 𝙩𝙝𝙚 𝙗𝙤𝙩❕"
                                       "________________________________________________________________________"
                                       "/𝙨𝙩𝙖𝙧𝙩   <-  This word is to start the bot!"
                                       "________________________________________________________________________"
                                       "/𝙄𝙢𝙖𝙜𝙚   <-  This word is to bot's picture for you!"
                                       "________________________________________________________________________"
                                       "/𝙀𝙣𝙙     <-  This word is to audio for you to try!"
                                       "________________________________________________________________________"
                                       "/1𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/2𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/3𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/4𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/5𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/6𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/7𝙈𝙪𝙨𝙞𝙘 <- To find this word music!"
                                       "________________________________________________________________________"
                                       "/8𝙈𝙪𝙨𝙞𝙘 <- To find this word music!")


@bot1.message_handler(commands=["31Music"])
def kir_1(auo1):
    bot1.send_audio(auo1.chat.id, audio="https://mp3bob.ru/download/muz/Tarkan_-_Ask_Gitti_Bizden_(Dj_Tarkan_Official_Remix)_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Tarkan_-_Ask_Gitti_Bizden_(Dj_Tarkan_Official_Remix)")


@bot1.message_handler(commands=["32Music"])
def kir_2(auo2):
    bot1.send_audio(auo2.chat.id, audio="https://mp3bob.ru/download/muz/Nurlan_Tehmezli_-_Neylerem_sensiz_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Nurlan_Tehmezli_-_Neylerem_sensiz")


@bot1.message_handler(commands=["33Music"])
def kir_3(auo3):
    bot1.send_audio(auo3.chat.id, audio="https://mp3bob.ru/download/muz/Rafet_El_Roman_-_Yalan_sevgi_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Rafet_El_Roman_-_Yalan_sevgi")


@bot1.message_handler(commands=["34Music"])
def kir_4(auo4):
    bot1.send_audio(auo4.chat.id, audio="https://mp3bob.ru/download/muz/Uzeyir_Mehdizade_-_Teki_Men_Tenha_Qalmayim_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Uzeyir_Mehdizade_-_Teki_Men_Tenha_Qalmayim")


@bot1.message_handler(commands=["35Music"])
def kir_5(auo5):
    bot1.send_audio(auo5.chat.id, audio="https://mp3bob.ru/download/muz/Yusuf_Guney_-_Hazin_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Yusuf_Guney_-_Hazin")


@bot1.message_handler(commands=["36Music"])
def kir_6(auo6):
    bot1.send_audio(auo6.chat.id, audio="https://mp3bob.ru/download/muz/Ufuk_Caliskan_-_Unutmaq_Istiyorum_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Ufuk_Caliskan_-_Unutmaq_Istiyorum")


@bot1.message_handler(commands=["37Music"])
def kir_7(auo7):
    bot1.send_audio(auo7.chat.id, audio="https://mp3bob.ru/download/muz/Azim_Ali_-_Sen_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Azim_Ali_-_Sen")


@bot1.message_handler(commands=["38Music"])
def kir_8(auo8):
    bot1.send_audio(auo8.chat.id, audio="https://mp3bob.ru/download/muz/Uzeyir_Mehdizade_-_Divaneyem_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Uzeyir_Mehdizade_-_Divaneyem")


@bot1.message_handler(commands=["39Music"])
def kir_9(auo9):
    bot1.send_audio(auo9.chat.id, audio="https://mp3bob.ru/download/muz/Orxan_Deniz_ft_Asiq_Sebuhi_-_Menim_Balam_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Orxan_Deniz_ft_Asiq_Sebuhi_-_Menim_Balam")


@bot1.message_handler(commands=["40Music"])
def kir_10(auo10):
    bot1.send_audio(auo10.chat.id, audio="https://mp3bob.ru/download/muz/Uzeyir_Mehdizade_ft_Fuad_Ibrahimov_-_Anamla_Getdi_Her_Sey_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Uzeyir_Mehdizade_ft_Fuad_Ibrahimov_-_Anamla_Getdi_Her_Sey")


@bot1.message_handler(commands=["41Music"])
def kir_11(auo11):
    bot1.send_audio(auo11.chat.id, audio="https://mp3bob.ru/download/muz/Magomed_Kerimov_-_Neler_Danisdim_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Magomed_Kerimov_-_Neler_Danisdim")


@bot1.message_handler(commands=["42Music"])
def kir_12(auo12):
    bot1.send_audio(auo12.chat.id, audio="https://mp3bob.ru/download/muz/Talib_Tale_-_Baki_axsamlari_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Talib_Tale_-_Baki_axsamlari")


@bot1.message_handler(commands=["43Music"])
def kir_13(auo13):
    bot1.send_audio(auo13.chat.id, audio="https://mp3bob.ru/download/muz/Ferid_Esqin_-_Seni_Sevirem_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Ferid_Esqin_-_Seni_Sevirem")


@bot1.message_handler(commands=["44Music"])
def kir_14(auo14):
    bot1.send_audio(auo14.chat.id, audio="https://mp3bob.ru/download/muz/Amid_Sani_-_Oyun_acdin_basima_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Amid_Sani_-_Oyun_acdin_basima")


@bot1.message_handler(commands=["45Music"])
def kir_15(auo15):
    bot1.send_audio(auo15.chat.id, audio="https://mp3bob.ru/download/muz/Teymur_Gozelov_-_Olmaz_olmaz_[mp3pulse.ru].mp3",
                    caption="All songs are for you!"
                            "Teymur_Gozelov_-_Olmaz_olmaz")


@bot1.message_handler(commands=["End"])
def end_bot(photo):
    bot1.send_photo(photo.chat.id,
                    photo="https://yandex.ru/images/search?img_url=https%3A%2F%2Fassets.website-files.com%2F629127723a265d001190e73b%2F62f15bcb23230306ae66684b_BYB_Logo_2.webp&lr=10335&pos=12&rpt=simage&source=serp&text=bye%20foto%20png",
                    caption=f"Thank you for using Pinguin bot! {photo.from_user.first_name}")


bot1.polling()

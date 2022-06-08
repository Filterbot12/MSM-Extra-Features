"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
ADMIN = "<b>𝙼𝚂𝙼 𝙰𝙳𝙼𝙸𝙽 ›› https://t.me/MSMadminBot</b>"
CHANNEL = "<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›  https://t.me/msmOTT\n\n<b>𝙼𝙾𝚅𝙸𝙴 𝙶𝚁𝙾𝚄𝙿 ›› https://t.me/msmOTT</b>\n\n<b>𝙽𝙴𝚆 𝚁𝙴𝙻𝙴𝙰𝚂𝙴 ›› https://t.me/+4fYWefZL12U1YjZl</b>"
MOVIE = "സിനിമ ഇവിടെ ലഭിക്കില്ല..  ഈ ഗ്രൂപ്പിൽ സിനിമയുടെ Correct Name അടിച്ചാൽ സിനിമ കിട്ടും <b>𝙼𝚂𝙼 𝙲𝙷𝙰𝚃 ›› https://t.me/MSMchat</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("admin", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(ADMIN)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("movie", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(MOVIE)



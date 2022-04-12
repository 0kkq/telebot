from info import *

markup_inline = types.InlineKeyboardMarkup()

zkhrafah = types.InlineKeyboardButton(text='زخرفه', callback_data='zkh')
markup_inline.row_width = 2
markup_inline.add(zkhrafah)

# !/usr/bin/python
import config
import telegram
import os
import subprocess
import sys
import shlex
import datetime
import logging

from subprocess import Popen, PIPE
from telegram.ext import CommandHandler
from importlib import reload

from telegram.ext import Updater, CallbackContext
from telegram import Update

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = telegram.Bot(token=config.token)
# Проверка бота
print(bot.get_me())

updater = Updater(token=config.token, use_context=True)
dispatcher = updater.dispatcher


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def help(update: Update, context: CallbackContext):
    reload(config)
    context.bot.send_message(chat_id=update.message.chat_id, text='''список доступных команд:
  /id - id пользователя
  /ifconfig - сетевые настройки
  /df - информация о дисковом пространстве (df -h)
  /free - информация о памяти
  /mpstat - информация о нагрузке на процессор

  ''')


# функция команады id
def myid(update: Update, context: CallbackContext):
    userid = update.message.from_user.id
    context.bot.send_message(chat_id=update.message.chat_id, text=userid)


# функция команады ifconfig
def ifconfig(update: Update, context: CallbackContext):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:  # если пользовательский id в списке admin то команда выполняется
        run_command("ifconfig")
        context.bot.send_message(chat_id=update.message.chat_id, text=textoutput)


# функция команады df
def df(update: Update, context: CallbackContext):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:  # если пользовательский id в списке admin то команда выполняется
        run_command("df -h")
        context.bot.send_message(chat_id=update.message.chat_id, text=textoutput)


# функция команады free
def free(update: Update, context: CallbackContext):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:  # если пользовательский id в списке admin то команда выполняется
        run_command("free -m")
        context.bot.send_message(chat_id=update.message.chat_id, text=textoutput)


# функция команады mpstat
def mpstat(update: Update, context: CallbackContext):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:  # если пользовательский id в списке admin то команда выполняется
        run_command("mpstat")
        context.bot.send_message(chat_id=update.message.chat_id, text=textoutput)


# функция команады top
def apachestatus(update: Update, context: CallbackContext):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:  # если пользовательский id в списке admin то команда выполняется
        run_command("apachestatus")
        context.bot.send_message(chat_id=update.message.chat_id, text=textoutput)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

ifconfig_handler = CommandHandler('ifconfig', ifconfig)
dispatcher.add_handler(ifconfig_handler)

df_handler = CommandHandler('df', df)
dispatcher.add_handler(df_handler)

free_handler = CommandHandler('free', free)
dispatcher.add_handler(free_handler)

mpstat_handler = CommandHandler('mpstat', mpstat)
dispatcher.add_handler(mpstat_handler)

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()

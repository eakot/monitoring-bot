# monitoring-bot

```
sudo apt install sysstat
pip install poetry
```
# Настройка
Для создания чат-бота в Telegram используется бот @BotFather. 
Token нужно ввести в ./src/config. Для получения chat_id нужно перейти в ваш с ним чат и 
нажать старт и отправить любой символ. После этого в браузере перейти по адресу:
https://api.telegram.org/bot<token>/getUpdates — где <token> это API который выдал BotFather.

# Скрипты запуска

Отредактировать поля User, пути к репозиторию и poetry. Затем скопировать файлы и включить 

```
sudo cp ./systemctl/monitoring-bot.service /etc/systemd/system/
sudo cp ./systemctl/monitoring-bot-on-boot.service /etc/systemd/system/

sudo systemctl enable monitoring-bot.service
sudo systemctl enable monitoring-bot-on-boot.service 

sudo systemctl start monitoring-bot.service
```
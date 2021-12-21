FROM python

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install pyTelegramBotAPI
RUN python -m pip install python-dotenv

COPY . .

CMD ["python", "echo_bot.py"]
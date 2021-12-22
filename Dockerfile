FROM python

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install pyTelegramBotAPI
RUN python -m pip install googletrans==4.0.0-rc1
RUN python -m pip install pylint

COPY . .

CMD ["python", "bot.py"]
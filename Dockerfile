FROM python:3.8

# WORKDIR /usr/src/app
# COPY . /usr/src/app/

WORKDIR /app
COPY . ./

RUN pip install --user telebot
# RUN pip install --no-cache-dir -r --user requirements.txt
# run app
# CMD [ "python", "./main.py" ]
CMD python3.8 InCommunityHelpBot/main.py

import pathlib
from pathlib import Path

from InCommunityHelpBot.main import InCommunityHelpBot, token

if __name__ == '__main__':
    InCommunityHelpBot.polling(none_stop=True)
    # InCommunityHelpBot.infinity_polling()

    # InCommunityHelpBot.remove_webhook()
    InCommunityHelpBot.delete_webhook()
    InCommunityHelpBot.set_webhook('https://test.com/' + token)

# @app.route("/" + token, methods=['POST'])
# def getMessage():
#     InCommunityHelpBot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200

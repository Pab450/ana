from revChatGPT.revChatGPT import Chatbot
import tweepy
import json


class Ana(tweepy.StreamingClient):
    conversation_ids = {}

    def __init__(self, bot_username, twitter_credentials_file, open_ai_credentials_file):
        twitter_credentials = self.read_credentials(twitter_credentials_file)
        self.client = tweepy.Client(**twitter_credentials)

        self.chatbot = Chatbot(self.read_credentials(open_ai_credentials_file), conversation_id=None)
        self.chatbot.refresh_session()

        super().__init__(twitter_credentials['bearer_token'])

        for rule in self.get_rules().data:
            self.delete_rules(rule.id)

        self.add_rules(tweepy.StreamRule(bot_username))
        self.filter()

    @staticmethod
    def read_credentials(filename):
        with open(filename, "r") as file:
            creds = json.load(file)

        return creds

    def on_tweet(self, tweet):
        tweet = self.client.get_tweet(tweet.id, tweet_fields="conversation_id,in_reply_to_user_id,author_id")
        twitter_conversation_id = tweet.data.conversation_id

        if tweet.data.text[:2] == "RT":
            return

        print(tweet.data.text)

        if self.get_username(tweet.data.author_id) == self.get_bot_username():
            return

        if tweet.data.id != twitter_conversation_id and \
                self.get_username(tweet.data.in_reply_to_user_id) != self.get_bot_username():
            return

        if twitter_conversation_id not in self.conversation_ids:
            self.conversation_ids[twitter_conversation_id] = None

        self.chatbot.conversation_id = self.conversation_ids[twitter_conversation_id]

        try:
            chat_response = self.chatbot.get_chat_response(self.text_modifier(tweet.data.text), output="text")
            self.conversation_ids[twitter_conversation_id] = chat_response['conversation_id']
        except Exception as e:
            self.client.create_tweet(
                text="We're working to restore all services as soon as possible. Please check back soon.",
                in_reply_to_tweet_id=tweet.data.id
            )
            return

        for i in range(0, len(chat_response['message']), 280):
            tweet.data.id = self.client.create_tweet(text=chat_response['message'][i:i + 280],
                                                     in_reply_to_tweet_id=tweet.data.id).data['id']

    def get_username(self, user_id):
        if user_id is None:
            return None

        return '@' + self.client.get_user(id=user_id).data.username.lower()

    def get_bot_username(self):
        return self.get_rules().data[0].value.lower()

    @staticmethod
    def text_modifier(text):
        text = ' '.join(word for word in text.split() if not word.startswith('@'))
        return text

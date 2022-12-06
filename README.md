# ChatGPT
Reverse Engineered ChatGPT by OpenAI. Extensible for chatbots etc. Forked from https://github.com/acheong08/ChatGPT

# Setup

## Configuration of the twitter bot and credentials

1. Go to https://developer.twitter.com/en/portal/projects-and-appscreate an application.
2. Once the configuration is done, retrieve all the tokens
3. Save your twitter `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` and the `bearer_token` into `twitter_credentials.json`
4. Replace in the main.py file `@twittosAcc` by the `@username` of your bot so that it can receive all tweets mentioning it

## Get your OpenAI session token

1. Go to https://chat.openai.com/chat and log in or sign up
2. Open console with `F12`
3. Open `Application` tab > Cookies
![image](https://user-images.githubusercontent.com/36258159/205494773-32ef651a-994d-435a-9f76-a26699935dac.png)
4. Copy the value for `__Secure-next-auth.session-token` and paste it into `open_ai_credentials.json` under `session_token`. You do not need to fill out `Authorization`
![image](https://user-images.githubusercontent.com/36258159/205495076-664a8113-eda5-4d1e-84d3-6fad3614cfd8.png)

## Install

`pip3 install revChatGPT --upgrade`
`pip3 install tweepy`

## Running

`python3 main.py`

## Result

![image](https://raw.githubusercontent.com/Pab450/ana/main/images/img2.png)
![image](https://raw.githubusercontent.com/Pab450/ana/main/images/img1.png)

### Ana is available here : https://twitter.com/TwittosAcc

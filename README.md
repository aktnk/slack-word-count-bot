# Slack bot that counts the number of characters.

## User case

* When you talk to this bot on a channel of slack, he will answer the number of characters you talked to.

```
 your name 10:23
 @counter_bot 文字数を教えて下さい。
```
```
 counter_bot [app] 10:23
 @your name: メッセージは
 "文字数を教えて下さい。"
  文字数:11
```

## System config

1. counter_bot : slack bot application programed by Python
1. heroku : execution environment of the counter_bot
1. slack

## how to deploy on heroku

You must have your account of the Heroku. 
And you must have installed the Heroku CLI on your PC.
1. Clone this repository on your PC.
    ```
    $ git clone https://github.com/aktnk/slack-word-count-bot.git
    ```
1. Login your heroku acount.
    ```
    $ heroku login
    ```
1. Create application.
    ```
    $ heroku create (application name)
    ```
1. Set config vars API_TOKEN to the heroku application settings.

    [Settings] > [Config Vars] 

    Set "API_TOKEN" at KEY and the API Token code which you got from the Slack App Bots Settings at VALUE.

1. Add remote repository to the heroku repository.
    ```
    $ heroku git:remote -a (application name)
    ```
1. Push source code to the heroku repository.
    ```
    $ git push heroku master
    ```

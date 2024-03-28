# ai_pngtuber_ollama

### Table of content
- [ai\_pngtuber\_ollama](#ai_pngtuber_ollama)
    - [Table of content](#table-of-content)
  - [Video example HERE](#video-example-here)
  - [What is Ai PngTuber Ollama?](#what-is-ai-pngtuber-ollama)
  - [Do i need to pay something?](#do-i-need-to-pay-something)
  - [How to install Ollama and what model?](#how-to-install-ollama-and-what-model)
  - [How to run Ollama as server?](#how-to-run-ollama-as-server)
  - [How to setup this app?](#how-to-setup-this-app)
  - [How to change the avatar of the PngTuber?](#how-to-change-the-avatar-of-the-pngtuber)
  - [How to have substitles of the PngTuber's speech on my stream?](#how-to-have-substitles-of-the-pngtubers-speech-on-my-stream)
  - [How to change the lore of the PngTuber?](#how-to-change-the-lore-of-the-pngtuber)
  - [Mediagraphy](#mediagraphy)


## Video example [HERE](https://youtu.be/A_WwJ3yPXB4)

## What is Ai PngTuber Ollama?

> This app is made from Python scripts to generate a PngTuber that use **Ollama** system and api has **AI language model**. In another words, that use a locale, free and private **ChatGpt-like** in your network as Ai of this PngTuber.

## Do i need to pay something?

> This app is made to offer a full experience free and customizable. But if you want a better voice than the basic Google one. You need to use the api named **ElevensLabs**. P.S.: There is a free plan with **ElevenLabs**, but you will maybe touch the limit of characters per month of it with the free one.

## How to install Ollama and what model?

> This app use as default the model of **llama2** who is easily downloable by **Ollama**.

> To download and install **Ollama** there is a great video to explain how **Ollama** is used for and how to install it. **[Video Here](https://www.youtube.com/watch?v=WxYC9-hBM_g)** P.S.: You don't need necessary the fine tuning or custom models. Just the first part of the video explain the necessary.

## How to run Ollama as server?

> It's important for this app to be able to communicate with **Ollama**. For that you need to tell to **Ollama** to run as a local server.

Terminal command to run **Ollama** as server:
``` bash
  OLLAMA_ORIGINS=* OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

## How to setup this app?

> First, rename all the files in the [./env](./env) folder by removing the *.example* of them. For the custom settings, it's in them that will be done. And all the explaination of each setting is in these files. But, the default settings will make it work.
>
> Second, install python if it's not already done. The recommended version is Python 3.12.2. Also, be sure to install pip too when you install Python. 
>
> Third, install all the dependencies with pip.
>
> Fourth, run the **app.py** script in a terminal or use the **app.exe** in the release section.
>
> P.S.: There is for now only user's messages by terminal input, but I will try to add a Twitch integration in the future.

## How to change the avatar of the PngTuber?

> The 2 images of the avatar is in the [./res/img](./res/img) folder. I recommend to use 480x480 images. The app doesn't work with gif files. If you need to change the path of the imgs for the software, you have to edit the [./env/avatar.env](./env/avatar.env.example).
>
> ***P.S.: I recommend also to colorize the background of your images to be able to make it transparent in OBS.***
> 
> ***P.S.2: The default avatar if from [PngTuber Maker](https://store.steampowered.com/app/2266940/PngTuber_Maker/), so it's not recommend to use it for stream or recording.***

## How to have substitles of the PngTuber's speech on my stream?

>There is [./res/content/subs.txt](./res/content/subs.txt) that you can use as file source for the text to show in OBS.

## How to change the lore of the PngTuber?

> You change the lore in the [./res/content/lore.txt](./res/content/lore.txt). I suggest to write the lore in english because the models of **Ollama**
are generally build in english first. So there will be better responds from the chatbot.
>
> That is also why there is a translator in the app.

## Mediagraphy

 - [Ollama](https://ollama.com/)
 - [llama2](https://ollama.com/library/llama2)
 - [ElevenLabs](https://elevenlabs.io/)
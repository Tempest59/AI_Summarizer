from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import json
from NotionApi.api import createPage, createPageData
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import TextFormatter
import openai



def getAPIKey():
    key = st.text_input('OpenAI API key')
    return key

openai.api_key = getAPIKey()

def getVideoId():
    url = st.text_input('Youtube URL')
    if len(url) >= 35:
        videoId = url[32:]
    else:
        videoId = url[17:]
    return videoId

def getSubs():
    st.title("AI Video Summarizer")
    return YouTubeTranscriptApi.get_transcript(videoId, languages=['en', 'fr'])

def convert(transcript):
    formatter = TextFormatter()
    text_formatted= formatter.format_transcript(transcript) 

    return text_formatted   


text =[]
n=0

videoId = getVideoId()

def splitter(num, text):
    return [text[i:i+num] for i in range(0, len(text), num)]


def summarizeAi(text, max_tokens):
    prompt = "Summarize this text by rewriting it in an academical and detailed style. Text: '" + text + "' Prompt:"
    response = json.dumps(openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=max_tokens, temperature=0.9))
    return json.loads(response)["choices"][0]["text"]


def summarizer(srt):
    st.header("Summary")
    final = ""
    print(convert(srt))
    if (len(convert(srt)) >= 3085):
        split_text = splitter(2000, convert(srt))
    else:
        split_text = convert(srt)
    with st.spinner('Summarizing the video...⌛'):
        for i in range(0, len(split_text)):
            final += summarizeAi(split_text[i], 1330)
    createPageData("Test", '🕴️', "getVideoId[1]", final)
    st.markdown(final)


if st.button("Add API key"):
    openai.api_key = getAPIKey()
    if st.button("Summarize"):
        srt = getSubs()
        summarizer(srt)

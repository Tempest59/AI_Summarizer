from youtube_transcript_api import YouTubeTranscriptApi
import os
import collections
import pprint
import urllib
import streamlit as st
import json
from openAIInjector import summarizeAi
from NotionApi.api import createPage, createPageData
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import TextFormatter




def getVideoId():
    url = st.text_input('Youtube URL')
    if len(url) >= 35:
        videoId = url[32:]
    else:
        videoId = url[17:]
    return videoId

def getSubs():
    st.title("AI Video Summarizer")
    return YouTubeTranscriptApi.get_transcript(videoId, languages=['fr', 'en'])

def convert(transcript):
    formatter = TextFormatter()
    text_formatted= formatter.format_transcript(transcript) 

    return text_formatted   


text =[]
n=0

videoId = getVideoId()






def splitter(num, text):
    return [text[i:i+num] for i in range(0, len(text), num)]





def summarizer(srt, total_char):
    st.header("Summary")
    final = ""
    print(convert(srt))
    if (len(convert(srt)) >= 3085):
        split_text = splitter(5000, convert(srt))
    else:
        split_text = convert(srt)

    max_character = total_char // (len(split_text) + 1)
    max_tokens = max_character // 4
    with st.spinner('Summarizing the video...⌛'):
        for i in range(0, len(split_text)):
            final += summarizeAi(split_text[i], max_tokens)
    createPageData("Test", '🕴️', "getVideoId[1]", final)
    st.markdown(final)

total_char = st.slider('How long should the summary be ?', 100, 5000, 2000)

if st.button("Summarize"):
    st.markdown(total_char)
    srt = getSubs()
    summarizer(srt, total_char)

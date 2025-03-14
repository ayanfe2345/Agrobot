# -*- coding: utf-8 -*-
"""
Created on Friday January 14 1:27:03 2022
Created to search and translate search results in other languages.

@author: Adamu Ayanfeoluwa Samuel. @ayanfe2345 on github.
Comments and explanations done by Adamu Ayanfeoluwa.
@Teacher: Olufemi Victor Tolulope

Helper script with functions to call google's seach and translate libraries.
"""

from serpapi import GoogleSearch
from googletrans import Translator
import os

api_key = os.environ['my_api_key']# key already stored as a secret on GitHub and mapped in workflow
#print(api_key)
translator = Translator()
def search_and_translate(search_string, dest_language):
  params = {
    "q": search_string,
    "hl": "en",
    "gl": "us",
    "api_key": api_key
  }

  search = GoogleSearch(params)
  results = search.get_dict()

  try:
    answers = (results['knowledge_graph']['description'])
  except Exception:
    try:
      answers = (results["answer_box"]["snippet"] + "\n" + "\n".join(results["answer_box"]["list"]).replace("...","") )
    except Exception:
      try:
        answers = (results["answer_box"]["snippet"])
      except Exception:
        try:
          answers = (results["organic_results"][0]["snippet"])
        except Exception:
          answers = ("No results found")
  if search_string.split()[-1] == "Nothing":
    return(translator.translate("I'm sorry I didn't find anything. Kindly refer to the list of possible detections above, or reduce the threshold in settings.Thanks for your understanding.", dest=dest_language, src= 'en').text)
  else:
    return(translator.translate(answers, dest=dest_language, src= 'en').text)

def translate_alone(answers,dest_language):
  return(translator.translate(answers, dest=dest_language, src= 'en').text)

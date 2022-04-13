import telebot
import requests
from telebot import types
from telebot.types import Message
import flask
from flask import Flask, request 


Admin = 1818416834
took = '5234559529:AAEHj9OoEX5gJr3DjqyICohTB1VpjAAqbQI'
bot = telebot.TeleBot(took)
APP_URL = "https://telemero.herokuapp.com/" + took

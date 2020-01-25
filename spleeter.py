import spleeter
import requests
from spleeter.separator import Separator
from os import path
from setuptools import setup
import sys
import importlib.resources


# from pydub import AudioSegment
#Using embedded configuration.
separator = Separator('spleeter:2stems')

separator.separate_to_file(r"C:\Users\Gaumati Khan\PycharmProjects\untitled\songs\test.wav", r"C:\Users\Gaumati Khan\PycharmProjects\untitled\songs")
#files
# src = r"C:\Users\Gaumati Khan\PycharmProjects\untitled\songs\gerua.mp3"
# dst = r"C:\Users\Gaumati Khan\PycharmProjects\untitled\songs\test.wav"
#
# # convert wav to mp3
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

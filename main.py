import multiprocessing
import streamlit as st
from LSysGen import lsysgen
from draw import *

st.title("L System")
title = st.text_input("Canvas Title", value="My Canvas")
width = st.number_input("Canvas Width", value=500)
heading = st.number_input("Heading", value=0)
height = st.number_input("Canvas Height", value=500)
line_length = st.number_input("Square Length", value=15)
clicked = st.button("Paint")
screen_height=height
screen_width=width
speed=0
x=0
y=-100
size=0.2
iterations=2
angle = 60
axiom = "YF"
rules = {
'X -> YF+XF+Y',
'Y -> XF-YF-X'
}
t = multiprocessing.Process(target=create_turtle, args=(screen_height,screen_width,speed,heading,x,y,size,iterations,line_length,angle,axiom,rules))

if clicked:
   t.start()
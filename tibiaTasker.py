#!/usr/bin/env python

"""Find the currently active window."""

import sys
import time
import wnck
import pyautogui
import math

totalMana = 9600 #regen de sorcerer/druid
hasPromotion = True
hasSoftBoots = True
hasRingOfHealing = True
hasFullBonus = True

if hasPromotion:
    totalMana = 14400
if hasSoftBoots:
    totalMana += 28800
if hasRingOfHealing:
    totalMana += 57600
if hasFullBonus:
    totalMana *=2

def focus_tibia_window():
    screen = wnck.screen_get_default()
    screen.force_update()
    window = screen.get_active_window()


    window.activate(int(time.time()))
    for w in screen.get_windows():
        if not w.get_name().startswith('Tibia'):
            w.minimize()
        else:
            w.maximize()
            w.activate(int(time.time()))


focus_tibia_window()
seconds = 1

food = 'f12'
foodLasting=264 #seconds brown mushroom
runeSpell = 'f11'
runeMana = 985.0 # SD cost
#runeLasting = int(math.ceil(runeMana/(totalMana/14400)))
runeLasting = math.floor(runeMana/(totalMana/14400))
spellTime = math.floor(runeMana/(totalMana/14400))
roh = 'f10'
rohLasting = 450 #seconds
softBoots = 'f8'
softBootsLasting = 14400 #seconds

time.sleep(2)
pyautogui.press(food)
time.sleep(2)
pyautogui.press(softBoots)
time.sleep(2)
pyautogui.press(roh)

while True:
    if seconds>spellTime:
        pyautogui.press(runeSpell)        
        spellTime +=runeLasting
    if seconds%rohLasting == 0:
        pyautogui.press(roh)
    if seconds%foodLasting == 0:
        pyautogui.press(food)
    if seconds%softBootsLasting == 0:
        pyautogui.press(softBoots)
    time.sleep(1)
    seconds += 1

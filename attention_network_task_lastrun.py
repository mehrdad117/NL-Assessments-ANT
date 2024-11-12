﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 12, 2024, at 20:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'attention_network_task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\NoteBook\\Desktop\\mehrdad projects\\ANT-NL\\2\\attention_network_task-master\\attention_network_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0.0039, 0.0039, 0.0039], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0039, 0.0039, 0.0039]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('startresp') is None:
        # initialise startresp
        startresp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startresp',
        )
    if deviceManager.getDevice('startresp2') is None:
        # initialise startresp2
        startresp2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startresp2',
        )
    if deviceManager.getDevice('resp') is None:
        # initialise resp
        resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp',
        )
    if deviceManager.getDevice('resp_2') is None:
        # initialise resp_2
        resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instr" ---
    startresp = keyboard.Keyboard(deviceName='startresp')
    inst1textbox = visual.TextBox2(
         win, text='به این آزمایش خوش آمدید.\n\nدر این آزمایش، یک فلش مرکزی به شما نمایش داده می\u200cشود که با فلش\u200cها یا بلوک\u200cهایی در اطرافش احاطه شده است. فلش مرکزی به سمت چپ یا راست اشاره می\u200cکند.\n\nگاهی فلش\u200cهای جانبی هم\u200cجهت با فلش مرکزی هستند و گاهی در جهت مخالف آن.\n\nبه عنوان مثال: >>>>> یا >><>>\n\nوظیفه\u200cی شما این است که به جهت فلش مرکزی پاسخ دهید.\n\nاگر فلش مرکزی به سمت راست اشاره می\u200cکند، کلید فلش راست را فشار دهید، و اگر به سمت چپ اشاره می\u200cکند، کلید فلش چپ را فشار دهید.\n\nبرای ادامه، کلید فاصله (space) را فشار دهید.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1.1, 0.9), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='inst1textbox',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "instr2" ---
    startresp2 = keyboard.Keyboard(deviceName='startresp2')
    inst1textbox_2 = visual.TextBox2(
         win, text='در این وظیفه، شما باید با استفاده از کلیدهای جهت، به جهت فلش مرکزی پاسخ دهید.\n\nابتدا یک علامت به علاوه در مرکز صفحه نمایش داده می\u200cشود. این علامت گاهی با ظاهر شدن مربع\u200cهایی در صفحه همراه است که ممکن است محل هدف را نشان دهند یا ندهند. اگر مربع\u200cها بعد از علامت ظاهر شوند، به این معناست که هدف به زودی نمایش داده خواهد شد.\n\nاگر مربع\u200cها در بالا یا پایین علامت به علاوه ظاهر شوند، هدف به زودی در همان موقعیت نشان داده\u200cشده نمایان خواهد شد.\n\nانگشتان اشاره خود را روی کلیدهای جهت چپ و راست آماده کنید و برای شروع، کلید فاصله (space) را فشار دهید.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1.1, 0.9), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='inst1textbox_2',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from fix_dur_code
    # Create durations
    durations = [0.4,  0.45, 0.5,  0.55]
    image = visual.TextStim(win=win, name='image',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    trial_counter_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.45), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.1), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='trial_counter_2',
         depth=-2, autoLog=True,
    )
    reminder = visual.TextBox2(
         win, text='به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(1, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='reminder',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "trial" ---
    text_fp1 = visual.TextStim(win=win, name='text_fp1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cues = visual.ImageStim(
        win=win,
        name='cues', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    text_fp2 = visual.TextStim(win=win, name='text_fp2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    target = visual.ImageStim(
        win=win,
        name='target', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    resp = keyboard.Keyboard(deviceName='resp')
    fixationshort = visual.TextStim(win=win, name='fixationshort',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    trial_counter = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.45), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.1), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='trial_counter',
         depth=-6, autoLog=True,
    )
    reminder_2 = visual.TextBox2(
         win, text='به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(1, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='reminder_2',
         depth=-7, autoLog=True,
    )
    
    # --- Initialize components for Routine "feedback" ---
    # Run 'Begin Experiment' code from fb_code
    # create empty string to present feedback
    msg = ''
    correct_count = 0
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='Arabic',
        depth=-1.0);
    trial_counter_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.45), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.1), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='trial_counter_3',
         depth=-2, autoLog=True,
    )
    reminder_3 = visual.TextBox2(
         win, text='به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(1, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='reminder_3',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "fix2" ---
    # Run 'Begin Experiment' code from fix_dur_code_2
    # Create durations
    durations = [0.4,  0.45, 0.5,  0.55]
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='height', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "trialsb" ---
    fixationshort_3 = visual.ImageStim(
        win=win,
        name='fixationshort_3', units='height', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    cues_2 = visual.ImageStim(
        win=win,
        name='cues_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    target_2 = visual.ImageStim(
        win=win,
        name='target_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    resp_2 = keyboard.Keyboard(deviceName='resp_2')
    fixationshort_2 = visual.ImageStim(
        win=win,
        name='fixationshort_2', units='height', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    
    # --- Initialize components for Routine "End" ---
    background_6 = visual.ImageStim(
        win=win,
        name='background_6', 
        image='background.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 1.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    inst1textbox_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1.1, 0.9), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=False,
         name='inst1textbox_3',
         depth=-1, autoLog=True,
    )
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instr" ---
    # create an object to store info about Routine instr
    instr = data.Routine(
        name='instr',
        components=[startresp, inst1textbox],
    )
    instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for startresp
    startresp.keys = []
    startresp.rt = []
    _startresp_allKeys = []
    inst1textbox.reset()
    # store start times for instr
    instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr.tStart = globalClock.getTime(format='float')
    instr.status = STARTED
    thisExp.addData('instr.started', instr.tStart)
    instr.maxDuration = None
    # keep track of which components have finished
    instrComponents = instr.components
    for thisComponent in instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr" ---
    instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *startresp* updates
        waitOnFlip = False
        
        # if startresp is starting this frame...
        if startresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startresp.frameNStart = frameN  # exact frame index
            startresp.tStart = t  # local t and not account for scr refresh
            startresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startresp.started')
            # update status
            startresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startresp.status == STARTED and not waitOnFlip:
            theseKeys = startresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _startresp_allKeys.extend(theseKeys)
            if len(_startresp_allKeys):
                startresp.keys = _startresp_allKeys[-1].name  # just the last key pressed
                startresp.rt = _startresp_allKeys[-1].rt
                startresp.duration = _startresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *inst1textbox* updates
        
        # if inst1textbox is starting this frame...
        if inst1textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1textbox.frameNStart = frameN  # exact frame index
            inst1textbox.tStart = t  # local t and not account for scr refresh
            inst1textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inst1textbox.started')
            # update status
            inst1textbox.status = STARTED
            inst1textbox.setAutoDraw(True)
        
        # if inst1textbox is active this frame...
        if inst1textbox.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr" ---
    for thisComponent in instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr
    instr.tStop = globalClock.getTime(format='float')
    instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr.stopped', instr.tStop)
    thisExp.nextEntry()
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr2" ---
    # create an object to store info about Routine instr2
    instr2 = data.Routine(
        name='instr2',
        components=[startresp2, inst1textbox_2],
    )
    instr2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for startresp2
    startresp2.keys = []
    startresp2.rt = []
    _startresp2_allKeys = []
    inst1textbox_2.reset()
    # store start times for instr2
    instr2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr2.tStart = globalClock.getTime(format='float')
    instr2.status = STARTED
    thisExp.addData('instr2.started', instr2.tStart)
    instr2.maxDuration = None
    # keep track of which components have finished
    instr2Components = instr2.components
    for thisComponent in instr2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr2" ---
    instr2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *startresp2* updates
        waitOnFlip = False
        
        # if startresp2 is starting this frame...
        if startresp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startresp2.frameNStart = frameN  # exact frame index
            startresp2.tStart = t  # local t and not account for scr refresh
            startresp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startresp2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startresp2.started')
            # update status
            startresp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startresp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startresp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startresp2.status == STARTED and not waitOnFlip:
            theseKeys = startresp2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _startresp2_allKeys.extend(theseKeys)
            if len(_startresp2_allKeys):
                startresp2.keys = _startresp2_allKeys[-1].name  # just the last key pressed
                startresp2.rt = _startresp2_allKeys[-1].rt
                startresp2.duration = _startresp2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *inst1textbox_2* updates
        
        # if inst1textbox_2 is starting this frame...
        if inst1textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1textbox_2.frameNStart = frameN  # exact frame index
            inst1textbox_2.tStart = t  # local t and not account for scr refresh
            inst1textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1textbox_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inst1textbox_2.started')
            # update status
            inst1textbox_2.status = STARTED
            inst1textbox_2.setAutoDraw(True)
        
        # if inst1textbox_2 is active this frame...
        if inst1textbox_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr2" ---
    for thisComponent in instr2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr2
    instr2.tStop = globalClock.getTime(format='float')
    instr2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr2.stopped', instr2.tStop)
    thisExp.nextEntry()
    # the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('cond.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[image, trial_counter_2, reminder],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fix_dur_code
        # Randomize durations 
        shuffle(durations) 
        
        # Take one of the randomized durations
        fixDuration  = durations[0] 
        image.setText('+')
        trial_counter_2.reset()
        trial_counter_2.setText(str(trials.thisN+1) + '/' + str(trials.nTotal))
        reminder.reset()
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + fixDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.tStopRefresh = tThisFlipGlobal  # on global time
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # *trial_counter_2* updates
            
            # if trial_counter_2 is starting this frame...
            if trial_counter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_counter_2.frameNStart = frameN  # exact frame index
                trial_counter_2.tStart = t  # local t and not account for scr refresh
                trial_counter_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_counter_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_counter_2.started')
                # update status
                trial_counter_2.status = STARTED
                trial_counter_2.setAutoDraw(True)
            
            # if trial_counter_2 is active this frame...
            if trial_counter_2.status == STARTED:
                # update params
                pass
            
            # if trial_counter_2 is stopping this frame...
            if trial_counter_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_counter_2.tStartRefresh + fixDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_counter_2.tStop = t  # not accounting for scr refresh
                    trial_counter_2.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_counter_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_counter_2.stopped')
                    # update status
                    trial_counter_2.status = FINISHED
                    trial_counter_2.setAutoDraw(False)
            
            # *reminder* updates
            
            # if reminder is starting this frame...
            if reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminder.frameNStart = frameN  # exact frame index
                reminder.tStart = t  # local t and not account for scr refresh
                reminder.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminder, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminder.started')
                # update status
                reminder.status = STARTED
                reminder.setAutoDraw(True)
            
            # if reminder is active this frame...
            if reminder.status == STARTED:
                # update params
                pass
            
            # if reminder is stopping this frame...
            if reminder.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reminder.tStartRefresh + fixDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    reminder.tStop = t  # not accounting for scr refresh
                    reminder.tStopRefresh = tThisFlipGlobal  # on global time
                    reminder.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'reminder.stopped')
                    # update status
                    reminder.status = FINISHED
                    reminder.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # Run 'End Routine' code from fix_dur_code
        # save duration used to csv output
        #thisExp.addData("fixDuration", fixDuration)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[text_fp1, cues, text_fp2, target, resp, fixationshort, trial_counter, reminder_2],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        cues.setImage(cue)
        target.setOri(targOrientation)
        target.setImage(tar)
        # create starting attributes for resp
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        trial_counter.reset()
        trial_counter.setText(str(trials.thisN+1) + '/' + str(trials.nTotal))
        reminder_2.reset()
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fp1* updates
            
            # if text_fp1 is starting this frame...
            if text_fp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fp1.frameNStart = frameN  # exact frame index
                text_fp1.tStart = t  # local t and not account for scr refresh
                text_fp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fp1.started')
                # update status
                text_fp1.status = STARTED
                text_fp1.setAutoDraw(True)
            
            # if text_fp1 is active this frame...
            if text_fp1.status == STARTED:
                # update params
                pass
            
            # if text_fp1 is stopping this frame...
            if text_fp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fp1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fp1.tStop = t  # not accounting for scr refresh
                    text_fp1.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fp1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fp1.stopped')
                    # update status
                    text_fp1.status = FINISHED
                    text_fp1.setAutoDraw(False)
            
            # *cues* updates
            
            # if cues is starting this frame...
            if cues.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cues.frameNStart = frameN  # exact frame index
                cues.tStart = t  # local t and not account for scr refresh
                cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cues, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cues.started')
                # update status
                cues.status = STARTED
                cues.setAutoDraw(True)
            
            # if cues is active this frame...
            if cues.status == STARTED:
                # update params
                pass
            
            # if cues is stopping this frame...
            if cues.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cues.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    cues.tStop = t  # not accounting for scr refresh
                    cues.tStopRefresh = tThisFlipGlobal  # on global time
                    cues.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cues.stopped')
                    # update status
                    cues.status = FINISHED
                    cues.setAutoDraw(False)
            
            # *text_fp2* updates
            
            # if text_fp2 is starting this frame...
            if text_fp2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                text_fp2.frameNStart = frameN  # exact frame index
                text_fp2.tStart = t  # local t and not account for scr refresh
                text_fp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fp2.started')
                # update status
                text_fp2.status = STARTED
                text_fp2.setAutoDraw(True)
            
            # if text_fp2 is active this frame...
            if text_fp2.status == STARTED:
                # update params
                pass
            
            # if text_fp2 is stopping this frame...
            if text_fp2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fp2.tStartRefresh + 2.1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fp2.tStop = t  # not accounting for scr refresh
                    text_fp2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fp2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fp2.stopped')
                    # update status
                    text_fp2.status = FINISHED
                    text_fp2.setAutoDraw(False)
            
            # *target* updates
            
            # if target is starting this frame...
            if target.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                target.frameNStart = frameN  # exact frame index
                target.tStart = t  # local t and not account for scr refresh
                target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target.started')
                # update status
                target.status = STARTED
                target.setAutoDraw(True)
            
            # if target is active this frame...
            if target.status == STARTED:
                # update params
                pass
            
            # if target is stopping this frame...
            if target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    target.tStop = t  # not accounting for scr refresh
                    target.tStopRefresh = tThisFlipGlobal  # on global time
                    target.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target.stopped')
                    # update status
                    target.status = FINISHED
                    target.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            
            # if resp is starting this frame...
            if resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.started')
                # update status
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if resp is stopping this frame...
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.tStopRefresh = tThisFlipGlobal  # on global time
                    resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.stopped')
                    # update status
                    resp.status = FINISHED
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[0].name  # just the first key pressed
                    resp.rt = _resp_allKeys[0].rt
                    resp.duration = _resp_allKeys[0].duration
                    # was this correct?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *fixationshort* updates
            
            # if fixationshort is starting this frame...
            if fixationshort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationshort.frameNStart = frameN  # exact frame index
                fixationshort.tStart = t  # local t and not account for scr refresh
                fixationshort.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationshort, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationshort.started')
                # update status
                fixationshort.status = STARTED
                fixationshort.setAutoDraw(True)
            
            # if fixationshort is active this frame...
            if fixationshort.status == STARTED:
                # update params
                pass
            
            # if fixationshort is stopping this frame...
            if fixationshort.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationshort.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationshort.tStop = t  # not accounting for scr refresh
                    fixationshort.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationshort.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationshort.stopped')
                    # update status
                    fixationshort.status = FINISHED
                    fixationshort.setAutoDraw(False)
            
            # *trial_counter* updates
            
            # if trial_counter is starting this frame...
            if trial_counter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_counter.frameNStart = frameN  # exact frame index
                trial_counter.tStart = t  # local t and not account for scr refresh
                trial_counter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_counter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_counter.started')
                # update status
                trial_counter.status = STARTED
                trial_counter.setAutoDraw(True)
            
            # if trial_counter is active this frame...
            if trial_counter.status == STARTED:
                # update params
                pass
            
            # if trial_counter is stopping this frame...
            if trial_counter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_counter.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_counter.tStop = t  # not accounting for scr refresh
                    trial_counter.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_counter.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_counter.stopped')
                    # update status
                    trial_counter.status = FINISHED
                    trial_counter.setAutoDraw(False)
            
            # *reminder_2* updates
            
            # if reminder_2 is starting this frame...
            if reminder_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminder_2.frameNStart = frameN  # exact frame index
                reminder_2.tStart = t  # local t and not account for scr refresh
                reminder_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminder_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminder_2.started')
                # update status
                reminder_2.status = STARTED
                reminder_2.setAutoDraw(True)
            
            # if reminder_2 is active this frame...
            if reminder_2.status == STARTED:
                # update params
                pass
            
            # if reminder_2 is stopping this frame...
            if reminder_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reminder_2.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    reminder_2.tStop = t  # not accounting for scr refresh
                    reminder_2.tStopRefresh = tThisFlipGlobal  # on global time
                    reminder_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'reminder_2.stopped')
                    # update status
                    reminder_2.status = FINISHED
                    reminder_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
            trials.addData('resp.duration', resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trial.maxDurationReached:
            routineTimer.addTime(-trial.maxDuration)
        elif trial.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.200000)
        
        # --- Prepare to start Routine "feedback" ---
        # create an object to store info about Routine feedback
        feedback = data.Routine(
            name='feedback',
            components=[text, trial_counter_3, reminder_3],
        )
        feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fb_code
        # custom feedback message
        msg = "Incorrect!"
        fbcol = 'black'
        if resp.corr:
            msg = "صحیح سرعت پاسخ شما: " + str(int(resp.rt*1000)) + 'ms'
            correct_count  += 1
            fbcol = 'green'
        elif not resp.keys:
            msg = "پاسخ فراموش نشود"
        
            
        text.setColor(fbcol, colorSpace='rgb')
        text.setText(msg )
        trial_counter_3.reset()
        trial_counter_3.setText(str(trials.thisN+1) + '/' + str(trials.nTotal))
        reminder_3.reset()
        # store start times for feedback
        feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback.tStart = globalClock.getTime(format='float')
        feedback.status = STARTED
        thisExp.addData('feedback.started', feedback.tStart)
        feedback.maxDuration = None
        # keep track of which components have finished
        feedbackComponents = feedback.components
        for thisComponent in feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # *trial_counter_3* updates
            
            # if trial_counter_3 is starting this frame...
            if trial_counter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_counter_3.frameNStart = frameN  # exact frame index
                trial_counter_3.tStart = t  # local t and not account for scr refresh
                trial_counter_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_counter_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_counter_3.started')
                # update status
                trial_counter_3.status = STARTED
                trial_counter_3.setAutoDraw(True)
            
            # if trial_counter_3 is active this frame...
            if trial_counter_3.status == STARTED:
                # update params
                pass
            
            # if trial_counter_3 is stopping this frame...
            if trial_counter_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_counter_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_counter_3.tStop = t  # not accounting for scr refresh
                    trial_counter_3.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_counter_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_counter_3.stopped')
                    # update status
                    trial_counter_3.status = FINISHED
                    trial_counter_3.setAutoDraw(False)
            
            # *reminder_3* updates
            
            # if reminder_3 is starting this frame...
            if reminder_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminder_3.frameNStart = frameN  # exact frame index
                reminder_3.tStart = t  # local t and not account for scr refresh
                reminder_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminder_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminder_3.started')
                # update status
                reminder_3.status = STARTED
                reminder_3.setAutoDraw(True)
            
            # if reminder_3 is active this frame...
            if reminder_3.status == STARTED:
                # update params
                pass
            
            # if reminder_3 is stopping this frame...
            if reminder_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reminder_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    reminder_3.tStop = t  # not accounting for scr refresh
                    reminder_3.tStopRefresh = tThisFlipGlobal  # on global time
                    reminder_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'reminder_3.stopped')
                    # update status
                    reminder_3.status = FINISHED
                    reminder_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback
        feedback.tStop = globalClock.getTime(format='float')
        feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback.stopped', feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback.maxDurationReached:
            routineTimer.addTime(-feedback.maxDuration)
        elif feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler2(
        name='blocks',
        nReps=3.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in blocks:
        currentLoop = blocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('cond-blocks.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "fix2" ---
            # create an object to store info about Routine fix2
            fix2 = data.Routine(
                name='fix2',
                components=[image_2],
            )
            fix2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fix_dur_code_2
            # Randomize durations 
            shuffle(durations) 
            
            # Take one of the randomized durations
            fixDuration  = durations[0] 
            # store start times for fix2
            fix2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fix2.tStart = globalClock.getTime(format='float')
            fix2.status = STARTED
            thisExp.addData('fix2.started', fix2.tStart)
            fix2.maxDuration = None
            # keep track of which components have finished
            fix2Components = fix2.components
            for thisComponent in fix2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fix2" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            fix2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_2* updates
                
                # if image_2 is starting this frame...
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    # update status
                    image_2.status = STARTED
                    image_2.setAutoDraw(True)
                
                # if image_2 is active this frame...
                if image_2.status == STARTED:
                    # update params
                    pass
                
                # if image_2 is stopping this frame...
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + fixDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        # update status
                        image_2.status = FINISHED
                        image_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    fix2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fix2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fix2" ---
            for thisComponent in fix2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fix2
            fix2.tStop = globalClock.getTime(format='float')
            fix2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fix2.stopped', fix2.tStop)
            # Run 'End Routine' code from fix_dur_code_2
            # save duration used to csv output
            thisExp.addData("fixDuration", fixDuration)
            # the Routine "fix2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "trialsb" ---
            # create an object to store info about Routine trialsb
            trialsb = data.Routine(
                name='trialsb',
                components=[fixationshort_3, cues_2, target_2, resp_2, fixationshort_2],
            )
            trialsb.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            cues_2.setImage(cue)
            target_2.setOri(targOrientation)
            target_2.setImage(tar)
            # create starting attributes for resp_2
            resp_2.keys = []
            resp_2.rt = []
            _resp_2_allKeys = []
            # store start times for trialsb
            trialsb.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trialsb.tStart = globalClock.getTime(format='float')
            trialsb.status = STARTED
            thisExp.addData('trialsb.started', trialsb.tStart)
            trialsb.maxDuration = None
            # keep track of which components have finished
            trialsbComponents = trialsb.components
            for thisComponent in trialsb.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trialsb" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            trialsb.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixationshort_3* updates
                
                # if fixationshort_3 is starting this frame...
                if fixationshort_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixationshort_3.frameNStart = frameN  # exact frame index
                    fixationshort_3.tStart = t  # local t and not account for scr refresh
                    fixationshort_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationshort_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationshort_3.started')
                    # update status
                    fixationshort_3.status = STARTED
                    fixationshort_3.setAutoDraw(True)
                
                # if fixationshort_3 is active this frame...
                if fixationshort_3.status == STARTED:
                    # update params
                    pass
                
                # *cues_2* updates
                
                # if cues_2 is starting this frame...
                if cues_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    cues_2.frameNStart = frameN  # exact frame index
                    cues_2.tStart = t  # local t and not account for scr refresh
                    cues_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cues_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cues_2.started')
                    # update status
                    cues_2.status = STARTED
                    cues_2.setAutoDraw(True)
                
                # if cues_2 is active this frame...
                if cues_2.status == STARTED:
                    # update params
                    pass
                
                # if cues_2 is stopping this frame...
                if cues_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cues_2.tStartRefresh + .1-frameTolerance:
                        # keep track of stop time/frame for later
                        cues_2.tStop = t  # not accounting for scr refresh
                        cues_2.tStopRefresh = tThisFlipGlobal  # on global time
                        cues_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cues_2.stopped')
                        # update status
                        cues_2.status = FINISHED
                        cues_2.setAutoDraw(False)
                
                # *target_2* updates
                
                # if target_2 is starting this frame...
                if target_2.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    target_2.frameNStart = frameN  # exact frame index
                    target_2.tStart = t  # local t and not account for scr refresh
                    target_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_2.started')
                    # update status
                    target_2.status = STARTED
                    target_2.setAutoDraw(True)
                
                # if target_2 is active this frame...
                if target_2.status == STARTED:
                    # update params
                    pass
                
                # if target_2 is stopping this frame...
                if target_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_2.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        target_2.tStop = t  # not accounting for scr refresh
                        target_2.tStopRefresh = tThisFlipGlobal  # on global time
                        target_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_2.stopped')
                        # update status
                        target_2.status = FINISHED
                        target_2.setAutoDraw(False)
                
                # *resp_2* updates
                waitOnFlip = False
                
                # if resp_2 is starting this frame...
                if resp_2.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    resp_2.frameNStart = frameN  # exact frame index
                    resp_2.tStart = t  # local t and not account for scr refresh
                    resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp_2.started')
                    # update status
                    resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if resp_2 is stopping this frame...
                if resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > resp_2.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        resp_2.tStop = t  # not accounting for scr refresh
                        resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp_2.stopped')
                        # update status
                        resp_2.status = FINISHED
                        resp_2.status = FINISHED
                if resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = resp_2.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                    _resp_2_allKeys.extend(theseKeys)
                    if len(_resp_2_allKeys):
                        resp_2.keys = _resp_2_allKeys[0].name  # just the first key pressed
                        resp_2.rt = _resp_2_allKeys[0].rt
                        resp_2.duration = _resp_2_allKeys[0].duration
                        # was this correct?
                        if (resp_2.keys == str(corrAns)) or (resp_2.keys == corrAns):
                            resp_2.corr = 1
                        else:
                            resp_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *fixationshort_2* updates
                
                # if fixationshort_2 is starting this frame...
                if fixationshort_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixationshort_2.frameNStart = frameN  # exact frame index
                    fixationshort_2.tStart = t  # local t and not account for scr refresh
                    fixationshort_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationshort_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationshort_2.started')
                    # update status
                    fixationshort_2.status = STARTED
                    fixationshort_2.setAutoDraw(True)
                
                # if fixationshort_2 is active this frame...
                if fixationshort_2.status == STARTED:
                    # update params
                    pass
                
                # if fixationshort_2 is stopping this frame...
                if fixationshort_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixationshort_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixationshort_2.tStop = t  # not accounting for scr refresh
                        fixationshort_2.tStopRefresh = tThisFlipGlobal  # on global time
                        fixationshort_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationshort_2.stopped')
                        # update status
                        fixationshort_2.status = FINISHED
                        fixationshort_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trialsb.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialsb.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trialsb" ---
            for thisComponent in trialsb.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trialsb
            trialsb.tStop = globalClock.getTime(format='float')
            trialsb.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trialsb.stopped', trialsb.tStop)
            # check responses
            if resp_2.keys in ['', [], None]:  # No response was made
                resp_2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   resp_2.corr = 1;  # correct non-response
                else:
                   resp_2.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_2 (TrialHandler)
            trials_2.addData('resp_2.keys',resp_2.keys)
            trials_2.addData('resp_2.corr', resp_2.corr)
            if resp_2.keys != None:  # we had a response
                trials_2.addData('resp_2.rt', resp_2.rt)
                trials_2.addData('resp_2.duration', resp_2.duration)
            # the Routine "trialsb" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'blocks'
    
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[background_6, inst1textbox_3],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    inst1textbox_3.reset()
    inst1textbox_3.setText('لطفا تا ذخیره نتایج صبر کنید...')
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_6* updates
        
        # if background_6 is starting this frame...
        if background_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_6.frameNStart = frameN  # exact frame index
            background_6.tStart = t  # local t and not account for scr refresh
            background_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_6.started')
            # update status
            background_6.status = STARTED
            background_6.setAutoDraw(True)
        
        # if background_6 is active this frame...
        if background_6.status == STARTED:
            # update params
            pass
        
        # *inst1textbox_3* updates
        
        # if inst1textbox_3 is starting this frame...
        if inst1textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1textbox_3.frameNStart = frameN  # exact frame index
            inst1textbox_3.tStart = t  # local t and not account for scr refresh
            inst1textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1textbox_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inst1textbox_3.started')
            # update status
            inst1textbox_3.status = STARTED
            inst1textbox_3.setAutoDraw(True)
        
        # if inst1textbox_3 is active this frame...
        if inst1textbox_3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

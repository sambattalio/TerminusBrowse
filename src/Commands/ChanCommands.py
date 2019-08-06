from debug import DEBUG
from Views.viewClass import View
from customeTypes import SITE

from Frames.defaultFrame import FrameFactory

import Frames.fchan.boardFrame as fchanBoard
import Frames.fchan.threadFrame as fchanThread

import Frames.lchan.boardFrame as lchanBoard
import Frames.lchan.threadFrame as lchanThread

ChanCommandList = [
    'b', 'board',
    't', 'thread'
]

def chanCommands(cmd, uvm):
    cmd = cmd.split()

    if cmd[0] in ('b', 'board'):
        DEBUG('executing board command')
        # uvm.currFocusView.updateHistory(f'setattr(uvm.currFocusView, "frame", BoardFrame("{cmd[1]}", uvm))')
        board(uvm, cmd[1])
    if cmd[0] in ('t', 'thread'):
        DEBUG('executing thread command')
        # uvm.currFocusView.updateHistory(f'setattr(uvm.currFocusView, "frame", ThreadFrame("{cmd[1]}", "{cmd[2]}", uvm))')
        thread(uvm, cmd[1], cmd[2])

    DEBUG(uvm.history)

def board(uvm, boardString):
    DEBUG('Executing board command')
    try:
        if uvm.currFocusView.site == SITE.FCHAN:
            setattr(uvm.currFocusView, 'frame', fchanBoard.BoardFrame(boardString, uvm))
            uvm.currFocusView.updateHistory(FrameFactory(fchanBoard.BoardFrame), [boardString, uvm])
        elif uvm.currFocusView.site is SITE.LCHAN:
            setattr(uvm.currFocusView, 'frame', lchanBoard.BoardFrame(boardString, uvm))
            uvm.currFocusView.updateHistory(FrameFactory(lchanBoard.BoardFrame), [boardString, uvm])
    except:
        uvm.currFocusView.frame.headerString = f'Error connecting to board {boardString}, does it exist?'
        DEBUG(f'Error connecting to board {boardString}, does it exist?')

def thread(uvm, boardString, threadNumber):
    DEBUG('Executing thread command')
    if uvm.currFocusView.site is SITE.FCHAN:
        uvm.currFocusView.updateHistory(FrameFactory(fchanThread.ThreadFrame), [boardString, threadNumber, uvm])
        setattr(uvm.currFocusView, 'frame', fchanThread.ThreadFrame(boardString, threadNumber, uvm))
    elif uvm.currFocusView.site is SITE.LCHAN:
        uvm.currFocusView.updateHistory(FrameFactory(lchanThread.ThreadFrame), [boardString, threadNumber, uvm])
        setattr(uvm.currFocusView, 'frame', lchanThread.ThreadFrame(boardString, threadNumber, uvm))

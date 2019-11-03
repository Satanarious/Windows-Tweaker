from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog
from tkinter import messagebox,Tk
import os,subprocess,time
import winreg as w
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI.ui', self)
        self.themes=['Ubuntu.qss','DarkOrange.qss','ConsoleStyle.qss','ElegantDark.qss']
        f=open('Assets\\Operation files\\preference.txt','r')
        out=eval(f.read())
        self.set_theme(self.themes[out['theme']],out['theme'])
        f.close()
        self.tabWidget.tabBar().setVisible(0)
        self.tabs()
        self.other_buttons()
        self.theme_widget()
        self.placeholders()
        self.label_3.setPixmap(QPixmap('Assets\\no-image.png'))
        self.label_3.setScaledContents(True)
        self.show()
    def boot(self):
        typ=self.comboBox_3.currentText()
        try:
            time=int(self.lineEdit_2.text())
        except:
            return
        if(typ=='Shutdown'):
            cmd='shutdown -s -f -t '+str(time)
        else:
            cmd='shutdown -r -f -t '+str(time)
        Tk().wm_withdraw()
        ans=messagebox.askyesno('Boot Timer','Are you sure you want to set this timer?')
        if(ans==True):
            os.system(cmd)
            Tk().wm_withdraw()
            messagebox.showwarning('Timer Set Successfully','Your '+typ+' timer for '+str(time)+' seconds has been set.')
    def placeholders(self):
        self.lineEdit.setPlaceholderText("Enter Path")
        self.lineEdit_3.setPlaceholderText("Enter Path")
        self.lineEdit_2.setPlaceholderText("In Seconds")
    def other_buttons(self):
        self.pushButton_4.clicked.connect(self.systeminfo)
        self.pushButton_13.clicked.connect(self.open_file)
        self.pushButton_14.clicked.connect(self.open_folder)
        self.pushButton_5.clicked.connect(self.HideorUnhide)
        self.pushButton_15.clicked.connect(self.display_hidden)
        self.pushButton_6.clicked.connect(self.boot)
        self.pushButton_16.clicked.connect(self.open_icon)
        self.pushButton_17.clicked.connect(self.drive_icon)
        self.pushButton_19.clicked.connect(self.prefix)
        self.pushButton_20.clicked.connect(self.suffix)
        self.pushButton_21.clicked.connect(self.hidden)
        self.pushButton_22.clicked.connect(self.drives_hide)
        self.pushButton_23.clicked.connect(self.drives_unhide)
        self.pushButton_25.clicked.connect(self.seconds_show)
        self.pushButton_26.clicked.connect(self.seconds_hide)
        self.pushButton_29.clicked.connect(self.about)
    def display_hidden(self):
        self.textEdit.setText('')
        f=open('Assets//Operation files//preference.txt','r')
        out=eval(f.read())
        if(out['hidden'] == []):
            return
        else:
            for i in range(len(out['hidden'])):
                self.textEdit.append(str(i+1)+') '+out['hidden'][i])
    def HideorUnhide(self):
        text = str(self.comboBox.currentText())
        path=str(self.lineEdit.text())
        if(path==''):
            return
        elif not(os.path.exists(path)):
            Tk().wm_withdraw()
            messagebox.showerror('Not Exist','File/Folder doesn\'t exist')
        if(text=='Hide'):
            cmd='attrib "'+path+'" +s +h +r /s /d'
            os.system(cmd)
            f=open('Assets//Operation files//preference.txt','r')
            out=eval(f.read())
            f.close
            if path in out['hidden']:
                pass
            else:
                f=open('Assets//Operation files//preference.txt','w')
                out['hidden'].append(path)
                f.write(str(out))
                f.close()
                Tk().wm_withdraw()
                messagebox.showinfo('Successfull','File/Folder Hidden')
            self.display_hidden()
        else:
            cmd='attrib "'+path+'" -s -h -r /s /d'
            os.system(cmd)
            f=open('Assets//Operation files//preference.txt','r')
            out=eval(f.read())
            f.close()
            f=open('Assets//Operation files//preference.txt','w')
            out['hidden'].remove(path)
            f.write(str(out))
            f.close()
            Tk().wm_withdraw()
            messagebox.showinfo('Successfull','File/Folder Unhidden')
            self.display_hidden()
    def open_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
    def open_icon(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image files (*.ico *.exe *.dll)", options=options)
        if fileName:
            self.lineEdit_3.setText(fileName)
            self.label_3.setPixmap(QPixmap(fileName))
        else:
            self.label_3.setPixmap(QPixmap('Assets\\no-image.png'))
            
    def open_folder(self):
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if fileName:
            self.lineEdit.setText(fileName)
    def about(self):
        abt="""
    ___    __                __ 
   /   |  / /_  ____  __  __/ /_
  / /| | / __ \/ __ \/ / / / __/
 / ___ |/ /_/ / /_/ / /_/ / /_  
/_/  |_/_.___/\____/\__,_/\__/  
                                
"""
                             

        Tk().wm_withdraw()
        messagebox.showinfo("About",f"\t\t{abt}\n\nWindows Tweaker V1.0\n\nCreated and designed by Satyam Singh Niranjan")
    def systeminfo(self):
        cwd = 'Assets\\Operation files\\'
        os.startfile(cwd+'info.bat')
        time.sleep(3.5)
        f=open(cwd+'info.txt','r')
        out=f.read()
        f.close()
        self.plainTextEdit.setPlainText(out)
    def drive_icon(self):
        text = str(self.comboBox_2.currentText())
        path="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\DriveIcons\\"+text+'\\defaulticon'
        icon_path=str(self.lineEdit_3.text())
        key = w.CreateKey(w.HKEY_LOCAL_MACHINE, path)
        if(icon_path==''):
            return
        elif not(os.path.exists(icon_path)):
            Tk().wm_withdraw()
            messagebox.showerror('Not Exist','Path doesn\'t exist')
        else:
            try:
                w.SetValueEx(key, "", 0, w.REG_SZ, icon_path)
                Tk().wm_withdraw()
                messagebox.showinfo('Successful','Drive Icon changed successfully')
            except PermissionError:
                Tk().wm_withdraw()
                messagebox.showerror('Access Denied','Run the program as Administrator')    
        key.Close()
    def prefix(self):
        path="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer"
        key = w.CreateKey(w.HKEY_LOCAL_MACHINE, path)
        try:
            w.SetValueEx(key, "ShowDriveLettersFirst", 0, w.REG_DWORD,0x00000004)
            Tk().wm_withdraw()
            messagebox.showinfo('Successful','Drive Letters Prefixed successfully')
        except PermissionError:
                Tk().wm_withdraw()
                messagebox.showerror('Access Denied','Run the program as Administrator')
    def suffix(self):
        path="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer"
        key = w.CreateKey(w.HKEY_LOCAL_MACHINE, path)
        try:
            w.SetValueEx(key, "ShowDriveLettersFirst", 0, w.REG_DWORD,0x00000001)
            Tk().wm_withdraw()
            messagebox.showinfo('Successful','Drive Letters Suffixed successfully')
        except PermissionError:
                Tk().wm_withdraw()
                messagebox.showerror('Access Denied','Run the program as Administrator')
    def hidden(self):
        path="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer"
        key = w.CreateKey(w.HKEY_LOCAL_MACHINE, path)
        try:
            w.SetValueEx(key, "ShowDriveLettersFirst", 0, w.REG_DWORD,0x00000002)
            Tk().wm_withdraw()
            messagebox.showinfo('Successful','Drive Letters Hidden successfully')
        except PermissionError:
                Tk().wm_withdraw()
                messagebox.showerror('Access Denied','Run the program as Administrator')
    def drives_hide(self):
        path="Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer"
        key = w.CreateKey(w.HKEY_CURRENT_USER, path)
        w.SetValueEx(key, "NoDrives", 0, w.REG_DWORD,0x03ffffff)
        Tk().wm_withdraw()
        messagebox.showinfo('Successful','Drives Hidden successfully')
    def drives_unhide(self):
        path="Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer"
        key = w.CreateKey(w.HKEY_CURRENT_USER, path)
        w.SetValueEx(key, "NoDrives", 0, w.REG_DWORD,0x00000000)
        Tk().wm_withdraw()
        messagebox.showinfo('Successful','Drives Unhidden successfully')
    def seconds_show(self):
        path="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"
        key = w.CreateKey(w.HKEY_CURRENT_USER, path)
        w.SetValueEx(key, "ShowSecondsInSystemClock", 0, w.REG_DWORD,0x00000001)
        Tk().wm_withdraw()
        messagebox.showinfo('Successful','System Clock altered successfully')
    def seconds_hide(self):
        path="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"
        key = w.CreateKey(w.HKEY_CURRENT_USER, path)
        w.SetValueEx(key, "ShowSecondsInSystemClock", 0, w.REG_DWORD,0x00000000)
        Tk().wm_withdraw()
        messagebox.showinfo('Successful','System Clock altered successfully')
    def tabs(self):
        self.pushButton.clicked.connect(lambda : self.tabWidget.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda : self.tabWidget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda : self.tabWidget.setCurrentIndex(2))
        self.pushButton_18.clicked.connect(lambda : self.tabWidget.setCurrentIndex(3))
        self.pushButton_7.clicked.connect(lambda : self.frame.show())
        self.pushButton_8.clicked.connect(lambda : self.frame.setHidden(1))
        
        self.frame.setHidden(1)
    def theme_widget(self):
        self.pushButton_9.clicked.connect(lambda: self.set_theme(self.themes[0],0))
        self.pushButton_10.clicked.connect(lambda: self.set_theme(self.themes[1],1))
        self.pushButton_11.clicked.connect(lambda: self.set_theme(self.themes[2],2))
        self.pushButton_12.clicked.connect(lambda: self.set_theme(self.themes[3],3))
    def set_theme(self,filename,pos):
        file = QFile("Assets//Stylesheets//"+filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())
        f=open('Assets\\Operation files\\preference.txt','r')
        out=eval(f.read())
        f.close()
        f=open('Assets\\Operation files\\preference.txt','w')
        out['theme']=pos
        f.write(str(out))
        f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())


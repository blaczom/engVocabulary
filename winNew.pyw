#!/usr/bin/env python
import tkinter as tk

import os
l_cwd = os.getcwd() if os.getcwd()[-1] == os.sep else os.getcwd()+os.sep

f = open(l_cwd + "engdict.txt", "rt", encoding="utf8")
s = f.readlines()
g_word = {}
import re
l_re = re.compile(r"(\S+)\s(.+)")
for i in s:
    if len(i) > 0 :
        try:
            l_result = l_re.match(i).groups()
            g_word.update({l_result[0]:l_result[1]})
        except Exception as e:
            print(e.args)
            print(i)
f.close()

      
class Application(tk.Frame):    
    global g_word #
    #
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()        
    #
    def click_search(self):
        self.text2.delete(0.0, tk.END)                
        l_sum = ""
        for i in g_word.items():
            if eval( self.text1.get('0.0', tk.END) ):
                l_sum = l_sum + str(i) + os.linesep
        self.text2.insert(0.0, l_sum)            
    #
    def event_ctrlS(self, event):
        self.text1.insert(0.0, dir(event))
    #
    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        #
        l_row0 = 0
        l_row1 = 1
        l_row2 = 2
        self.rowconfigure(l_row0, weight=0)
        self.rowconfigure(l_row1, weight=0)
        self.rowconfigure(l_row2, weight=1)
        l_col0 = 0
        l_col1 = 1
        l_col2 = 2
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)    
        self.columnconfigure(2, weight=0)    
        
        # l_row0 l_col0
        self.label1 = tk.Label(self,text = '用i代表(englishword, "汉字意思")', anchor=tk.W)
        self.label1.grid(row=l_row0, column=l_col0, padx=5,sticky=tk.E+tk.W)                
        # l_row1 l_col0
        self.text1 = tk.Text(self, height=2, width=20, bg='#009900')
        self.text1.insert(0.0,'(i[0][-1] == "g") and (i[0][-3:] != "ing" )')
        self.text1.grid(row=l_row1, column=l_col0, padx=5, pady=5, sticky=tk.E+tk.W)
        # l_row1 l_col2
        self.search = tk.Button(self, text='search', command=self.click_search)
        self.search.grid(row=l_row1, column=l_col2, sticky=tk.N)           
        # l_row2  l_col0
        self.text2 = tk.Text(self)
        self.text2.insert(0.0,'here the result')        
        self.text2.grid(row=l_row2, column=l_col0, padx=(5,0), sticky=tk.E+tk.W+tk.N+tk.S)
        # l_row2  l_col1
        self.text2_sv = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text2.yview)          
        self.text2_sv.grid(row=l_row2,column=l_col1, stick=tk.E+tk.W+tk.N+tk.S)
        self.text2['yscrollcommand'] = self.text2_sv.set
        # l_row2  l_col2
        self.quit = tk.Button(self, text='Quit', command=self.quit)
        self.quit.grid(row=l_row2, column=l_col2, sticky=tk.S+tk.E+tk.W)    
        
app = Application()
app.master.title('Sample application')
app.mainloop()
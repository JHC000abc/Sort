import os
import tkinter as tk
from tkinter import messagebox,filedialog


def search():
    key=enter1.get()
    type1=enter2.get()
    # print(key,type1)
    if not key:
        messagebox.showinfo(title='ERROR !!!',message='请输入关键字')
    if not type1:
        messagebox.showinfo(title='ERROR !!!',message='请输入关键字')
        return
    # 获取文件管理器窗口
    fn=filedialog.askdirectory()
    print(fn)
    # 遍历文件目录
    fn_list=os.walk(fn)
    for root_path,dirs,files in fn_list:
        # print(root_path,dirs,files)
        for file in files:
            if file.endswith(type1):
                # print(root_path+'\\'+file)
                result=root_path+'\\'+file
                listbox.insert(tk.END,result)
    print('本次搜索完成')



root=tk.Tk()

root.title('搜索工具')
root.geometry('600x300')

search_frame = tk.Frame()
search_frame.pack()

tk.Label(search_frame,text='关键字 :').pack(side=tk.LEFT,ipady=10,padx=5)
enter1=tk.Entry(search_frame)
enter1.pack(side=tk.LEFT,padx=5)

tk.Label(search_frame,text='文件类型 :').pack(side=tk.LEFT,ipadx=10,padx=5)
enter2=tk.Entry(search_frame)
enter2.pack(side=tk.LEFT,padx=5)

button=tk.Button(search_frame,text='搜 索')
button.pack(side=tk.LEFT,padx=30,ipadx=5)
button.config(command=search)





listbox=tk.Listbox(root,width=80)
listbox.pack(fill=tk.BOTH,expand=True)



root.mainloop()
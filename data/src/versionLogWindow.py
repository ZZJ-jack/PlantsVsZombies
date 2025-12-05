from tkinter import *
from tkinter import scrolledtext, ttk
import re
from data.src.const import GAME_VERSION, ICON_PATH
import webbrowser
import os

class VersionLogWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pvz版本更新日志")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        
        # 设置窗口图标
        if os.path.exists(ICON_PATH):
            self.root.iconbitmap(ICON_PATH)
        
        # 设置主题色
        self.theme_color = "#4CAF50"
        self.accent_color = "#FF5722"
        self.text_bg = "#F5F5F5"
        self.text_fg = "#333333"
        
        # 读取README.md文件
        self.readme_content = self.read_readme()
        # 解析版本更新日志
        self.version_logs = self.parse_version_logs()
        # 获取最新版本
        self.latest_version = self.get_latest_version()
        
        self.create_widgets()
        self.display_version_logs()
        
    def read_readme(self):
        """读取README.md文件内容"""
        try:
            with open("./README.md", "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"无法读取README.md文件: {e}"
    
    def parse_version_logs(self):
        """解析版本更新日志"""
        logs = {}
        # 使用正则表达式匹配版本更新记录
        pattern = r'\s*([0-9]+\.[0-9]+(?:\.[0-9]+)?)\s+([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})\s+(.+)'
        matches = re.findall(pattern, self.readme_content)
        
        for match in matches:
            version = match[0]
            date = match[1]
            description = match[2]
            logs[version] = {"date": date, "description": description}
        
        return logs
    
    def get_latest_version(self):
        """获取最新版本号"""
        if not self.version_logs:
            return GAME_VERSION
        
        # 将版本号转换为元组以便比较
        versions = list(self.version_logs.keys())
        versions.sort(key=lambda v: tuple(map(int, v.split('.'))), reverse=True)
        return versions[0]
    
    def is_latest_version(self):
        """检查当前版本是否为最新版本"""
        current = tuple(map(int, GAME_VERSION.split('.')))
        latest = tuple(map(int, self.latest_version.split('.')))
        return current >= latest
    
    def create_widgets(self):
        """创建窗口组件"""
        # 创建主框架
        main_frame = Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=BOTH, expand=True)
        
        # 标题标签
        title_label = Label(main_frame, text="Pvz版本更新日志", font=(
            "Microsoft YaHei", 22, "bold"), fg=self.theme_color)
        title_label.pack(pady=(0, 20))
        
        # 版本信息框架
        version_frame = Frame(main_frame, bg="#E8F5E9", bd=2, relief=GROOVE)
        version_frame.pack(fill=X, pady=(0, 20), padx=10)
        
        # 当前版本标签
        current_version_text = f"当前版本: {GAME_VERSION}"
        latest_version_text = f"最新版本: {self.latest_version}"
        
        current_version = Label(version_frame, text=current_version_text, font=(
            "Microsoft YaHei", 12, "bold"), 
                               bg="#E8F5E9", fg="#2E7D32", padx=15, pady=10)
        current_version.pack(side=LEFT)
        
        # 版本状态标签
        if self.is_latest_version():
            status_text = "(已是最新版本)"
            status_color = "#4CAF50"
        else:
            status_text = "(不是最新版本)"
            status_color = "#FF5722"
        
        status_label = Label(version_frame, text=status_text, font=(
            "Microsoft YaHei", 12, "bold"), 
                               bg="#E8F5E9", fg=status_color, padx=15, pady=10)
        status_label.pack(side=LEFT)
        
        # 最新版本标签
        latest_version = Label(version_frame, text=latest_version_text, font=(
            "Microsoft YaHei", 12, "bold"), 
                              bg="#E8F5E9", fg="#2E7D32", padx=15, pady=10)
        latest_version.pack(side=LEFT)
        
        # 滚动文本框
        text_frame = Frame(main_frame, bd=2, relief=SOLID, bg="#FFFFFF")
        text_frame.pack(fill=BOTH, expand=True, pady=(0, 20), padx=10)
        
        self.text_area = scrolledtext.ScrolledText(text_frame, wrap=WORD, font=(
            "Microsoft YaHei", 10), 
                                                  bg=self.text_bg, fg=self.text_fg, bd=0, relief=FLAT,
                                                  highlightthickness=0, padx=10, pady=10)
        self.text_area.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.text_area.config(state=DISABLED, insertbackground=self.text_fg)
        
        # 设置滚动条样式
        scrollbar = ttk.Scrollbar(self.text_area)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)
        
        # 更新提示和按钮框架
        bottom_frame = Frame(main_frame)
        bottom_frame.pack(fill=X, pady=(0, 10), padx=10)
        
        # 更新提示标签
        if not self.is_latest_version():
            update_label = Label(bottom_frame, text="🔔 发现新版本！建议前往官网下载最新版本", 
                                font=(
                                    "Microsoft YaHei", 11, "bold"), fg=self.accent_color)
            update_label.pack(pady=(0, 15))
            
            # 按钮容器
            button_container = Frame(bottom_frame)
            button_container.pack(side=RIGHT)
            
            # 下载按钮
            download_button = ttk.Button(button_container, text="前往下载", command=self.open_download_url, 
                                       style="Accent.TButton")
            download_button.pack(side=LEFT, padx=(0, 15))
            
            # 关闭按钮
            close_button = ttk.Button(button_container, text="关闭", command=self.root.destroy, 
                                    style="Normal.TButton")
            close_button.pack(side=LEFT)
        else:
            # 仅显示关闭按钮，居中对齐
            button_container = Frame(bottom_frame)
            button_container.pack(side=RIGHT)
            close_button = ttk.Button(button_container, text="关闭", command=self.root.destroy, 
                                    style="Normal.TButton")
            close_button.pack()
        
        # 创建自定义样式
        self.create_styles()
    
    def create_styles(self):
        """创建自定义样式"""
        style = ttk.Style()
        
        # 配置按钮样式
        style.configure("Normal.TButton", font=("Microsoft YaHei", 11), padding=8)
        style.configure("Accent.TButton", font=("Microsoft YaHei", 11, "bold"), padding=8, 
                       foreground=self.accent_color)
        
        # 配置滚动条样式
        style.configure("Vertical.TScrollbar", gripcount=0, troughrelief=FLAT, 
                       background=self.text_bg, darkcolor=self.theme_color, 
                       lightcolor=self.theme_color, troughcolor=self.text_bg, 
                       bordercolor=self.text_bg, arrowcolor=self.theme_color)
        
        style.configure("Horizontal.TScrollbar", gripcount=0, troughrelief=FLAT, 
                       background=self.text_bg, darkcolor=self.theme_color, 
                       lightcolor=self.theme_color, troughcolor=self.text_bg, 
                       bordercolor=self.text_bg, arrowcolor=self.theme_color)
    
    def display_version_logs(self):
        """显示版本更新日志"""
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        
        # 配置文本标签样式
        self.text_area.tag_config("section_heading", font=("Microsoft YaHei", 12, "bold"), foreground=self.theme_color)
        self.text_area.tag_config("version_header", font=(
            "Microsoft YaHei", 11, "bold"), foreground="#1976D2")
        self.text_area.tag_config("version_number", font=(
            "Microsoft YaHei", 10, "bold"), foreground="#FF5722")
        self.text_area.tag_config("version_date", font=(
            "Microsoft YaHei", 10, "italic"), foreground="#666666")
        self.text_area.tag_config("version_content", font=(
            "Microsoft YaHei", 10), foreground=self.text_fg)
        self.text_area.tag_config("highlight", font=(
            "Microsoft YaHei", 10, "bold"), foreground=self.accent_color)
        
        # 显示当前版本更新日志
        if GAME_VERSION in self.version_logs:
            log = self.version_logs[GAME_VERSION]
            self.text_area.insert(END, "当前版本更新日志\n", "section_heading")
            self.text_area.insert(END, "- " * 40 + "\n")
            self.text_area.insert(END, "版本: ", "version_header")
            self.text_area.insert(END, f"{GAME_VERSION}  ", "version_number")
            self.text_area.insert(END, f"({log['date']})\n", "version_date")
            self.text_area.insert(END, "更新内容:\n", "version_header")
            self.text_area.insert(END, f"  • {log['description']}\n\n", "version_content")
        
        # 显示最新版本更新日志
        if self.latest_version != GAME_VERSION and self.latest_version in self.version_logs:
            log = self.version_logs[self.latest_version]
            self.text_area.insert(END, "最新版本更新日志\n", "section_heading")
            self.text_area.insert(END, "- " * 40 + "\n")
            self.text_area.insert(END, "版本: ", "version_header")
            self.text_area.insert(END, f"{self.latest_version}  ", "highlight")
            self.text_area.insert(END, f"({log['date']})\n", "version_date")
            self.text_area.insert(END, "更新内容:\n", "version_header")
            self.text_area.insert(END, f"  • {log['description']}\n\n", "version_content")
        
        # 显示所有版本更新日志
        self.text_area.insert(END, "所有版本更新日志\n", "section_heading")
        self.text_area.insert(END, "- " * 40 + "\n")
        for version in sorted(self.version_logs.keys(), key=lambda v: tuple(map(int, v.split('.'))), reverse=True):
            log = self.version_logs[version]
            self.text_area.insert(END, "  • ", "version_header")
            self.text_area.insert(END, f"{version}  ", "version_number")
            self.text_area.insert(END, f"({log['date']}) ", "version_date")
            self.text_area.insert(END, f"- {log['description']}\n", "version_content")
        
        self.text_area.config(state=DISABLED)
    
    def open_download_url(self):
        """打开下载链接"""
        webbrowser.open("http://pvz.zzjjack.us.kg")
    
    def show(self):
        """显示窗口"""
        self.root.mainloop()
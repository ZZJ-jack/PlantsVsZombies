from tkinter import *
from tkinter import scrolledtext, ttk, filedialog
import re
from data.src.const import GAME_VERSION, ICON_PATH
import webbrowser
import os
import requests
from PIL import Image, ImageTk
import threading
import time

class VersionLogWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pvz版本更新日志")
        self.root.geometry("1000x720")  # 高度适中减小
        self.root.resizable(False, False)
        
        # 设置关闭按钮行为 - 退出整个进程
        self.root.protocol("WM_DELETE_WINDOW", self.exit_program)
        
        # 设置窗口图标
        if os.path.exists(ICON_PATH):
            self.root.iconbitmap(ICON_PATH)
        
        # 设置主题色
        self.theme_color = "#4CAF50"
        self.accent_color = "#FF5722"
        self.text_bg = "#F5F5F5"
        self.text_fg = "#333333"
        
        # 网络版本更新日志URL
        self.version_log_url = "https://raw.gitcode.com/ZZJ-JACK/Pvz/raw/master/README.md"
        
        # 读取版本更新日志内容（优先网络，失败则本地）
        self.readme_content, self.network_status = self.read_version_logs()
        # 解析版本更新日志
        self.version_logs = self.parse_version_logs()
        # 获取最新版本
        self.latest_version = self.get_latest_version()
        
        self.create_styles()  # 先创建样式
        self.create_widgets()
        self.display_version_logs()
        
    def read_version_logs(self):
        """从网络获取版本更新日志，失败则读取本地文件，返回内容和网络状态"""
        network_status = "success"
        try:
            # 尝试从网络获取版本更新日志
            response = requests.get(self.version_log_url, timeout=10)
            response.raise_for_status()  # 检查请求是否成功
            return response.text, network_status
        except requests.exceptions.RequestException as e:
            network_status = "failed"
            # 网络请求失败，尝试读取本地文件
            try:
                with open("./README.md", "r", encoding="utf-8") as f:
                    return f.read(), network_status
            except Exception as local_e:
                return f"无法获取版本更新日志\n网络错误: {e}\n本地文件错误: {local_e}", network_status
    
    def parse_version_logs(self):
        """解析版本更新日志"""
        logs = {}
        # 读取所有行，逐行解析
        lines = self.readme_content.split('\n')
        
        # 查找版本迭代部分
        in_version_section = False
        for line in lines:
            # 检查是否进入版本迭代部分
            if '游戏版本迭代' in line:
                in_version_section = True
                continue
            
            if in_version_section:
                # 跳过空行
                if not line.strip():
                    continue
                
                # 检查是否退出版本迭代部分
                if line.startswith('-') and not (re.match(r'\-\s*([0-9]+\.[0-9])', line) or re.match(r'\-\s*([0-9]{4}-[0-9])', line)):
                    break
                
                # 移除行首的'- '（如果有）
                if line.startswith('- '):
                    line = line[2:].strip()
                
                # 尝试匹配各种版本记录格式
                # 格式1: 版本号 日期 描述 (如: 1.0.0 2024-07-15 完成游戏主程序)
                version_date_desc_pattern = r'\s*([0-9]+\.[0-9]+(?:\.[0-9]+)?)\s+([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})\s+(.+)'
                match = re.match(version_date_desc_pattern, line)
                if match:
                    version = match.group(1)
                    date = match.group(2)
                    description = match.group(3)
                    logs[version] = {"date": date, "description": description}
                    continue
                
                # 格式2: 日期 描述 (如: 2024-07-01 项目创建)
                date_desc_pattern = r'\s*([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})\s+(.+)'
                match = re.match(date_desc_pattern, line)
                if match:
                    date = match.group(1)
                    description = match.group(2)
                    # 对于没有版本号的记录，使用日期作为键
                    logs[date] = {"date": date, "description": description}
                    continue
        
        return logs
    
    def get_latest_version(self):
        """获取最新版本号"""
        if not self.version_logs:
            return GAME_VERSION
        
        # 过滤出有版本号的记录
        version_records = []
        for key, log in self.version_logs.items():
            if key != log["date"]:  # 有版本号的记录
                version_records.append(key)
        
        if not version_records:
            return GAME_VERSION
        
        # 将版本号转换为元组以便比较
        version_records.sort(key=lambda v: tuple(map(int, v.split('.'))), reverse=True)
        return version_records[0]
    
    def is_latest_version(self):
        """检查当前版本是否为最新版本"""
        current = tuple(map(int, GAME_VERSION.split('.')))
        latest = tuple(map(int, self.latest_version.split('.')))
        return current >= latest
    
    def create_styles(self):
        """创建自定义样式"""
        style = ttk.Style()
        
        # 配置按钮样式
        style.configure("Normal.TButton", font=("Microsoft YaHei", 10), padding=5)
        style.configure("Accent.TButton", font=("Microsoft YaHei", 10, "bold"), padding=5, 
                       foreground=self.accent_color)
    
    def create_widgets(self):
        """创建窗口组件"""
        # 创建主框架
        main_frame = Frame(self.root, padx=15, pady=12)
        main_frame.pack(fill=BOTH, expand=True)
        
        # 标题标签 - 保持原字体大小
        title_label = Label(main_frame, text="Pvz版本更新日志", font=(
            "Microsoft YaHei", 18, "bold"), fg=self.theme_color)
        title_label.pack(pady=(0, 12))
        
        # 版本信息框架 - 紧凑布局
        version_frame = Frame(main_frame, bg="#E8F5E9", bd=1, relief=GROOVE)
        version_frame.pack(fill=X, pady=(0, 10), padx=10)
        
        # 版本信息容器 - 减少内边距
        version_info_container = Frame(version_frame, bg="#E8F5E9")
        version_info_container.pack(fill=X, padx=8, pady=4)
        
        # 左侧版本信息
        left_version_frame = Frame(version_info_container, bg="#E8F5E9")
        left_version_frame.pack(side=LEFT, fill=X, expand=True)
        
        # 当前版本标签 - 保持原字体大小
        current_version_text = f"当前版本: {GAME_VERSION}"
        current_version = Label(left_version_frame, text=current_version_text, font=(
            "Microsoft YaHei", 10), 
                               bg="#E8F5E9", fg="#2E7D32")
        current_version.pack(side=LEFT, padx=(0, 20))
        
        # 最新版本标签 - 保持原字体大小
        latest_version_text = f"最新版本: {self.latest_version}"
        latest_version = Label(left_version_frame, text=latest_version_text, font=(
            "Microsoft YaHei", 10), 
                              bg="#E8F5E9", fg="#2E7D32")
        latest_version.pack(side=LEFT, padx=(0, 20))
        
        # 版本状态标签 - 保持原字体大小
        if self.is_latest_version():
            status_text = "✓ 已是最新版本"
            status_color = "#4CAF50"
        else:
            status_text = "↑ 发现新版本"
            status_color = "#FF5722"
        
        status_label = Label(left_version_frame, text=status_text, font=(
            "Microsoft YaHei", 10, "bold"), 
                           bg="#E8F5E9", fg=status_color)
        status_label.pack(side=LEFT)
        
        # 右侧网络测试区域
        right_network_frame = Frame(version_info_container, bg="#E8F5E9")
        right_network_frame.pack(side=RIGHT)
        
        # 网络状态指示器
        network_status_frame = Frame(right_network_frame, bg="#E8F5E9")
        network_status_frame.pack(side=LEFT, padx=(0, 10))
        
        # 网络图标和状态标签 - 保持原字体大小
        network_icon = Label(network_status_frame, text="🌐", font=("Microsoft YaHei", 12), 
                           bg="#E8F5E9")
        network_icon.pack(side=LEFT, padx=(0, 5))
        
        self.network_status_var = StringVar()
        self.update_network_status()
        network_status = Label(network_status_frame, textvariable=self.network_status_var, 
                             font=("Microsoft YaHei", 10), bg="#E8F5E9", fg="#555555")
        network_status.pack(side=LEFT)
        
        # 网络测试按钮 - 保持原字体大小
        test_button = ttk.Button(right_network_frame, text="测试网络", 
                               command=self.test_network_connection,
                               style="Normal.TButton", width=10)
        test_button.pack(side=LEFT)
        
        # 内容区域框架 - 减小上下间距
        content_frame = Frame(main_frame)
        content_frame.pack(fill=BOTH, expand=True, pady=(0, 8))
        
        # 左侧文本区域
        left_frame = Frame(content_frame)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        
        # 文本框容器 - 减小高度
        text_container = Frame(left_frame, bd=2, relief=SOLID, bg="#FFFFFF", height=380)
        text_container.pack(fill=BOTH, expand=True)
        text_container.pack_propagate(False)  # 固定高度
        
        # 创建文本框和滚动条
        scrollbar = Scrollbar(text_container, bg="#E0E0E0", troughcolor="#F5F5F5")
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # 文本框 - 保持原字体大小
        self.text_area = Text(text_container, wrap=WORD, font=("Microsoft YaHei", 10),
                             bg=self.text_bg, fg=self.text_fg, bd=0, relief=FLAT,
                             highlightthickness=0, padx=10, pady=10,
                             yscrollcommand=scrollbar.set)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=self.text_area.yview)
        
        # 设置文本框为只读
        self.text_area.config(state=DISABLED)
        
        # 右侧赞赏码区域 - 减小高度
        right_frame = Frame(content_frame, width=250, height=380, bg="#FFFFFF", bd=2, relief=GROOVE)
        right_frame.pack(side=RIGHT)
        right_frame.pack_propagate(False)  # 固定高度
        
        # 右侧内容容器
        right_inner = Frame(right_frame, bg="#FFFFFF")
        right_inner.pack(fill=BOTH, expand=True, padx=15, pady=12)
        
        # 赞赏码标题 - 保持原字体大小
        reward_title = Label(right_inner, text="👍 支持开发者", 
                           font=("Microsoft YaHei", 12, "bold"), fg=self.accent_color, bg="#FFFFFF")
        reward_title.pack(pady=(0, 8))
        
        # 赞赏码提示 - 保持原字体大小
        reward_tip = Label(right_inner, text="请扫描下方赞赏码", 
                          font=("Microsoft YaHei", 10), fg="#666666", bg="#FFFFFF")
        reward_tip.pack(pady=(0, 10))
        
        # 赞赏码图片容器 - 减小高度
        image_container = Frame(right_inner, bg="#FFFFFF", height=220)
        image_container.pack(fill=X, pady=(0, 10))
        image_container.pack_propagate(False)
        
        # 赞赏码图片
        reward_image_path = "data/image/Other/reward.png"
        if os.path.exists(reward_image_path):
            try:
                image = Image.open(reward_image_path)
                max_width = 180  # 减小图片宽度
                max_height = 180  # 减小图片高度
                
                width, height = image.size
                if width > max_width or height > max_height:
                    ratio = min(max_width/width, max_height/height)
                    new_width = int(width * ratio)
                    new_height = int(height * ratio)
                    image = image.resize((new_width, new_height), Image.LANCZOS)
                
                self.reward_photo = ImageTk.PhotoImage(image)
                
                reward_label = Label(image_container, image=self.reward_photo, bg="#FFFFFF")
                reward_label.pack(expand=True)
            except Exception as e:
                error_label = Label(image_container, text=f"无法加载赞赏码", 
                                  font=("Microsoft YaHei", 9), fg="#FF0000", bg="#FFFFFF")
                error_label.pack(expand=True)
        else:
            not_found_label = Label(image_container, text="赞赏码图片未找到", 
                                  font=("Microsoft YaHei", 9), fg="#FF0000", bg="#FFFFFF")
            not_found_label.pack(expand=True)
        
        # 赞赏码说明 - 保持原字体大小
        reward_desc = Label(right_inner, text="您的支持是我持续更新的动力", 
                          font=("Microsoft YaHei", 9), fg="#888888", bg="#FFFFFF")
        reward_desc.pack()
        
        # 底部按钮区域 - 减小上边距
        bottom_frame = Frame(main_frame)
        bottom_frame.pack(fill=X, pady=(5, 0))
        
        # 左侧提示信息
        left_tip_frame = Frame(bottom_frame)
        left_tip_frame.pack(side=LEFT, fill=X, expand=True)
        
        if not self.is_latest_version():
            update_tip = Label(left_tip_frame, text="🔔 发现新版本！建议前往官网下载最新版本", 
                             font=("Microsoft YaHei", 11, "bold"), fg=self.accent_color)
            update_tip.pack(anchor=W)
        
        # 右侧按钮容器
        button_frame = Frame(bottom_frame)
        button_frame.pack(side=RIGHT)
        
        # 下载按钮（仅在非最新版本时显示）
        if not self.is_latest_version():
            download_button = ttk.Button(button_frame, text="前往下载", 
                                       command=self.open_download_url,
                                       style="Accent.TButton", width=10)
            download_button.pack(side=LEFT, padx=(0, 10))
        
        # 官网入口按钮
        website_button = ttk.Button(button_frame, text="官方网站", 
                                command=self.open_official_website,
                                style="Normal.TButton", width=10)
        website_button.pack(side=LEFT, padx=(0, 10))
        
        # 开始游戏按钮
        start_button = ttk.Button(button_frame, text="开始游戏", 
                                command=self.root.destroy,
                                style="Normal.TButton", width=10)
        start_button.pack(side=LEFT)
    
    def display_version_logs(self):
        """显示完整版本更新日志内容"""
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        
        # 配置文本标签样式 - 保持原字体大小
        self.text_area.tag_config("network_status", font=(
            "Microsoft YaHei", 12, "bold"), foreground=self.accent_color)
        self.text_area.tag_config("version_entry", font=(
            "Microsoft YaHei", 11, "bold"), foreground="#FF5722")
        self.text_area.tag_config("date", font=(
            "Microsoft YaHei", 10, "italic"), foreground="#666666")
        self.text_area.tag_config("description", font=(
            "Microsoft YaHei", 10), foreground=self.text_fg)
        self.text_area.tag_config("error", font=(
            "Microsoft YaHei", 10), foreground="#FF0000")
        
        # 显示网络状态
        if self.network_status == "success":
            self.text_area.insert(END, "✅ 网络连接成功！获取到最新版本更新日志\n", "network_status")
        else:
            self.text_area.insert(END, "⚠️ 网络连接失败！显示本地缓存版本更新日志\n", "network_status")
            self.text_area.insert(END, "   注意：必须使用中国大陆内网才能获取最新版本信息\n", "network_status")
        self.text_area.insert(END, "- " * 40 + "\n\n")
        
        # 检查是否有错误信息
        if "无法获取版本更新日志" in self.readme_content:
            self.text_area.insert(END, self.readme_content + "\n", "error")
        else:
            # 按日期降序排序所有记录
            def get_sort_key(item):
                version, log = item
                date = log["date"]
                # 转换日期为可排序格式
                year, month, day = map(int, date.split('-'))
                return (-year, -month, -day)
            
            sorted_logs = sorted(self.version_logs.items(), key=get_sort_key)
            
            for key, log in sorted_logs:
                date = log["date"]
                description = log["description"]
                
                # 检查是否是版本记录还是只有日期的记录
                if key != date:  # 有版本号的记录
                    # 显示版本和日期
                    self.text_area.insert(END, f"{key}  ", "version_entry")
                    self.text_area.insert(END, f"({date})\n", "date")
                else:  # 只有日期的记录
                    # 只显示日期
                    self.text_area.insert(END, f"{date}  ", "date")
                
                # 显示更新描述
                self.text_area.insert(END, f"  {description}\n", "description")
                self.text_area.insert(END, "\n")
        
        self.text_area.config(state=DISABLED)
    
    def open_download_url(self):
        """从Gitee获取最新便携版下载链接并自动下载到当前目录"""
        # 创建下载进度窗口
        self.download_window = Toplevel(self.root)
        self.download_window.title("下载最新版本")
        self.download_window.geometry("400x150")
        self.download_window.resizable(False, False)
        
        # 设置窗口图标
        if os.path.exists(ICON_PATH):
            self.download_window.iconbitmap(ICON_PATH)
        
        # 创建标签
        status_label = Label(self.download_window, text="正在获取最新下载链接...", font=("Microsoft YaHei", 10))
        status_label.pack(pady=10)
        
        # 创建进度条
        self.progress_bar = ttk.Progressbar(self.download_window, orient=HORIZONTAL, length=300, mode='determinate')
        self.progress_bar.pack(pady=10)
        
        # 创建进度标签
        self.progress_label = Label(self.download_window, text="0%", font=("Microsoft YaHei", 10))
        self.progress_label.pack(pady=5)
        
        # 在单独线程中执行下载，避免阻塞GUI
        download_thread = threading.Thread(target=self._download_latest_version)
        download_thread.daemon = True
        download_thread.start()
    
    def _download_latest_version(self):
        """下载最新版本的实际逻辑"""
        try:
            # 获取下载链接文件
            self.download_window.after(0, lambda: self._update_status("正在获取最新下载链接..."))
            downloads_url = "https://gitee.com/zzj-jack/pvz-site/raw/main/downloads.txt"
            response = requests.get(downloads_url, timeout=10)
            response.raise_for_status()
            
            # 解析下载链接
            content = response.text
            lines = content.split('\n')
            portable_links = []
            
            for line in lines:
                line = line.strip()
                if line and "便携版" in line and "http" in line:
                    # 提取链接
                    link_start = line.find("http")
                    if link_start != -1:
                        portable_links.append(line[link_start:])
            
            if not portable_links:
                self.download_window.after(0, lambda: self._update_status("未找到便携版下载链接", error=True))
                time.sleep(2)
                self.download_window.after(0, self.download_window.destroy)
                return
            
            # 使用第一个便携版链接作为最新版本
            latest_download_url = portable_links[0]
            
            # 提取文件名
            file_name = latest_download_url.split('/')[-1]
            
            # 设置保存路径为当前游戏目录
            save_path = os.path.join(os.getcwd(), file_name)
            
            # 开始下载
            self.download_window.after(0, lambda: self._update_status(f"正在下载: {file_name}"))
            
            # 下载文件并显示进度
            response = requests.get(latest_download_url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded_size = 0
            
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        downloaded_size += len(chunk)
                        
                        # 更新进度条
                        if total_size > 0:
                            progress_percent = int((downloaded_size / total_size) * 100)
                            self.download_window.after(0, lambda p=progress_percent: self._update_progress(p))
            
            # 下载完成
            self.download_window.after(0, lambda: self._update_status(f"下载完成！文件已保存至: {save_path}"))
            
            # 2秒后关闭窗口
            time.sleep(2)
            self.download_window.after(0, self.download_window.destroy)
            
        except Exception as e:
            error_msg = f"下载失败: {str(e)}"
            self.download_window.after(0, lambda: self._update_status(error_msg, error=True))
            time.sleep(3)
            self.download_window.after(0, self.download_window.destroy)
    
    def _update_status(self, message, error=False):
        """更新下载状态标签"""
        status_label = self.download_window.children.get('!label')
        if status_label:
            status_label.config(text=message, fg="red" if error else "black")
    
    def _update_progress(self, percent):
        """更新进度条和进度标签"""
        self.progress_bar['value'] = percent
        self.progress_label.config(text=f"{percent}%")
        self.download_window.update_idletasks()
    
    def open_official_website(self):
        """打开官方网站"""
        webbrowser.open("http://pvz.zzjjack.us.kg")
    
    def exit_program(self):
        """退出整个进程"""
        self.root.destroy()
        import sys
        sys.exit()
    
    def update_network_status(self):
        """更新网络状态显示"""
        if self.network_status == "success":
            self.network_status_var.set("网络: 正常")
        else:
            self.network_status_var.set("网络: 离线")
    
    def test_network_connection(self):
        """测试网络连通性"""
        # 立即显示测试中状态
        self.network_status_var.set("网络: 测试中...")
        
        # 使用单独的线程进行网络测试
        import threading
        test_thread = threading.Thread(target=self._do_network_test)
        test_thread.daemon = True
        test_thread.start()
    
    def _do_network_test(self):
        """执行网络测试的实际逻辑"""
        try:
            # 尝试连接到版本日志URL
            response = requests.get(self.version_log_url, timeout=5)
            response.raise_for_status()
            self.network_status = "success"
        except requests.exceptions.RequestException:
            self.network_status = "failed"
        
        # 更新网络状态显示
        self.root.after(0, self.update_network_status)
        
        # 如果是网络测试成功，重新获取并显示日志
        if self.network_status == "success":
            try:
                response = requests.get(self.version_log_url, timeout=5)
                self.readme_content = response.text
                self.version_logs = self.parse_version_logs()
                self.latest_version = self.get_latest_version()
            except:
                pass
        
        self.root.after(0, self.display_version_logs)
    
    def show(self):
        """显示窗口"""
        self.root.mainloop()
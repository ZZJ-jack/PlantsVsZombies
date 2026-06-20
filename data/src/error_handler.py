"""
全局异常捕获模块
捕获游戏中未处理的异常，收集错误信息并通过弹窗提示用户
"""
import sys
import traceback
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import os
import json
import urllib.request
import urllib.error
from data.src.const import GAME_VERSION  # 导入游戏版本号

# 错误日志文件路径
ERROR_LOG_PATH = "./data/log/error.log"

# 远程 Bug 提交地址
BUG_SUBMIT_URL = "https://pvzbug.zzjjack.us.kg/submit"

# 保存游戏实例引用，用于报错时关闭游戏窗口
_game_instance = None
_gameset_instance = None


def register_game_instances(game, gameset_window):
    """
    注册游戏实例和游戏设置窗口实例
    供 main.py 在初始化后调用，以便报错时能自动关闭游戏窗口
    """
    global _game_instance, _gameset_instance
    _game_instance = game
    _gameset_instance = gameset_window


def ensure_log_dir():
    """确保日志目录存在"""
    log_dir = os.path.dirname(ERROR_LOG_PATH)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


def extract_error_data(exc_type, exc_value, exc_traceback, source=""):
    """
    提取结构化的错误数据
    :return: (short_msg, error_info_text, data_dict)
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    tb_text = "".join(tb_lines)
    error_type = exc_type.__name__
    error_content = str(exc_value)

    # 构建完整错误文本
    error_info = (
        f"游戏发生错误\n"
        f"时间：{now}\n"
        f"错误类型：{error_type}\n"
        f"错误内容：{error_content}\n\n"
        f"--- 详细堆栈信息 ---\n"
        f"{tb_text}"
    )

    short_msg = f"错误类型：{error_type}\n错误内容：{error_content}"

    data = {
        "source": source,
        "time": now,
        "type": error_type,
        "content": error_info,  # 提交完整错误信息
        "traceback": tb_text
    }

    return short_msg, error_info, data


def save_error_to_file(error_text):
    """将错误信息保存到日志文件"""
    ensure_log_dir()
    try:
        with open(ERROR_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*60}\n")
            f.write(error_text)
            f.write(f"\n{'='*60}\n")
    except Exception:
        pass  # 如果写入日志也失败，则忽略


def submit_bug_report(data):
    """
    向远程服务器提交 Bug 报告
    :return: True 表示提交成功，False 表示提交失败（网络不可用）
    """
    try:
        req = urllib.request.Request(
            BUG_SUBMIT_URL,
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"Pvz-Game/{GAME_VERSION}"
            },
            method="POST"
        )
        # 5 秒超时，避免阻塞
        with urllib.request.urlopen(req, timeout=5) as resp:
            resp.read()
        return True
    except Exception:
        return False  # 网络不可用或服务器异常


def kill_game_processes():
    """
    报错时先杀死游戏主进程和游戏设置窗口
    关闭 pygame 窗口和 tkinter 设置窗口，然后再弹出错误提示
    """
    # 1. 销毁游戏设置 tkinter 窗口
    if _gameset_instance is not None:
        try:
            if hasattr(_gameset_instance, 'loginWindow'):
                _gameset_instance.loginWindow.destroy()
        except Exception:
            pass
        try:
            if hasattr(_gameset_instance, 'SetWindow'):
                _gameset_instance.SetWindow.destroy()
        except Exception:
            pass

    # 2. 停止游戏主循环
    if _game_instance is not None:
        try:
            _game_instance.running = False
            _game_instance.really = False
        except Exception:
            pass

    # 3. 退出 pygame
    try:
        import pygame
        pygame.quit()
    except Exception:
        pass


def show_error_dialog(short_msg, error_info, submitted_online=False):
    """
    显示错误弹窗
    先弹简洁的错误提示，再弹详细信息窗口
    submitted_online: 是否已成功在线提交
    """
    # 先弹出一个简单的错误提示
    messagebox.showerror("游戏运行错误", short_msg)

    # 再弹出一个包含详细信息的窗口
    detail_window = tk.Tk()
    detail_window.title("错误详细信息")
    detail_window.geometry("700x500")
    detail_window.resizable(True, True)

    # 窗口置顶，确保用户能看到
    detail_window.attributes('-topmost', True)
    # 500ms 后取消置顶，恢复正常窗口层级
    detail_window.after(500, lambda: detail_window.attributes('-topmost', False))

    # 设置窗口图标（如果存在）
    try:
        detail_window.iconbitmap("./data/image/Other/icon.ico")
    except Exception:
        pass

    # 提示标签
    tk.Label(
        detail_window,
        text="游戏运行过程中发生了未处理的异常，详细信息如下：",
        font=("微软雅黑", 10),
        fg="red",
        wraplength=650
    ).pack(pady=(10, 5))

    # 详细信息文本框
    text_area = scrolledtext.ScrolledText(
        detail_window,
        wrap=tk.WORD,
        width=80,
        height=20,
        font=("Consolas", 9)
    )
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, error_info)
    text_area.config(state=tk.DISABLED)  # 只读

    # 提示已保存到日志
    if submitted_online:
        status_msg = "错误信息已在线提交至服务器"
        status_color = "green"
    else:
        status_msg = f"错误信息已保存至本地日志：{ERROR_LOG_PATH}"
        status_color = "gray"
    tk.Label(
        detail_window,
        text=status_msg,
        font=("微软雅黑", 9),
        fg=status_color
    ).pack(pady=(0, 5))

    # 关闭按钮 — 关闭窗口后退出整个进程
    def on_close():
        detail_window.destroy()
        os._exit(0)

    detail_window.protocol("WM_DELETE_WINDOW", on_close)
    tk.Button(
        detail_window,
        text="关闭",
        command=on_close,
        width=10,
        height=1
    ).pack(pady=(0, 10))

    detail_window.mainloop()


def handle_exception(exc_type, exc_value, exc_traceback, source=""):
    """
    统一处理异常：杀进程 -> 检测网络 -> 在线提交 或 本地保存 -> 弹窗提示
    """
    short_msg, error_info, data = extract_error_data(
        exc_type, exc_value, exc_traceback, source
    )

    # 先杀死游戏进程
    kill_game_processes()

    # 尝试在线提交，成功则不再保存本地日志
    submitted_online = submit_bug_report(data)
    if not submitted_online:
        # 网络不可用，保存到本地日志
        save_error_to_file(error_info)

    # 弹窗提示
    show_error_dialog(short_msg, error_info, submitted_online)


def global_exception_handler(exc_type, exc_value, exc_traceback):
    """
    全局异常处理函数（用于 sys.excepthook）
    """
    # 忽略 KeyboardInterrupt 等系统退出异常
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    handle_exception(exc_type, exc_value, exc_traceback, source="主线程")


def thread_exception_handler(args):
    """
    线程异常处理函数（用于 threading.excepthook）
    """
    exc_type = args.exc_type
    exc_value = args.exc_value
    exc_traceback = args.exc_traceback

    # 忽略 KeyboardInterrupt
    if issubclass(exc_type, KeyboardInterrupt):
        return

    source = args.thread.name if args.thread else "未知线程"
    handle_exception(exc_type, exc_value, exc_traceback, source=source)


def install_error_handler():
    """
    安装全局异常处理器
    在程序入口处调用一次即可
    """
    sys.excepthook = global_exception_handler
    threading.excepthook = thread_exception_handler
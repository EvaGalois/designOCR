import psutil

process_pid = 11960

# 使用 psutil 来查询进程是否存在
if psutil.pid_exists(process_pid):
    print(f"进程 {process_pid} 存在。")
    # 终止进程：
    # psutil.Process(process_pid).terminate()
else:
    print(f"进程 {process_pid} 不存在。")
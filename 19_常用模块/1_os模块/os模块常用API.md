`os` 模块是 Python 标准库中的一个重要模块，主要用于与操作系统进行交互。它提供了一些简单的接口来进行文件和目录操作、环境变量管理以及其他与操作系统相关的操作。以下是 `os` 模块的一些常用功能：

### 1. **文件和目录操作**
   - **`os.getcwd()`**: 获取当前工作目录的路径。
   - **`os.chdir(path)`**: 改变当前工作目录到指定的路径。
   - **`os.listdir(path='.')`**: 返回指定路径下的文件和目录列表。
   - **`os.mkdir(path)`**: 创建一个新的目录。
   - **`os.makedirs(path)`**: 递归地创建目录。
   - **`os.remove(path)`**: 删除指定文件。
   - **`os.rmdir(path)`**: 删除指定目录。
   - **`os.rename(src, dst)`**: 重命名文件或目录。

### 2. **环境变量操作**
   - **`os.environ`**: 获取系统的环境变量。
   - **`os.getenv(key, default=None)`**: 获取指定环境变量的值。
   - **`os.putenv(key, value)`**: 设置一个环境变量的值。

### 3. **路径操作**
   - **`os.path.join(path, *paths)`**: 将多个路径组合后返回。
   - **`os.path.abspath(path)`**: 返回指定路径的绝对路径。
   - **`os.path.exists(path)`**: 检查路径是否存在。
   - **`os.path.isfile(path)`**: 判断指定路径是否为文件。
   - **`os.path.isdir(path)`**: 判断指定路径是否为目录。
   - **`os.path.split(path)`**: 将路径分割成目录和文件名。
   - **`os.path.splitext(path)`**: 分离文件名和扩展名。

### 4. **进程管理**
   - **`os.system(command)`**: 使用系统的 shell 执行命令。
   - **`os.popen(command)`**: 打开一个与命令交互的管道。
   - **`os.exit(code)`**: 终止当前进程并返回状态码。

### 5. **权限和属性**
   - **`os.chmod(path, mode)`**: 更改文件或目录的权限。
   - **`os.stat(path)`**: 获取文件或目录的状态。

这些功能使得 `os` 模块在进行与操作系统相关的任务时非常方便和强大。

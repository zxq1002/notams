# REQUIREMENTS: notams

## 1. 跨平台兼容性 (Cross-platform Compatibility)
- **1.1 [COMPAT-1.1] 替换 Windows 特有依赖**: 
    - 移除 `pywin32` 及其相关模块（如 `win32clipboard`）。
    - 引入跨平台剪贴板库（如 `pyperclip`）或使用 Flask 接口处理剪贴板逻辑。
- **1.2 [COMPAT-1.2] 改进文件对话框**:
    - 目前使用的 `tkinter.filedialog` 在 macOS/Linux 上可能需要额外的依赖（如 `python3-tk`）。
    - 考虑使用 `pywebview` 原生的 `window.create_file_dialog` 或其他跨平台方案。
- **1.3 [COMPAT-1.3] 环境适配**:
    - 确保 `pywebview` 在 macOS (WebKit) 和 Linux (GTK/QT) 上的初始化正常。

## 2. 依赖管理 (Dependency Management)
- **2.1 [DEPS-2.1] Python 版本要求**:
    - 将最低支持版本定为 Python 3.9。
- **2.2 [DEPS-2.2] 优化 requirements.txt**:
    - 移除 `pywin32`。
    - 锁定核心库的版本以防止环境差异导致的运行失败。

## 3. 功能增强 (Functional Enhancements)
- **3.1 [ENHANCE-3.1] 错误处理**:
    - 增加对网络请求失败（抓取 NOTAM 失败）的健壮处理。
    - 改进跨平台环境下的路径处理（使用 `os.path` 或 `pathlib`）。

## 4. 验证 (Validation)
- **4.1 [VALID-4.1] 本地测试 (macOS)**: 验证在 macOS 下能否成功启动窗口并加载地图。
- **4.2 [VALID-4.2] 容器化/自动化测试**: 考虑增加基础的自动化测试以验证数据抓取和解析逻辑。

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| COMPAT-1.1 | Phase 1 | Pending |
| COMPAT-1.2 | Phase 2 | Pending |
| COMPAT-1.3 | Phase 1 | Pending |
| DEPS-2.1 | Phase 1 | Pending |
| DEPS-2.2 | Phase 1 | Pending |
| ENHANCE-3.1 | Phase 2 | Pending |
| VALID-4.1 | Phase 3 | Pending |
| VALID-4.2 | Phase 3 | Pending |

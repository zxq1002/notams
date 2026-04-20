# PROJECT: notams

## Vision
通过 NOTAMS 获取并绘制火箭发射落区，成为一个跨平台、高性能、易于使用的可视化工具。

## Context
项目目前是一个基于 Python Flask 和 pywebview 的混合桌面应用。它能够从 DINS、FAA 等数据源抓取航行通告 (NOTAM)，并使用 Leaflet.js 在地图上绘制落区。

## Goals
- **跨平台兼容性**: 消除 Windows 特有依赖（如 `pywin32`），支持 macOS 和 Linux。
- **依赖管理**: 将 Python 版本要求调整为 3.9 及以上，并优化现有的 `requirements.txt`。
- **稳定性**: 确保在不同操作系统上的窗口渲染和数据抓取逻辑一致。

## Constraints
- 维持现有的 Python Flask + pywebview 架构。
- 保证离线或半离线环境下的地图绘制能力（通过高德地图瓦片源）。

## Core Tech
- **Backend**: Python 3.9+, Flask
- **Frontend**: Leaflet.js, Vanilla JS/CSS
- **Desktop**: pywebview
- **Data**: requests, BeautifulSoup4, shapely, pandas, numpy

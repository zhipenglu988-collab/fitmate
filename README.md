# FitMate 🏋️

**移动健身助手** — Python + KivyMD 打造，完全离线，数据本地存储。

## 功能

- 👤 **个人资料** — 身体指标录入（身高/体重/目标等）
- ⚖️ **BMI 计算** — 自动计算 BMI + 体型分类
- 📋 **智能计划** — 根据目标（减脂/增肌/保持）和活动水平自动生成 7 天训练计划
- 🥗 **饮食记录** — 早餐/午餐/晚餐/加餐 热量追踪
- 🏆 **成就系统** — 5 枚成就徽章
- ⏰ **定时提醒** — 早晚健身通知（可自定义时间）
- 📊 **数据追踪** — 体重历史、训练统计

## 技术栈

- **语言**: Python 3.11
- **UI**: KivyMD 1.1.1 (Material Design 3)
- **存储**: SQLite（本地）
- **通知**: APScheduler + Plyer
- **打包**: Buildozer (GitHub Actions)

## 开发

```bash
pip install -r requirements.txt
python main.py
```

## 构建 APK

每次推送到 GitHub 自动构建：

```bash
git push origin main
# → Actions 自动编译，20-40 分钟后在 Actions 页面下载 APK
```

或手动触发：GitHub → Actions → Build FitMate APK → Run workflow

# universalCompanionManagementSystem
# 通用陪玩系统 V3.0

**一站式 SaaS 中台，支持人工下单+抢单池、预存支付、一键结算、污点申诉、灰度发布。**

---

## 🚀 核心特性

| 功能域 | 亮点 |
|---|---|
| **下单** | 客服人工指定、客户自助抢单 |
| **支付** | 预存余额冻结支付，零超买 |
| **审核** | 客服一键审核 → 自动结算 |
| **提现** | 财务周批量 CSV 打款 |
| **申诉** | 店长污点标记，大屏统计 |
| **权限** | Casbin RBAC + 按钮级 |
| **监控** | Prometheus + 钉钉告警 |
| **灰度** | 尾号 5% 回滚 <30 s |

---

## 🛠️ 技术栈

- **后端**：Django 4.2 + DRF + Casbin + PostgreSQL 15 + Redis 7
- **前端**：Vue3 + Pinia + Arco Design + WebSocket
- **部署**：Docker + K8s + Helm + GitHub Actions

---

## 📦 快速开始

```bash
# 1️⃣ 克隆
git clone https://github.com/xxx/escort.git && cd escort

# 2️⃣ 启动
docker-compose up -d

# 3️⃣ 浏览
open http://localhost:8000/api/docs
```

---

## 📖 文档

| 链接 | 内容 |
|---|---|
| [完整接口文档](docs/openapi.yaml) | 85 个接口 |
| [数据库脚本](db/migrations/001_full.sql) | 一键建表 |
| [部署手册](deploy/README.md) | Helm + K8s |
| [测试报告](docs/test_report.md) | 并发脚本 |

---

## 🛡️ 开源协议

本项目采用 **Apache-2.0** 协议，允许闭源商用，保留作者署名。  
如需商业授权或白标 SaaS，请邮件联系。

---

## 📞 联系我们

- 产品：`a2778978136@163.com`
- 技术：`a2778978136@163.com`
- 运维：`a2778978136@163.com`

---
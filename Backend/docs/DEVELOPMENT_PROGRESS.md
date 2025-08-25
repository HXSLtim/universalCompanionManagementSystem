# 通用陪玩系统开发进度文档

## 项目概述

通用陪玩系统是一个基于Django框架的后端系统，包含用户管理、权限控制、钱包系统、订单管理等核心功能模块。

## 当前项目结构

```
.
├── apps
│   ├── audit (审计模块)
│   ├── business (业务模块)
│   │   ├── companion (陪玩管理)
│   │   ├── dispute (纠纷处理)
│   │   ├── order (订单管理)
│   │   └── project (项目管理)
│   ├── common (公共模块)
│   ├── identity (身份认证模块)
│   ├── monitor (监控模块)
│   └── wallet (钱包模块)
├── config (配置模块)
├── docs (文档)
└── public (公共资源)
```

## 已完成模块分析

### 1. 基础设施（已完成）

- Django项目骨架已创建
- 项目配置已分层
- 环境配置模板已准备

### 2. 数据层（部分完成）

#### 2.1 BaseModel + 审计字段（已完成）
文件：[apps/common/models.py](file://d:\Desktop\Code\universalCompanionManagementSystem\Backend\apps\common\models.py)
- 创建人、创建时间
- 更新人、更新时间
- 软删除标记
- 乐观锁版本号
- JSON扩展字段

#### 2.2 用户/角色/权限表（已完成）
文件：[apps/identity/models.py](file://d:\Desktop\Code\universalCompanionManagementSystem\Backend\apps\identity\models.py)
- Role角色模型（角色名、描述）
- User用户模型（继承AbstractUser，包含手机号、头像、角色关联等）
- UserRole用户角色关联模型

#### 2.3 钱包/充值/冻结表（未完成）
文件：[apps/wallet/models.py](file://d:\Desktop\Code\universalCompanionManagementSystem\Backend\apps\wallet\models.py)
- 模型文件已创建，但具体内容尚未实现

#### 2.4 订单 & 子单 & 申诉表（未完成）
文件：[apps/business/order/models.py](file://d:\Desktop\Code\universalCompanionManagementSystem\Backend\apps\business/order/models.py)
- 模型文件已创建，但具体内容尚未实现

#### 2.5 迁移脚本 & 假数据（未完成）
- 需要生成迁移脚本和假数据

## 待开发模块

### 3. 权限 & 认证
- JWT登录/刷新接口
- Casbin策略表和中间件
- 按钮级权限装饰器

### 4. 预存域接口
- 充值单创建和回调处理
- 钱包余额查询接口
- 冻结/解冻服务
- 退款申请和审核接口

### 5. 业务域接口
- 客服人工下单
- 客户自助下单
- 抢单锁和子单生成
- 子单完成和审核
- 结算触发器（信号）

### 6. 财务接口
- 提现申请创建
- 财务批量打款CSV
- 银行回调解析

### 7. 前端小程序（并行开发）
- 登录和路由守卫
- 充值页面
- 抢单列表和实时推送
- 客服审核页面
- 店长污点大屏

### 8. 测试
- 并发抢单脚本
- 钱包并发扣款脚本
- 端到端Cypress测试

### 9. 部署 & 上线
- Docker镜像构建
- Helm Chart配置
- Prometheus规则配置
- 蓝绿灰度发布策略

## 当前开发进度评估

根据代码分析，项目已完成阶段1（基础设施）和阶段2的部分工作（BaseModel和用户/角色模型），钱包、订单等业务模型尚未实现，权限认证、接口开发等工作尚未开始。

## 后续开发建议

1. 完成钱包和订单模型的定义
2. 实现数据迁移脚本
3. 按照开发顺序表逐步实现各模块功能
4. 同步进行前端开发和测试工作
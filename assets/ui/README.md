# UI 素材库

目录：`Project BA/game/prototype/assets/ui/`

## 按钮（像素风方块按钮）

位置：`buttons/`

| 文件名 | 尺寸 | 主题色 | 用途 |
|--------|------|--------|------|
| `btn_attack.png` | 128×128 | 红 | 攻击/战斗按钮 |
| `btn_defend.png` | 128×128 | 蓝 | 防御/护盾按钮 |
| `btn_item.png` | 128×128 | 绿 | 背包/道具按钮 |
| `btn_endturn.png` | 128×128 | 紫 | 结束回合按钮 |
| `btn_shop.png` | 128×128 | 金 | 商店按钮 |
| `btn_rest.png` | 128×128 | 橙 | 篝火/休息按钮 |
| `btn_event.png` | 128×128 | 紫 | 随机事件按钮 |
| `btn_settings.png` | 128×128 | 灰 | 设置按钮 |
| `btn_boss.png` | 128×128 | 红 | Boss 战按钮 |
| `btn_card.png` | 128×128 | 蓝 | 卡牌/牌库按钮 |

### 生成方式

源脚本：`gen_buttons.py`（Pillow 生成 32×32 基础像素图，最近邻放大到 128×128）

重新生成命令：
```bash
cd assets/ui
python gen_buttons.py
```

### 使用示例

```html
<img src="assets/ui/buttons/btn_attack.png" alt="攻击" width="48">
```

或 CSS 背景：
```css
.btn-attack {
  background: url('assets/ui/buttons/btn_attack.png') center/contain no-repeat;
  width: 48px;
  height: 48px;
}
```

## 角色立绘

- `../aris_pixel_v5.png` — 爱丽丝像素风立绘
- `../aris_transparent.png` — 爱丽丝透明背景立绘
- `../portrait.png` — 默认角色立绘占位

## 待补充素材

- [ ] 像素风面板/边框
- [ ] 状态图标（HP/费用/护盾）
- [ ] 地图节点图标（像素化版）
- [ ] 品质徽章（白/蓝/紫/金）
- [ ] 卡牌边框（对应品质和类型）

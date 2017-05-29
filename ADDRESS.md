Address
====

## First 12 bytes of GameData.dat
Start: 0x00004
Length: 12 bytes

## Time spent in game in seconds
Start: 0x00024
Length: 4 bytes

## Current chapter
Start: 0x0002C
Length: 4 bytes, -1 if not present (due to saving after an ending)

## Character name
Start: 0x00034
Length: 70 bytes maximum, UTF-16 or UCS-2 encoded, null terminated and padded.

## Gameworld state
Start: 0x0007C
Length: 0x30000 bytes, null terminated and padded.
Structure: This segment is formatted as whitespace-delimited ascii text. Each nesting level adds an additional space at the start of each line. This section contains all quest/story/world state. The structure is formatted approximately as follows:

```
version v0.0.2
Scene
 Action
  [random 32-bit hex id]
   [several subcommands exist, like:
    ch [number, usually -1],
    Hp [number]
    Hacked [1/0]
    bSpStun [1/0]
    state [decimal number? or bitflag? or DONE]
    done [1/0]
    disabled [1/0]
    value [hexadecimal value, prefixed with 0x]
    user0 {starts an array}
    user1 {starts an array}
    layout {starts an array}
    script {starts an array}

    arrays start with a "size [decimal number]" command indicating the amount of sub entries, additionally, within a script, all entries are "value first [flag] second [something or DONE]"
   ]
 Behaviour
  [random 32-bit hex id]
SceneState
 [Long list of things that seem like string boolean flags that influence the state of the world.
  Seems to be there to keep track of which variants of environments need to be loaded and which quests have been finished. Examples:
  Tower_Appear: is the tower in the world.
  PV_All_Cadaver: Should the bodies of robots appear in Pascal's village
  q122_DONE - quest 122 is finished. Note that the naming for quests is very variable. Some end in FIN, some in DONE and separation happens with both slashes and underscores.
 ]
Flags
 [collection of flags identified by their string id.
  Most seem to be for the transporters, which have the following ids:
  ft_BK, ft_RC, ft_CC, ft_CRb, ft_CS, ft_DC, ft_DI, ft_DO, ft_DD, ft_AP, ft_RME, ft_AS, ft_PV, ft_FC, ft_FC2, ft_FC3, ft_SC (bunker, resistance camp, city, desert, apartments, ?, attraction square, pascal village, forest kingdom, ? (question marks are flooded city and cave probably))
 ]
Values
 [string id followed by 0x7 and then a decimal value, i.e. "novelunlock 0x7 15"]
Quest
 [active quests denoted by their id, i.e. q561]
```

## Money
Start: 0x3056C
Length: 4 Bytes

## Experience
Start: 0x3871C
Length: 4 Bytes

## Items
Start: 0x30570
End: 0x6116F
Single Item Length: 12 Bytes

Format: Item ID (2 bytes) 00 00 00 00 07 00 Amount(1 Bytes) 00 00 00
Example: B7 03 00 00 00 00 07 00 01 00 00 00
Item ID:
0000 回復薬：小
0001 回復薬：中
0002 回復薬：大
0003 回復薬：全
0032 耐電薬
003C 状態異常回復：視覚
0046 状態異常回復：聴覚
004B 状態異常回復：操作
0050 状態異常回復：全体
005A 全HP?全異常回復
0064 物理攻撃力UP：小
0066 物理攻撃力UP：大
006E 射撃攻撃力UP：小
0070 射撃攻撃力UP：大
0078 物理ダメージ軽減：小
007A 物理ダメージ軽減：大
0082 射撃ダメージ軽減：小
0084 射撃ダメージ軽減：大
008C スキル回復速度UP：小
008E スキル回復速度UP：大
0096 耐衝撃：小
0098 耐衝撃：大
00A0 高速走行：小
00A2 高速走行：大
012C 動物の餌
014A お金ドロップUP：小
014C お金ドロップUP：大
0190 電子ドラッグ
01EF 獣皮
0204 シカの肉
0208 磨り減ったネジ
0209 新品のネジ
020D 小さな歯車
020E 大きな歯車
0212 錆びた塊
0213 隕石の欠片
0217 チタン合金
0218 形状記憶合金
021C 壊れたゼンマイ
0221 壊れたバッテリー
0222 大きなバッテリー
0226 切れたケーブル
0227 綺麗なケーブル
022B 新品のボルト
0230 綺麗なナット
023A 機械生命体の腕
023B 機械生命体の脚
023C 機械生命体の胴体
023D 機械生命体の頭
0244 単純な機械
0245 精巧な機械
0246 複雑な機械
0247 強化パーツ：小
0248 強化パーツ：中
0249 強化パーツ：大
0258 銅鉱
0259 鉄鉱
025A 銀鉱
025B 金鉱
0262 凹んだ金属板
026D 植物の種
026E 樹液
026F 綺麗な水
0270 木の実
0271 砂漠のバラ
0272 キノコ
0273 汚れた本
0274 機械油
0275 なめし剤
0276 溶加材
0277 染料
0278 パイライト
0279 アンバー
027A 天然ゴム
027B 錆びたボルト
027C つぶれたナット
027D 巨大な卵
027E 鷲の卵
027F 黒真珠
0280 割れたイヤリング
0281 くすんだ腕輪
0282 頑丈なソケット
0283 歪んだ針金
0284 伸びたコイル
0285 凹んだソケット
0286 壊れた回路
028A 水晶
029A 綺麗なチョーカー
02AA 古い仮面
02AB 貴金属のピアス
02AC 何かの技術書
02AD 分厚い辞典
02AE 真珠
02AF モルダバイト
02B0 メテオライト
02B2 機械生命体のコア
02BF サルトルの置手紙
02CB メモリーチップ
02CC 男の日記
030C 壊れたおもちゃ
030D 汚れた家計簿
030E 小さな靴
0319 歯ブラシ
031A 化粧品
031B ダイエットグッズ
031C 筆記用具
031D 医学書
0340 機械生命体の部品
0341 スタンプ
0342 スタンプカード
0369 ピンクリボン
036A 水色リボン
0398 匂い袋
0399 高級な匂い袋
039A 極上の匂い袋
03A2 レコード：第一集
03A3 レコード：第二集
1F44 フナ
1F50 アジ


## Chips
Start: 0x326CC

Format: Code (4 bytes) ID (4 bytes) Type (4 bytes) Level (4 bytes) Size (4 bytes) Equipt Start A (4 bytes) Equipt Start B (4 bytes) Equipt Start C (4 bytes) FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00

Example:  Evade Range Up+3 in size 7, not equipted 
AF 00 00 00 28 0C 00 00 0D 00 00 00 03 00 00 00 07 00 00 00 FF FF FF FF FF FF FF FF FF FF FF FF  FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00

Level - Minimum size (diamond mark): 
0 - 04
1 - 05
2 - 06
3 - 07
4 - 09
5 - 0B
6 - 0E
7 - 11
9 - 15

**Weapon Attack Up** 00 00 00 00 B9 0B 00 00 01 00 00 00
**Weapon Attack Up +1** 01 00 00 00 BA 0B 00 00 01 00 00 00
**Weapon Attack Up +2** 02 00 00 00 BB 0B 00 00 01 00 00 00
**Weapon Attack Up +3** 03 00 00 00 BC 0B 00 00 01 00 00 00
**Weapon Attack Up +4** 04 00 00 00 BD 0B 00 00 01 00 00 00
**Weapon Attack Up +5** 05 00 00 00 BE 0B 00 00 01 00 00 00
**Weapon Attack Up +6** 06 00 00 00 BF 0B 00 00 01 00 00 00
**Weapon Attack Up +7** 07 00 00 00 C0 0B 00 00 01 00 00 00
**Weapon Attack Up +8** 08 00 00 00 C1 0B 00 00 01 00 00 00
**Down-Attack Up** 09 00 00 00 C2 0B 00 00 02 00 00 00
**Down-Attack Up +1** 0A 00 00 00 C3 0B 00 00 02 00 00 00
**Down-Attack Up +2** 0B 00 00 00 C4 0B 00 00 02 00 00 00
**Down-Attack Up +3** 0C 00 00 00 C5 0B 00 00 02 00 00 00
**Down-Attack Up +4** 0D 00 00 00 C6 0B 00 00 02 00 00 00
**Down-Attack Up +5** 0E 00 00 00 C7 0B 00 00 02 00 00 00
**Down-Attack Up +6** 0F 00 00 00 C8 0B 00 00 02 00 00 00
**Down-Attack Up +7** 10 00 00 00 C9 0B 00 00 02 00 00 00
**Down-Attack Up +8** 11 00 00 00 CA 0B 00 00 02 00 00 00
**Critical Up** 12 00 00 00 CB 0B 00 00 03 00 00 00
**Critical Up +1** 13 00 00 00 CC 0B 00 00 03 00 00 00
**Critical Up +2** 14 00 00 00 CD 0B 00 00 03 00 00 00
**Critical Up +3** 15 00 00 00 CE 0B 00 00 03 00 00 00
**Critical Up +4** 16 00 00 00 CF 0B 00 00 03 00 00 00
**Critical Up +5** 17 00 00 00 D0 0B 00 00 03 00 00 00
**Critical Up +6** 18 00 00 00 D1 0B 00 00 03 00 00 00
**Critical Up +7** 19 00 00 00 D2 0B 00 00 03 00 00 00
**Critical Up +8** 1A 00 00 00 D3 0B 00 00 03 00 00 00
**Ranged Attack Up** 1B 00 00 00 D4 0B 00 00 04 00 00 00
**Ranged Attack Up +1** 1C 00 00 00 D5 0B 00 00 04 00 00 00
**Ranged Attack Up +2** 1D 00 00 00 D6 0B 00 00 04 00 00 00
**Ranged Attack Up +3** 1E 00 00 00 D7 0B 00 00 04 00 00 00
**Ranged Attack Up +4** 1F 00 00 00 D8 0B 00 00 04 00 00 00
**Ranged Attack Up +5** 20 00 00 00 D9 0B 00 00 04 00 00 00
**Ranged Attack Up +6** 21 00 00 00 DA 0B 00 00 04 00 00 00
**Ranged Attack Up +7** 22 00 00 00 DB 0B 00 00 04 00 00 00
**Ranged Attack Up +8** 23 00 00 00 DC 0B 00 00 04 00 00 00
**Fast Cooldown** A3 00 00 00 DD 0B 00 00 05 00 00 00
**Fast Cooldown +1** A4 00 00 00 DE 0B 00 00 05 00 00 00
**Fast Cooldown +2** A5 00 00 00 DF 0B 00 00 05 00 00 00
**Fast Cooldown +3** A6 00 00 00 E0 0B 00 00 05 00 00 00
**Fast Cooldown +4** A7 00 00 00 E1 0B 00 00 05 00 00 00
**Fast Cooldown +5** A8 00 00 00 E2 0B 00 00 05 00 00 00
**Fast Cooldown +6** A9 00 00 00 E3 0B 00 00 05 00 00 00
**Fast Cooldown +7** AA 00 00 00 E4 0B 00 00 05 00 00 00
**Fast Cooldown +8** AB 00 00 00 E5 0B 00 00 05 00 00 00
**Melee Defence Up** 49 00 00 00 E6 0B 00 00 06 00 00 00
**Melee Defence Up +1** 4A 00 00 00 E7 0B 00 00 06 00 00 00
**Melee Defence Up +2** 4B 00 00 00 E8 0B 00 00 06 00 00 00
**Melee Defence Up +3** 4C 00 00 00 E9 0B 00 00 06 00 00 00
**Melee Defence Up +4** 4D 00 00 00 EA 0B 00 00 06 00 00 00
**Melee Defence Up +5** 4E 00 00 00 EB 0B 00 00 06 00 00 00
**Melee Defence Up +6** 4F 00 00 00 EC 0B 00 00 06 00 00 00
**Melee Defence Up +7** 50 00 00 00 ED 0B 00 00 06 00 00 00
**Melee Defence Up +8** 51 00 00 00 EE 0B 00 00 06 00 00 00
**Ranged Defence Up** 52 00 00 00 EF 0B 00 00 07 00 00 00
**Ranged Defence Up +1** 53 00 00 00 F0 0B 00 00 07 00 00 00
**Ranged Defence Up +2** 54 00 00 00 F1 0B 00 00 07 00 00 00
**Ranged Defence Up +3** 55 00 00 00 F2 0B 00 00 07 00 00 00
**Ranged Defence Up +4** 56 00 00 00 F3 0B 00 00 07 00 00 00
**Ranged Defence Up +5** 57 00 00 00 F4 0B 00 00 07 00 00 00
**Ranged Defence Up +6** 58 00 00 00 F5 0B 00 00 07 00 00 00
**Ranged Defence Up +7** 59 00 00 00 F6 0B 00 00 07 00 00 00
**Ranged Defence Up +8** 5A 00 00 00 F7 0B 00 00 07 00 00 00
**Anti Chain Damage** 5B 00 00 00 F8 0B 00 00 08 00 00 00
**Anti Chain Damage +1** 5C 00 00 00 F9 0B 00 00 08 00 00 00
**Anti Chain Damage +2** 5D 00 00 00 FA 0B 00 00 08 00 00 00
**Anti Chain Damage +3** 5E 00 00 00 FB 0B 00 00 08 00 00 00
**Anti Chain Damage +4** 5F 00 00 00 FC 0B 00 00 08 00 00 00
**Anti Chain Damage +5** 60 00 00 00 FD 0B 00 00 08 00 00 00
**Anti Chain Damage +6** 61 00 00 00 FE 0B 00 00 08 00 00 00
**Anti Chain Damage +7** 62 00 00 00 FF 0B 00 00 08 00 00 00
**Anti Chain Damage +8** 63 00 00 00 00 0C 00 00 08 00 00 00
**Max HP Up** 6D 00 00 00 01 0C 00 00 09 00 00 00
**Max HP Up +1** 6E 00 00 00 02 0C 00 00 09 00 00 00
**Max HP Up +2** 6F 00 00 00 03 0C 00 00 09 00 00 00
**Max HP Up +3** 70 00 00 00 04 0C 00 00 09 00 00 00
**Max HP Up +4** 71 00 00 00 05 0C 00 00 09 00 00 00
**Max HP Up +5** 72 00 00 00 06 0C 00 00 09 00 00 00
**Max HP Up +6** 73 00 00 00 07 0C 00 00 09 00 00 00
**Max HP Up +7** 74 00 00 00 08 0C 00 00 09 00 00 00
**Max HP Up +8** 75 00 00 00 09 0C 00 00 09 00 00 00
**Offensive Heal** 76 00 00 00 0A 0C 00 00 0A 00 00 00
**Offensive Heal +1** 77 00 00 00 0B 0C 00 00 0A 00 00 00
**Offensive Heal +2** 78 00 00 00 0C 0C 00 00 0A 00 00 00
**Offensive Heal +3** 79 00 00 00 0D 0C 00 00 0A 00 00 00
**Offensive Heal +4** 7A 00 00 00 0E 0C 00 00 0A 00 00 00
**Offensive Heal +5** 7B 00 00 00 0F 0C 00 00 0A 00 00 00
**Offensive Heal +6** 7C 00 00 00 10 0C 00 00 0A 00 00 00
**Offensive Heal +7** 7D 00 00 00 11 0C 00 00 0A 00 00 00
**Offensive Heal +8** 7E 00 00 00 12 0C 00 00 0A 00 00 00
**Deadly Heal** 7F 00 00 00 13 0C 00 00 0B 00 00 00
**Deadly Heal +1** 80 00 00 00 14 0C 00 00 0B 00 00 00
**Deadly Heal +2** 81 00 00 00 15 0C 00 00 0B 00 00 00
**Deadly Heal +3** 82 00 00 00 16 0C 00 00 0B 00 00 00
**Deadly Heal +4** 83 00 00 00 17 0C 00 00 0B 00 00 00
**Deadly Heal +5** 84 00 00 00 18 0C 00 00 0B 00 00 00
**Deadly Heal +6** 85 00 00 00 19 0C 00 00 0B 00 00 00
**Deadly Heal +7** 86 00 00 00 1A 0C 00 00 0B 00 00 00
**Deadly Heal +8** 87 00 00 00 1B 0C 00 00 0B 00 00 00
**Auto-Heal** 88 00 00 00 1C 0C 00 00 0C 00 00 00
**Auto-Heal +1** 89 00 00 00 1D 0C 00 00 0C 00 00 00
**Auto-Heal +2** 8A 00 00 00 1E 0C 00 00 0C 00 00 00
**Auto-Heal +3** 8B 00 00 00 1F 0C 00 00 0C 00 00 00
**Auto-Heal +4** 8C 00 00 00 20 0C 00 00 0C 00 00 00
**Auto-Heal +5** 8D 00 00 00 21 0C 00 00 0C 00 00 00
**Auto-Heal +6** 8E 00 00 00 22 0C 00 00 0C 00 00 00
**Auto-Heal +7** 8F 00 00 00 23 0C 00 00 0C 00 00 00
**Auto-Heal +8** 90 00 00 00 24 0C 00 00 0C 00 00 00
**Evade Range Up** AC 00 00 00 25 0C 00 00 0D 00 00 00
**Evade Range Up +1** AD 00 00 00 26 0C 00 00 0D 00 00 00
**Evade Range Up +2** AE 00 00 00 27 0C 00 00 0D 00 00 00
**Evade Range Up +3** AF 00 00 00 28 0C 00 00 0D 00 00 00
**Evade Range Up +4** B0 00 00 00 29 0C 00 00 0D 00 00 00
**Evade Range Up +5** B1 00 00 00 2A 0C 00 00 0D 00 00 00 
**Evade Range Up +6** B2 00 00 00 2B 0C 00 00 0D 00 00 00
**Evade Range Up +7** B3 00 00 00 2C 0C 00 00 0D 00 00 00
**Evade Range Up +8** B4 00 00 00 2D 0C 00 00 0D 00 00 00
**Moving Speed Up** B5 00 00 00 2E 0C 00 00 0E 00 00 00
**Moving Speed Up +1** B6 00 00 00 2F 0C 00 00 0E 00 00 00
**Moving Speed Up +2** B7 00 00 00 30 0C 00 00 0E 00 00 00
**Moving Speed Up +3** B8 00 00 00 31 0C 00 00 0E 00 00 00
**Moving Speed Up +4** B9 00 00 00 32 0C 00 00 0E 00 00 00
**Moving Speed Up +5** BA 00 00 00 33 0C 00 00 0E 00 00 00
**Moving Speed Up +6** BB 00 00 00 34 0C 00 00 0E 00 00 00
**Moving Speed Up +7** BC 00 00 00 35 0C 00 00 0E 00 00 00
**Moving Speed Up +8** BD 00 00 00 36 0C 00 00 0E 00 00 00
**Drop Rate Up** BE 00 00 00 37 0C 00 00 0F 00 00 00
**Drop Rate Up +1** BF 00 00 00 38 0C 00 00 0F 00 00 00
**Drop Rate Up +2** C0 00 00 00 39 0C 00 00 0F 00 00 00
**Drop Rate Up +3** C1 00 00 00 3A 0C 00 00 0F 00 00 00
**Drop Rate Up +4** C2 00 00 00 3B 0C 00 00 0F 00 00 00
**Drop Rate Up +5** C3 00 00 00 3C 0C 00 00 0F 00 00 00
**Drop Rate Up +6** C4 00 00 00 3D 0C 00 00 0F 00 00 00
**Drop Rate Up +7** C5 00 00 00 3E 0C 00 00 0F 00 00 00
**Drop Rate Up +8** C6 00 00 00 3F 0C 00 00 0F 00 00 00
**EXP Gain Up** C7 00 00 00 40 0C 00 00 10 00 00 00
**EXP Gain Up +1** C8 00 00 00 41 0C 00 00 10 00 00 00
**EXP Gain Up +2** C9 00 00 00 42 0C 00 00 10 00 00 00
**EXP Gain Up +3** CA 00 00 00 43 0C 00 00 10 00 00 00
**EXP Gain Up +4** CB 00 00 00 44 0C 00 00 10 00 00 00
**EXP Gain Up +5** CC 00 00 00 45 0C 00 00 10 00 00 00
**EXP Gain Up +6** CD 00 00 00 46 0C 00 00 10 00 00 00
**EXP Gain Up +7** CE 00 00 00 47 0C 00 00 10 00 00 00
**EXP Gain Up +8** CF 00 00 00 48 0C 00 00 10 00 00 00
**Shock Wave** 24 00 00 00 49 0C 00 00 11 00 00 00
**Shock Wave +1** 25 00 00 00 4A 0C 00 00 11 00 00 00
**Shock Wave +2** 26 00 00 00 4B 0C 00 00 11 00 00 00
**Shock Wave +3** 27 00 00 00 4C 0C 00 00 11 00 00 00
**Shock Wave +4** 28 00 00 00 4D 0C 00 00 11 00 00 00
**Shock Wave +5** 29 00 00 00 4E 0C 00 00 11 00 00 00
**Shock Wave +6** 2A 00 00 00 4F 0C 00 00 11 00 00 00
**Shock Wave +7** 2B 00 00 00 50 0C 00 00 11 00 00 00
**Shock Wave +8** 2C 00 00 00 51 0C 00 00 11 00 00 00
**Last Stand** 2D 00 00 00 52 0C 00 00 12 00 00 00
**Last Stand +1** 2E 00 00 00 53 0C 00 00 12 00 00 00
**Last Stand +2** 2F 00 00 00 54 0C 00 00 12 00 00 00
**Last Stand +3** 30 00 00 00 55 0C 00 00 12 00 00 00
**Last Stand +4** 31 00 00 00 56 0C 00 00 12 00 00 00
**Last Stand +5** 32 00 00 00 57 0C 00 00 12 00 00 00
**Last Stand +6** 33 00 00 00 58 0C 00 00 12 00 00 00
**Last Stand +7** 34 00 00 00 59 0C 00 00 12 00 00 00
**Last Stand +8** 35 00 00 00 5A 0C 00 00 12 00 00 00
**Damage Absorb** 91 00 00 00 5B 0C 00 00 13 00 00 00
**Damage Absorb +1** 92 00 00 00 5C 0C 00 00 13 00 00 00
**Damage Absorb +2** 93 00 00 00 5D 0C 00 00 13 00 00 00
**Damage Absorb +3** 94 00 00 00 5E 0C 00 00 13 00 00 00
**Damage Absorb +4** 95 00 00 00 5F 0C 00 00 13 00 00 00
**Damage Absorb +5** 96 00 00 00 60 0C 00 00 13 00 00 00
**Damage Absorb +6** 97 00 00 00 61 0C 00 00 13 00 00 00
**Damage Absorb +7** 98 00 00 00 62 0C 00 00 13 00 00 00
**Damage Absorb +8** 99 00 00 00 63 0C 00 00 13 00 00 00
**Vengeance** D0 00 00 00 64 0C 00 00 14 00 00 00
**Vengeance +1** D1 00 00 00 65 0C 00 00 14 00 00 00
**Vengeance +2** D2 00 00 00 66 0C 00 00 14 00 00 00
**Vengeance +3** D3 00 00 00 67 0C 00 00 14 00 00 00
**Vengeance +4** D4 00 00 00 68 0C 00 00 14 00 00 00
**Vengeance +5** D5 00 00 00 69 0C 00 00 14 00 00 00
**Vengeance +6** D6 00 00 00 6A 0C 00 00 14 00 00 00
**Vengeance +7** D7 00 00 00 6B 0C 00 00 14 00 00 00
**Vengeance +8** D8 00 00 00 6C 0C 00 00 14 00 00 00
**Reset** 9A 00 00 00 6D 0C 00 00 15 00 00 00
**Reset +1** 9B 00 00 00 6E 0C 00 00 15 00 00 00
**Reset +2** 9C 00 00 00 6F 0C 00 00 15 00 00 00
**Reset +3** 9D 00 00 00 70 0C 00 00 15 00 00 00
**Reset +4** 9E 00 00 00 71 0C 00 00 15 00 00 00
**Reset +5** 9F 00 00 00 72 0C 00 00 15 00 00 00
**Reset +6** A0 00 00 00 73 0C 00 00 15 00 00 00
**Reset +7** A1 00 00 00 74 0C 00 00 15 00 00 00
**Reset +8** A2 00 00 00 75 0C 00 00 15 00 00 00
**Overclock** D9 00 00 00 76 0C 00 00 16 00 00 00
**Overclock +1** DA 00 00 00 77 0C 00 00 16 00 00 00
**Overclock +2** DB 00 00 00 78 0C 00 00 16 00 00 00
**Overclock +3** DC 00 00 00 79 0C 00 00 16 00 00 00
**Overclock +4** DD 00 00 00 7A 0C 00 00 16 00 00 00
**Overclock +5** DE 00 00 00 7B 0C 00 00 16 00 00 00
**Overclock +6** DF 00 00 00 7C 0C 00 00 16 00 00 00
**Overclock +7** E0 00 00 00 7D 0C 00 00 16 00 00 00
**Overclock +8** E1 00 00 00 7E 0C 00 00 16 00 00 00
**Resilience** 64 00 00 00 7F 0C 00 00 17 00 00 00
**Resilience +1** 65 00 00 00 80 0C 00 00 17 00 00 00
**Resilience +2** 66 00 00 00 81 0C 00 00 17 00 00 00
**Resilience +3** 67 00 00 00 82 0C 00 00 17 00 00 00
**Resilience +4** 68 00 00 00 83 0C 00 00 17 00 00 00
**Resilience +5** 69 00 00 00 84 0C 00 00 17 00 00 00
**Resilience +6** 6A 00 00 00 85 0C 00 00 17 00 00 00
**Resilience +7** 6B 00 00 00 86 0C 00 00 17 00 00 00
**Resilience +8** 6C 00 00 00 87 0C 00 00 17 00 00 00

**Counter** 36 00 00 00 91 0C 00 00 18 00 00 00
**Counter +1** 37 00 00 00 92 0C 00 00 18 00 00 00
**Counter +2** 38 00 00 00 93 0C 00 00 18 00 00 00
**Counter +3** 39 00 00 00 94 0C 00 00 18 00 00 00
**Counter +4** 3A 00 00 00 95 0C 00 00 18 00 00 00
**Counter +5** 3B 00 00 00 96 0C 00 00 18 00 00 00
**Counter +6** 3C 00 00 00 97 0C 00 00 18 00 00 00
**Counter +7** 3D 00 00 00 98 0C 00 00 18 00 00 00
**Counter +8** 3E 00 00 00 99 0C 00 00 18 00 00 00
**Taunt Up** E2 00 00 00 9A 0C 00 00 19 00 00 00
**Taunt Up +1** E3 00 00 00 9B 0C 00 00 19 00 00 00
**Taunt Up +2** E4 00 00 00 9C 0C 00 00 19 00 00 00
**Taunt Up +2** E5 00 00 00 9D 0C 00 00 19 00 00 00
**Taunt Up +2** E6 00 00 00 9E 0C 00 00 19 00 00 00
**Taunt Up +2** E7 00 00 00 9F 0C 00 00 19 00 00 00
**Taunt Up +2** E8 00 00 00 A0 0C 00 00 19 00 00 00
**Taunt Up +2** E9 00 00 00 A1 0C 00 00 19 00 00 00
**Taunt Up +2** EA 00 00 00 A2 0C 00 00 19 00 00 00
**Charge Attack** 3F 00 00 00 A3 0C 00 00 1A 00 00 00
**Charge Attack +1** 40 00 00 00 A4 0C 00 00 1A 00 00 00
**Charge Attack +2** 41 00 00 00 A5 0C 00 00 1A 00 00 00
**Charge Attack +3** 42 00 00 00 A6 0C 00 00 1A 00 00 00
**Charge Attack +4** 43 00 00 00 A7 0C 00 00 1A 00 00 00
**Charge Attack +5** 44 00 00 00 A8 0C 00 00 1A 00 00 00
**Charge Attack +6** 45 00 00 00 A9 0C 00 00 1A 00 00 00
**Charge Attack +7** 46 00 00 00 AA 0C 00 00 1A 00 00 00
**Charge Attack +8** 47 00 00 00 AB 0C 00 00 1A 00 00 00
**Auto-use Item** EB 00 00 00 AC 0C 00 00 1B 00 00 00
**Auto-use Item +1** EC 00 00 00 AD 0C 00 00 1B 00 00 00
**Auto-use Item +2** ED 00 00 00 AE 0C 00 00 1B 00 00 00
**Auto-use Item +3** EE 00 00 00 AF 0C 00 00 1B 00 00 00
**Auto-use Item +4** EF 00 00 00 B0 0C 00 00 1B 00 00 00
**Auto-use Item +5** F0 00 00 00 B1 0C 00 00 1B 00 00 00
**Auto-use Item +6** F1 00 00 00 B2 0C 00 00 1B 00 00 00
**Auto-use Item +7** F2 00 00 00 B3 0C 00 00 1B 00 00 00
**Auto-use Item +8** F3 00 00 00 B4 0C 00 00 1B 00 00 00

**Hijack Boost** FD 00 00 00 BE 0C 00 00 1D 00 00 00
**Hijack Boost +1** FE 00 00 00 BF 0C 00 00 1D 00 00 00
**Hijack Boost +2** FF 00 00 00 C0 0C 00 00 1D 00 00 00
**Hijack Boost +3** 00 01 00 00 C1 0C 00 00 1D 00 00 00
**Hijack Boost +4** 01 01 00 00 C2 0C 00 00 1D 00 00 00
**Hijack Boost +5** 02 01 00 00 C3 0C 00 00 1D 00 00 00
**Hijack Boost +6** 03 01 00 00 C4 0C 00 00 1D 00 00 00
**Hijack Boost +7** 04 01 00 00 C5 0C 00 00 1D 00 00 00
**Hijack Boost +8** 05 01 00 00 C6 0C 00 00 1D 00 00 00
**Stun** 06 01 00 00 D9 0C 00 00 1E 00 00 00
**Stun +1** 07 01 00 00 DA 0C 00 00 1E 00 00 00
**Stun +2** 08 01 00 00 DB 0C 00 00 1E 00 00 00
**Stun +3** 09 01 00 00 DC 0C 00 00 1E 00 00 00
**Stun +4** 0A 01 00 00 DD 0C 00 00 1E 00 00 00
**Stun +5** 0B 01 00 00 DE 0C 00 00 1E 00 00 00
**Stun +6** 0C 01 00 00 DF 0C 00 00 1E 00 00 00
**Stun +7** 0D 01 00 00 E0 0C 00 00 1E 00 00 00
**Stun +8** 0E 01 00 00 E1 0C 00 00 1E 00 00 00
**Combust** 0F 01 00 00 E2 0C 00 00 1F 00 00 00
**Combust +1** 10 01 00 00 E3 0C 00 00 1F 00 00 00
**Combust +2** 11 01 00 00 E4 0C 00 00 1F 00 00 00
**Combust +3** 12 01 00 00 E5 0C 00 00 1F 00 00 00
**Combust +4** 13 01 00 00 E6 0C 00 00 1F 00 00 00
**Combust +5** 14 01 00 00 E7 0C 00 00 1F 00 00 00
**Combust +6** 15 01 00 00 E8 0C 00 00 1F 00 00 00
**Combust +7** 16 01 00 00 E9 0C 00 00 1F 00 00 00
**Combust +8** 17 01 00 00 EA 0C 00 00 1F 00 00 00

**Heal Drops Up** 18 01 00 00 FD 0C 00 00 22 00 00 00
**Heal Drops Up +1** 19 01 00 00 FE 0C 00 00 22 00 00 00
**Heal Drops Up +2** 1A 01 00 00 FF 0C 00 00 22 00 00 00
**Heal Drops Up +3** 1B 01 00 00 00 0D 00 00 22 00 00 00
**Heal Drops Up +4** 1C 01 00 00 01 0D 00 00 22 00 00 00
**Heal Drops Up +5** 1D 01 00 00 02 0D 00 00 22 00 00 00
**Heal Drops Up +6** 1E 01 00 00 03 0D 00 00 22 00 00 00
**Heal Drops Up +7** 1F 01 00 00 04 0D 00 00 22 00 00 00
**Heal Drops Up +8** 20 01 00 00 05 0D 00 00 22 00 00 00
**Item Scan** F5 00 00 00 88 0C 00 00 23 00 00 00 00 00 00 00 06 00 00 00
**Death Rattle** 21 01 00 00 06 0D 00 00 26 00 00 00 00 00 00 00 06 00 00 00
**HUD: HP Gauge** 23 01 00 00 07 0D 00 00 27 00 00 00 00 00 00 00 02 00 00 00
**HUD: Sound Waves** 2D 01 00 00 08 0D 00 00 28 00 00 00 00 00 00 00 03 00 00 00
**HUD: Enemy Data** 26 01 00 00 09 0D 00 00 29 00 00 00 00 00 00 00 02 00 00 00
**OS Chip** 22 01 00 00 0A 0D 00 00 2A 00 00 00 00 00 00 00 02 00 00 00
**Evasive System** F6 00 00 00 0B 0D 00 00 2C 00 00 00 00 00 00 00 06 00 00 00
**Continuous Combo** 48 00 00 00 0C 0D 00 00 2D 00 00 00 00 00 00 00 06 00 00 00
**Bullet Detonation** F7 00 00 00 0D 0D 00 00 2E 00 00 00 00 00 00 00 06 00 00 00
**Auto-collect Items** F4 00 00 00 0E 0D 00 00 2F 00 00 00 00 00 00 00 06 00 00 00
**HUD: Skill Gauge** 25 01 00 00 0F 0D 00 00 30 00 00 00 00 00 00 00 02 00 00 00
**HUD: Text Log** 29 01 00 00 10 0D 00 00 31 00 00 00 00 00 00 00 02 00 00 00
**HUD: Mini-map** 27 01 00 00 11 0D 00 00 32 00 00 00 00 00 00 00 02 00 00 00
**HUD: EXP Gauge** 24 01 00 00 12 0D 00 00 33 00 00 00 00 00 00 00 01 00 00 00
**HUD: Save Points** 2A 01 00 00 13 0D 00 00 34 00 00 00 00 00 00 00 01 00 00 00
**HUD: Damage Values** 2C 01 00 00 14 0D 00 00 35 00 00 00 00 00 00 00 03 00 00 00
**HUD: Objectives** 28 01 00 00 15 0D 00 00 36 00 00 00 00 00 00 00 01 00 00 00
**HUD: Control** 2E 01 00 00 16 0D 00 00 37 00 00 00 00 00 00 00 03 00 00 00
**HUD: Fishing Spots** 2B 01 00 00 19 0D 00 00 3A 00 00 00 00 00 00 00 03 00 00 00
**Auto-Attack** F8 00 00 00 1A 0D 00 00 3B 00 00 00 00 00 00 00 01 00 00 00
**Auto-Fire** F9 00 00 00 1B 0D 00 00 3C 00 00 00 00 00 00 00 01 00 00 00
**Auto-Evade** FA 00 00 00 1C 0D 00 00 3D 00 00 00 00 00 00 00 01 00 00 00
**Auto-Program** FB 00 00 00 1D 0D 00 00 3E 00 00 00 00 00 00 00 01 00 00 00
**Auto-Weapon Switch** FC 00 00 00 1E 0D 00 00 3F 00 00 00 00 00 00 00 01 00 00 00




## Weapons
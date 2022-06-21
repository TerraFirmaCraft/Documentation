---
layout: page
title: "World Generation"
permalink: /1.18.x/worldgen/
---

# World Generation

Note: this documentation will assume a working knowledge of how both data packs, and custom world generation works in vanilla Minecraft. If you are unfamiliar with those topics, the wiki provides a good starting point to learn about [Data Packs](https://minecraft.gamepedia.com/Data_Pack), [Custom World Generation](https://minecraft.gamepedia.com/Custom_world_generation), and [Custom Dimensions](https://minecraft.gamepedia.com/Custom_dimension).

TFC exposes the "TFC World Generation" `level-type` (for servers), and preset (for clients). When you create a new world using this generation, it creates a default chunk generator and biome source. In order to modify these, you will need to override the overworld dimension (`data/minecraft/dimension/overworld.json`), and use the TFC chunk generator and biome source. More information can be found in the [dimension](dimension/) article.

All other world generation, including biomes, configured features, decorators, carvers, and surface builders can be customized to various extents by replacing the specific files.

Finally, **all** of TFC's world generation is already done using JSON, and every existing file can be found in the [world generation folder](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.18.x/src/main/resources/data/tfc/worldgen) in the TFC repository.

### Sections

- [Dimension](dimension/)
- [Biomes](biomes/)
- [Configured Features](features/)
- [Decorators](decorators/)
- [Configured Carvers](carvers/)
- [Common Types](common-types/)
- [WorldGen Tags](tags/)

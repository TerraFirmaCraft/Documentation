---
layout: page
title: "World Generation"
permalink: /1.16.x/worldgen/
---

# World Generation

Note: this documentation will assume a working knowledge of how both data packs, and custom world generation works in vanilla Minecraft. If you are unfamiliar with those topics, the wiki provides a good starting point to learn about [Data Packs](https://minecraft.gamepedia.com/Data_Pack), [Custom World Generation](https://minecraft.gamepedia.com/Custom_world_generation), and [Custom Dimensions](https://minecraft.gamepedia.com/Custom_dimension).

TFC exposes the "TFC World Generation" `level-type` (for servers), and preset (for clients). When you create a new world using this generation, it creates a default `chunk generator`, and `biome source`. These are **not modifiable** when using the TFC presets as that's what they are - presets.

If you wish to customize these elements, you will need to generate a new world using a customized `chunk generator` and/or `biome source`. For all other customizations, using the TFC presets, you can customize each of TFC's `biome`, `configured_feature`, `configured_carver`, and/or `configured_surface_builder`.

Finally, **all** of TFC's world generation is already done using JSON, and every existing file can be found in the [world generation folder](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.16.x/src/main/resources/data/tfc/worldgen) in the TFC repository.

### Sections

- [Chunk Generator](chunk-generator/)
- [Biome Source](biome-source/)
- [Biomes](biomes/)
- [Configured Features](features/)
  - [Decorators](decorators/)
- [Configured Carvers](carvers/)
- [Configured Surface Builders](surface-builders/)

---
layout: page
title: "Configured Surface Builders"
permalink: /1.18.x/worldgen/surface-builders/
---

# Configured Surface Builders

*[Vanilla Reference for Surface Builders](https://minecraft.gamepedia.com/Custom_world_generation#Surface_builders)*

TFC uses several custom surface builders, most of which have no configuration options. In addition, these surface builder cannot be used outside a TFC enabled chunk generator, as they need data such as climate and rock types which are not given from vanilla chunk generators.

TFC adds the following surface builder types:

- [Normal](#normal)
- [Badlands](#badlands)
- [Mountains](#mountains)
- [Shore](#shore)
- [Icebergs](#icebergs)
- [With Volcanoes](#with-volcanoes)

### Normal

This is the standard TFC surface builder. It places TFC surface material, including dirt, sand, grass, and gravel. Its surface depth is adjusted based on the slope (erosion) of the generated area.

- Type: `tfc:normal`
- Config: None


### Badlands

This surface builder will do different things above and below a specific y value (between 110 and 114, that varies by location). Beneath this cutoff, this surface builder will place one layer of TFC Red and Brown sand in an alternating pattern - similar to vanilla badlands. Above this layer, it will function as the TFC normal surface builder.

- Type: `tfc:thin`
- Config: None

### Mountains

This surface builder acts as a normal surface builder, but will also place patches of gravel, stone, and cobblestone.

- Type: `tfc:mountains`
- Config: None

### Shore

This is used to build TFC's shore biomes. It creates sand and gravel patches, which may later get replaced with different sand colors. Shores in tropical areas (Rainfall > 300 and Average temperature > 15) may have pink sand, other high rainfall areas (Rainfall > 300) may have black sand.

- Type: `tfc:shore`
- Config: None

### Icebergs

This is a hybrid of the vanilla `frozen_ocean` surface builder and TFC's `tfc:normal` surface builder.

- Type: `tfc:icebergs`
- Config: None

### With Volcanoes

This is a special type of surface builder used in volcanic regions. It places volcanic basalt near volcanoes, and delegates to the parent surface builder in all other situations.

- Type: `tfc:with_volcanoes`
- Config:
  - `parent`: A string, which is the name of a configured surface builder to use when there is no volcano at a given location.

Example:

```json
{
    "type": "tfc:with_volcanoes",
    "config": {
        "parent": "tfc:mountains"
    }
}
```

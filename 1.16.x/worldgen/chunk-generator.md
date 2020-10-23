---
layout: page
title: "Chunk Generator"
permalink: /1.16.x/worldgen/chunk-generator/
---

# Chunk Generator

TFC has one chunk generator which is used for the overworld.

#### TFC Overworld

Type: `tfc:overworld`

Configuration:

- `biome_source` is a [Biome Source](../biome-source/). It is a required field.
  - In addition to being a valid biome source, the included biome source **must** extend `TFCBiomeProvider`. In TFC, this restricts the choice of biome source to `tfc:overworld`.
- `settings` is a [Noise Settings](https://minecraft.gamepedia.com/Custom_world_generation#Noise_settings)
  - Almost everything here is unused by TFC, with the exception of the `default_block` and `default_fluid` fields. However, changing these may have major consequences on other stages of world generation!
- `flat_bedrock` is a `boolean`. If true, the bedrock layer at the bottom of the world will be only one tall. If false, it will be varied similar to vanilla bedrock.
- `seed` is a `integer`. It is the seed used for the chunk generator. This is replaced by a seed specified in the create world screen or `server.properties` file.

Example:

```json
{
    "type": "tfc:overworld",
    "settings": "minecraft:overworld",
    "biome_source": "tfc:overworld",
    "flat_bedrock": false,
    "seed": 1234
}
```


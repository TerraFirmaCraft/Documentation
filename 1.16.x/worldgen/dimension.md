---
layout: page
title: "Dimension"
permalink: /1.16.x/worldgen/dimension/
---

In order to modify the `TerraFirmaCraft` world preset, it is nessecary to override the vanilla overworld dimension (`data/minecraft/dimension/overworld.json`). The format of a dimension can be found [here](https://minecraft.fandom.com/wiki/Custom_dimension#Dimension_syntax). Included here is [an example](#example) of an override for the vanilla overworld, with TFC properties set to defaults.

Configuration:

- `type` is the namespaced ID of the [dimension type](https://minecraft.fandom.com/wiki/Custom_dimension#Dimension_type). The default is `minecraft:overworld`.
- `generator` is an object:
    - `type` is the namespaced ID of the chunk generator. It must be `tfc:overworld`.
    - `seed` is a `long`. It is the seed of the world. (This will be overriden by a seed in the world creation screen, or `server.properties` if not present.)
    - `noise_settings` is the [noise settings](https://minecraft.fandom.com/wiki/Custom_world_generation#Noise_settings) used in the chunk generator. The default is `minecraft:overworld`.
    - `flat_bedrock` is a `boolean`. It controls if the bottom layer of bedrock in the world is flat.
    - `biome_source` is an object:
        - `type` is the namespaced ID of the biome source. It must be `tfc:overworld`.
        - `seed` is a `long`. It is the seed used for the biome source. (This will be overriden by a seed in the world creation screen, or `server.properties` if not present.)
        - `spawn_distance` is an integer. It is the farthest distance away from the spawn center location the player is allowed to spawn.
        - `spawn_center_x` is an integer. It is the center x position that the player tries to spawn at.
        - `spawn_center_z` is an integer. It is the center z position that the player tries to spawn at.
        - `rock_layer_settings` is an object. It is a [rock layer settings](#rock-layer-settings).
        - `climate_settings` is an object. It is a [climate settings](#climate-settings).

#### Rock Layer Settings

This is an object representing the rocks, and layers, which spawn in the world. Each rock defines a series of blocks, which are used during world generation. These need not be TFC blocks, or even TFC-like blocks. They also need not be different.

Configuration:

- `rock_layer_scale` is an integer. It represents a multiplier of how far apart rock layers are. It must be a power of two.
- `rocks` is an array of objects:
    - `id` is the namespaced ID of the rock.
    - `raw` is the block ID of the rock's raw block.
    - `hardened` is the block ID of the rock's hardened block.
    - `gravel` is the block ID of the rock's gravel block.
    - `cobble` is the block ID of the rock's cobblestone block.
    - `sand` is the block ID of the rock's sand block.
    - `sandstone` is the block ID of the rock's sandstone block.
    - `spike` is an optional block ID of the rock's spike block. This must be a TFC-like rock spike block.
    - `loose` is an optional block ID of the rock's loose rock block. This must be a TFC-like loose rock block.
    - `top_layer` is a boolean. If true, this rock will generate in the top rock layer.
    - `middle_layer` is a boolean. If true, this rock will generate in the middle rock layer.
    - `bottom_layer` is a boolean. If true, this rock will generate in the bottom rock layer.

#### Climate Settings

This is an object which represents how different biomes are placed, according to climate parameters. TFC places additional climate variant biomes for modder and pack maker convienience, allowing biome dictionary and other tools to be used which expect biomes to define a particular climate. This just controls how TFC assigns climate parameters (rainfall, and temperature) to biomes.

In TFC, an average annual temperature value may range from -20 C to 25 C. An average annual rainfall value may range from 0 mm to 500 mm.

Configuration:

- `frozen_cold_cutoff` is a float. It represents the cutoff between frozen and cold temperature biomes.
- `cold_normal_cutoff` is a float. It represents the cutoff between cold and normal temperature biomes.
- `normal_lukewarm_cutoff` is a float. It represents the cutoff between normal and lukewarm temperature biomes.
- `lukewarm_warm_cutoff` is a float. It represents the cutoff between lukewarm and warm temperature biomes.
- `arid_dry_cutoff` is a float. It represents the cutoff between arid and dry rainfall biomes.
- `dry_normal_cutoff` is a float. It represents the cutoff between dry and normal rainfall biomes.
- `normal_damp_cutoff` is a float. It represents the cutoff between normal and damp rainfall biomes.
- `damp_wet_cutoff` is a float. It represents the cutoff between damp and wet rainfall biomes.


### Example

This is an example `overworld.json` override, with almost all properties set to the exact same as TFC. (The one exception is the `rocks` field, of which only one rock has been included here.)

File: `data/minecraft/dimension/overworld.json`
```json
{
  "type": "minecraft:overworld",
  "generator": {
    "type": "tfc:overworld",
    "noise_settings": "minecraft:overworld",
    "flat_bedrock": false,
    "biome_source": {
      "type": "tfc:overworld",
      "spawn_distance": 8000,
      "spawn_center_x": 0,
      "spawn_center_z": 0,
      "rock_layer_settings": {
        "rock_layer_scale": 128,
        "rocks": [
          {
            "id": "basalt",
            "raw": "tfc:rock/raw/basalt",
            "hardened": "tfc:rock/hardened/basalt",
            "gravel": "tfc:rock/gravel/basalt",
            "cobble": "tfc:rock/cobble/basalt",
            "sand": "tfc:sand/red",
            "sandstone": "tfc:raw_sandstone/red",
            "top_layer": true,
            "middle_layer": true,
            "bottom_layer": false
          }
        ]
      },
      "climate_settings": {
        "frozen_cold_cutoff": -17.25,
        "cold_normal_cutoff": -3.75,
        "normal_lukewarm_cutoff": 9.75,
        "lukewarm_warm_cutoff": 23.25,
        "arid_dry_cutoff": 125,
        "dry_normal_cutoff": 200,
        "normal_damp_cutoff": 300,
        "damp_wet_cutoff": 375
      }
    }
  }
}
```
---
layout: page
title: "Biome Source"
permalink: /1.16.x/worldgen/biome-source/
---

# Biome Source

TFC has one biome source which is used for the overworld. Using this biome source will generate biomes using a plate tectonics based layer generation method, and will use TFC's biomes for the world.

### TFC Overworld

Type: `tfc:overworld`

Configuration:

- `seed` is an integer. It is the seed used for the biome source.
- `spawn_distance` is an optional integer (Default: `8000`). It represents the maximum (Manhattan) distance from (0, 0), that the player spawn location will be placed.
- `ocean_percent` is an optional integer in the range `[0, 100]` (Default: `45`). It represents the percentage of biome area (as placed during initial plate tectonic seeding) that will be considered ocean.
- `rock_layer_scale` is an optional positive integer (Default: `7`). It controls the size of the rock layers. Increasing this value by one will double the size of the rock layers, and vice versa.

The following options are all climate related options. Each of these represents the cut off point between two different biome classifications.

TFC biomes are split into five temperature categories (Frozen, Cold, Normal, Lukewarm, and Warm), and five rainfall categories (Arid, Dry, Normal, Damp, Wet). These are vary rarely used within TFC (as in most cases, TFC queries the actual rainfall and temperature at the location). However, these are split into different biomes for the purposes of other mods, which may want to recognize specific biomes by climate.

Each of these is a cut off between either a temperature value or a rainfall value. They are all optional float values. The default values are provided below:

- `frozen_cold_cutoff`, Default -17.25
- `cold_normal_cutoff`, Default -3.75
- `normal_lukewarm_cutoff`, Default 9.75
- `lukewarm_warm_cutoff`, Default 23.25
- `arid_dry_cutoff`, Default 125
- `dry_normal_cutoff`, Default 200
- `normal_damp_cutoff`, Default 300
- `damp_wet_cutoff`, Default 375

Example:

```json
{
    "type": "tfc:overworld",
    "seed": 1234,
    "spawn_distance": 8000,
    "rock_layer_scale": 7,
    "frozen_cold_cutoff": -17.25,
    "cold_normal_cutoff": -3.75,
    "normal_lukewarm_cutoff": 9.75,
    "lukewarm_warm_cutoff": 23.25,
    "arid_dry_cutoff": 125,
    "dry_normal_cutoff": 200,
    "normal_damp_cutoff": 300,
    "damp_wet_cutoff": 375
}
```

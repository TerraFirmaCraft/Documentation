---
layout: page
title: "Decorators"
permalink: /1.18.x/worldgen/decorators/
---

# Decorators

*[Vanilla Reference for Placement Modifiers / Decorators](https://minecraft.fandom.com/wiki/Placed_feature)*

Note that historically, Placement Modifiers / Placed Features were called Decorators, and TFC still refers to the two interchangeably. TFC adds the following placement modifier types, for use in placed features:

<!--linky_begin_sort_alphabetical-->

- [Biome](#biome)
- [Carving Mask](#carving-mask)
- [Climate](#climate)
- [Flat Enough](#flat-enough)
- [Near Water](#near-water)
- [On Top](#on-top)
- [Shallow Water](#shallow-water)
- [Underground](#underground)
- [Volcano](#volcano)

<!--linky_end_sort_alphabetical-->

### Biome

This is an extension of the vanilla `minecraft:biome_filter` decorator, but which respects the way TFC features are used in biomes (via tags). This exists to fix an unfortunate bug in [Forge](https://github.com/MinecraftForge/MinecraftForge/issues/8743) in 1.18.

- Type: `tfc:biome`

### Carving Mask

This is an extension of the vanilla carving mask decorator, but with additional constraints on y level. It is used for large spikes to restrict them to a maximum y level.

- Type: `tfc:carving_mask`
- Config:
  - `min_y`: An optional [Vertical Anchor](../common-types/#vertical-anchor), the minimum allowed y value for this to spawn at.
  - `max_y`: An optional [Vertical Anchor](../common-types/#vertical-anchor), the maximum allowed y value for this to spawn at.
  - `probability`: A float in the range `[0, 1]`, the probability this will spawn at any given position.
  - `step`: The carving stage to use. Must be either `air` or `liquid`.

### Climate

This decorator will conditionally place a feature based on specific climate properties. All config values are optional, and if omitted will allow all positions. This is used in clay deposits to restrict them based on minimum rainfall.

The typical range for yearly average temperatures is -25 to +30 C. Rainfall values can vary between 0 mm and 500 mm.

- Type: `tfc:climate`
- Config:
  - `min_temperature` is an optional float representing the minimum allowed average yearly temperature.
  - `max_temperature` is an optional float representing the maximum allowed average yearly temperature.
  - `min_rainfall` is an optional float representing the minimum allowed rainfall.
  - `max_rainfall` is an optional float representing the maximum allowed rainfall.
  - `min_forest` is an optional [Forest Type](../common-types/#forest-type) representing the minimum required forest density.
  - `max_forest` is an optional [Forest Type](../common-types/#forest-type) representing the maximum required forest density.
  - `fuzzy` is an optional boolean (Default: `false`). If true, the temperature and rainfall requirements will be probabilistic relative to the center point, with maximum density at the exact center, and zero density at the edges.


### Flat Enough

This decorator will check an area around the initial position for solid blocks. If it's not found, it will attempt to move lower down, until the max depth is reached (and then the position is thrown out), or enough solid blocks are found. This is used by TFC's boulders feature, and is why they can be set into the ground.

- Type: `tfc:flat_enough`
- Config:
  - `flatness` is an optional float (Default: `0.5`), in the range `[0, 1]`. It describes the how many solid blocks, as a percentage the surrounding area must contain.
  - `radius` is an optional positive integer (Default: `2`), which is the radius around the initial position that the area is checked for solid blocks.
  - `max_depth` is an optional positive integer (Default: `4`), which is how deep from the original position the decorator should try and search.

### Near Water

This decorator will conditionally place a feature if there is water within a `radius` in the x and z directions, and within `[-radius, 0]` in the y direction. Water is checked against the fluid tag `minecraft:water`. It is used to create near-water clay deposits.

- Type: `tfc:near_water`
- Config:
  - `radius`: An integer representing the distance to search for water.

### On Top

This decorator checks the block below for a predicate, and passes if that predicate passes.

- Type: `tfc:on_top`
- Config:
  - `predicate`: A vanilla Block Predicate.

### Shallow Water

This decorator checks that the water is not too deep at a location.

- Type: `tfc:shallow_water`
- Config:
  - `max_depth`: An optional integer (Default: `5`), specifying the max depth of the water.

### Underground

This decorator passes if the position is below the world surface level.

- Type: `tfc:underground`
- Config: None

### Volcano

This decorator places things near, or at, volcanoes.

- Type: `tfc:volcano`
- Config:
  - `center`: A boolean. If `true`, this decorator will ignore the `distance` argument and place the feature at the exact center of any volcanoes.
  - `distance`: A float in the range `[0, 1]`, representing the distance from the center of a volcano that this position must be in order to generate. 1 is the maximum radius of the volcano.

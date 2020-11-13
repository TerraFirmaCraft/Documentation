---
layout: page
title: "Decorators"
permalink: /1.16.x/worldgen/decorators/
---

# Decorators

*[Vanilla Reference for Decorators](https://minecraft.gamepedia.com/Custom_world_generation#Decorators)*

TFC adds the following decorators, for use in the `minecraft:decorated` configured feature:

- [Flat Enough](#flat-enough)
- [Climate](#climate)
- [Near Water](#near-water)
- [Bounded Carving Mask](#bounded-carving-mask)

### Flat Enough

This decorator will check an area around the initial position for solid blocks. If it's not found, it will attempt to move lower down, until the max depth is reached (and then the position is thrown out), or enough solid blocks are found. This is used by TFC's boulders feature, and is why they can be set into the ground.

- Type: `tfc:flat_enough`
- Config:
  - `flatness` is an optional float (Default: `0.5`), in the range `[0, 1]`. It describes the how many solid blocks, as a percentage the surrounding area must contain.
  - `radius` is an optional positive integer (Default: `2`), which is the radius around the initial position that the area is checked for solid blocks.
  - `max_depth` is an optional positive integer (Default: `4`), which is how deep from the original position the decorator should try and search.

### Climate

This decorator will conditionally place a feature based on specific climate properties. All config values are optional, and if omitted will allow all positions. This is used in clay deposits to restrict them based on minimum rainfall.

The typical range for yearly average temperatures is -25 to +30 C. Rainfall values can vary between 0 mm and 500 mm.

- Type: `tfc:climate`
- Config:
  - `min_temperature` is an optional float representing the minimum allowed average yearly temperature.
  - `max_temperature` is an optional float representing the maximum allowed average yearly temperature.
  - `min_rainfall` is an optional float representing the minimum allowed rainfall.
  - `max_rainfall` is an optional float representing the maximum allowed rainfall.

### Near Water

This decorator will conditionally place a feature if there is water within a `radius` in the x and z directions, and within `[-radius, 0]` in the y direction. Water is checked against the fluid tag `minecraft:water`. It is used to create near-water clay deposits.

- Type: `tfc:near_water`
- Config:
  - `radius`: An integer representing the distance to search for water.

### Bounded Carving Mask

This is an extension of the vanilla carving mask decorator, but with additional constraints on y level. It is used for large spikes to restrict them to a maximum y level.

- Type: `tfc:bounded_carving_mask`
- Config:
  - `min_y`: An optional integer (Default: 0), the minimum allowed y value for this to spawn at.
  - `max_y`: An optional integer (Default: 256), the maximum allowed y value for this to spawn at.
  - `probability`: A float in the range `[0, 1]`, the probability this will spawn at any given position.
  - `step`: The carving stage to use. Must be either `air` or `liquid`.

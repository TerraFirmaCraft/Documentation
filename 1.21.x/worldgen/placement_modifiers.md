---
layout: page
title: "Placement Modifiers"
permalink: /1.21.x/worldgen/placement-modifiers/
---

# Placement Modifier Types

*[Vanilla Reference for Placement Modifier Types](https://minecraft.wiki/w/Custom_feature#Placed_feature)*

TFC adds the following placement modifier types, for use in placed features:

<!--linky_begin_sort_alphabetical-->

- [Carving Mask](#carving-mask)
- [Climate](#climate)
- [Flat Enough](#flat-enough)
- [Intertidal](#intertidal)
- [Near Fluid](#near-fluid)
- [No Solid Neighbors](#no-solid-neighbors)
- [On Top](#on-top)
- [Shallow Water](#shallow-water)
- [Tuff Ring](#tuff-ring)
- [Tuya](#tuya)
- [Underground](#underground)
- [Volcano](#volcano)

<!--linky_end_sort_alphabetical-->

### Carving Mask

Extension of the vanilla carving mask placement modifier which allows min and max y bounds.

- Type: `tfc:carving_mask`
- Config:
  - `min_y`: An optional [Vertical Anchor](../common-types/#vertical-anchor) (Default: `bottom`), the minimum allowed y value for this to spawn at.
  - `max_y`: An optional [Vertical Anchor](../common-types/#vertical-anchor) (Default: `top`), the maximum allowed y value for this to spawn at.
  - `step`: The carving stage to use. Must be either `air` or `liquid`.

### Climate

This placement modifier will conditionally place a feature based on specific climate properties. All config values are optional, and if omitted will allow all positions. This is used in clay deposits to restrict them based on minimum rainfall.

The typical range for yearly average temperatures is -25 to +30 C. Rainfall values can vary between 0 mm and 500 mm.

- Type: `tfc:climate`
- Config:
  - `min_temperature`: An optional float representing the minimum allowed average yearly temperature.
  - `max_temperature`: An optional float representing the maximum allowed average yearly temperature.
  - `min_groundwater`: An optional float representing the minimum allowed groundwater level.
  - `max_groundwater`: An optional float representing the maximum allowed groundwater level.
  - `min_rain_variance`: An optional float (Default: `-1`) representing the minimum allowed rain variance.
  - `max_rain_variance`: An optional float (Default: `1`) representing the maximum allowed rain variance.
  - `rain_variance_absolute`: An optional boolean (Default: `false`). If true, uses the absolute value of rain variance.
  - `min_forest`: An optional non-negative integer (Default: `0`) representing the minimum required forest density.
  - `max_forest`: An optional non-negative integer (Default: `4`) representing the maximum required forest density.
  - `forest_types`: An optional list of [Forest Types](../common-types/#forest-type) (Default: empty list). If empty, all forest types are allowed.
  - `min_elevation`: An optional integer (Default: `-64`) representing the minimum allowed elevation.
  - `max_elevation`: An optional integer (Default: `320`) representing the maximum allowed elevation.
  - `fuzzy`: An optional boolean (Default: `false`). If true, the temperature and rainfall requirements will be probabilistic relative to the center point, with maximum density at the exact center, and zero density at the edges.
  - `ignore_rivers`: An optional boolean (Default: `false`). If true, uses average rainfall instead of average groundwater for the groundwater check.

### Flat Enough

This placement modifier will check an area around the initial position for solid blocks. If it's not found, it will attempt to move lower down, until the max depth is reached (and then the position is thrown out), or enough solid blocks are found. This is used by TFC's boulders feature, and is why they can be set into the ground.

- Type: `tfc:flat_enough`
- Config:
  - `flatness`: An optional float (Default: `0.5`), in the range `[0, 1]`. It describes how many solid blocks, as a percentage the surrounding area must contain.
  - `radius`: An optional positive integer (Default: `2`), which is the radius around the initial position that the area is checked for solid blocks.
  - `max_depth`: An optional positive integer (Default: `4`), which is how deep from the original position the placement modifier should try and search.

### Intertidal

This placement modifier places features in the intertidal zone based on high tide noise.

- Type: `tfc:intertidal`
- Config:
  - `min_elevation`: An optional integer (Default: `-64`) representing the minimum elevation difference from high tide level.
  - `max_elevation`: An optional integer (Default: `320`) representing the maximum elevation difference from high tide level.

### Near Fluid

This placement modifier will conditionally place a feature if there is a given fluid within a `radius` in the x and z directions, and within `[-radius, 0]` in the y direction.

- Type: `tfc:near_fluid`
- Config:
  - `radius`: An optional non-negative integer (Default: `2`) representing the distance to search for fluid.
  - `fluids`: An optional array of fluid ids that it will search for. If none are provided, any fluid will match (except air).

### No Solid Neighbors

This placement modifier checks that the position has no solid horizontal neighbors. Used for features that should not be placed next to solid blocks.

- Type: `tfc:no_solid_neighbors`
- Config: None

### On Top

This placement modifier checks the block below for a predicate, and passes if that predicate passes.

- Type: `tfc:on_top`
- Config:
  - `predicate`: A vanilla Block Predicate.

### Shallow Water

This placement modifier checks that the water is not too deep at a location.

- Type: `tfc:shallow_water`
- Config:
  - `min_depth`: An optional positive integer (Default: `0`), specifying the minimum depth of the water.
  - `max_depth`: An optional positive integer (Default: `5`), specifying the maximum depth of the water.

### Tuff Ring

This placement modifier places things near, or at, tuff rings (a type of volcanic feature).

- Type: `tfc:tuff_cone`
- Config:
  - `center`: An optional boolean (Default: `false`). If `true`, this placement modifier will ignore the `distance` argument and place the feature at the exact center of any tuff rings.
  - `distance`: An optional float (Default: `0`) in the range `[0, 1]`, representing the distance from the center of a tuff ring that this position must be in order to generate. 1 is the maximum radius of the tuff ring.

### Tuya

This placement modifier places things near, or at, tuyas (subglacial volcanoes).

- Type: `tfc:tuya`
- Config:
  - `center`: An optional boolean (Default: `false`). If `true`, this placement modifier will ignore the `distance` argument and place the feature at the exact center of any tuyas.
  - `distance`: An optional float (Default: `0`) in the range `[0, 1]`, representing the distance from the center of a tuya that this position must be in order to generate. 1 is the maximum radius of the tuya.

### Underground

This placement modifier passes if the position is below the world surface level.

- Type: `tfc:underground`
- Config: None

### Volcano

This placement modifier places things near, or at, volcanoes (cinder cones).

- Type: `tfc:volcano`
- Config:
  - `center`: An optional boolean (Default: `false`). If `true`, this placement modifier will ignore the `distance` argument and place the feature at the exact center of any volcanoes.
  - `distance`: An optional float (Default: `0`) in the range `[0, 1]`, representing the distance from the center of a volcano that this position must be in order to generate. 1 is the maximum radius of the volcano.

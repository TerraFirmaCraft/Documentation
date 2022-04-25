---
layout: page
title: "Configured Features"
permalink: /1.18.x/worldgen/features/
---

# Configured Features

*[Vanilla Reference for Features](https://minecraft.fandom.com/wiki/Configured_feature)*

TFC adds the following features:

- Caves:
  - [Cave Spike](#cave-spike)
  - [Large Cave Spike](#large-cave-spike)
  - [Thin Spike](#thin-spike)
  - [Cave Vegetation](#cave-vegetation)
  - [Ice Cave](#ice-cave)
- Fluids:
  - [Rivulet](#rivulet)
  - [Fissure](#fissure)
  - [Hot Spring](#hot-spring)
  - [Flood Fill Lake](#flood-fill-lake)
  - [Spring](#spring)
- Veins:
  - [Cluster Vein](#cluster-vein)
  - [Disc Vein](#disc-vein)
  - [Pipe Vein](#pipe-vein)
- Decoration:
  - [Boulder](#boulder)
  - [Loose Rock](#loose-rock)
  - [Soil Disc](#soil-disc)
  - [Iceberg](#iceberg)
  - [Weeping Vines](#weeping-vines)
  - [Twisting Vines](#twisting-vines)
  - [Kelp](#kelp)
  - [Coral Claw](#coral-claw)
  - [Coral Mushroom](#coral-mushroom)
  - [Coral Tree](#coral-tree)
  - [Vines](#vines)
  - [Berry Bushes](#berry-bushes) (Deprecated, will be removed)
  - [Fruit Trees](#fruit-trees)
  - [Bananas](#bananas)
- Trees and Forests:
  - [Forest](#forest)
  - [Overlay Tree](#overlay-tree)
  - [Random Tree](#random-tree)
  - [Stacked Tree](#stacked-tree)
- Technical:
  - [Erosion](#erosion)
  - [Ice And Snow](#ice-and-snow)
  - [Random Patch](#random-patch)
  - [Multiple](#multiple)

todo: wow there's a lot of these to document...

## Caves

### Cave Spike

This places a single cave spike, either 2, 3 or 4 blocks tall, either from the ceiling or floor. It uses the rock type of the current position.

- Type: `tfc:cave_spike`
- Config: None

### Large Cave Spike

This places a large cave spike, which can be up to 5 blocks wide and 16 blocks tall. It uses the rock type of the current position.

- Type: `tfc:large_cave_spike`
- Config: None

### Thin Spike

This places a thin spike like block (calcite or iceicles), in a small cluster around a given location.

- Type: `tfc:thin_spike`
- Config:
  - `state`: A [Lenient Blockstate](../common-types#lenient-blockstate) of the state to place. Must be a thin spike block.
  - `radius`: A integer in the range [1, 16]. The radius around the target location to place spikes in.
  - `tries`: A positive integer. The number of attempts to place spikes.
  - `min_height`: A positive integer. The minimum height of a spike.
  - `max_height`: A positive integer greater than or equal to `min_height`. The maximum height of a spike.

### Cave Vegetation

A feature that places cobwebs, additional uniformly distributed random block replacements, and water springs.

- Type: `tfc:cave_vegetation`
- Config:
  - `blocks`: A [Block Replacement Map](../common-types#block-replacement-map) of representing random blocks to replace.

### Ice Cave

A feature that places ice in various formations within caves.

- Type: `tfc:ice_cave`
- Config: None

## Fluids

### Rivulet

This creates small winding depressions that travel down slopes. The rivulet state is inset two blocks underneath the surface, with one block cleared above. It is what forms the magma trails on volcanoes.

- Type: `tfc:rivulet`
- Config:
  - `state`: A [Lenient Blockstate](../common-types#lenient-blockstate). The state that the rivulet consists of.

### Fissure

This creates a winding one block wide fissure, filled with a given fluid, down from a given location.

- Type: `tfc:fissure`
- Config:
  - `wall_state`: An optional [Lenient Blockstate](../common-types#lenient-blockstate). The state used for the wall blocks of the fissure. If not present, will use the rock type of the lowest rock layer.
  - `fluid_state`: A [Lenient Blockstate](../common-types#lenient-blockstate). The fluid state to fill the fissure with, can be air.
  - `count`: An optional integer (Default: `5`). The number of fissures to place.
  - `radius`: An optional integer (Default: `12`). The radius around the target position to try and place fissures in.
  - `min_depth`: An optional [Vertical Anchor](../common-types#vertical-anchor).
  - `min_pieces`: An optional positive integer (Default: `10`).
  - `max_pieces`: An optional positive integer (Default: `24`).
  - `max_piece_length`: An optional positive integer (Default: `6`).
  - `decoration`. An fissure decoration object with the following properties:
    - `blocks`: A [Block Replacement Map](../common-types#block-replacement-map). The additional 'decoration' ore veins that should spawn around the fissure.
    - `rarity`: A positive integer. The rarity that blocks should be replaced with decoration ore states.
    - `radius`: A positive integer. The radius around the fissure that blocks should be replaced.
    - `count`: A positive integer. The number of blocks that should be replaced with decoration ore states. Actual amount will be `count / rarity`.

### Hot Spring

This creates a hot spring, with additional winding fissures underneath, filled with a given fluid.

- Type: `tfc:hot_spring`
- Config:
  - `wall_state`: An optional [Lenient Blockstate](../common-types#lenient-blockstate), which the hot spring is built from. If omitted, the lowest rock layer rock will be used instead.
  - `fluid_state`: A [Lenient Blockstate](../common-types#lenient-blockstate) to fill the fissure with. Can be air.
  - `radius`: An optional integer in the range [1, 16]. The approximate radius of the hot spring.
  - `decoration`: An optional [Fissure Decoration](#fissure) object.

### Flood Fill Lake

A lake that fills existing terrain locally with a fluid.

- Type: `tfc:flood_fill_lake`
- Config:
  - `state`: A [Lenient Blockstate](../common-types#lenient-blockstate) to fill the lake area with.
  - `replace_fluids`: A string array. A list of fluids that can be replaced by this lake.
  - `overfill`: An optional boolean (Default: `false`). If the lake should attempt to fill upwards from the starting position as well as downwards.

### Spring

A copy of the vanilla spring feature.

- Type: `tfc:spring`
- Config: See the configuration for `minecraft:spring`.

## Trees and Forests

todo

## Veins

Vein features are responsible for all underground ore veins. Can generate veins that are many chunks wide.

Note: when using vein features, they must be added to **all** biomes in the same dimension that they spawn, even if they cannot spawn in said biome, to avoid chunk boundaries. They can still whitelist biomes based on the biome filter within the vein config.

Vein configs have several common configuration options that apply to all veins:

- `blocks`: A [Block Replacement Map](#../common-typesblock-replacement-map) defining what blocks the ore vein will place.
- `rarity`: An optional positive integer (Default: `60`). The vein will occur in 1 / `rarity` chunks on average.
- `size`: An optional integer (Default: `8`).
- `density`: An optional number in the range [0, 1] (Default: `0.2`).
- `min_y`: A [Vertical Anchor](../common-types#vertical-anchor). The minimum y level at which the vein will spawn.
- `max_y`: A [Vertical Anchor](../common-types#vertical-anchor). The maximum y level at which the vein will spawn.
- `salt`: An integer which represents a random seed to the vein locations.
- `biomes`: An optional array of objects, which can have one of two fields. This represents a filter for allowed biomes. If omitted, all biomes will be allowed.
  - `category`: A [Biome Category](../common-types#biome-category).
  - `biome_dictionary`: A [Biome Dictionary](../common-types#biome-dictionary) tag.
- `indicator`: An optional object representing an indicator to spawn on the surface above the vein. If present, it must have the following fields:
  - `depth`: An optional positive integer (Default: `35`). The maximum depth below the surface that the vein will spawn an indicator at.
  - `spread`: An optional positive integer (Default: `15`). The maximum horizontal distance from a vein that can spawn an indicator.
  - `rarity`: An optional positive integer (Default: `10`). The rarity to spawn indicators, as a fraction of horizontal locations the vein places ore blocks.
  - `blocks`: A [Weighted List](../common-types#weighted-list) of indicator states to spawn, with the following value:
    - Value `block`: A [Lenient Blockstate](../common-types#lenient-blockstate) to spawn.

### Cluster Vein

A vein that places blobs using metaballs.

- Type: `tfc:cluster_vein`
- Additional Config: None

### Disc Vein

A vein that places a flat horizontal disc.

- Type: `tfc:disc_vein`
- Additional Config:
  - `height`: The height of the disc. The `size` parameter is interpreted as the radius.

### Pipe Vein

A vein that places a tall pipe, that can be skewed or slanted. Skew represents the horizontal variance of the vein position, with height. Slant represents the variance of the vein's horizontal radius, with height. The sign of the slant represents if the vein narrows as y increases, or thickens as y increases.

- Type: `tfc:pipe_vein`
- Additional Config:
  - `radius`: An optional positive integer (Default: `3`). The radius of the pipe vein.
  - `min_skew`: An optional positive integer (Default: `0`). The minimum skew of the vein.
  - `max_skew`: An optional positive integer (Default: `0`). The maximum skew of the vein.
  - `min_slant`: An optional positive integer (Default: `0`). The minimum slant of the vein.
  - `max_slant`: An optional positive integer (Default: `0`). The maximum slant of the vein.
  - `sign`: An optional number in [0, 1] (Default: `0.5`) The sign of the slant.

## Decoration

### Coral Claw

Places a coral claw, like vanilla, for TFC salt water oceans and corals.

- Type: `tfc:coral_claw`
- Config: None

### Coral Mushroom

Places a coral mushroom feature, like vanilla, for TFC salt water oceans and corals.

- Type: `tfc:coral_mushroom`
- Config: None

### Coral Tree

Places a coral tree feature, like vanilla, but for TFC salt water oceans and corals.

- Type: `tfc:coral_tree`
- Config: None

## Technical

### Multiple

This places all features in a list at the current position.

- Type: `tfc:multiple`
- Config:
  - `features`: A string array of configured feature ids to place.
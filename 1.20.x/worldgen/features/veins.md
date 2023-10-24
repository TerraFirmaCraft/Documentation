---
layout: page
title: "Ore Veins"
permalink: /1.20.x/worldgen/features/veins/
---

# Ore Veins

TFC's ore veins are generated using three different features: [Cluster Vein](#cluster-vein), [Disc Vein](#disc-vein), and [Pipe Vein](#pipe-vein). These are used to generate veins that span across many chunks, unlike normal [Features](https://minecraft.wiki/w/Custom_feature).

In order to do this, veins must be added to **every biome** in the same dimension, even if they cannot spawn in some biomes. Veins must instead whitelist certain biomes using their own biome filter.

In TFC, vein features are all added to the [Placed Feature Tag](../../tags/#placed-feature-tags) `#tfc:in_biome/veins`, which contains all ore veins placed during world generation. To add a new vein, simply add it to this tag and TFC will generate it in the world.

All vein features have several common options which apply to all veins:

- `blocks`: A [Block Replacement Map](../../common-types/#block-replacement-map) defining what blocks the ore vein will place.
- `rarity`: An optional positive integer (Default: `60`). The vein will occur in 1 / `rarity` chunks on average.
- `size`: An optional integer (Default: `8`).
- `density`: An optional number in the range [0, 1] (Default: `0.2`).
- `min_y`: A [Vertical Anchor](../../common-types/#vertical-anchor). The minimum y level at which the vein will spawn.
- `max_y`: A [Vertical Anchor](../../common-types/#vertical-anchor). The maximum y level at which the vein will spawn.
- `salt`: An integer which represents a random seed to the vein locations.
- `biomes`: An optional array of objects, which can have one of two fields. This represents a filter for allowed biomes. If omitted, all biomes will be allowed.
  - `category`: A [Biome Category](../../common-types/#biome-category).
  - `biome_dictionary`: A [Biome Dictionary](../../common-types/#biome-dictionary) tag.
- `indicator`: An optional object representing an indicator to spawn on the surface above the vein. If present, it must have the following fields:
  - `depth`: An optional positive integer (Default: `35`). The maximum depth below the surface that the vein will spawn an indicator at.
  - `spread`: An optional positive integer (Default: `15`). The maximum horizontal distance from a vein that can spawn an indicator.
  - `rarity`: An optional positive integer (Default: `10`). The rarity to spawn indicators, as a fraction of horizontal locations the vein places ore blocks.
  - `blocks`: A [Weighted List](../../common-types/#weighted-list) of indicator states to spawn, with the following value:
    - Value `block`: A [Lenient Blockstate](../../common-types/#lenient-blockstate) to spawn.

### Cluster Vein

A vein that places blob-like shapes using [Metaballs](https://en.wikipedia.org/wiki/Metaballs).

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
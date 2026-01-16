---
layout: page
title: "Ore Veins"
permalink: /1.21.x/worldgen/features/veins/
---

# Ore Veins

TFC's ore veins are generated using three different features: [Cluster Vein](#cluster-vein), [Disc Vein](#disc-vein), and [Pipe Vein](#pipe-vein). These are used to generate veins that span across many chunks, unlike normal [Features](https://minecraft.wiki/w/Custom_feature).

In order to do this, veins must be added to **every biome** in the same dimension, even if they cannot spawn in some biomes. Veins must instead whitelist certain biomes using their own biome filter.

In TFC, vein features are all added to the [Placed Feature Tag](../../tags/#placed-feature-tags) `#tfc:in_biome/veins`, which contains all ore veins placed during world generation. To add a new vein, simply add it to this tag and TFC will generate it in the world.

All vein features have several common options which apply to all veins:

- `blocks`: A [Block Replacement Map](../../common-types/#block-replacement-map) defining what blocks the ore vein will place.
- `rarity`: A positive integer. The vein will occur in 1 / `rarity` chunks on average.
- `density`: A number in the range [0, 1]. The density of ore blocks within the vein.
- `min_y`: An integer. The minimum y level at which the vein will spawn.
- `max_y`: An integer. The maximum y level at which the vein will spawn.
- `project`: An optional boolean (Default: `false`). This adds the height of the world surface to the position the vein will spawn at. This means that `min_y` and `max_y` must then be specified relative to the world surface, rather than as an absolute y level.
- `project_offset`: An optional boolean (Default: `false`). This offsets the surface height used to make the surface projection when `project` is enabled by a random amount laterally. For example, this might mean that a vein set to spawn a few blocks below the surface may occasionally break the surface, since the projection it is using is no longer completely accurate.
- `random_name`: Either a string or a long integer. This value should be unique to this configured feature, as it helps randomize the placement of the vein.
- `near_lava`: An optional boolean (Default: `false`). If true, the vein will only spawn if there are lava blocks detected nearby.
- `indicator`: An optional object representing an indicator to spawn on the surface above the vein. If present, it must have the following fields:
  - `depth`: A positive integer. The maximum depth below the surface that the vein will spawn an indicator at.
  - `rarity`: An integer. The rarity to spawn indicators, as a fraction of horizontal locations the vein places ore blocks.
  - `underground_rarity`: A positive integer. The rarity to spawn indicators underground when the vein is too deep to spawn on the surface, as a fraction of horizontal locations the vein places ore blocks.
  - `underground_count`: An integer. The number of attempts to spawn an underground indicator in a given location.
  - `blocks`: A [Weighted List](../../common-types/#weighted-list) of indicator states to spawn, with the following value:
    - Value `block`: A [Lenient Blockstate](../../common-types/#lenient-blockstate) to spawn.

### Cluster Vein

A vein that places blob-like shapes using [Metaballs](https://en.wikipedia.org/wiki/Metaballs).

- Type: `tfc:cluster_vein`
- Additional Config:
  - `size`: A positive integer. The size of the cluster vein.

### Disc Vein

A vein that places a flat horizontal disc.

- Type: `tfc:disc_vein`
- Additional Config:
  - `size`: A positive integer. The radius of the disc.
  - `height`: A positive integer. The height of the disc.

### Pipe Vein

A vein that places a tall pipe, that can be skewed or slanted. Skew represents the horizontal variance of the vein position, with height. Slant represents the variance of the vein's horizontal radius, with height. The sign of the slant represents if the vein narrows as y increases, or thickens as y increases.

- Type: `tfc:pipe_vein`
- Additional Config:
  - `height`: An integer. The height of the pipe vein.
  - `radius`: An integer. The radius of the pipe vein.
  - `min_skew`: An integer. The minimum skew of the vein.
  - `max_skew`: An integer. The maximum skew of the vein.
  - `min_slant`: An integer. The minimum slant of the vein.
  - `max_slant`: An integer. The maximum slant of the vein.
  - `sign`: A number in the range [0, 1]. The sign of the slant.

### Kaolin Disc Vein

A vein that places a kaolin clay disc. This is otherwise the same as a disc vein, but ignores the `blocks` field in favor of setting layered clay blocks.

- Type: `tfc:kaolin_disc_vein`
- Additional Config:
  - `size`: A positive integer. The radius of the disc.
  - `height`: A positive integer. The height of the disc.

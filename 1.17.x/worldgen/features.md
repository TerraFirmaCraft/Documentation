---
layout: page
title: "Configured Features"
permalink: /1.17.x/worldgen/features/
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
  - [Lake](#lake) (Deprecated, will be removed)
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

### Cave Spike

This places a single cave spike, either 2, 3 or 4 blocks tall, either from the ceiling or floor. It uses the rock type of the current position.

- Type: `tfc:cave_spike`
- Config: None

### Large Cave Spike

This places a large cave spike, which can be up to 5 blocks wide and 16 blocks tall. It uses the rock type of the current position.

- Type: `tfc:large_cave_spike`
- Config: None

### Multiple

This places all features in a list at the current position.

- Type: `tfc:multiple`
- Config:
  - `features`: A string array of configured feature ids to place.
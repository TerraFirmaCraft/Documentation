---
layout: page
title: "Tags"
permalink: /1.18.x/tags/
---

# Tags

This page details all the tags that TFC adds, and uses for various functions. These have been separated out into [Block Tags](#block-tags), [Fluid Tags](#fluid-tags), and [Item Tags](#item-tags).

## Block Tags

Tag Id | Function
---|---
`tfc:can_trigger_collapse` | Blocks which when mined will search a nearby area for potential blocks that can **start** a collapse.
`tfc:can_start_collapse` | Blocks which can form the epicenter of a collapse. Without a start, a collapse cannot occur.
`tfc:can_collapse` | Blocks which, once a collapse has **started**, can collapse as part of the destruction. Must also have a valid [Collapse Recipe](../recipes/#collapse) defined for this block.
`tfc:can_landslide` | Blocks which can landslide to below or adjacent blocks, and are affected by gravity. Must also have a valid [Landslide Recipe](../recipes/#landslide) defined for this block.
`tfc:supports_landslide` | Blocks which are not full blocks, but count as full blocks when determining if an adjacent block might support a block against landsliding. Blocks cannot landslide when they are supported on at least two sides.
`tfc:toughness_1` | Blocks which are defined to have toughness 1 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block. 
`tfc:toughness_2` | Blocks which are defined to have toughness 2 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block.
`tfc:toughness_3` | Blocks which are defined to have toughness 3 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block.

<hr>

## Fluid Tags

<hr>

## Item Tags

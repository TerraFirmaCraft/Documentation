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
`tfc:tree_grows_on` | Blocks which a tree is able to spawn on, during world generation.
`tfc:bush_plantable_on` | Blocks which many plants, including bushes, fruit trees, and seasonal plants are able to spawn on, during world generation.
`tfc:single_block_replaceable` | Single blocks which can be replaced during world generation by other features, such as single block plants or grasses.
`tfc:sea_bush_plantable_on` | Blocks which many underwater plants are able to spawn on, during world generation.
`tfc:creeping_plantable_on` | Blocks which creeping plants are able to spawn on, during world generation.
`tfc:thatch_bed_thatch` | Blocks which count as valid 'thatch' blocks when trying to make a thatch bed.
`tfc:can_be_snow_piled` | Blocks which can be hidden by snow formation. Can include both single blocks and two-tall plant blocks.
`tfc:can_be_ice_piled` | Blocks which can be hidden by ice formation. Can include both blocks in the ice and immediately above (i.e. lily pads)
`tfc:breaks_when_isolated` | When surrounded on all sides by air blocks, this will pop off as an item upon being updated.
`tfc:lit_by_dropped_torch` | Blocks which, when a torch item entity is dropped on them, might start a fire atop them,

<hr>

## Fluid Tags

<hr>

## Item Tags

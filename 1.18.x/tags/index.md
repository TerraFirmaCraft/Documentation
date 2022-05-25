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
`tfc:thatch_bed_thatch` | Blocks which are valid for the two base blocks of a thatch bed.
`tfc:scraping_surface` | Blocks which can act as a flat surface for a [Scraping Recipe](../recipes/#scraping) to be performed on.
`tfc:logs_that_log` | Log blocks which can be felled as trees, using TFC's tree chopping functionality.
`tfc:prospectable` | Blocks which can be found with the prospectors pick. When found, they will display a message with the translation key `<block translation key>.prospected`.

<hr>

## Fluid Tags

<hr>

## Item Tags

Tag Id | Function
---|---
`tfc:thatch_bed_hides` | Items which when right clicked on two `#tfc:thatch_bed_thatch` blocks, will form a thatch bed.
`tfc:firepit_kindling` | Items which are valid **kindling** for creating a Firepit with a fire starter. More kindling increases the chance of success.
`tfc:firepit_sticks` | Items which are valid **sticks** for creating a Firepit with a fire starter. A firepit requires three sticks to be created.
`tfc:firepit_logs` | Items which are valid **logs** for creating a Firepit with a fire starter. A firepit require one log, which will be immediately inserted as the first [Fuel](../data/#fuels) item of the Firepit.
`tfc:starts_fires_with_durability` | Items which when right clicked, can start fires at the cost of durability like Flint and Steel. These items can then be used on most light-able TFC devices (firepit, forge, etc.).
`tfc:starts_fires_with_items` | Items which when right clicked, can start fires at the cost of the item itself like Fire Charges. These items can then be used on most light-able TFC devices (firepit, forge, etc.).
`tfc:extinguisher` | Items which can be used on a fire pit to put out the fire.
`tfc:log_pile_logs` | Items which are able to be placed into a log pile.
`tfc:pit_kiln_straw` | Items which are valid for the eight straw layers of a pit kiln.
`tfc:pit_kiln_logs` | Items which are valid for the eight log layers of a pit kiln.
`tfc:can_be_lit_on_torch` | Items which, when right clicked on a lit torch, can be lit into a torch themselves.
`tfc:firepit_fuel` | Items that are valid [Fuels](../data/#fuels) for the Firepit.
`tfc:forge_fuel` | Items that are valid [Fuels](../data/#fuels) for the Charcoal Forge.
`tfc:handstone` | Items that are valid hand stones for a Quern.
`tfc:scrapable` | Items that can be placed flat on a block, with a valid [Scraping Recipe](../recipes/#scraping).
`tfc:rock_knapping` | Items that can be right clicked to knap, with a valid [Rock Knapping Recipe](../recipes/#rock-knapping).
`tfc:clay_knapping` | Items that can be right clicked to knap, with a valid [Clay Knapping Recipe](../recipes/#knapping).
`tfc:fire_clay_knapping` | Items that can be right clicked to knap, with a valid [Fire Clay Knapping Recipe](../recipes/#knapping).
`tfc:leather_knapping` | Items that can be right clicked to knap, with a valid [Leather Knapping Recipe](../recipes/#knapping).
`tfc:axes_that_log` | Tools that can be used to fell entire trees, via TFC's tree chopping functionality.
`tfc:usable_on_tool_rack` | Tools that can be placed onto a tool rack.
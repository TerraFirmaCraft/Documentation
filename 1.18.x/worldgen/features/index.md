---
layout: page
title: "Features"
permalink: /1.18.x/worldgen/features/
---

# Features

*[Vanilla Reference for Features](https://minecraft.fandom.com/wiki/Custom_feature)*

Features are small decorations that modify individual chunks, based on the biome present in that chunk. In TFC, features are all added to biomes via the use of [Biome Tags](../tags/#biome-tags), which means that they can also be added to biomes via the use of these tags.

TFC adds the following features:

- **[Trees and Forests](trees/)**
- **[Ore Veins](veins/)**
- Caves:
  - [Cave Spike](#cave-spike)
  - [Large Cave Spike](#large-cave-spike)
  - [Thin Spike](#thin-spike)
  - [Cave Vegetation](#cave-vegetation)
  - [Ice Cave](#ice-cave)
  - [Geode](#geode)
- Fluids:
  - [Rivulet](#rivulet)
  - [Fissure](#fissure)
  - [Hot Spring](#hot-spring)
  - [Flood Fill Lake](#flood-fill-lake)
  - [Spring](#spring)
- Decoration:
  - [Boulder](#boulder)
  - [Loose Rock](#loose-rock)
  - [Soil Disc](#soil-disc)
  - [Iceberg](#iceberg)
  - [Powder Snow](#powder-snow)
  - [Weeping Vines](#weeping-vines)
  - [Twisting Vines](#twisting-vines)
  - [Kelp](#kelp)
  - [Kelp Tree](#kelp-tree)
  - [Emergent Plant](#emergent-plant)
  - [Tall Plant](#tall-plant)
  - [Tall Wild Crop](#tall-wild-crop)
  - [Spreading Bush](#spreading-bush)
  - [Block With Fluid](#block-with-fluid)
  - [Coral Claw](#coral-claw)
  - [Coral Mushroom](#coral-mushroom)
  - [Coral Tree](#coral-tree)
  - [Vines](#vines)
  - [Fruit Trees](#fruit-trees)
  - [Bananas](#bananas)
- Technical:
  - [Erosion](#erosion)
  - [Ice And Snow](#ice-and-snow)
  - [Multiple](#multiple)
  - [If Then](#if-then)
  - [Noisy Multiple](#noisy-multiple)


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
  - `state`: A [Lenient Blockstate](../common-types/#lenient-blockstate) of the state to place. Must be a thin spike block.
  - `radius`: A integer in the range [1, 16]. The radius around the target location to place spikes in.
  - `tries`: A positive integer. The number of attempts to place spikes.
  - `min_height`: A positive integer. The minimum height of a spike.
  - `max_height`: A positive integer greater than or equal to `min_height`. The maximum height of a spike.

### Cave Vegetation

A feature that places cobwebs, additional uniformly distributed random block replacements, and water springs.

- Type: `tfc:cave_vegetation`
- Config:
  - `blocks`: A [Block Replacement Map](../common-types/#block-replacement-map) of representing random blocks to replace.

### Ice Cave

A feature that places ice in various formations within caves.

- Type: `tfc:ice_cave`
- Config: None

### Geode

A feature that generates a simplified version of vanilla's Geode, a cracked sphere. The sphere has an outer and middle block, and then a replacement map for the inner blocks.
- Type: `tfc:geode`
- Config:
  - `outer` A [Lenient Blockstate](../common-types/#lenient-blockstate) of the state to place on the outside layer.
  - `middle` A [Lenient Blockstate](../common-types/#lenient-blockstate) of the state to place in the middle layer.
  - `inner` A [Block Replacement Map](../common-types/#block-replacement-map) of blocks to place in the inner layer.

## Fluids

### Rivulet

This creates small winding depressions that travel down slopes. The rivulet state is inset two blocks underneath the surface, with one block cleared above. It is what forms the magma trails on volcanoes.

- Type: `tfc:rivulet`
- Config:
  - `state`: A [Lenient Blockstate](../common-types/#lenient-blockstate). The state that the rivulet consists of.

### Fissure

This creates a winding one block wide fissure, filled with a given fluid, down from a given location.

- Type: `tfc:fissure`
- Config:
  - `wall_state`: An optional [Lenient Blockstate](../common-types/#lenient-blockstate). The state used for the wall blocks of the fissure. If not present, will use the rock type of the lowest rock layer.
  - `fluid_state`: A [Lenient Blockstate](../common-types/#lenient-blockstate). The fluid state to fill the fissure with, can be air.
  - `count`: An optional integer (Default: `5`). The number of fissures to place.
  - `radius`: An optional integer (Default: `12`). The radius around the target position to try and place fissures in.
  - `min_depth`: An optional [Vertical Anchor](../common-types/#vertical-anchor).
  - `min_pieces`: An optional positive integer (Default: `10`).
  - `max_pieces`: An optional positive integer (Default: `24`).
  - `max_piece_length`: An optional positive integer (Default: `6`).
  - `decoration`. An fissure decoration object with the following properties:
    - `blocks`: A [Block Replacement Map](../common-types/#block-replacement-map). The additional 'decoration' ore veins that should spawn around the fissure.
    - `rarity`: A positive integer. The rarity that blocks should be replaced with decoration ore states.
    - `radius`: A positive integer. The radius around the fissure that blocks should be replaced.
    - `count`: A positive integer. The number of blocks that should be replaced with decoration ore states. Actual amount will be `count / rarity`.

### Hot Spring

This creates a hot spring, with additional winding fissures underneath, filled with a given fluid.

- Type: `tfc:hot_spring`
- Config:
  - `wall_state`: An optional [Lenient Blockstate](../common-types/#lenient-blockstate), which the hot spring is built from. If omitted, the lowest rock layer rock will be used instead.
  - `fluid_state`: A [Lenient Blockstate](../common-types/#lenient-blockstate) to fill the fissure with. Can be air.
  - `radius`: An optional integer in the range [1, 16]. The approximate radius of the hot spring.
  - `decoration`: An optional [Fissure Decoration](#fissure) object.

### Flood Fill Lake

A lake that fills existing terrain locally with a fluid.

- Type: `tfc:flood_fill_lake`
- Config:
  - `state`: A [Lenient Blockstate](../common-types/#lenient-blockstate) to fill the lake area with.
  - `replace_fluids`: A string array. A list of fluids that can be replaced by this lake.
  - `overfill`: An optional boolean (Default: `false`). If the lake should attempt to fill upwards from the starting position as well as downwards.

### Spring

A copy of the vanilla spring feature.

- Type: `tfc:spring`
- Config: See the configuration for `minecraft:spring`.

## Decoration

### Boulder
Places a large boulder, shaped like a deformed sphere.

- Type: `tfc:boulder`
- Config:
  - `states`: A [Key Value List](../common-types/#key-value-list) with the following fields:
    - `rock` A [Lenient Blockstate](../common-types/#lenient-blockstate) corresponding to the 'raw' rock block of a rock type.
	- `blocks` An array of [Lenient Blockstates](../common-types/#lenient-blockstate) that will be chosen from randomly when placing the boulder.

### Loose Rock
Places a loose rock on the ground based on the rock type at the position.

- Type: `tfc:loose_rock`
- Config: None

### Soil Disc
Places a disc of blocks. Typically used for soil replacements like clay, but can be used for anything.

- Type: `tfc:soil_disc`
- Config:
  - `states`: A [Key Value List](../common-types/#key-value-list) with the following fields:
    - `replace`: A [Lenient Blockstate](../common-types/#lenient-blockstate) to be replaced
	- `with`: A [Lenient Blockstate](../common-types/#lenient-blockstate) that gets set in that block's place.
  - `min_radius`: A positive integer specifying the minimum horizontal radius of the disc.
  - `max_radius`: A positive integer specifying the maximum horizontal radius of the disc.
  - `height`: An integer [0, 256] specifying how tall the disc should be.

### Iceberg
A modified version of vanilla's iceberg feature to use salt water.

- Type: `tfc:iceberg`
- Config:
  - `state`: The main block of the iceberg.

### Powder Snow
Places a disc of a block, replacing anything with the `tfc:powder_snow_replaceable` [Block Tag](../../data/tags/)

- Type: `tfc:powder_snow`
- Config:
  - `state`: The block to place.

### Weeping Vines
Places a cluster of long plants hanging down from leaves, logs, or stone.

- Type: `tfc:weeping_vines`
- Config:
  - `body`: A [Lenient Blockstate](../common-types/#lenient-blockstate) representing the main block of the vine.
  - `head` A [Lenient Blockstate](../common-types/#lenient-blockstate) representing the tip of the vine.
  - `tries`: An integer [1, 128] specifying how many times a vine placement should be attempted.
  - `radius`: An integer [1, 16] specifying how far the cluster of vines should spread.
  - `min_height`: An integer [1, 100] specifying the minimum length of a vine that should be placed.
  - `max_height`: An integer [1, 100] specifying the maximum length of a vine that should be placed.

### Twisting Vines
The same as [Weeping Vines](#weeping-vines), but it places plants that grow up from the ground.

- Type: `tfc:twisting_vines`
- Config: See [Weeping Vines](#weeping-vines)

### Kelp
The same as [Twisting Vines](#twisting-vines), but built to only place underwater plants on the sea floor.

- Type: `tfc:twisting_vines`
- Config: See [Weeping Vines](#weeping-vines)

### Kelp Tree
Places a cluster of tree kelp.

- Type: `tfc:kelp_tree`
- Config:
  - `block`: A block that is a kind of kelp tree flower, which will be forcibly grown into a kelp tree.

### Emergent Plant
Places an emergent plant, with the bottom half of the block submerged and the top not submerged.

- Type: `tfc:emergent_plant`
- Config:
  - `block`: A tall water plant block to be placed.

### Tall Plant
Places a two block high plant block.

- Type: `tfc:tall_plant`
- Config:
  - `block`: A tall plant block, to be placed.

### Tall Wild Crop
Places a two block high wild crop block.

- Type: `tfc:tall_wild_crop`
- Config:
  - `block`: A tall wild crop block to be placed.

### Spreading Bush
Places a spreading bush, with some growth already completed.

- Type: `tfc:spreading_bush`
- Config:
  - `block`: A spreading bush block to be grown.

### Block With Fluid
Places a block, attempting to fill it with the fluid at the position it finds. If the block cannot contain the fluid, nothing is placed.

- Type: `tfc:block_with_fluid`
- Config:
  - `to_place`: A fully specified blockstate (see [Lenient Blockstate](../common-types/#lenient-blockstate) for what that looks like)

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

### Vines

Places a single vine block. The vine block must be in the style of vanilla vines.

- Type: `tfc:vine`
- Config:
  - `state`: A fully defined blockstate.

### Fruit Trees

Locates a position for and places a fruit tree, fully grown.

- Type: `tfc:fruit_trees`
- Config:
  - `state`: A [Lenient Blockstate](../common-types/#lenient-blockstate) of the fruit tree's growing branch block.

### Bananas

Places a fully grown banana plant.

- Type: `tfc:bananas`
- Config:
  - `state`: A [Lenient Blockstate](../common-types/#lenient-blockstate) corresponding to a Banana-like plant block.

## Technical

### Erosion

Traverses a chunk, either removing blocks or supporting them with hardened stone if it seems that they might fall when the chunk is loaded.

- Type: `tfc:erosion`
- Config: None

### Ice and Snow

Conducts an initial climate update on the surface, adding ice and snow when appropriate.

- Type: `tfc:ice_and_snow`
- Config: None


### Multiple

This places all features in a list at the current position.

- Type: `tfc:multiple`
- Config:
  - `features`: A string array of configured feature ids to place.

### If Then

Attempts to place the first feature, and if that succeeds, places the second feature.

- Type: `tfc:if_then`
- Config:
  - `if`: A placed feature id, that will always try to place.
  - `then`: The placed feature id, that will only place if the first feature places.

### Noisy Multiple

Similar to [Multiple](#multiple), except that only two of the provided features will be placed. The list of features is cycled through depending on the position in the world. If a feature is invalid at a position, it is skipped. The result is smooth transitions between different features.

- Type: `tfc:noisy_multiple`
- Config:
  - `features`: A string array of configured feature ids to place.

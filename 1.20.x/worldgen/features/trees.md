---
layout: page
title: "Trees and Forests"
permalink: /1.20.x/worldgen/features/trees/
---

# Trees and Forests

TFC uses the `tfc:forest` feature to place all trees of all types, and various other forest related decoration. This feature includes specifying the climate ranges for different trees, adhering to the global [Forest Type](../../common-types/#forest-type), selecting which tree types to generate in a given area, and placing forest adjacent decoration.

If you are looking to **add new trees or modify existing trees**, you will want to start at [Forest Entries](#forest-entry).

TFC also adds a few different features used for generating individual trees themselves. These can be used by datapacks but **are not required to use the TFC forest feature**. These are [Random Tree](#random-tree), [Overlay Tree](#overlay-tree), and [Stacked Tree](#stacked-tree).

<hr>

### Forest Feature

This feature is added to all biomes via being present in the [Placed Feature Tag](../../tags/#placed-feature-tags) `#tfc:in_biome/large_features/<biome>` for every biome that may contain forests.

- Type: `tfc:forest`
- Config:
  - `entries`: A [Configured Feature Holder Set](../../common-types/#holder-set). Each entry **must** be a [Forest Entry](#forest-entry). In TFC, this references the 
  - `type`: The map with [Forest Types](../../common-types/#forest-type) as keys and the following config as values:
    - `tree_count`: An integer provider specifying how many trees should spawn.
	- `groundcover_count`: An integer provider specifying how much groundcover should spawn.
	- `per_chunk_chance`: An optional float, by default 1, of the chance per chunk of this forest type spawning.
	- `bush_count`: An optional integer provider specifying the amount of bushes that will try to spawn.
	- `has_spoiler_old_growth`: A boolean specifying if a random old growth tree will occasionally spawn amongst the existing trees.
	- `allows_old_growth`: A boolean specifying if old growth trees will spawn in this forest type.
  - `use_weirdness`: A boolean specifying if forest weirdness will be used to gradually alternate between what forest entry is placed, causing more varied but less climate-accurate forests.

<hr>

### Forest Entry

This feature is used to describe the spawning conditions of a single tree. They must be added to the [Configured Feature Tag](../../tags/#configured-feature-tags) `#tfc:forest_trees`, in order to be spawned by the `tfc:forest` feature.

- Type: `tfc:forest_entry`
- Config:
  - `min_rain`: The minimum rainfall for this tree to spawn.
  - `max_rain`: The maximum rainfall for this tree to spawn.
  - `min_temp`: The minimum temperature for this tree to spawn.
  - `max_temp`: The maximum temperature for this tree to spawn.
  - `bush_log`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the log used for bushes. If omitted, no bushes will spawn.
  - `bush_leaves`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the leaves used for bushes.
  - `groundcover`: An optional [Weighted List](../../common-types/#weighted-list) specifying the blocks that can spawn on the ground around the trees.
  - `normal_tree`: A [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a normal tree.
  - `dead_tree`: A [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a dead tree.
  - `old_growth_tree`: An optional [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a rare "old growth" tree.
  - `old_growth_chance`: (Default: `6`) An optional integer, representing the chance for an old growth tree to be selected. On average, 1 / `old_growth_chance` of trees will be old growth.
  - `spoiler_old_growth_chance`: (Default: `200`) An optional integer, representing the chance for a old growth tree to spawn in non-old-growth forests. On average, 1 / `spoiler_old_growth_chance` of trees in these areas will be old growth.
  - `fallen_tree_chance`: (Default: `14`) An optional integer, specifying how often fallen trees spawn. On average, 1 / `fallen_tree_chance` chunks will contain a fallen tree.
  - `dead_chance`: (Default: `75`) An optional integer, specifying how often dead trees spawn. On average, 1 / `dead_chance` of trees will spawn as dead trees instead.

<hr>

### Random Tree

This feature chooses structures randomly from a list, and places them. Optionally, it also creates a trunk of randomly chosen height beneath the tree. It is used for trees like Acacia and Kapok.

- Type:`tfc:random_tree`
- Config:
  - `structures`: A list of [Structures](../../common-types/#structure) to be placed.
  - `trunk`: A [Trunk](#trunk) for the trunk below the structure.
  - `placement`: A [Tree Placement](#tree-placement)

### Overlay Tree

This feature uses two structures: a "Base" structure, and an "Overlay" structure. The overlay structure is placed with each of it's blocks randomly chosen to place or not, using the "Integrity" option found in [Structure Blocks](https://minecraft.wiki/w/Structure_Block). It is used for trees like Oak and Ash.

- Type: `tfc:overlay_tree`
- Config:
  - `base`: A [Structure](../../common-types/#structure).
  - `overlay`: A [Structure](../../common-types/#structure).
  - `radius`: An integer. This value is unused.
  - `trunk`: A [Trunk](#trunk) for the trunk below the structure.
  - `overlay_integrity`: A float [0, 1] specifying the percent of the overlay structure that will be placed.
  - `placement`: A [Tree Placement](#tree-placement)

### Stacked Tree

This feature uses multiple layers of structures to create a stacked appearance. It chooses a random number of structures from each layer, and then stacks them on top of each other. It is used by Old Growth Sequoia trees.

- Type: `tfc:stacked_tree`
- Config:
  - `layers`: A list of **layers**. Each layer must be an object with the following fields:
    - `templates`: A list of [Structures](../../common-types/#structure).
	- `min_count`: The minimum number of structures from this layer to use.
	- `max_count`: The maximum number of structures from this layer to use.
  - `trunk`: A [Trunk](#trunk) for the trunk below the structure.
  - `placement`: A [Tree Placement](#tree-placement)

<hr>

There are a couple objects which are common to all tree features used by TFC:

#### Trunk

This is an object specifying the shape and size of a tree's trunk. It has the following properties:

- `state`: A [Lenient Blockstate](../../common-types/#lenient-blockstate) of the trunk block.
- `min_height`: The integer minimum height of the trunk.
- `max_height`: The integer maximum height of the trunk.
- `width`: The integer width of the trunk, in blocks.

#### Tree Placement

This is an object specifying how and when trees are placed in the world. It has the following properties:

- `width`: An integer specifying width of ground clearance needed.
- `height`: An integer specifying the open height needed to place the tree.
- `allow_submerged`: A boolean, if the tree can spawn in one block of water.
- `allow_deeply_submerged`: A boolean, if the tree can spawn in any height of water.
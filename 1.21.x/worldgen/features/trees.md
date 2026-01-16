---
layout: page
title: "Trees and Forests"
permalink: /1.21.x/worldgen/features/trees/
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
  - `climate`: A [Climate Placement](../placement_modifiers/#climate) specifying where this tree can spawn.
  - `bush_log`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the log used for bushes. If omitted, no bushes will spawn.
  - `bush_leaves`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the leaves used for bushes.
  - `fallen_log`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the log used for fallen trees.
  - `fallen_leaves`: An optional [Lenient Blockstate](../../common-types/#lenient-blockstate) specifying the leaves used for fallen trees.
  - `groundcover`: An optional [Weighted List](../../common-types/#weighted-list) specifying the blocks that can spawn on the ground around the trees.
  - `normal_tree`: A [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a normal tree.
  - `dead_tree`: A [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a dead tree.
  - `old_growth_tree`: An optional [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place a rare "old growth" tree.
  - `krummholz`: An optional [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place krummholz (stunted alpine trees).
  - `soil_disc`: An optional [Configured Feature](https://minecraft.wiki/w/Custom_feature#Configured_Feature) which will be used to place soil discs around the tree.
  - `old_growth_chance`: (Default: `6`) An optional integer, representing the chance for an old growth tree to be selected. On average, 1 / `old_growth_chance` of trees will be old growth.
  - `spoiler_old_growth_chance`: (Default: `200`) An optional integer, representing the chance for a old growth tree to spawn in non-old-growth forests. On average, 1 / `spoiler_old_growth_chance` of trees in these areas will be old growth.
  - `fallen_tree_chance`: (Default: `14`) An optional integer, specifying how often fallen trees spawn. On average, 1 / `fallen_tree_chance` chunks will contain a fallen tree.
  - `dead_chance`: (Default: `75`) An optional integer, specifying how often dead trees spawn. On average, 1 / `dead_chance` of trees will spawn as dead trees instead.
  - `floating`: (Default: `false`) A boolean specifying if the tree will spawn on top of water.

<hr>

### Random Tree

This feature chooses structures randomly from a list, and places them. Optionally, it also creates a trunk of randomly chosen height beneath the tree. It is used for trees like Acacia and Kapok.

- Type:`tfc:random_tree`
- Config:
  - `structures`: A list of [Structures](../../common-types/#structure) to be placed.
  - `trunk`: An optional [Trunk](#trunk) for the trunk below the structure.
  - `placement`: A [Tree Placement](#tree-placement)
  - `root_system`: An optional [Root System](#root-system) for placing roots around the tree base.

### Overlay Tree

This feature uses two structures: a "Base" structure, and an "Overlay" structure. The overlay structure is placed with each of it's blocks randomly chosen to place or not, using the "Integrity" option found in [Structure Blocks](https://minecraft.wiki/w/Structure_Block). It is used for trees like Oak and Ash.

- Type: `tfc:overlay_tree`
- Config:
  - `base`: A [Structure](../../common-types/#structure).
  - `overlay`: A [Structure](../../common-types/#structure).
  - `trunk`: An optional [Trunk](#trunk) for the trunk below the structure.
  - `overlay_integrity`: (Default: `0.5`) A float [0, 1] specifying the percent of the overlay structure that will be placed.
  - `placement`: A [Tree Placement](#tree-placement)
  - `root_system`: An optional [Root System](#root-system) for placing roots around the tree base.

### Stacked Tree

This feature uses multiple layers of structures to create a stacked appearance. It chooses a random number of structures from each layer, and then stacks them on top of each other. It is used by Old Growth Sequoia trees.

- Type: `tfc:stacked_tree`
- Config:
  - `layers`: A list of **layers**. Each layer must be an object with the following fields:
    - `templates`: A list of [Structures](../../common-types/#structure).
	- `min_count`: The minimum number of structures from this layer to use.
	- `max_count`: The maximum number of structures from this layer to use.
  - `trunk`: A [Trunk](#trunk) for the trunk below the structure. This field is required.
  - `placement`: A [Tree Placement](#tree-placement)
  - `root_system`: An optional [Root System](#root-system) for placing roots around the tree base.

### Krummholz

This feature places stunted alpine trees (krummholz) that grow in harsh high-altitude environments. Unlike other tree features, this doesn't use structures but directly places blocks.

- Type: `tfc:krummholz`
- Config:
  - `block`: The block to use for the krummholz plant.
  - `height`: An integer provider specifying the height of the krummholz.
  - `spawns_on_stone`: (Default: `false`) A boolean specifying if the krummholz can spawn on stone blocks.
  - `spawns_on_gravel`: (Default: `false`) A boolean specifying if the krummholz can spawn on gravel blocks.

<hr>

There are a couple objects which are common to all tree features used by TFC:

#### Trunk

This is an object specifying the shape and size of a tree's trunk. It has the following properties:

- `state`: A [Lenient Blockstate](../../common-types/#lenient-blockstate) of the trunk block.
- `min_height`: The integer minimum height of the trunk.
- `max_height`: The integer maximum height of the trunk.
- `wide`: A boolean specifying if the trunk should be 2x2 blocks wide (true) or 1x1 (false).

#### Tree Placement

This is an object specifying how and when trees are placed in the world. It has the following properties:

- `width`: An integer specifying width of ground clearance needed.
- `height`: An integer specifying the open height needed to place the tree.
- `ground_type`: (Default: `normal`) An enum specifying what type of ground the tree can spawn on. Options are:
  - `normal`: Standard ground placement.
  - `sand`: Can only place on sand.
  - `shallow_water`: Can place in one block of freshwater.
  - `submerged`: Can place in any depth of freshwater.
  - `shallow_allow_saltwater`: Can place in one block of any water (including saltwater).
  - `submerged_allow_saltwater`: Can place in any depth of any water.
  - `floating`: The tree will spawn on top of water.

#### Root System

This is an optional object that defines how tree roots are placed around the base of the tree. It has the following properties:

- `blocks`: A map of block types to [Weighted Lists](../../common-types/#weighted-list) of block states. The key is the block that the root can replace, and the value is a weighted list of possible root blocks to place.
- `width`: (Default: `4`) An integer specifying the horizontal radius around the tree where roots can spawn.
- `height`: (Default: `3`) An integer specifying the vertical height below the tree where roots can spawn.
- `tries`: (Default: `5`) An integer specifying how many attempts to make when placing each root.
- `special_placer`: An optional special root placer for custom root placement logic.
- `required`: (Default: `false`) A boolean specifying if roots are required for the tree to place. If true and roots cannot be placed, the tree will not spawn.
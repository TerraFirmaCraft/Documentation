---
layout: page
title: "Ore Generation"
permalink: /1.12.x/oregen/
---

# Ore Generation

TFC's ore generation is currently done using a JSON configuration based system. This can be customized by either addon makers, by providing their own ore generation files, or by pack makers. It is mostly meant to be used with TFC / addon added ores, however it can be used (in a limited sense) by other mod ores.

For addons interested in adding TFC-compatible ores, see how to add TFC [registry types](/Documentation/1.12.x/registry-types/)

## Files

TFC will look for any files in the `config/tfc/` directory (recursively) for ore generation. If there are none, a default one is generated. If you are noticing problems with ore generation, **check the log for messages**, as in most cases ore veins will output various errors if problems are present in the configuration.

Each file must be a valid `.json` file. If you're getting JSON parse errors, check the validity with a tool such as [JsonLint](https://jsonlint.com/).

Each file may contain any number of veins. The structure must be as follows:

```json
{
    "vein_name": { "... a vein object ..." },
    "another_vein_name": { "... another vein object ..." },
    "..."
}
```

## Vein Names

Each vein is named based on the absolute file path, joined to the vein name (in each JSON entry). These vein names must be unique. These are used for instance, in the `/findveins` command.

## Vein Parameters

Each vein object has a series of parameters that must be supplied:

- `minimum_height`: This is the minimum Y level the vein is allowed to spawn ores at. Veins on the edge will be cut off below this level.
- `maximum_height`: This is the maximum Y level that the vein is allowed to spawn ores at. Veins on the edge will be cut off above this level. This must be not be strictly smaller than `minimum_height`
- `rarity`: This is the approximate rarity of the vein. It must be an positive integer. On average veins will spawn in 1 / `rarity` chunks.
- `density`: This is the density of the vein. This is used as a modifier for each spawn location - it's not a percentage. It must be a non-negative integer. Higher density means more ores per vein, on average.
- `width`: This is the width of the vein, approximately, in blocks.
- `height`: This is the height of the vein, approximately, in blocks.
- `shape`: This is the shape of the vein. It must be a string. Currently (this will be the case until at least 1.15+), valid shapes are `sphere`, or `cluster`. Cluster is a collection of spheres around a central spawn location. 
- `base_rocks`: This is the list of rocks that the vein is allowed to spawn in. This may be rock names (e.g. `granite`), or [Rock Categories](#rock-categories) (e.g. `metamorphic`). A rock category indicates the vein can spawn in all rocks of that category.
- `loose`: The loose rock / ore item to spawn above the vein (surface samples). This can be an ore (in which case it will use the respective small ore item, or a direct item name.

In addition to the above, the vein must specify either an ore, or a block to spawn. An ore is used for TFC / TFC Addon ores, and will automatically use the ore of the stone that it spawns in. A block will spawn the same block regardless of stone type. That is, one of the following is required:

- To specify an ore, a `ore` field must be given. This must be a string, where the value is the name of the ore, as it is registered with TFC. Take a look at the default TFC ore generation for ore names, although when in doubt, the ore is always `lower_snake_case`, and prefixed with the mod that added it (e.g. `tfc:native_copper`).
- To specify an external block requires a `block` field and an optional `meta` (metadata) field. The `block` must be a string, specifying an exact block name (e.g. `minecraft:iron_ore`). If necessary, the `meta` field may be an integer in the closed interval `[0, 15]`, which will be used to get the correct block state based on the block and metadata. (If not provided, it defaults to `0`).

Additionally, to specify the loose rock (indicator item, found with sticks and rocks above ground), a `loose` field must be given. This must be a string, where the value is the name of the ore, as it is registered with TFC, or, the item/block registry name (e.g. `minecraft:egg`). If you need to specify a metadata, add an integer field called `looseMeta` (yes, `M` is upper case) with the value you want (e.g `"looseMeta": 30`)

## Rock Categories

Valid rock categories are `tfc:sedimentary`, `tfc:metamorphic`, `tfc:igneous_intrusive`, or `tfc:igneous_extrusive`, or any categories added by other mods (although this is highly unlikely and discouraged). They must be prefixed by the mod ID of the mod that added them. For examples, see the [default ore generation file](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/1.12.x/src/main/resources/assets/tfc/config/ore_spawn_data.json).

## Rocks

Rocks are all the rock types added by TFC. These names must be prefixed by the mod ID of the mod that added them. They are always `lower_snake_case`. For examples, see the [default ore generation file](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/1.12.x/src/main/resources/assets/tfc/config/ore_spawn_data.json).

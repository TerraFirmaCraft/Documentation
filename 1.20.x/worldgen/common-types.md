---
layout: page
title: "Common Types"
permalink: /1.20.x/worldgen/common-types/
---

# Common Types

There are a number of JSON types that are used in many different configurations for many different operations. These are all referenced here rather than repeating their definitions across every config they may belong to.

<!--linky_begin_sort_alphabetical-->

- [Biome Category](#biome-category)
- [Biome Dictionary](#biome-dictionary)
- [Block Replacement Map](#block-replacement-map)
- [Forest Type](#forest-type)
- [Holder Set](#holder-set)
- [Key Value List](#key-value-list)
- [Lenient Blockstate](#lenient-blockstate)
- [Structure](#structure)
- [Vertical Anchor](#vertical-anchor)
- [Weighted List](#weighted-list)

<!--linky_end_sort_alphabetical-->

<hr>

## Biome Category

A biome category is the `category` field of a biome. Valid values are:

- `none`, `tagia`, `extreme_hills`, `jungle`, `mesa`, `plains`, `savanna`, `icy`, `the_end`, `beach`, `forest`, `ocean`, `desert`, `river`, `swamp`, `mushroom`, `nether`, `underground`

<hr>

## Biome Dictionary

A biome dictionary tag is a tag, all uppercase (like `WET`), which describes a property of a biome. They are added by Forge and other mods.

<hr>

## Block Replacement Map

This defines a list of block -> block state replacements. For each block, it can be replaced with a random selection of blocks.

It is a [Key Value List](#key-value-list), with the following key and value entries:

- Key: `replace`: A block to be replaced.
- Value: `with`: A [Weighted List](#weighted-list) of objects, with the following value entry:
  - Value: `block`: A [Lenient Blockstate](#lenient-blockstate).

Example:

```json
[
    {
        "replace": "minecraft:stone",
        "with": [
            {
                "block": "minecraft:diamond_ore",
                "weight": 2
            },
            {
                "block": "minecraft:coal_ore",
                "weight": 10
            }
        ]
    },
    {
        "replace": "minecraft:dirt",
        "with": [
            {
                "block": "minecraft:grass"
            }
        ]
    }
]
```

<hr>

## Forest Type

A forest type is a string, from the following values:

- `none`, `sparse`, `edge`, `normal`, `old_growth`

When compared, they compare relative to the above order. (So, `normal` is considered "greater than" `edge`, for example.)

<hr>

## Holder Set

A Holder Set is a collection of elements of a given registry. For example, Configured Features, Placed Feature, or Biomes.

1. A List of strings, where each entry is the name of a given registry entry.
2. A String, prefixed by `#`, indicating a [Tag](../tags/)

<hr>

## Key Value List

This is a list that represents a map. It is a json array of objects, where each one has a key field, and a value field. There must be no duplicate key fields in the entire list.

Note, the names `key` and `value` may be different depending on the actual list in question.

Example:

```json
[
    {
        "key": "a key",
        "value": 3
    },
    {
        "key": "another key",
        "value": 6
    }
]
```

<hr>

## Lenient Blockstate

This is a more lenient version of the vanilla block state requirement. It can *either* be:

It is an object, with the following properties:

- `Name`: The registry name of the block to use
- `Properties`: An object with a collection of key -> value pairs for each block state property.

For example, the block state `minecraft:grass_block[snowy=false]` would become:

```json
{
    "Name": "minecraft:grass_block",
    "Properties": {
        "snowy": "false",
    }
}
```

Or, it can be a string with the registry name of the block to use. In this case, all block state properties will have their default values assigned, e.g. the above would be:

```json
"minecraft:grass_block"
```

<hr>

## Structure

A structure is a reference to an NBT file. They can be created and loaded using [Structure Blocks](https://minecraft.wiki/w/Structure_Block).

A structure file must have a file name such as `data/<domain>/structures/<path>.nbt`, which would then have the structure name `<domain>:<path>`.

#### Example

The structure [`data/tfc/structures/acacia/1.nbt`](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/1.18.x/src/main/resources/data/tfc/structures/acacia/1.nbt) is referenced as [`tfc:acacia/1`](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/e89f6c553e8178346c83a1266829c61437f0c50c/src/main/resources/data/tfc/worldgen/configured_feature/tree/acacia.json#L6).

<hr>

## Vertical Anchor

This represents a relative y height. It is an object with exactly one of the three following fields:

- `absolute`: An integer representing an absolute y height.
- `above_bottom`: An integer representing a number of blocks above the lowest y level in the world.
- `below_top`: An integer representing a number of blocks below the highest y level in the world.

Example (y = 63):
```json
{
    "absolute": 63
}
```

<hr>

## Weighted List

A weighted list is similar to a [Key Value List](#key-value-list) in that it is a list of pairs, except in this list, each object has two fields, where one is a `weight` entry. The `weight` determines the relative weight of that element of the list, and can be any positive number. The other entry might be any other field depending on the actual list in question.

The `weight` can also be omitted, in which case the entry will assume a default value of `1`.

Example:

```json
[
    {
        "value": "minecraft:coal",
        "weight": 1
    },
    {
        "value": "minecraft:diamond",
        "weight": 0.01
    }
]
```
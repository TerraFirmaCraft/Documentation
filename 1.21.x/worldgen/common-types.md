---
layout: page
title: "Common Types"
permalink: /1.21.x/worldgen/common-types/
---

# Common Types

There are a number of JSON types that are used in many different configurations for many different operations. These are all referenced here rather than repeating their definitions across every config they may belong to.

<!--linky_begin_sort_alphabetical-->

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

A forest type is a string. See the table for how forest types work. The density [`0`, `4`] roughly corresponds to how forest types `none` through `old_growth` used to work for those familiar with old versions. Thus, a `min_forest` and `max_forest` option has been provided in the Climate Placement if needed. Forests generally place trees which are closest to the center of their climate range. "Alternate" forest types change this by ignoring the first N trees in the climate-weighted list of eligible trees and thus look different, producing more variation. This replaced what was once "weirdness" in forest generation.

Many forest types place trees in every chunk, but some only rarely; this is the per-chunk chance. Primary forests are the oldest, and thus have old growth. Secondary forests lack old growth, and are more common. Monoculture forests spawn only one tree; diverse forests spawn much more.

| Forest type                  | Subtype     | Density | Tree count | Groundcover count | Leaf pile count | Bush count | Max tree types | Per-chunk chance | Alternate size |
|------------------------------|-------------|---------|------------|-------------------|-----------------|------------|----------------|------------------|----------------|
| `grassland`                  | `none`      | 0       | 0          | 0                 | 0               | 0          | 2              | 0                | 0              |
| `clearing`                   | `none`      | 0       | 0          | 0                 | 0               | 0          | 2              | 0                | 0              |
| `shrubland`                  | `none`      | 0       | 0          | 10                | 0 – 1           | 2 – 7      | 2              | 1                | 0              |
| `sparse`                     | `none`      | 0       | 2          | 6                 | 0               | 0 – 2      | 2              | 0.08             | 0              |
| `savanna_monoculture`        | `savanna`   | 1       | 3          | 6                 | 0               | 0 – 2      | 1              | 0.55             | 0              |
| `savanna_diverse`            | `savanna`   | 1       | 3          | 6                 | 0               | 0 – 2      | 2              | 0.65             | 0              |
| `savanna_alternate`          | `savanna`   | 1       | 3          | 6                 | 0               | 0 – 2      | 3              | 0.40             | 2              |
| `savanna_shrub_monoculture`  | `savanna`   | 1       | 1          | 6                 | 0               | 3 – 6      | 1              | 0.9              | 0              |
| `savanna_shrub_diverse`      | `savanna`   | 1       | 1          | 6                 | 0               | 3 – 6      | 2              | 1                | 0              |
| `savanna_shrub_alternate`    | `savanna`   | 1       | 1          | 6                 | 0               | 3 – 6      | 3              | 0.8              | 2              |
| `primary_monoculture`        | `primary`   | 3       | 5          | 25                | 0 – 1           | 0          | 1              | 1                | 0              |
| `primary_diverse`            | `primary`   | 4       | 7          | 40                | 0 – 1           | 0 – 3      | 2              | 1                | 0              |
| `primary_alternate`          | `primary`   | 4       | 7          | 40                | 0 – 1           | 0 – 3      | 3              | 1                | 2              |
| `secondary_monoculture`      | `secondary` | 3       | 5          | 25                | 0               | 1 – 2      | 1              | 1                | 0              |
| `secondary_monoculture_tall` | `secondary` | 3       | 5          | 25                | 0               | 1 – 2      | 1              | 1                | 0              |
| `secondary_diverse`          | `secondary` | 3       | 5          | 25                | 0               | 1 – 2      | 2              | 1                | 0              |
| `secondary_bamboo`           | `secondary` | 3       | 1          | 25                | 0 – 1           | 0 – 1      | 2              | 0.3              | 0              |
| `secondary_diverse_tall`     | `secondary` | 3       | 5          | 25                | 0               | 1 – 2      | 2              | 1                | 0              |
| `secondary_dense`            | `secondary` | 4       | 7          | 40                | 0 – 1           | 3          | 2              | 1                | 0              |
| `secondary_dense_tall`       | `secondary` | 4       | 7          | 40                | 0 – 1           | 3          | 2              | 1                | 0              |
| `secondary_alternate`        | `secondary` | 3       | 5          | 25                | 0               | 1 – 2      | 3              | 1                | 2              |
| `edge_monoculture`           | `edge`      | 2       | 2          | 10                | 0 – 1           | 0 – 1      | 1              | 1                | 0              |
| `edge_diverse`               | `edge`      | 2       | 2          | 10                | 0 – 1           | 0 – 1      | 2              | 1                | 0              |
| `edge_alternate`             | `edge`      | 2       | 2          | 10                | 0 – 1           | 0 – 1      | 3              | 1                | 2              |
| `edge_bamboo`                | `edge`      | 2       | 1          | 10                | 0 – 1           | 0 – 1      | 1              | 0.7              | 0              |
| `dead_monoculture`           | `dead`      | 2       | 5          | 25                | 0               | 2 – 4      | 1              | 1                | 0              |
| `dead_diverse`               | `dead`      | 2       | 5          | 25                | 0               | 2 – 4      | 2              | 1                | 0              |
| `dead_alternate`             | `dead`      | 3       | 4          | 40                | 0 – 1           | 0 – 3      | 3              | 1                | 2              |
| `dead_bamboo`                | `dead`      | 3       | 4          | 25                | 0 – 1           | 2 – 4      | 2              | 1                | 0              |

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
        "snowy": "false"
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
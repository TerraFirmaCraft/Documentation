---
layout: page
title: "Common Types"
permalink: /1.17.x/worldgen/common-types/
---

# Common Types

There are a number of JSON types that are used in many different configurations for many different operations. These are all referenced here rather than repeating their definitions across every config they may belong to.

### Lenient BlockState

This is a more lenient version of the vanilla block state requirement. It can *either* be:

A JSON object, with the following properties:

- `Name`: The registry name of the block to use
- `Properties`: An JSON object with a collection of key -> value pairs for each block state property.

For example, the block state `minecraft:grass_block[snowy=false]` would become:

```json
{
    "Name": "minecraft:grass_block",
    "Properties": {
        "snowy": "false",
    }
}
```

Or, it can be a JSON string with the registry name of the block to use. In this case, all block state properties will have their default values assigned, e.g. the above would be:

```java
"minecraft:grass_block"
```

### Forest Type

A forest type is a string, from the following values:

- `none`, `sparse`, `edge`, `normal`, `old_growth`

When compared, they compare realitive to the above order. (So, `normal` is considered "greater than" `edge`, for example.)


### Vertical Anchor

This represents a relative y height. It is an object with exactly one of the three following fields:

- `absolute`: An integer representing an absolute y height.
- `above_bottom`: An integer representing a number of blocks above the lowest y level in the world.
- `below_top`: An integer representing a number of blocks below the highest y level in the world.

Example (y = 63):
```java
{
    "absolute": 63
}
```
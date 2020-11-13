---
layout: page
title: "Common Types"
permalink: /1.16.x/worldgen/common-types/
---

# Common World Generation JSON Types

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

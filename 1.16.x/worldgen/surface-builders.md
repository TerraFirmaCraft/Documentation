---
layout: page
title: "Configured Surface Builders"
permalink: /1.16.x/worldgen/surface-builders/
---

# Configured Surface Builders

*[Vanilla Reference for Surface Builders](https://minecraft.gamepedia.com/Custom_world_generation#Surface_builders)*

When generating chunks, TFC uses only vanilla blocks - up until after surface generation - at which point all blocks in a chunk get replaced with TFC equivalent, that are selected based on the location and other information (for example, `minecraft:stone` gets converted to any of TFC's stone types based on the rock layer at that location). What this means is that the surface builders used by TFC occasionally produce weird or unrealistic blocks, as these are used as indicators later during generation and are replaced with something else.

{% include alert.html type="info" title="Note" content="Some of TFC's surface builders are IContextSurfaceBuilder instances. These surface builders must be used with a chunk generator that supports them." %}

TFC adds the following surface builder types:

- [Normal](#normal)
- [Thin](#thin)
- [Badlands](#badlands)
- [Mountains](#mountains)
- [Shore](#shore)
- [Underwater](#underwater)
- [With Glaciers](#with-glaciers)

### Normal

This is a TFC modified version of the vanilla default surface builder. Instead of using `underwater_material` it will use the Underwater surface builder instead.

- Type: `tfc:normal`
- Config:
  - `top_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the top material.
  - `under_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the subsurface material.

### Thin

This is a variant of the normal surface builder, that places no under material. It is used in TFC's canyon biomes.

- Type: `tfc:thin`
- Config:
  - `top_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the top material.
  - `under_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the subsurface material.

### Badlands

This surface builder will do different things above and below a specific y value (between 110 and 114, that varies by location). Beneath this cutoff, this surface builder will place one layer of TFC Red and Brown sand in an alternating pattern - similar to vanilla badlands. Above this layer, it will function as the TFC normal surface builder.

- Type: `tfc:thin`
- Config:
  - `top_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the top material.
  - `under_material`: A [Lenient BlockState](../common-types/#lenient-blockstate) representing the subsurface material.

### Mountains

This surface builder acts as a thin surface builder, but will also place patches of gravel, stone, and cobblestone.

- Type: `tfc:mountains`
- Config: None

### Shore

This is used to build TFC's shore biomes. It creates sand and gravel patches, which may later get replaced with different sand colors. Shores in tropical areas (Rainfall > 300 and Average temperature > 15) may have pink sand, other high rainfall areas (Rainfall > 300) may have black sand.

- Type: `tfc:shore`
- Config: None

### Underwater

This is used to all of TFC's underwater material. It creates sand and gravel patches based on the rock layer.

- Type: `tfc:underwater`
- Config: None

### With Glaciers

This is a special type of surface builder used in cold biomes. It is a `IContextSurfaceBuilder`, meaning it must be used with a compatible chunk generator. Based on the average temperature of the region, if it is cold enough, this surface builder will place a thick layer of packed ice and snow blocks on top of the surface. It also will freeze the top layers of water, creating large icebergs. Where the temperature is not cold enough, this will use the `parent` surface builder instead.

- Type: `tfc:with_glaciers`
- Config:
  - `parent`: A string, which is the name of a configured surface builder to use when there is no glacier at a given location.

Example:

```json

{
    "type": "tfc:with_glaciers",
    "config": {
        "parent": "tfc:mountains"
    }
}
```

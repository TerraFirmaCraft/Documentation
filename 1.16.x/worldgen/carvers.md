---
layout: page
title: "Configured Carvers"
permalink: /1.16.x/worldgen/carvers/
---

# Configured Carvers

*[Vanilla Reference for Carvers](https://minecraft.gamepedia.com/Custom_world_generation#Carvers)*

TFC handles carvers in a rather different way to vanilla. It delays carving until later in chunk generation, in order to have more context available at time of carving. In particular, this is how TFC's liquid and air caves avoid intersecting each other. This should have little to no effect on vanilla or other mod carvers, however, TFC carvers *must* be used with a chunk generator which supports them.

TFC's carvers are `IContextCarver` instances. It will produce an error to use one of these carvers with a chunk generator that does not support `IContextCarver`.

TFC adds the following carver types:

**Air Carvers**:

- [Cave](#cave)
- [Canyon](#canyon)
- [Worley Cave](#worley-cave)

**Underwater Carvers**:

- [Underwater Cave](#underwater-cave)
- [Underwater Canyon](#underwater-canyon)

### Cave

This is the vanilla "spaghetti" caves. It is tweaked to have a slightly higher starting Y value to accommodate TFC's sea level change. It has also been adjusted to account for gravity blocks when carving, and will pad cave entrances with stone.

- Type: `tfc:cave`
- Config:
  - `probability`: A float, representing the chance this cave will begin at a particular chunk.

Example:

```json
{
    "type": "tfc:cave",
    "config": {
        "probability": 0.1
    }
}

```

### Canyon

This is the vanilla ravine carver. It is tweaked to have a slightly higher starting Y value to accommodate TFC's sea level change. It has also been adjusted to account for gravity blocks when carving, and will pad cave entrances with stone.

- Type: `tfc:canyon`
- Config:
  - `probability`: A float, representing the chance this cave will begin at a particular chunk.

Example:

```json
{
    "type": "tfc:ravine",
    "config": {
        "probability": 0.015
    }
}
```

### Worley Cave

This is a custom noise based cave carver which generates caves using [Worley Noise](https://en.wikipedia.org/wiki/Worley_noise). It produces very large interconnected caves.

- Type: `tfc:worley_cave`
- Config: None

### Underwater Cave

This is an underwater version of the TFC cave carver.

- Type: `tfc:underwater_cave`
- Config:
  - `probability`: A float, representing the chance this cave will begin at a particular chunk.

### Underwater Canyon

This is an underwater version of the TFC ravine (canyon) carver.

- Type: `tfc:underwater_canyon`
- Config:
  - `probability`: A float, representing the chance this cave will begin at a particular chunk.

---
layout: page
title: "World Preset"
permalink: /1.21.x/worldgen/world-preset/
---

# World Presets

TFC adds a single world preset, which is used to generate a TFC world, and along with that, adds the TFC generator which has a number of important configuration options available. For the generic format of a world preset, see the [Minecraft Wiki](https://minecraft.wiki/w/World_preset_definition), or the [Example](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/1.21.x/src/generated/resources/data/tfc/worldgen/world_preset/overworld.json). This page is concerned with the `generator` field of the world preset.

The TFC world generator has the following fields:

- `type` must be `"tfc:overworld"`
- `biome_source` must be `{ "type": "tfc:overworld" }`
- `settings` is the name of a [Noise Settings](https://minecraft.wiki/w/Noise_settings) to use. The default is `"minecraft:overworld"`
- `tfc_settings` is an object with various settings that affect TFC world generation. It has the following fields:
  - `flat_bedrock` (Boolean): If the bottom of the world is a single layer of flat bedrock, or random like vanilla
  - `spawn_center_x` (Integer): The center X position around which the spawn position is chosen
  - `spawn_center_z` (Integer): The center Z position around which the spawn position is chosen
  - `spawn_distance` (Integer): The maximum distance from the spawn center the spawn position will be chosen
  - `temperature_scale` (Integer): The distance between two temperature extremes, in blocks. If zero, the temperature will be a constant based on `temperature_constant`
  - `temperature_constant` (Optional Number, Default `0`). A number representing the temperature for an entire world, where `-1.0` is polar and `1.0` is tropical.
  - `rainfall_scale` (Integer): The distance between two rainfall extremes, in blocks. If zero, the rainfall will be a constant based on `rainfall_constant`
  - `rainfall_constant` (Optional Number, Default `0`): A number representing the rainfall for an entire world, where `-1.0` is arid and `1.0` is tropical.
  - `rock_layer_settings` is the [Rock Layer Settings](#rock-layer-settings) for a world.
  - `continentalness` (Number): This is a value between `-1.0` and `1.0` which determines the nature of continents. Smaller values create smaller continents, more islands, whereas larger values create larger, blobbier continents.
  - `grass_density` (Optional Number, Default `0.5`): This is a number which affects how much grass generates in the world. Higher values indicate more grass coverage. 
  - `finite_continents` (Boolean): If the world should generate only a few continents, leaving a vast ocean beyond.

### Rock Layer Settings

This describes the rocks that exist in the world, what blocks they use, and how they spawn. It is useful to understand how rock layers generate in TFC:

First, TFC picks the overall **Layer Type** of the area. This may be one of `ocean_floor` (Oceans), `volcanic` (Volcanic islands, and volcanic mountains), `uplift` (Inland mountains), or `land` (All other non-ocean areas). It then looks in the rock layer settings for what [Layer](#rock-layer) correspond to that **Layer Type**.

#### Rock Layer

A **Layer** consists of an object, with two fields:

- `id` (String) The name or ID of the layer
- `layers` (Object) A map of **Rock** IDs to **Layer** IDs

##### Example

```jsonc
// A single "Layer", named "igneous_extrusive", with four rocks (rhyolite, andesite, dacite, and basalt),
// mapped to three layers (felsic, intermediate, and mafic)
{
  "id": "igneous_extrusive",
  "layers": {
    "rhyolite": "felsic",
    "andesite": "intermediate",
    "dacite": "intermediate",
    "basalt": "mafic"
  }
}
```

#### Rock

A **Rock** is a collection of mappings of a name to the resulting blocks that are used for that rock. It can be either, a preset name (these are registered by TFC for ease of use), or an object with the following fields:

- `raw`, `hardened`, `gravel`, `cobble`, `sand`, `sandstone` (String) These are names of blocks that are used for this rock in the respective places in world generation
- `spike`, `mossy`, `mossy_loose` (Optional String) These are names of blocks that are used for this rock in the respective places in world generation, but are optional, and won't generate if not present.
- `karst` and `mafic` (Optional Boolean) if these rocks are mafic or karst types.

##### Example

```jsonc
// An example "Rock" using default TFC blocks
{
  "raw": "tfc:rock/raw/basalt",
  "hardened": "tfc:rock/hardened/basalt",
  "gravel": "tfc:rock/gravel/basalt",
  "cobble": "tfc:rock/cobble/basalt",
  "sand": "tfc:sand/red",
  "sandstone": "tfc:raw_sandstone/red",
}
```

When considering a layer, TFC will pick a random **Rock** from that layer, and then move onto the following **Layer**, before repeating the process. For example here, TFC could place `basalt`, and then under the basalt, would be a rock from the `mafic` layer.

There is a special **Layer** named `bottom` - This is a layer consisting only of a list of **Rocks**. Once the `bottom` layer is reached, any further rocks underneath it will repeat endlessly from the `bottom` layer (until there are no more Y positions left to generate).

With all that in mind, a **Rock Layer Settings** has the following fields:

- `rocks` is an object which is a map of **Rock** IDs, to [Rock](#rock) objects, or preset names.
- `bottom` is a list of **Rock** IDs, which form the `bottom` layer
- `layers` is a list of all the [Layers](#rock-layer) which exist
- `ocean_floor`, `volcanic`, `uplift`, and `land` are each the default **Layer Types**. They are each a list of the **Layer** IDs which are used for the top rock of each type.

##### Example

```jsonc
// This is the default rock layer settings used by TFC, found at
// data/tfc/worldgen/world_preset/overworld.json
{
    "bottom": [
      "gneiss",
      "schist",
      "diorite",
      "granite",
      "gabbro"
    ],
    "land": [
      "igneous_extrusive",
      "sedimentary"
    ],
    "layers": [
      {
        "id": "felsic",
        "layers": {
          "granite": "bottom"
        }
      },
      {
        "id": "intermediate",
        "layers": {
          "diorite": "bottom"
        }
      },
      {
        "id": "mafic",
        "layers": {
          "gabbro": "bottom"
        }
      },
      {
        "id": "igneous_extrusive",
        "layers": {
          "andesite": "intermediate",
          "basalt": "mafic",
          "dacite": "intermediate",
          "rhyolite": "felsic"
        }
      },
      {
        "id": "igneous_extrusive_x2",
        "layers": {
          "andesite": "igneous_extrusive",
          "basalt": "igneous_extrusive",
          "dacite": "igneous_extrusive",
          "rhyolite": "igneous_extrusive"
        }
      },
      {
        "id": "high_grade",
        "layers": {
          "gneiss": "bottom",
          "schist": "bottom"
        }
      },
      {
        "id": "low_grade",
        "layers": {
          "phyllite": "high_grade",
          "slate": "high_grade"
        }
      },
      {
        "id": "marble",
        "layers": {
          "marble": "bottom"
        }
      },
      {
        "id": "quartzite",
        "layers": {
          "quartzite": "bottom"
        }
      },
      {
        "id": "sedimentary",
        "layers": {
          "chalk": "marble",
          "chert": "quartzite",
          "claystone": "low_grade",
          "conglomerate": "low_grade",
          "dolomite": "marble",
          "limestone": "marble",
          "shale": "low_grade"
        }
      },
      {
        "id": "uplift",
        "layers": {
          "diorite": "low_grade",
          "gabbro": "low_grade",
          "granite": "low_grade",
          "marble": "bottom",
          "phyllite": "high_grade",
          "quartzite": "bottom",
          "slate": "high_grade"
        }
      }
    ],
    "ocean_floor": [
      "igneous_extrusive"
    ],
    "rocks": {
      "andesite": {
        "cobble": "tfc:rock/cobble/andesite",
        "gravel": "tfc:rock/gravel/andesite",
        "hardened": "tfc:rock/hardened/andesite",
        "karst": false,
        "loose": "tfc:rock/loose/andesite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/andesite",
        "raw": "tfc:rock/raw/andesite",
        "sand": "tfc:sand/red",
        "sandstone": "tfc:raw_sandstone/red",
        "spike": "tfc:rock/spike/andesite"
      },
      "basalt": {
        "cobble": "tfc:rock/cobble/basalt",
        "gravel": "tfc:rock/gravel/basalt",
        "hardened": "tfc:rock/hardened/basalt",
        "karst": false,
        "loose": "tfc:rock/loose/basalt",
        "mafic": true,
        "mossy_loose": "tfc:rock/mossy_loose/basalt",
        "raw": "tfc:rock/raw/basalt",
        "sand": "tfc:sand/black",
        "sandstone": "tfc:raw_sandstone/black",
        "spike": "tfc:rock/spike/basalt"
      },
      "chalk": {
        "cobble": "tfc:rock/cobble/chalk",
        "gravel": "tfc:rock/gravel/chalk",
        "hardened": "tfc:rock/hardened/chalk",
        "karst": true,
        "loose": "tfc:rock/loose/chalk",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/chalk",
        "raw": "tfc:rock/raw/chalk",
        "sand": "tfc:sand/white",
        "sandstone": "tfc:raw_sandstone/white",
        "spike": "tfc:rock/spike/chalk"
      },
      "chert": {
        "cobble": "tfc:rock/cobble/chert",
        "gravel": "tfc:rock/gravel/chert",
        "hardened": "tfc:rock/hardened/chert",
        "karst": false,
        "loose": "tfc:rock/loose/chert",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/chert",
        "raw": "tfc:rock/raw/chert",
        "sand": "tfc:sand/red",
        "sandstone": "tfc:raw_sandstone/red",
        "spike": "tfc:rock/spike/chert"
      },
      "claystone": {
        "cobble": "tfc:rock/cobble/claystone",
        "gravel": "tfc:rock/gravel/claystone",
        "hardened": "tfc:rock/hardened/claystone",
        "karst": false,
        "loose": "tfc:rock/loose/claystone",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/claystone",
        "raw": "tfc:rock/raw/claystone",
        "sand": "tfc:sand/brown",
        "sandstone": "tfc:raw_sandstone/brown",
        "spike": "tfc:rock/spike/claystone"
      },
      "conglomerate": {
        "cobble": "tfc:rock/cobble/conglomerate",
        "gravel": "tfc:rock/gravel/conglomerate",
        "hardened": "tfc:rock/hardened/conglomerate",
        "karst": false,
        "loose": "tfc:rock/loose/conglomerate",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/conglomerate",
        "raw": "tfc:rock/raw/conglomerate",
        "sand": "tfc:sand/brown",
        "sandstone": "tfc:raw_sandstone/brown",
        "spike": "tfc:rock/spike/conglomerate"
      },
      "dacite": {
        "cobble": "tfc:rock/cobble/dacite",
        "gravel": "tfc:rock/gravel/dacite",
        "hardened": "tfc:rock/hardened/dacite",
        "karst": false,
        "loose": "tfc:rock/loose/dacite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/dacite",
        "raw": "tfc:rock/raw/dacite",
        "sand": "tfc:sand/red",
        "sandstone": "tfc:raw_sandstone/red",
        "spike": "tfc:rock/spike/dacite"
      },
      "diorite": {
        "cobble": "tfc:rock/cobble/diorite",
        "gravel": "tfc:rock/gravel/diorite",
        "hardened": "tfc:rock/hardened/diorite",
        "karst": false,
        "loose": "tfc:rock/loose/diorite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/diorite",
        "raw": "tfc:rock/raw/diorite",
        "sand": "tfc:sand/red",
        "sandstone": "tfc:raw_sandstone/red",
        "spike": "tfc:rock/spike/diorite"
      },
      "dolomite": {
        "cobble": "tfc:rock/cobble/dolomite",
        "gravel": "tfc:rock/gravel/dolomite",
        "hardened": "tfc:rock/hardened/dolomite",
        "karst": true,
        "loose": "tfc:rock/loose/dolomite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/dolomite",
        "raw": "tfc:rock/raw/dolomite",
        "sand": "tfc:sand/white",
        "sandstone": "tfc:raw_sandstone/white",
        "spike": "tfc:rock/spike/dolomite"
      },
      "gabbro": {
        "cobble": "tfc:rock/cobble/gabbro",
        "gravel": "tfc:rock/gravel/gabbro",
        "hardened": "tfc:rock/hardened/gabbro",
        "karst": false,
        "loose": "tfc:rock/loose/gabbro",
        "mafic": true,
        "mossy_loose": "tfc:rock/mossy_loose/gabbro",
        "raw": "tfc:rock/raw/gabbro",
        "sand": "tfc:sand/black",
        "sandstone": "tfc:raw_sandstone/black",
        "spike": "tfc:rock/spike/gabbro"
      },
      "gneiss": {
        "cobble": "tfc:rock/cobble/gneiss",
        "gravel": "tfc:rock/gravel/gneiss",
        "hardened": "tfc:rock/hardened/gneiss",
        "karst": false,
        "loose": "tfc:rock/loose/gneiss",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/gneiss",
        "raw": "tfc:rock/raw/gneiss",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/gneiss"
      },
      "granite": {
        "cobble": "tfc:rock/cobble/granite",
        "gravel": "tfc:rock/gravel/granite",
        "hardened": "tfc:rock/hardened/granite",
        "karst": false,
        "loose": "tfc:rock/loose/granite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/granite",
        "raw": "tfc:rock/raw/granite",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/granite"
      },
      "limestone": {
        "cobble": "tfc:rock/cobble/limestone",
        "gravel": "tfc:rock/gravel/limestone",
        "hardened": "tfc:rock/hardened/limestone",
        "karst": true,
        "loose": "tfc:rock/loose/limestone",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/limestone",
        "raw": "tfc:rock/raw/limestone",
        "sand": "tfc:sand/white",
        "sandstone": "tfc:raw_sandstone/white",
        "spike": "tfc:rock/spike/limestone"
      },
      "marble": {
        "cobble": "tfc:rock/cobble/marble",
        "gravel": "tfc:rock/gravel/marble",
        "hardened": "tfc:rock/hardened/marble",
        "karst": true,
        "loose": "tfc:rock/loose/marble",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/marble",
        "raw": "tfc:rock/raw/marble",
        "sand": "tfc:sand/white",
        "sandstone": "tfc:raw_sandstone/white",
        "spike": "tfc:rock/spike/marble"
      },
      "phyllite": {
        "cobble": "tfc:rock/cobble/phyllite",
        "gravel": "tfc:rock/gravel/phyllite",
        "hardened": "tfc:rock/hardened/phyllite",
        "karst": false,
        "loose": "tfc:rock/loose/phyllite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/phyllite",
        "raw": "tfc:rock/raw/phyllite",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/phyllite"
      },
      "quartzite": {
        "cobble": "tfc:rock/cobble/quartzite",
        "gravel": "tfc:rock/gravel/quartzite",
        "hardened": "tfc:rock/hardened/quartzite",
        "karst": false,
        "loose": "tfc:rock/loose/quartzite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/quartzite",
        "raw": "tfc:rock/raw/quartzite",
        "sand": "tfc:sand/white",
        "sandstone": "tfc:raw_sandstone/white",
        "spike": "tfc:rock/spike/quartzite"
      },
      "rhyolite": {
        "cobble": "tfc:rock/cobble/rhyolite",
        "gravel": "tfc:rock/gravel/rhyolite",
        "hardened": "tfc:rock/hardened/rhyolite",
        "karst": false,
        "loose": "tfc:rock/loose/rhyolite",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/rhyolite",
        "raw": "tfc:rock/raw/rhyolite",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/rhyolite"
      },
      "schist": {
        "cobble": "tfc:rock/cobble/schist",
        "gravel": "tfc:rock/gravel/schist",
        "hardened": "tfc:rock/hardened/schist",
        "karst": false,
        "loose": "tfc:rock/loose/schist",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/schist",
        "raw": "tfc:rock/raw/schist",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/schist"
      },
      "shale": {
        "cobble": "tfc:rock/cobble/shale",
        "gravel": "tfc:rock/gravel/shale",
        "hardened": "tfc:rock/hardened/shale",
        "karst": false,
        "loose": "tfc:rock/loose/shale",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/shale",
        "raw": "tfc:rock/raw/shale",
        "sand": "tfc:sand/brown",
        "sandstone": "tfc:raw_sandstone/brown",
        "spike": "tfc:rock/spike/shale"
      },
      "slate": {
        "cobble": "tfc:rock/cobble/slate",
        "gravel": "tfc:rock/gravel/slate",
        "hardened": "tfc:rock/hardened/slate",
        "karst": false,
        "loose": "tfc:rock/loose/slate",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/slate",
        "raw": "tfc:rock/raw/slate",
        "sand": "tfc:sand/yellow",
        "sandstone": "tfc:raw_sandstone/yellow",
        "spike": "tfc:rock/spike/slate"
      },
      "tuff": {
        "cobble": "tfc:rock/cobble/tuff",
        "gravel": "tfc:rock/gravel/tuff",
        "hardened": "tfc:rock/hardened/tuff",
        "karst": false,
        "loose": "tfc:rock/loose/tuff",
        "mafic": false,
        "mossy_loose": "tfc:rock/mossy_loose/tuff",
        "raw": "tfc:rock/raw/tuff",
        "sand": "tfc:sand/green",
        "sandstone": "tfc:raw_sandstone/green",
        "spike": "tfc:rock/spike/tuff"
      }
    },
    "uplift": [
      "sedimentary",
      "uplift"
    ],
    "volcanic": [
      "igneous_extrusive",
      "igneous_extrusive_x2"
    ]
  }
```

---
layout: page
title: "Biomes"
permalink: /1.18.x/worldgen/biomes/
---

# Biomes

TFC adds a total of 288 biomes. These are organized into a biome type, and then climate variants for both rainfall and temperature.

- Biome types determine the overall shape of the land, and the features that are generated. They **do not** determine the temperature, rainfall, or other climate related features.
- Low Altitude Continental Biomes:
  - Plains, Hills, Lowlands, Low Canyons
- Mid Altitude Continental Biomes:
  - Rolling Hills, Badlands, Plateau, Canyons.
- High Altitude Continental Biomes:
  - Mountains, Old Mountains, Oceanic Mountains, Volcanic Mountains, Volcanic Oceanic Mountains.
- Oceanic Biomes:
  - Ocean, Ocean Reef, Deep Ocean, Deep Ocean Trench
- Technical / Decoration Biomes:
  - Shore
  - Lake, Plateau Lake, Mountains Lake, Old Mountains Lake, Oceanic Mountains Lake, Volcanic Mountains Lake, Volcanic Oceanic Mountains Lake.
  - River, Mountains River, Old Mountains River, Volcanic Mountains River, Oceanic Mountains River, Volcanic Oceanic Mountains River.
- Temperature variants are one of Cold, Normal, and Warm.
- Rainfall variants are one of Dry, Normal, and Wet.

The resultant biome will have a registry name in the form `[type]_[temperature]_[rainfall]`, for example `tfc:badlands_cold_wet`. All possible TFC biomes, and their world generation JSON can be found [here](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.18.x/src/main/resources/data/tfc/worldgen/biome).

{% include alert.html type="info" title="Note" content="Due to fundamental issues with Mojang's biome jsons, the only way to add, remove, or edit any features of biomes is to override the entire biome. There are work in progress plans to fix this, both from Forge's end, and eventually, on our end." %}

### TFC Ignored Properties

TFC ignores several properties of biomes in favor of other methods. TFC redirects vanilla methods to call TFC-enhanced methods for functions such as temperature, rainfall, or sky color. These will only apply to biomes which have extensions registered (aka, TFC recognizes them). In these cases, other mods may still use these properties but within TFC and vanilla they will be ignored.

- `depth` and `scale` are ignored completely - they are not used at all by the TFC chunk generator, TFC uses completely custom noise generators for it's terrain.
- `temperature`, `temperature_modifier`, and `downfall` and `precipitation` are ignored in the default TFC overworld, or dimensions with custom TFC climate support.
- In `effects`, `fog_color`, `sky_color`, `water_color`, and `water_color` are ignored. They are instead queried based off a color map texture file (In `tfc:textures/colormap/*.png`), based off of the actual rainfall and temperature of an area.

### Using Non-TFC Biomes in TFC

In order to use non-TFC biomes in TFC, there are a couple requirements:

- In order to use non-TFC biomes with a TFC biome source, the biomes must have a `BiomeExtension` registered. This object is responsible for identifying TFC biomes so that various hooks replace calls to biome methods with ones with TFC enhanced methods.
- In order to use non-TFC biomes with a TFC chunk generator, the biomes must *additionally* have a valid `BiomeVariants` attached. This object is responsible for integrating with the chunk generator, and includes noise generation and noise blending groups.
- If you want TFC biomes to be *generated* by the TFC biome source, this will very likely require custom hooks based on the sophistication of injections into the biome layer generation. Please consult us on discord with the nature of what you are attempting.

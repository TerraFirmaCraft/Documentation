---
layout: page
title: "Biomes"
permalink: /1.16.x/worldgen/biomes/
---

# Biomes

TFC adds a total of 425 biomes. These are organized into a biome type, and then climate variants.

- Biome types are one of Ocean, Deep Ocean, Plains, Hills, Lowlands, Low Canyons, Rolling Hills, Badlands, Plateau, Old Mountains, Mountains, Flooded Mountains, Canyons, Shore, Lake, River, Mountain River.
- Temperature variants are one of Frozen, Cold, Normal, Lukewarm, Warm.
- Rainfall variants are one of Arid, Dry, Normal, Damp, Wet.

The resultant biome will have a registry name in the form `[type]_[temperature]_[rainfall]`, for example `tfc:badlands_cold_wet`.

### TFC Ignored Properties

TFC ignores several properties of biomes in favor of other methods. TFC redirects vanilla methods to call TFC-enhanced methods for functions such as temperature, rainfall, or sky color. These will only apply to biomes which have extensions registered (aka, TFC recognizes them). In these cases, other mods may still use these properties but within TFC and vanilla they will be ignored.

- `precipitation` is ignored completely, it is queried based on the actual temperature and rainfall of the area.
- `depth` and `scale` are ignored completely - they are not used at all by the TFC chunk generator, TFC uses completely custom noise generators for it's terrain.
- `temperature`, `temperature_modifier`, and `downfall` are ignored completely, they are replaced with TFC climate calculations.
- In `effects`, `fog_color`, `sky_color`, `water_color`, and `water_color` are ignored. They are instead queried based off a color map texture file (In `tfc:textures/colormap/*.png`), based off of the actual rainfall and temperature of an area.

### Using Non-TFC Biomes in TFC

In order to use non-TFC biomes in TFC, there are a couple requirements:

- In order to use non-TFC biomes with a TFC biome source, the biomes must have a `BiomeExtension` registered. This object is responsible for identifying TFC biomes so that various hooks replace calls to biome methods with ones with TFC enhanced methods.
- In order to use non-TFC biomes with a TFC chunk generator, the biomes must *additionally* have a valid `BiomeVariants` attached. This object is responsible for integrating with the chunk generator, and includes noise generation and noise blending groups.
- If you want TFC biomes to be *generated* by the TFC biome source, this will very likely require custom hooks based on the sophistication of injections into the biome layer generation.

# Arclight Material Tag List Generator

This Python script automates the process of extracting material tags from Minecraft mods and the base game, generating a comprehensive JSON file. This is particularly useful for server administrators and plugin developers using Arclight, which supports modded materials within Spigot plugin configurations.

## Why This Tool?

Platforms like Arclight allow you to use modded materials in Spigot plugin configurations. However, manually finding and listing all the available materials and tags can be tedious and time-consuming. This script solves this problem by:

* **Automating Extraction:** It scans your mod folder and the Minecraft client JAR to extract all block material tags.
* **Comprehensive Lists:** It generates a single JSON file containing all material tags and their associated materials.
* **Faster Configuration:** This makes it significantly quicker and easier to configure plugins that use modded materials.

## How It Works

1.  **Downloads Minecraft Client JAR:** The script downloads the specified Minecraft client JAR from Mojang's official servers.
2.  **Extracts Tags:** It scans the downloaded JAR and all JAR files in your specified mods folder, extracting block material tags.
3.  **Generates JSON:** It compiles all extracted tags and materials into a `materials_tags.json` file.

## Configuration

1.  **Install Python:** Ensure you have Python 3.6 or later installed.
2.  **Place Mods:** Put all your Minecraft mod JAR files into a folder named `mods` in the same directory as the script.
3.  **Run the Script:**
    * Open a terminal or command prompt.
    * Navigate to the script's directory.
    * Run the script: `python main.py`
4.  **Configure Version:**
    * To change the Minecraft version, modify the `version` variable in the `main()` function within the script. For example: `version = "1.18.2"`
5.  **Configure Mods Folder:**
    * To change the mods folder, modify the `mods_folder` variable in the `main()` function within the script. For example: `mods_folder = "./my_custom_mods_folder"`
6.  **Output:** The generated `materials_tags.json` file will be created in the same directory as the script.

## Example Usage (Arclight)

After running the script, you can use the generated `materials_tags.json` file to quickly find the material names and tags you need for your Arclight plugin configurations.

Example JSON output:

```json
{
    "#dirt": [
        "#AETHER_AETHER_DIRT",
        "BIOMEMAKEOVER_MOSSY_PEAT",
        "BIOMEMAKEOVER_PEAT",
        "BIOMESWEVEGONE_LUSH_DIRT",
        "BIOMESWEVEGONE_LUSH_GRASS_BLOCK",
        "BIOMESWEVEGONE_OVERGROWN_DACITE",
        "BIOMESWEVEGONE_OVERGROWN_STONE",
        "BIOMESWEVEGONE_PEAT",
        "BIOMESWEVEGONE_PODZOL_DACITE",
        "BIOMESWEVEGONE_SANDY_DIRT",
        "CHIPPED_ANGRY_DIRT",
        "CHIPPED_BLANK_DIRT_CARVING",
        "CHIPPED_BORDERED_DIRT",
        "CHIPPED_BRICK_BORDERED_DIRT",
        "CHIPPED_CARVED_DIRT",
        "CHIPPED_CHECKERED_DIRT_TILES",
        "CHIPPED_COBBLED_DIRT",
        "CHIPPED_CRACKED_DIRT_BRICKS",
        "CHIPPED_CRACKED_DISORDERED_DIRT_BRICKS",
        "CHIPPED_CRACKED_FLAT_DIRT_TILES",
        "CHIPPED_CREEPER_DIRT_CARVING",
        "CHIPPED_CRYING_DIRT",
        "CHIPPED_CURLY_DIRT_PILLAR",
        "CHIPPED_CUT_BLANK_DIRT",
        "CHIPPED_CUT_DIRT_COLUMN",
        "CHIPPED_DIRT_BRICKS",
        "CHIPPED_DIRT_MINI_TILES",
        "CHIPPED_DIRT_PILLAR",
        "CHIPPED_DIRT_PILLAR_TOP",
        "CHIPPED_DIRT_SCALES",
        "CHIPPED_DUH_DIRT",
        "CHIPPED_EDGED_DIRT_BRICKS",
        "CHIPPED_ENGRAVED_DIRT",
        "CHIPPED_ERODED_DIRT",
        "CHIPPED_ETCHED_DIRT_BRICKS",
        "CHIPPED_FINE_DIRT_PILLAR",
        "CHIPPED_FLAT_DIRT_TILES",
        "CHIPPED_GLAD_DIRT",
        "CHIPPED_INLAYED_DIRT",
        "CHIPPED_INSCRIBED_DIRT",
        "CHIPPED_LAYED_DIRT_BRICKS",
        "CHIPPED_LODED_DIRT",
        "CHIPPED_MASSIVE_DIRT_BRICKS",
        "CHIPPED_OFFSET_DIRT_BRICKS",
        "CHIPPED_ORNATE_DIRT_PILLAR",
        "CHIPPED_OVERLAPPING_DIRT_TILES",
        "CHIPPED_PILLAR_DIRT_BRICKS",
        "CHIPPED_POLISHED_DIRT",
        "CHIPPED_PRISMAL_DIRT_REMNANTS",
        "CHIPPED_ROUGH_DIRT",
        "CHIPPED_ROUNDED_DIRT_BRICKS",
        "CHIPPED_RUNIC_CARVED_DIRT",
        "CHIPPED_SAD_DIRT",
        "CHIPPED_SANDED_DIRT",
        "CHIPPED_SIMPLE_DIRT_PILLAR",
        "CHIPPED_SMALL_DIRT_BRICKS",
        "CHIPPED_SMOOTHED_DOUBLE_INLAYED_DIRT",
        "CHIPPED_SMOOTH_DIRT_COLUMN",
        "CHIPPED_SMOOTH_INLAYED_DIRT",
        "CHIPPED_SMOOTH_RINGED_DIRT",
        "CHIPPED_SPIDER_DIRT_CARVING",
        "CHIPPED_SPIRALED_DIRT",
        "CHIPPED_STACKED_DIRT_BRICKS",
        "CHIPPED_THICK_INLAYED_DIRT",
        "CHIPPED_TILED_BORDERED_DIRT",
        "CHIPPED_TILED_DIRT",
        "CHIPPED_TILED_DIRT_COLUMN",
        "CHIPPED_TINY_BRICK_BORDERED_DIRT",
        "CHIPPED_TINY_DIRT_BRICKS",
        "CHIPPED_TINY_LAYERED_DIRT_BRICKS",
        "CHIPPED_TINY_LAYERED_DIRT_SLABS",
        "CHIPPED_TRODDEN_DIRT",
        "CHIPPED_UNAMUSED_DIRT",
        "CHIPPED_VERTICAL_CUT_DIRT",
        "CHIPPED_VERTICAL_DISORDERED_DIRT_BRICKS",
        "CHIPPED_WEATHERED_DIRT",
        "DEEPERDARKER_BLOOMING_MOSS_BLOCK",
        "DIRT",
        "FARMERSDELIGHT_RICH_SOIL",
        "GALOSPHERE_LICHEN_MOSS",
        "GRAVEYARD_SOIL",
        "GRAVEYARD_TG_COARSE_DIRT",
        "GRAVEYARD_TG_DIRT",
        "GRAVEYARD_TG_GRASS_BLOCK",
        "GRAVEYARD_TG_MOSS_BLOCK",
        "GRAVEYARD_TG_ROOTED_DIRT",
        "GRAVEYARD_TURF",
        "IMMERSIVE_WEATHERING_EARTHEN_CLAY",
        "IMMERSIVE_WEATHERING_GRASSY_EARTHEN_CLAY",
        "IMMERSIVE_WEATHERING_GRASSY_PERMAFROST",
        "IMMERSIVE_WEATHERING_GRASSY_SANDY_DIRT",
        "IMMERSIVE_WEATHERING_GRASSY_SILT",
        "IMMERSIVE_WEATHERING_LOAM",
        "IMMERSIVE_WEATHERING_MULCH_BLOCK",
        "IMMERSIVE_WEATHERING_PERMAFROST",
        "IMMERSIVE_WEATHERING_ROOTED_GRASS_BLOCK",
        "IMMERSIVE_WEATHERING_SANDY_DIRT",
        "IMMERSIVE_WEATHERING_SILT",
        "ITER_RPG_WITCHMUD",
        "LUMINOUS_NETHER_FUNGIRRACK",
        "LUMINOUS_NETHER_GOLDEN_NYLIUM",
        "MINECRAFT_COARSE_DIRT",
        "MINECRAFT_DIRT",
        "MINECRAFT_GRASS_BLOCK",
        "MINECRAFT_MOSS_BLOCK",
        "MINECRAFT_MUD",
        "MINECRAFT_MUDDY_MANGROVE_ROOTS",
        "MINECRAFT_MYCELIUM",
        "MINECRAFT_PODZOL",
        "MINECRAFT_ROOTED_DIRT"
    ],
    "#ores": [
        "#FORGE_ORES/JADE",
        "#FORGE_ORES/SILVER",
        "#FORGE_ORES/STELLA_ARCANUM",
        "#FORGE_ORES/URANIUM",
        "#FORGE_ORES/XPETRIFIED_ORE",
        "#MINECRAFT_COAL_ORES",
        "#MINECRAFT_COPPER_ORES",
        "#MINECRAFT_DIAMOND_ORES",
        "#MINECRAFT_EMERALD_ORES",
        "#MINECRAFT_GOLD_ORES",
        "#MINECRAFT_IRON_ORES",
        "#MINECRAFT_LAPIS_ORES",
        "#MINECRAFT_REDSTONE_ORES",
        "AETHER_AMBROSIUM_ORE",
        "AETHER_GRAVITITE_ORE",
        "AETHER_ZANITE_ORE",
        "CREATE_DEEPSLATE_ZINC_ORE",
        "CREATE_ZINC_ORE",
        "DEEPERDARKER_GLOOMSLATE_COAL_ORE",
        "DEEPERDARKER_GLOOMSLATE_COPPER_ORE",
        "DEEPERDARKER_GLOOMSLATE_DIAMOND_ORE",
        "DEEPERDARKER_GLOOMSLATE_EMERALD_ORE",
        "DEEPERDARKER_GLOOMSLATE_GOLD_ORE",
        "DEEPERDARKER_GLOOMSLATE_IRON_ORE",
        "DEEPERDARKER_GLOOMSLATE_LAPIS_ORE",
        "DEEPERDARKER_GLOOMSLATE_REDSTONE_ORE",
        "DEEPERDARKER_SCULK_STONE_COAL_ORE",
        "DEEPERDARKER_SCULK_STONE_COPPER_ORE",
        "DEEPERDARKER_SCULK_STONE_DIAMOND_ORE",
        "DEEPERDARKER_SCULK_STONE_EMERALD_ORE",
        "DEEPERDARKER_SCULK_STONE_GOLD_ORE",
        "DEEPERDARKER_SCULK_STONE_IRON_ORE",
        "DEEPERDARKER_SCULK_STONE_LAPIS_ORE",
        "DEEPERDARKER_SCULK_STONE_REDSTONE_ORE",
        "EIDOLON_DEEP_LEAD_ORE",
        "EIDOLON_DEEP_SILVER_ORE",
        "EIDOLON_LEAD_ORE",
        "EIDOLON_SILVER_ORE",
        "ICEANDFIRE_DEEPSLATE_SILVER_ORE",
        "ICEANDFIRE_SAPPHIRE_ORE",
        "ICEANDFIRE_SILVER_ORE",
        "MALUM_BLAZING_QUARTZ_ORE",
        "MALUM_BRILLIANT_DEEPSLATE",
        "MALUM_BRILLIANT_STONE",
        "MALUM_CTHONIC_GOLD_ORE",
        "MALUM_DEEPSLATE_QUARTZ_ORE",
        "MALUM_DEEPSLATE_SOULSTONE_ORE",
        "MALUM_NATURAL_QUARTZ_ORE",
        "MALUM_SOULSTONE_ORE",
        "MEADOW_ALPINE_COAL_ORE",
        "MEADOW_ALPINE_COPPER_ORE",
        "MEADOW_ALPINE_DIAMOND_ORE",
        "MEADOW_ALPINE_EMERALD_ORE",
        "MEADOW_ALPINE_GOLD_ORE",
        "MEADOW_ALPINE_IRON_ORE",
        "MEADOW_ALPINE_LAPIS_ORE",
        "MEADOW_ALPINE_REDSTONE_ORE",
        "MEADOW_ALPINE_SALT_ORE",
        "MINECRAFT_ANCIENT_DEBRIS",
        "MINECRAFT_COAL_ORE",
        "MINECRAFT_COPPER_ORE",
        "MINECRAFT_DEEPSLATE_COAL_ORE",
        "MINECRAFT_DEEPSLATE_COPPER_ORE",
        "MINECRAFT_DEEPSLATE_DIAMOND_ORE",
        "MINECRAFT_DEEPSLATE_EMERALD_ORE",
        "MINECRAFT_DEEPSLATE_GOLD_ORE",
        "MINECRAFT_DEEPSLATE_IRON_ORE",
        "MINECRAFT_DEEPSLATE_LAPIS_ORE",
        "MINECRAFT_DEEPSLATE_REDSTONE_ORE",
        "MINECRAFT_DIAMOND_ORE",
        "MINECRAFT_EMERALD_ORE",
        "MINECRAFT_GOLD_ORE",
        "MINECRAFT_IRON_ORE",
        "MINECRAFT_LAPIS_ORE",
        "MINECRAFT_NETHER_GOLD_ORE",
        "MINECRAFT_REDSTONE_ORE",
        "MNA_VINTEUM_ORE"
    ],
    "#logs": [
        "#BIOMESWEVEGONE_ASPEN_LOGS",
        "#BIOMESWEVEGONE_BAOBAB_LOGS",
        "#BIOMESWEVEGONE_BLUE_ENCHANTED_LOGS",
        "#BIOMESWEVEGONE_CIKA_LOGS",
        "#BIOMESWEVEGONE_CYPRESS_LOGS",
        "#BIOMESWEVEGONE_EBONY_LOGS",
        "#BIOMESWEVEGONE_FIR_LOGS",
        "#BIOMESWEVEGONE_FLORUS_LOGS",
        "#BIOMESWEVEGONE_GREEN_ENCHANTED_LOGS",
        "#BIOMESWEVEGONE_HOLLY_LOGS",
        "#BIOMESWEVEGONE_IRONWOOD_LOGS",
        "#BIOMESWEVEGONE_JACARANDA_LOGS",
        "#BIOMESWEVEGONE_MAHOGANY_LOGS",
        "#BIOMESWEVEGONE_MAPLE_LOGS",
        "#BIOMESWEVEGONE_PALM_LOGS",
        "#BIOMESWEVEGONE_PALO_VERDE_LOGS",
        "#BIOMESWEVEGONE_PINE_LOGS",
        "#BIOMESWEVEGONE_RAINBOW_EUCALYPTUS_LOGS",
        "#BIOMESWEVEGONE_REDWOOD_LOGS",
        "#BIOMESWEVEGONE_SAKURA_LOGS",
        "#BIOMESWEVEGONE_SKYRIS_LOGS",
        "#BIOMESWEVEGONE_WHITE_MANGROVE_LOGS",
        "#BIOMESWEVEGONE_WILLOW_LOGS",
        "#BIOMESWEVEGONE_WITCH_HAZEL_LOGS",
        "#BIOMESWEVEGONE_ZELKOVA_LOGS",
        "#FORBIDDEN_ARCANUS_EDELWOOD_LOGS",
        "#FORBIDDEN_ARCANUS_FUNGYSS_STEMS",
        "#FORBIDDEN_ARCANUS_MYSTERYWOOD_LOGS",
        "#GOETY_HAUNTED_LOGS",
        "#GOETY_PINE_LOGS",
        "#GOETY_ROTTEN_LOGS",
        "#GOETY_WINDSWEPT_LOGS",
        "#MEADOW_BIRCH_LOGS",
        "#MEADOW_LOGS",
        "#MEADOW_PINE_LOGS",
        "#MINECRAFT_CRIMSON_STEMS",
        "#MINECRAFT_LOGS",
        "#MINECRAFT_LOGS_THAT_BURN",
        "#MINECRAFT_WARPED_STEMS",
        "ALEXSCAVES_PEWEN_LOG",
        "ALEXSCAVES_PEWEN_WOOD",
        "ALEXSCAVES_STRIPPED_PEWEN_LOG",
        "ALEXSCAVES_STRIPPED_PEWEN_WOOD",
        "ALEXSCAVES_STRIPPED_THORNWOOD_LOG",
        "ALEXSCAVES_STRIPPED_THORNWOOD_WOOD",
        "ALEXSCAVES_THORNWOOD_LOG",
        "ALEXSCAVES_THORNWOOD_WOOD",
        "BIOMEMAKEOVER_ANCIENT_OAK_LOG",
        "BIOMEMAKEOVER_ANCIENT_OAK_WOOD",
        "BIOMEMAKEOVER_BLIGHTED_BALSA_LOG",
        "BIOMEMAKEOVER_BLIGHTED_BALSA_WOOD",
        "BIOMEMAKEOVER_STRIPPED_ANCIENT_OAK_LOG",
        "BIOMEMAKEOVER_STRIPPED_ANCIENT_OAK_WOOD",
        "BIOMEMAKEOVER_STRIPPED_BLIGHTED_BALSA_LOG",
        "BIOMEMAKEOVER_STRIPPED_BLIGHTED_BALSA_WOOD",
        "BIOMEMAKEOVER_STRIPPED_SWAMP_CYPRESS_LOG",
        "BIOMEMAKEOVER_STRIPPED_SWAMP_CYPRESS_WOOD",
        "BIOMEMAKEOVER_STRIPPED_WILLOW_LOG",
        "BIOMEMAKEOVER_STRIPPED_WILLOW_WOOD",
        "BIOMEMAKEOVER_SWAMP_CYPRESS_LOG",
        "BIOMEMAKEOVER_SWAMP_CYPRESS_WOOD",
        "BIOMEMAKEOVER_WILLOW_LOG",
        "BIOMEMAKEOVER_WILLOW_WOOD",
        "ENCHANTED_ALDER_LOG",
        "ENCHANTED_HAWTHORN_LOG",
        "ENCHANTED_ROWAN_LOG",
        "GOETY_STEEP_WOOD",
        "HEXEREI_MAHOGANY_LOG",
        "HEXEREI_MAHOGANY_WOOD",
        "HEXEREI_STRIPPED_MAHOGANY_LOG",
        "HEXEREI_STRIPPED_MAHOGANY_WOOD",
        "HEXEREI_STRIPPED_WILLOW_LOG",
        "HEXEREI_STRIPPED_WILLOW_WOOD",
        "HEXEREI_STRIPPED_WITCH_HAZEL_LOG",
        "HEXEREI_STRIPPED_WITCH_HAZEL_WOOD",
        "HEXEREI_WILLOW_LOG",
        "HEXEREI_WILLOW_WOOD",
        "HEXEREI_WITCH_HAZEL_LOG",
        "HEXEREI_WITCH_HAZEL_WOOD",
        "ITER_RPG_SACRED_LOG",
        "ITER_RPG_SACRED_WOOD",
        "LUMINOUS_NETHER_GOLDENSTEM",
        "LUMINOUS_NETHER_SHREDDED_STEM",
        "LUMINOUS_NETHER_WITHERED_LOG",
        "MALUM_BLIGHTED_SOULWOOD",
        "MALUM_EXPOSED_RUNEWOOD_LOG",
        "MALUM_EXPOSED_SOULWOOD_LOG",
        "MALUM_REVEALED_RUNEWOOD_LOG",
        "MALUM_REVEALED_SOULWOOD_LOG",
        "MALUM_RUNEWOOD",
        "MALUM_RUNEWOOD_LOG",
        "MALUM_SOULWOOD",
        "MALUM_SOULWOOD_LOG",
        "MALUM_STRIPPED_RUNEWOOD",
        "MALUM_STRIPPED_RUNEWOOD_LOG",
        "MALUM_STRIPPED_SOULWOOD",
        "MALUM_STRIPPED_SOULWOOD_LOG",
        "MINECRAFT_BIRCH_LOG",
        "MINECRAFT_MANGROVE_ROOTS",
        "MINECRAFT_OAK_LOG",
        "OUTER_END_AZURE_STEM",
        "VINERY_APPLE_LOG",
        "VINERY_APPLE_WOOD",
        "VINERY_DARK_CHERRY_LOG",
        "VINERY_DARK_CHERRY_WOOD",
        "VINERY_STRIPPED_DARK_CHERRY_LOG",
        "VINERY_STRIPPED_DARK_CHERRY_WOOD"
    ]
}

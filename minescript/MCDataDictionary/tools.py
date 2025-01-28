tool_dict = {}

tool_dict.update({
    'Obsidian': 'Diamond',
    'Crying Obsidian': 'Diamond',
    'Respawn Anchor': 'Diamond',
    'Block of Netherite': 'Diamond',
    'Ancient Debris': 'Diamond',
    'Ender Chest': 'Wood',
    'Anvil': 'Wood',
    'Bell': 'Wood',
    'Block of Coal': 'Wood',
    'Block of Diamond': 'Iron',
    'Block of Emerald': 'Iron',
    'Block of Iron': 'Stone',
    'Block of Raw Copper': 'Stone',
    'Block of Raw Gold': 'Iron',
    'Block of Raw Iron': 'Stone',
    'Block of Redstone': 'Wood',
    'Chain': 'Wood',
    'Enchantment Table': 'Wood',
    'Iron Bars': 'Wood',
    'Iron Door': 'Wood',
    'Iron Trapdoor': 'Wood',
    'Monster Spawner': 'Wood',
    'Deepslate Coal Ore': 'Wood',
    'Deepslate Copper Ore': 'Wood',
    'Deepslate Diamond Ore': 'Wood',
    'Deepslate Emerald Ore': 'Wood',
    'Deepslate Gold Ore': 'Wood',
    'Deepslate Iron Ore': 'Wood',
    'Deepslate Lapis Lazuli Ore': 'Wood',
    'Deepslate Redstone Ore': 'Wood',
    'Blast furnace': 'Wood',
    # Continue the pattern for the rest of the items...
})

tool_dict.update({
    'Cobbled Deepslate': 'Wood',
    'Chiseled Deepslate': 'Wood',
    'Deepslate Bricks': 'Wood',
    'Deepslate Tiles': 'Wood',
    'Polished Deepslate': 'Wood',
    'Dispenser': 'Wood',
    'Dropper': 'Wood',
    'Furnace': 'Wood',
    'Lantern': 'wood',
    'Lodestone': 'Wood',
    'Smoker': 'Wood',
    'Stonecutter': 'Wood',
    'Conduit': '',  # No specified material in the provided data
    'Block of Gold': 'Iron',
    'Block of Lapis Lazuli': 'Stone',
    'Coal Ore': 'Wood',
    'Copper Ore': 'Wood',
    'Copper Blocks': 'Wood',
    'Cut Copper': 'Wood',
    'Cut Copper Slab': 'Wood',
    'Cut Copper Stairs': 'Wood',
    'Deepslate': 'Wood',
    'Diamond Ore': 'Iron',
    'Emerald Ore': 'Iron',
    'End Stone': 'Wood',
    'Gold Ore': 'Iron',
    'Hopper': 'Wood',
    'Iron Ore': 'Stone',
    'Lightning Rod': 'Wood',
    'Lapis Lazuli Ore': 'Stone',
    # Add more items as needed following the same structure...
})

tool_dict.update({
    'Nether Quartz Ore': 'Wood',
    'Nether Gold Ore': 'Wood',
    'Observer': 'Wood',
    'Redstone Ore': 'Iron',
    'Blue Ice': '',  # No specified material in the provided data
    'Heat Block': 'Wood',
    'Grindstone': 'Wood',
    'Bone Block': 'Wood',
    'Brick Stairs': 'Wood',
    'Bricks': 'Wood',
    'Cauldron': 'Wood',
    'Cobblestone': 'Wood',
    'Cobblestone Stairs': 'Wood',
    'Cobblestone Wall': 'Wood',
    'Mossy Cobblestone': 'Wood',
    'Nether Bricks': 'Wood',
    'Nether Brick Fence': 'Wood',
    'Nether Brick Stairs': 'Wood',
    'Red Nether Bricks': 'Wood',
    'Polished Blackstone': 'Wood',
    'Stone Slabs': 'Wood',  # Assuming the material follows the pattern
    'Smooth Stone': 'Wood',
    'Shulker Box': '',  # No specified material in the provided data
    'Concrete': 'Wood',
    'Andesite': 'Wood',
    'Dark Prismarine': 'Wood',
    'Diorite': 'Wood',
    'Dripstone Block': 'Wood',
    'Granite': 'Wood',
    'Mud Bricks': 'Wood',
    # Add more items as needed following the same structure...
})

tool_dict.update({
    'Pointed Dripstone': '',  # No specified material in the provided data
    'Prismarine': 'Wood',
    'Prismarine Bricks': 'Wood',
    'Purpur block': 'Wood',
    'Purpur pillar': 'Wood',
    'Stone': 'Wood',
    'Stone Bricks': 'Wood',
    'Tuff': 'Wood',
    'Stone Brick Stairs': 'Wood',
    'Amethyst Bud': '',  # No specified material in the provided data
    'Amethyst Cluster': '',  # No specified material in the provided data
    'Blackstone': 'Wood',
    'Block of Amethyst': 'Wood',
    'Budding Amethyst': '',  # No specified material in the provided data
    'Chiseled Polished Blackstone': 'Wood',
    'Polished Blackstone Bricks': 'Wood',
    'Gilded Blackstone': 'Wood',
    'Glazed Terracotta': 'Wood',
    'Terracotta': 'Wood',
    'Basalt': 'Wood',
    'Smooth Basalt': 'Wood',
    'Polished Basalt': 'Wood',
    'Packed Mud': '',  # No specified material in the provided data
    'Block of Quartz': 'Wood',
    'Quartz Stairs': 'Wood',
    'Red Sandstone': 'Wood',
    'Red Sandstone Stairs': 'Wood',
    'Sandstone': 'Wood',
    'Sandstone Stairs': 'Wood',
    'Calcite': 'Wood',
    # Add more items as needed following the same structure...
})

tool_dict.update({
    'Rail': '',  # No specified material in the provided data
    'Brewing Stand': 'Wood',
    'Ice': '',  # No specified material in the provided data
    'Magma Block': 'Wood',
    'Packed Ice': '',  # No specified material in the provided data
    'Frosted Ice': '',  # No specified material in the provided data
    'Stone Pressure Plate': 'Wood',
    'Netherrack': 'Wood',
    'Warped Nylium': 'Wood',  # Assuming 'Wood' based on the pattern, please confirm
    'Crimson Nylium': 'Wood',
    # Add more items as needed following the same structure...
})

import displayname
displayname.item_dict

inverted_item_dict = {v: k for k, v in displayname.item_dict.items()}

# Create a new dictionary by replacing the tool names with their respective item IDs
new_tool_dict = {inverted_item_dict.get(tool_name, tool_name): material for tool_name, material in tool_dict.items()}

# Print or use the new_tool_dict as needed
print(new_tool_dict)

with open('tools.py', 'w') as py_file:
    py_file.write('recipes = ')
    py_file.write(repr(new_tool_dict))
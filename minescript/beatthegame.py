#import minescript as message
from MCDataDictionary import displayname , block_drops , mob_drops , crafting_recipes , smelting_recipes , required_tools
from UI_map import fourxfour,ninexnine,furnace,inventory,recipe_book,recipe_search
import time
import sys
import minescript as ms
import pynput


start_time = time.time()

args = sys.argv
input = "iron_ingot"
quantity = 2
task_list = []

def FindBestSource(item,count=1,AddtoTaskList=True):
    sources = []
    smelt = smelting_recipes.search(item)
    craft = crafting_recipes.search(item)
    mine  = block_drops.search(item)
    loot  = mob_drops.search(item)
    if smelt != None: sources.append(["smelt",smelt,item,count])
    if craft != None: sources.append(["craft",craft,item,count])
    if mine  != None: sources.append(["mine" ,mine ,item,count])
    if loot  != None: sources.append(["loot" ,loot ,item,count])
    if AddtoTaskList == True:
        task_list.append(sources[0])
    else: return sources[0]

def task_list_execute():
    task = task_list[-1]
    temp_list = []
    if task[0] == 'smelt': 
        for item in task[1]:
            temp_list.append(FindBestSource(item,task[3],False))
        task_list.append(max(temp_list, key=lambda x: len(x[1])))
        task_list_execute()
        # if 'furnace' not in [t[2] for t in task_list]:
        #     FindBestSource('furnace')
        #     task_list_execute()
    if task[0] == 'mine':
        for item in task[1]:
            temp_list.append(required_tools.search(item))
        requiredtool = required_tools.tool_hierarchy(temp_list)
        if not requiredtool: pass
        else:
            # if required_tools not in [t[2] for t in task_list]:
                FindBestSource(requiredtool)
                task_list_execute()
    if task[0] == 'craft':
        if task[2] == 'crafting_table': pass
        else:
            for item in task[1]:
                FindBestSource(item[0],item[1])
                task_list_execute()
        
def Optimize_task_list():
    craft_once = True; smelt_once = True
    i = len(task_list)-1
    for job in [t[0] for t in task_list[::-1]]:
        if job == 'craft' and craft_once == True:
            task_list.insert(i,['craft', [['tag:planks', 4]], 'crafting_table', 1]); j = i + 1
            task_list.insert(j,['craft', [['tag:logs', 1]], 'tag:planks', 4]); j = j + 1
            task_list.insert(j,['mine', ['oak_log', 'spruce_log', 'birch_log', 'jungle_log', 'acacia_log', 'dark_oak_log', 'mangrove_log', 'cherry_log'], 'tag:logs', 1]); j = j + 1
            craft_once = False
        if job == 'smelt' and smelt_once == True:
            task_list.insert(i,['craft', [['cobblestone', 8]], 'furnace', 1]); j = i + 1
            task_list.insert(j,['mine', ['stone'], 'cobblestone', 8]); j = j + 1
            task_list.insert(j,['craft', [['tag:planks', 3], ['stick', 2]], 'wooden_pickaxe', 1]); j = j + 1
            task_list.insert(j,['craft', [['tag:logs', 1]], 'tag:planks', 3]); j = j + 1
            task_list.insert(j,['mine', ['oak_log', 'spruce_log', 'birch_log', 'jungle_log', 'acacia_log', 'dark_oak_log', 'mangrove_log', 'cherry_log'], 'tag:logs', 1]); j = j + 1
            task_list.insert(j,['craft', [['tag:planks', 2]], 'stick', 2]); j = j + 1
            task_list.insert(j,['craft', [['tag:logs', 1]], 'tag:planks', 2]); j = j + 1
            smelt_once = False

    i = 0
    while i < len(task_list):
        j = i - 1
        while j > -1:
            if task_list[j][0:3] == task_list[i][0:3]:
                task_list[i][3] = task_list[i][3] + task_list[j][3]
                del task_list[j]
                i = -1
            j = j - 1
        i = i + 1
    i = 0
    for item in [t[2] for t in task_list]:
        if item == 'wooden_pickaxe' or item == 'stone_pickaxe' or item == 'iron_pickaxe' or item == 'diamond_pickaxe' or item == 'crafting_table' or item == 'furnace':
            task_list[i][3] = 1
        i = i + 1

FindBestSource(input,quantity)
task_list_execute()
# print(task_list)

Optimize_task_list()
# print("______________________________________________________________________________________________________________________________________")
# print(task_list)
ctl = task_list




def move_mouse(inv_slot,click):
    pynput.mouse.Controller().position = (0,0)
    time.sleep(0.05)
    pynput.mouse.Controller().position = (inv_slot[0],inv_slot[1])
    time.sleep(0.05)
    if click == 0 : pynput.mouse.Controller().click(pynput.mouse.Button.left)  #ms.player_press_attack(True);time.sleep(0.05);  ms.player_press_attack(False)
    if click == 1 : pynput.mouse.Controller().click(pynput.mouse.Button.right) #ms.player_press_use(True);   time.sleep(0.05);  ms.player_press_use(False)

def Inventory():
    pynput.keyboard.Controller().press("e")
    pynput.keyboard.Controller().release("e")
    
def use_recipe(recipe_name,type):
    if type == 0:
        Inventory()
        move_mouse(recipe_book.recipe_book[0],0)
    if type == 1:
        ms.chat('#goto crafting_table'); time.sleep(0.05)
        move_mouse(recipe_book.recipe_book[2],0)
    if type == 2:
        ms.chat('#goto furnace'); time.sleep(0.05)
        move_mouse(recipe_book.recipe_book[4],0)

    move_mouse(recipe_search.recipe_search[0],0)
    pynput.keyboard.Controller().type(recipe_name)
    move_mouse(recipe_search.recipe_search[1],0)
    if type == 0:
        move_mouse(recipe_search.recipe_search[2],0)
        move_mouse(recipe_book.recipe_book[1],0)
        Inventory()
    if type == 1:
        move_mouse(recipe_search.recipe_search[3],0)
        move_mouse(recipe_book.recipe_book[3],0)
        Inventory()
        time.sleep(0.5); repeat = 21
        while True:
            if repeat > 20:
                ms.player_press_jump(True);ms.player_press_backward(True);time.sleep(0.625);ms.player_press_jump(False);ms.player_press_backward(False)
                ms.chat('#mine crafting_table'); repeat = 0
            prev_inv = ms.player_inventory() ; repeat = repeat + 1
            time.sleep(0.5); item_count = 0
            if prev_inv == ms.player_inventory():pass
            else: 
                for slot in ms.player_inventory():
                    if slot.get("item") == 'crafting_table':
                        return 'done'
    if type == 2:
        move_mouse(recipe_book.recipe_book[5],0)
        for slot in ms.player_inventory(): 
            if slot.get("item") in block_drops.search('tag:planks'):
                move_mouse(inventory.inventory[slot.get("slot")],0)
                move_mouse(furnace.furnace[1],1)
                move_mouse(inventory.inventory[slot.get("slot")],0)
                break
        time.sleep(10)
        move_mouse(furnace.furnace[2],0)
        Inventory()
        


def spin_and_use(item):
    has_item = 0
    for slot in ms.player_inventory(): 
                if slot.get("item") == item:
                    if slot.get("slot") > 8: ms.player_inventory_select_slot(ms.player_inventory_slot_to_hotbar(slot.get("slot")));has_item = 1;break
                    else: ms.player_inventory_select_slot(slot.get("slot"));has_item = 1;break
    if has_item == 1:
        ms.player_press_use(True)
        x = -180; y = -90
        while x<180:
            y = -90
            while y<90:
                ms.player_set_orientation(x,y)
                y = y + 30
            x = x + 30
        ms.player_press_use(False)
    
    
def task_list_perform():
    if len(ctl)>0:
        task = ctl[-1]; item_count = 0
    if task[0] == 'mine':
        if task[2][0:4] == 'tag:':
            for slot in ms.player_inventory():
                if slot.get("item") in task[1]:
                    item_count = item_count + int(slot.get("count"))
            if item_count >= task[3]: ctl.pop();task_list_perform()
            else:
                ms.chat("#mine "+" ".join(task[1]))
                while True:
                    prev_inv = ms.player_inventory(); time.sleep(0.5); item_count = 0
                    if prev_inv == ms.player_inventory():pass
                    else: 
                        for slot in ms.player_inventory():
                            if slot.get("item") in task[1]:
                                item_count = item_count + int(slot.get("count"))
                        if item_count >= task[3]: ms.chat('stop'); ctl.pop(); task_list_perform(); break
        else:
            for slot in ms.player_inventory():
                if slot.get("item") == task[2]:
                    item_count = item_count + int(slot.get("count"))
            if item_count >= task[3]: ctl.pop();task_list_perform()
            else:
                ms.chat("#mine "+" ".join(task[1]))
                while True:
                    prev_inv = ms.player_inventory(); time.sleep(0.5); item_count = 0
                    if prev_inv == ms.player_inventory():pass
                    else: 
                        for slot in ms.player_inventory():
                            if slot.get("item") == task[2]:
                                item_count = item_count + int(slot.get("count"))
                        if item_count >= task[3]: ms.chat('stop'); ctl.pop(); task_list_perform(); break

    if task[0] == 'craft':
        if sum([ric[1] for ric in task[1]]) == 1 and task[2][0:4] == 'tag:':
            for slot in ms.player_inventory():
                if slot.get("item") in block_drops.search(task[2]):
                    item_count = item_count + int(slot.get("count"))
            if item_count >= task[3]: ctl.pop();task_list_perform()
            else:
                while True:
                    prev_inv = ms.player_inventory(); time.sleep(0.05); item_count = 0
                    use_recipe(displayname.search(task[2]),0)
                    if prev_inv == ms.player_inventory():pass
                    else:
                        for slot in ms.player_inventory():
                            if slot.get("item") in block_drops.search(task[2]):
                                item_count = item_count + int(slot.get("count"))
                        if item_count >= task[3]: ctl.pop(); task_list_perform(); break
        elif sum([ric[1] for ric in task[1]]) <= 4:
            for slot in ms.player_inventory():
                if slot.get("item") == task[2]:
                    item_count = item_count + int(slot.get("count"))
            if item_count >= task[3]: ctl.pop();task_list_perform()
            else:
                while True:
                    prev_inv = ms.player_inventory(); time.sleep(0.05); item_count = 0
                    use_recipe(displayname.search(task[2]),0)
                    if prev_inv == ms.player_inventory():pass
                    else:
                        for slot in ms.player_inventory():
                            if slot.get("item") == task[2]:
                                item_count = item_count + int(slot.get("count"))
                        if item_count >= task[3]: ctl.pop(); task_list_perform(); break
        else:
            for slot in ms.player_inventory():
                if slot.get("item") == task[2]:
                    item_count = item_count + int(slot.get("count"))
            if item_count >= task[3]: ctl.pop();task_list_perform()
            else:
                spin_and_use('crafting_table')
                ms.chat('#goto crafting_table')
                while True:
                    try:
                        if ms.player_get_targeted_block(3)[-1] == 'minecraft:crafting_table': time.sleep(0.1); break
                    except TypeError : time.sleep(3);ms.chat('#goto crafting_table')
                while True:
                    prev_inv = ms.player_inventory(); time.sleep(0.05); item_count = 0
                    use_recipe(displayname.search(task[2]),1)
                    if prev_inv == ms.player_inventory():pass
                    else:
                        for slot in ms.player_inventory():
                            if slot.get("item") == task[2]:
                                item_count = item_count + int(slot.get("count"))
                        if item_count >= task[3]: ctl.pop(); task_list_perform(); break
    if task[0] == 'smelt':
        for slot in ms.player_inventory():
                if slot.get("item") == task[2]:
                    item_count = item_count + int(slot.get("count"))
        if item_count >= task[3]: ctl.pop()
        else:
            spin_and_use('furnace')
            ms.chat('#goto furnace')
            while True:
                if not ms.player_get_targeted_block(): time.sleep(0.5)
                elif ms.player_get_targeted_block()[-1][0:17] == 'minecraft:furnace': time.sleep(0.1); break
            while True:
                prev_inv = ms.player_inventory(); time.sleep(0.05); item_count = 0
                use_recipe(displayname.search(task[2]),2)
                if prev_inv == ms.player_inventory():pass
                else:
                    for slot in ms.player_inventory():
                        if slot.get("item") == task[2]:
                            item_count = item_count + int(slot.get("count"))
                    if item_count >= task[3]: ctl.pop(); task_list_perform(); break

            
task_list_perform()
        
            
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")



from telethon import TelegramClient, events, sync, utils
from time import sleep
import asyncio, random

loop = asyncio.get_event_loop()

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

akun1 = "Kin"
akun2 = "Lado"
client = TelegramClient(akun1, api_id, api_hash).start()
client2 = TelegramClient(akun2, api_id, api_hash).start()

total = 0
total2 = 0

chat = 'kampungmaifamxbot'

@client.on(events.NewMessage(chat))
async def handler(event):
    global maling
    global total 
    global tmp
    

    if "Villager's Abandoned" in event.text:
        tmp = 0
        rem = 0
        maling = [x for x in event.text.split() if '/stealitem' in x]
        sleep(1.8)
        await event.respond(maling[tmp])
        return
        
    if "The house you are trying to" in event.raw_text:
        sleep(1.8)
        tmp +=1
        total += 40
        print('Skill = ', total)
        
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
        
    if "ve stolen" in event.raw_text:
        sleep(1.8)
        tmp +=1
        total += 40
        print('Skill = ', total)
        
        if tmp == 5:
            await event.respond("Remove using Cash")
            return
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
            
    if 'No bounty' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        #print(tmp)
        return
      
    if 'Oh snap' in event.text:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond("Remove using Cash")
            return
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
        
    if 'has no item to steal' in event.text:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond("Remove using Cash")
            return
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
    
    if 'The house you visited' in event.text:
        sleep(1.8)
        tmp += 1
        if tmp == 5:
            await event.respond("Remove using Cash")
            return
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return

    if 'Same address' in event.text:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond("Remove using Cash")
            return
        if tmp == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        
        return
    
    if 'stuck in bloody' in event.text:
        sleep(1.8)
        await event.respond('/release')
        return
        
    if 'Great!!' in event.text:
        sleep(1.8)
        await event.respond('/casino_result')
        return
        
    if 'Successfully cooked' in event.text:
        sleep(1.8)
        await event.respond('/masak_minibacon_220')
        return
        
    if '60 times' in event.raw_text:
        sleep(1.8)
        await event.respond('/casino_UltraLuck_{}_5000000000000'.format(random.randint(1,20)))
        return
        
    if "End previous game" in event.text:
        sleep(1.8)
        await event.respond('/casino_result')
        return
        
    if "Successfully bet" in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if "You can see" in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if "You bet on" in event.text:
        sleep(1.8)
        await event.respond('/casino_UltraLuck_13_5e12')
        return
        
    if "Not bet placed," in event.text:
        sleep(1.8)
        await event.respond('/casino_UltraLuck_{}_5000000000000'.format(random.randint(1,20)))
        return
        
    if "You won" in event.text:
        sleep(1.8)
        await event.respond('/casino_UltraLuck_17_5e12')
        return
        
    if 'as free as' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if 'Are you sure' in event.text:
        sleep(1.8)
        await event.click(text="Confirm")
        return

    if 'Address code changed' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
       
@client2.on(events.NewMessage(chat))
async def handler(event):
    global maling2
    global total2
    global tmp2
    

    if "Villager's Abandoned" in event.text:
        tmp2 = 0
        rem2 = 0
        maling2 = [x for x in event.text.split() if '/stealitem' in x]
        sleep(1.8)
        await event.respond(maling2[tmp2])
        return
        
    if "The house you are trying to" in event.raw_text:
        sleep(1.8)
        tmp2 +=1
        total2 += 40
        print('Skill2 = ', total2)
        
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        return
        
    if "ve stolen" in event.raw_text:
        sleep(1.8)
        tmp2 +=1
        total2 += 40
        print('Skill = ', total2)
        
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        return
            
    if 'No bounty' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        #print(tmp2)
        return
      
    if 'Oh snap' in event.text:
        sleep(1.8)
        tmp2 += 1
        
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        return
        
    if 'has no item to steal' in event.text:
        sleep(1.8)
        tmp2 += 1
        
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        return
    
    if 'The house you visited' in event.text:
        sleep(1.8)
        tmp2 += 1
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        return

    if 'Same address' in event.text:
        sleep(1.8)
        tmp2 += 1
        
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return
        if tmp2 == 5:
            await event.respond("Remove using Cash")
            return 
        else:
            await client2.send_message(chat, maling2[tmp2])
            return
        
        return
    
    if 'stuck in bloody' in event.text:
        sleep(1.8)
        await event.respond('/release')
        return
        
    if 'Great!!' in event.text:
        sleep(1.8)
        await event.respond('/casino_result')
        return
        
    if 'Successfully cooked' in event.text:
        sleep(1.8)
        await event.respond('/masak_minibacon_220')
        return
        
    if '60 times' in event.raw_text:
        sleep(1.8)
        await event.respond('/casino_FiftyFifty_{}_1e12'.format(random.randint(1,2)))
        return
        
    if "End previous game" in event.text:
        sleep(1.8)
        await event.respond('/casino_result')
        return
        
    if "Successfully bet" in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if "You can see" in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if "You bet on" in event.text:
        sleep(1.8)
        await event.respond('/casino_FiftyFifty_2_1e12')
        return
        
    if "Not bet placed," in event.text:
        sleep(1.8)
        await event.respond('/casino_FiftyFifty_{}_1e12'.format(random.randint(1,2)))
        return
        
    if "You won" in event.text:
        sleep(1.8)
        await event.respond('/casino_FiftyFifty_2_1e12')
        return
        
    if 'as free as' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
        
    if 'Are you sure' in event.text:
        sleep(1.8)
        await event.click(text="Confirm")
        return

    if 'Address code changed' in event.text:
        sleep(1.8)
        await event.respond('/homesx')
        return
                
client.run_until_disconnected()
client2.run_until_disconnected()
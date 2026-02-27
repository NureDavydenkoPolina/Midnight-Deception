define sophie = Character("Sophie", color="#e2d300", image = 'sophie')
define ann = Character("Ann", color="#ad042e", image = 'ann' )
define daniel = Character("Daniel", color="#85817c")
define miles = Character("Miles", color="#866238")
define victor = Character("Victor", color="#383058")
define player = 'Lina'
define suspicion_mc = 0
define suspicion_sophia = 0
define suspicion_ann = 0
define suspicion_victor = 0

label start:
    scene outside
    'It was raining when I arrived at the mansion.'
    'The house stood tall in the darkness - beautiful, elegant... and somehow unsettling. The warm lights in the windows didn`t make it feel any less intimidating.'
    'Daniel.'
    'We`ve known each other since I was a kid and he was just a broke teenager hanging out at the computer club. We used to sit for hours in front of old monitors, dreaming about the future.'
    'And now... look at him.'
    'I won`t lie. I`m jealous.'
    'He invited me to this party, said he wanted me to meet his friends.'
    'But everyone knows that`s not the real reason we`re here.'

    scene living_room
    'I step inside.'
    'A soft voice greets me.'
    show sophie
    '???' 'Good evening, sir/miss.'
    player 'Good evening... um, sorry, but you are..?'
    sophie happy'I`m Sophie. I used to work with Daniel`s wife...'
    sophie '...before she... you know.'
    player 'Oh... yes. Nice to meet you, Sophie. I`m [player].'
    show ann angry at right
    'Another voice cuts in.'
    '???' 'One more person. How many does that make now?'
    'A girl approaches us. She looks like she`d rather be anywhere else.'
    sophie angry'Ann, that`s not polite.'
    ann disgussed 'I don`t care. Everyone knows why we`re here. The more people there are, the smaller the chances.'
    sophie 'I`d rather not talk about it.'
    'Ann isn`t wrong, though.'
    'We all came here for the same reason. You just don`t usually say it out loud.'
    'I was about to ask Ann what Daniel meant to her when-'
    daniel '[player]! I`m glad you made it. I`m so happy everyone`s here. Let`s not waste time - dinner is ready.'

    menu:
        'Go to dinner.':
            jump dinner
        'I`d rather look around the house first.':
            $ suspicion_mc+=1
            jump lookaround
    return

label lookaround:
    scene living_room
    'I slip away while the others head toward the dining room.'
    'The living room is enormous - high ceilings, antique furniture, paintings that seem to follow you with their eyes.'
    #scene closed door
    'A cabinet catches my attention - locked.'
    scene balcony
    #sound rain
    'The balcony doors are slightly open.'
    show miles at right
    show victor at left
    #silloets
    'Two men are standing there.'
    'One looks nervous, constantly checking his phone.'
    'The other seems irritated - jaw tight, arms crossed.'

    menu:
        'Eavesdrop.':
            $ suspicion_mc+=1
            jump eavesdrop
        
        'Join the conversation.':
            jump conversation

        'Leave quietly.':
            jump dinner
    return

label eavesdrop:
    scene balcony
    show miles at right
    show victor at left
    'I stop just before stepping fully onto the balcony.'
    'The rain muffles their voices, but not enough.'
    miles 'So he really invited all of us?'
    victor 'Looks like it.'
    miles 'That doesn`t make sense.'
    victor 'Nothing about tonight makes sense.'
    #sound
    'A pause. I hear a lighter click.'
    miles 'You think he`s going to choose?'
    victor 'That`s what everyone assumes.'
    miles 'I didn`t come here to lose.'
    #sound
    'Victor lets out a dry chuckle.'
    victor 'You `re talking like this is a competition.'
    miles 'Isn`t it?'
    'Silence.'
    victor 'Just... don`t do anything stupid.'
    miles 'Depends on what he announces.'
    'The balcony door creaks slightly under my hand.'
    victor 'Did you hear that?'
    'I quickly step back.'
    jump dinner
    return
            

label conversation:
    scene balcony
    show miles at right
    show victor at left
    'I step onto the balcony.'
    'Both men look at me.'
    player 'Am I interrupting something?'
    victor 'Not at all.'
    miles 'Just discussing the weather.'
    player 'Right. Stormy night for a reunion.'
    victor 'Or a decision.'
    player 'Decision?'
    'Miles studies me carefully.'
    miles 'You don`t think Daniel brought us all here just for dinner, do you?'
    'Before I can answer-'
    'The balcony door opens.'
    show daniel
    daniel 'There you are. Hiding from the others already?'
    'He smiles - warm, confident, but his eyes quickly scan our faces...'
    'Like he`s measuring something.'
    daniel 'Come inside. We shouldnt keep everyone waiting.'

    

label dinner:
    scene kitchen
    show sophie
    show ann
    show miles
    show victor
    show daniel
    #photo
    'Daniel looks... calm. Too calm.'
    'After dinner, he stands up, raising his glass.'
    daniel 'As you all know, I don`t have a son or daughter to leave my fortune to. Of course, I could choose one of you... but then I would`ve invited only that person here.'
    #daniel smiles
    

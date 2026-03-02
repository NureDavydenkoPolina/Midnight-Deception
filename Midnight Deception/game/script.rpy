define sophie = Character("Sophie", color="#e2d300", image = 'sophie')
define ann = Character("Ann", color="#ad042e", image = 'ann' )
define daniel = Character("Daniel", color="#85817c", image = 'daniel')
define miles = Character("Miles", color="#866238", image = 'miles')
define victor = Character("Victor", color="#383058", image = 'victor')
define unknown = Character("???", color="#1f0099")
define voice1 = Character ('Voice 1', color="#7a5408")
define voice2 = Character ('Voice 2', color="#999999")

define player = 'Lina'

define suspicion_mc = 0
define suspicion_sophia = 0
define suspicion_ann = 0
define suspicion_victor = 0

#to work on emotions more

init:
    transform left2:
        xalign 0.3
        yalign 1.0
        anchor (0.5, 1.0)

    transform right2:
        xalign 0.7
        yalign 1.0
        anchor (0.5, 1.0)

    transform left3:
        xalign 0.2
        yalign 1.0
        anchor (0.5, 1.0)

    transform right3:
        xalign 0.8
        yalign 1.0
        anchor (0.5, 1.0)

    transform left4:
        xalign 0.05
        yalign 1.0
        anchor (0.5, 1.0)

    transform right4:
        xalign 0.95
        yalign 1.0
        anchor (0.5, 1.0)
        
    transform left5:
        xalign 0.05
        yalign 1.0
        anchor (0.5, 1.0)

    transform right5:
        xalign 0.95
        yalign 1.0
        anchor (0.5, 1.0)

label start:
    scene outside
    with fade
    'It was raining when I arrived at the mansion.'
    'The house stood tall in the darkness - beautiful, elegant... and somehow unsettling. The warm lights in the windows didn`t make it feel any less intimidating.'
    'Daniel.'
    'We`ve known each other since I was a kid and he was just a broke teenager hanging out at the computer club. We used to sit for hours in front of old monitors, dreaming about the future.'
    'And now... look at him.'
    'I won`t lie. I`m jealous.'
    'He invited me to this party, said he wanted me to meet his friends.'
    'But everyone knows that`s not the real reason we`re here.'

    scene living_room
    with fade
    'I step inside.'
    'A soft voice greets me.'
    show sophie normal
    '???' "Good evening."

    player "Good evening... um, sorry, but you are..?"

    sophie happy "I`m Sophie. I used to work with Daniel`s wife..."

    sophie sad "...before she... you know."

    player "Oh... yes. Nice to meet you, Sophie. I`m [player]."

    show sophie sad at left2
    with move
    
    show ann disgust at right2
    with dissolve   
    'Another voice cuts in.'

    '???' "One more person. How many does that make now?"
    sophie angry"Ann, that`s not polite."

    ann angry 'I don`t care. Everyone knows why we`re here. The more people there are, the smaller the chances.'

    sophie 'I`d rather not talk about it.'

    'Ann isn`t wrong, though.'
    'We all came here for the same reason. You just don`t usually say it out loud.'
    'I was about to ask Ann what Daniel meant to her when-'
    show daniel normal
    with dissolve   

    show sophie normal at left3
    with move
    
    show ann disgust at right3
    with move   
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
    with fade
    'I slip away while the others head toward the dining room.'
    'The living room is enormous - high ceilings, antique furniture, paintings that seem to follow you with their eyes.'
    #scene closed door
    'A cabinet catches my attention - locked.'
    scene balcony
    with fade
    #sound rain
    'The balcony doors are slightly open.'
    show miles sil at right2
    show victor sil at left2
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
    show miles sil at right2
    show victor sil at left2
    'I stop just before stepping fully onto the balcony.'
    'The rain muffles their voices, but not enough.'
    voice1 'So he really invited all of us?'
    voice2 'Looks like it.'
    voice1 'That doesn`t make sense.'
    voice2 'Nothing about tonight makes sense.'
    #sound
    'A pause. I hear a lighter click.'
    voice1 'You think he`s going to choose?'
    voice2 'That`s what everyone assumes.'
    voice1 'I didn`t come here to lose.'
    #sound Victor lets out a dry chuckle
    voice2 'You `re talking like this is a competition.'
    voice1 'Isn`t it?'
    'Silence.'
    voice2 'Just... don`t do anything stupid.'
    voice1 'Depends on what he announces.'
    'The balcony door creaks slightly under my hand.'
    voice2 'Did you hear that?'
    'I quickly step back.'
    jump dinner
    return
            

label conversation:
    scene balcony
    show miles disgust at right2
    show victor normal at left2
    'I step onto the balcony.'
    'Both men look at me.'
    'There were Victor and Miles.'
    'Daniel told me about them after I came to house.'
    player 'Am I interrupting something?'
    victor happy 'Not at all.'
    miles normal 'Just discussing the weather.'
    victor 'Right. Stormy night for a reunion.'
    miles 'Or a decision.'
    player 'Decision?'
    'Men on the right studies me carefully.'
    miles 'You don`t think Daniel brought us all here just for dinner, do you?'
    'Before I can answer-'
    'The balcony door opens.'
    show daniel normal
    daniel 'There you are. Hiding from the others already?'
    'He smiles - warm, confident, but his eyes quickly scan our faces...'
    'Like he`s measuring something.'
    daniel 'Come inside. We shouldnt keep everyone waiting.'
    jump dinner
    return

    

label dinner:
    scene kitchen
    with fade
    show daniel normal
    'Daniel looks... calm. Too calm.'
    'After dinner, he stands up, raising his glass.'
    daniel 'As you all know, I don`t have a son or daughter to leave my fortune to. Of course, I could choose one of you... but then I would`ve invited only that person here.'
    daniel quest'I have a better idea. After my death, the majority of my wealth will be donated to charity. Each of you will receive a generous amount - enough to change your life. And through this donation...'
    daniel normal '...perhaps you`ll become better people.'
    'Silence.'
    show sophie angry at left3
    'Even Sophie looks stunned, though she quickly hides it.'
    sophie normal 'That`s... such a wonderful idea.'
    show miles disgust at right3
    miles 'Are you serious? If you want to donate, just write it in your will.'
    daniel 'I believe doing good changes you spiritually. But no one is forced. If you refuse, I understand.'
    show ann normal at right4
    ann 'I`m fine with donating. But I want to choose the foundation.'
    sophie 'Guys, please... it`s not your money-'
    show victor normal at left4
    victor   'I agree with Sophie. If it`s Daniel`s will, we should respect it.'
    'Daniel turns to me.'
    'His eyes linger a little longer than they should.'
    daniel 'What about you, [player]?'
    
    menu:
        'Agree with Sophie and Victor.':
            player 'I think Victor is right. If it`s Daniel`s will, we should respect it. It`s his decision.'
            sophie 'That`s very mature of you.'
            victor 'At least someone here understands loyalty.'
            miles 'Loyalty? That`s a strong word when money is involved.'
            ann 'Easy for you to say.'
            daniel 'I`m glad to hear that, Y/N. I knew I could count on you.'
            'That sentence feels heavier than it should.'
            sophie 'Maybe we should open some wine?'
            'Sophie quickly changes the subject. The tension lowers - slightly.'


        'Agree with Ann and Miles.':
            $suspicion_mc +=1
            player 'I think Ann has a point. If we`re the ones donating, we should decide where the money goes.'
            sophie 'But that wasn`t the idea...'
            victor 'It sounds like you`re already dividing something that isn`t yours.'
            miles 'Finally. Someone honest.'
            ann 'At least [player] isn`t pretending this is some moral test.'
            daniel 'Interesting. I didn`t expect that answer from you.'
            victor 'People show their true colors when they see an opportunity.'
            miles 'Or when they`re tired of being manipulated.'
            daniel 'Enough. This isn`t a battlefield. We`re guests here. Let`s not ruin the evening.'

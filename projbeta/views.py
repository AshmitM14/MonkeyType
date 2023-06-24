from django.shortcuts import render
import random

arr = [
     "Autumn leaves painted the landscape in vibrant hues of red, orange, and gold. A crisp breeze carried the promise of change and new beginnings. The sound of waves lapping against the shore created a soothing rhythm. Sunlight danced on the water's surface, casting a shimmering reflection.",
     "The scent of jasmine filled the air, intoxicating the senses with its delicate fragrance. It whispered tales of  romance and moonlit gardens. As night fell, stars emerged one by one, transforming the sky into a celestial canvas.",
     "Constellations revealed ancient stories etched across the universe. The bustling market was a mosaic of colors, aromas, and sounds. Vendors called out their wares, enticing passersby with exotic spices and fresh produce.",
     "The sound of thunder echoed through the stormy night, punctuated by flashes of lightning. Rain poured down, cleansing the earth with its power. As dawn broke, birds greeted the day with a chorus of songs. The world awakened, bathed in golden sunlight, readyfor the adventures ahead",
     'The fragrance of freshly cut grass filled the air, evoking memories of carefree summer days. Bare feet embraced  the earth, reveling in nature\'s embrace. The sound of children\'s laughter echoed in the playground, their joy contagious.',
     'Swings soared high, and slides  became pathways to endless imagination.Fields of wildflowers stretched as far as the eye could see, a tapestry of nature\'s artistry. Bees danced from bloom to bloom, spreading life\'s sweetness.',
     'The aroma of spices permeated the kitchen, as a chef created culinary masterpieces. Flavors mingled harmoniously,enticing taste buds on a gastronomic journey. Morning mist enveloped the countryside, creating an ethereal landscape.',
      'Trees emerged like ancient guardians,their secrets hidden in the fog. The crackling of a campfire brought warmth and camaraderie under the starlit sky. Marshmallows toasted on sticks,becoming gooey delights.',
     'The sound of church bells rang out, announcing a moment of peace and reflection. Prayers intertwined with theair, connecting hearts across the world. The city\'s skyline glittered with skyscrapers, a testament to human ambition and progress.',
     'Lights flickered, revealing stories of dreams realized. The fragrance of ocean salt clung to the air as seagulls soared overhead. Sand slipped through fingers, leaving  imprints of memories in its wake.',
     'A gentle rain pitter-pattered on windowpanes, creating a soothing lullaby. Umbrellas danced in the streets,  shielding passersby from nature\'s tears. The scent of pine filled the forest, invigorating the senses with its evergreen embrace.',
     'Trees stood tall, offering shelter to creatures great and small. Colors exploded in the sky as fireworks illuminated the night. Spectators gazed in awe, witnessing fleeting  moments of beauty and celebration.',
     'The sound of a babbling brook provided a peaceful soundtrack to the woodland retreat. Sunlight filtered through  the canopy, creating a tranquil oasis. Ancient ruins stood as a testament to civilizations past, their stories etched in weathered stone.',
     'Time echoed inwhispers, revealing fragments of history. The fragrance of freshly brewed tea filled the cozy tearoom, offering solace in a delicate porcelain cup. Sips brought warmth and moments of reflection.',
     'The sound of a violin filled the concert hall, its melodies weaving emotions into the hearts of listeners. Music transcended language, speaking directly to the soul. Desert sands stretched infinitely, a vast expanse of untouched beauty.',
     'Footprints left behind told tales of  travelers embracing the spirit of adventure. The aroma of a home-cooked meal permeated the kitchen, inviting loved ones to gather and share in the warmth of  togetherness. Memories were made around the table.',
     'Stars sparkled overhead in the stillness of a summer night. Fireflies danced in the darkness, their  bioluminescence captivating imaginations. The gentle rustling of leaves in a forest whispered secrets of ancient wisdom.',
     'Each tree stood as a pillar of strength, rooted in the earth\'s embrace. A symphony of car horns and bustling crowds filled the city streets, a vibrant cacophony of urban life. Diversitythrived in this melting pot of cultures.',
     'The scent of rain on dry earth filled the air, signaling the arrival of a long-awaited storm. Petrichor awakened dormant senses, breathing life into the surroundings. Wind swept across the vast prairie, creating waves in fields of tall grass.',
     'The horizon stretched endlessly, inviting wanderers to explore its hidden treasures. The sound of church bells echoed through the cobbled streets, calling the faithful to prayer. Stained glass  windows illuminated the sanctuary in a kaleidoscope of colors.',
     'Autumn leaves danced on the breeze, a symphony of red, yellow, and orange. Nature painted a masterpiece, bidding farewell to summer with a flourish. The historic monument stood as a testament to the past, its weathered facade bearing witness to the passage of time.',
     'The fragrance of roses filled the garden, their delicate petals unfolding like secrets shared. Bees hummed a melody, collecting nectar from each blossom. The sound of a distant waterfall carried on the wind, drawing wanderers to its hidden sanctuary.',
     ' Nature\'s power  flowed, captivating all who listened. The aroma of freshly baked apple pie wafted from the kitchen, filling the home with warmth and comfort. Each slice held a taste of nostalgia. Shadows danced on thewalls, painting stories untold.',
     'Snowflakes gently fell from the sky, transforming the world into a winter wonderland. Laughter echoed as childrenbuilt snowmen and engaged in friendly snowball fights. The sound of footsteps echoed through the empty hallway, a whisper of presence in solitude.',
     'A gentle breeze rustled through fields of sunflowers, their vibrant faces following the sun\'s path. Nature\'s artistry bloomed, capturing the essence of joy. The scent of freshly mowed grass carried on the wind, a reminder of lazy summer afternoons.' ,
     'The sound of a crackling bonfire filled the night, casting a warm glow on faces gathered around. Tales were  shared, and friendships kindled in its flickering light. Bare feet felt the earth\'s embrace, grounding the spirit.',
     'The city skyline glowed with the vibrant lights of nightlife, a beacon of energy and possibilities. Streets  buzzed with excitement, capturing the essence of urban living. A gentle rain washed over the city, cleansing the streets and revitalizing the urban landscape.',
     ' Umbrellas dotted the sidewalks, a colorful canopy against the gray sky. The fragrance of blooming cherry blossoms filled the air, carrying with it a sense of fleeting beauty and thepromise of renewal. Nature painted a delicate portrait.',
     'The sound of crashing waves against the cliffs resonated through the coastal town, reminding its residents of theuntamed power of the ocean. Seagulls soared overhead. Sunlight filtered through the canopy of a dense forest, casting a soft glow on the lush foliage below. ',
     'Birds sangin harmony, celebrating the symphony of nature. The aroma of freshly brewed coffee enveloped the cafe, drawing in weary souls seeking a moment of respite. The rich flavors embraced their senses with warmth.',
     'The sound of children\'s laughter echoed in the playground, a chorus of joy and innocence. Swings soared through  the air, reaching for the sky with each push. Fields of lavender stretched endlessly, their vibrant purple hues painting the landscape.',
     'The air was perfumed with the flower\'s delicate fragrance, soothing the spirit. The crackling of leaves underfoot announced the arrival of autumn. Nature\'s palette transformed, unveiling shadesof gold, copper, and burgundy.',
     'The fragrance of freshly baked bread wafted from the neighborhood bakery, beckoning passersby with its  irresistible allure. Crusty loaves promised culinary delight. Raindrops tapped on the windowpane, creating a symphony of rhythm and melody. Each drop carried the promise of  growth and rejuvenation.',
     'The sound of footsteps echoed in the empty gallery, where art whispered stories of passion and creativity. Paintings hung in silence, inviting contemplation.',
     'A gentle breeze carried the sweet scent of wildflowers, painting the meadow in a tapestry of colors. Butterflies fluttered among the blossoms, dancing with grace.',
     'The aroma of freshly squeezed citrus filled the kitchen, awakening the senses with its vibrant tang. Each sip of juice held a burst of sunshine. Birds chirped in the early morning, heralding the arrival of a new day.',
     'Waves crashed against the rocky cliffs, their relentless power shaping the rugged coastline. Seashells were  treasures washed ashore, gifts from the ocean\'s depths.',
     'The sound of a crackling fireplace filled the cozy cabin, providing warmth and comfort on a chilly evening. A peaceful garden offered sanctuary from the chaos of the world. Fragrant flowers bloomed, inviting visitors to pause, breathe, and find solace in nature\'s embrace.',
     'The fragrance of blooming roses permeated the garden, evoking romance and beauty. Each petal held a secret whispered by nature\'s delicate touch. The sun\'s rays illuminating the world with hope and possibilities. Embers glowed, casting a soft glow on faces gathered around.',
     'The sound of distant laughter drifted on the breeze, a reminder of joy shared among friends. Memories were woven into the fabric of time, forever cherished. Sunlight filtered through the branches, casting patterns on the forest floor.',
     'The sun began to set, casting a warm glow across the tranquil lake. Birds chirped in the distance, creating a soothing symphony of sounds. Its weathered bark told stories of countless seasons gone by. The rustling of leaves in the forest created a symphony of nature\'s music.',
     'Waves crashed against the rocky shoreline, sending sprays of water into the air. Seagulls circled above, theircalls echoing in the salty breeze. The old oak tree stood tall and proud, its branches reaching towards the heavens.',
     'As the rain fell softly, flowers eagerly drank in the refreshing drops. Petrichor filled the air, awakening the senses and bringing a sense of renewal. The cityscape shimmered with lights and life.',
     'The sound of laughter echoed through the park as children played on the swings. Parents watched with joy, their hearts filled with love and pride. The moon cast a gentleglow, illuminating the world below. In the bustling city streets, people hurried by, their footsteps blending into a rhythmic melody.',
     'A gentle breeze rustled the leaves, creating a gentle whisper in the forest. The scent of pine filled the air,transporting you to a peaceful retreat. In the quiet of the night, stars adorned the velvet sky, twinkling with cosmic secrets.',
     'The aroma of freshly brewed coffee wafted through the cafe, enticing passersby to step inside. Baristas   skillfully crafted intricate designs in the foam. Amidst fields of golden wheat, a farmer toiled with love and dedication. ',
     'The sound of a roaring waterfall echoed through the canyon, captivating all who beheld its raw power. Mist rose in the air, refreshing weary souls. Music transcended time and space. Each harvest brought satisfaction andnourishment to the world.',
     'Mountains towered majestically in the distance, their peaks kissed by snow. Hikers embarked on a journey, seeking solace in nature\'s embrace. The sound of a piano filled the concert hall, its melodies resonating deep within the hearts of the audience.',
     'The scent of freshly baked bread drifted from the bakery, beckoning hungry customers to indulge in its warm goodness. Yeasty perfection awaited. Dappled sunlight filtered through the dense forest canopy, creating a magical play of light and shadow. Nature\'s  beauty flourished in this hidden realm.',
     'The sound of waves crashing against the shore provided a soothing soundtrack to the seaside escape. A gentle stream meandered through the meadow, its crystal-clear waters teeming with life. Dragonflies danced  above, adding splashes of color to the scene.',
     'Outside, snowflakes softly blanketed the world in white. The city skyline glowed in the evening haze, a testament to human ingenuity and ambition. Skyscrapers reached for the stars, touching the sky. Footprints in the sand marked memories made.',
     'The scent of lavender filled the air as a gentle breeze swept through the fields. Bees buzzed from flower to  flower, spreading nature\'s sweet embrace. A cozy fireplace crackled in the cabin, casting a warm glow on the wooden walls.', "This website is made by Ashmit Mahindroo who is a 8th grader studying in Sanskriti School and is a member of the computer club of the school ProjectBeta. This website is made with Python as its programming language."
]


def index(request):
    x = random.randint(0,53)
    global rpara
    rpara = arr[x]
    params = {'rpara':rpara}
    return render(request, 'projbeta/index.html', params)

def result(request):
    params = {} 
    if request.method == 'GET':
        words = request.GET.get('words')
        wpm = len(words.split())*2
        net_wpm = wpm
        mistakes = 0
        for i, j in zip(rpara.split()[:len(words)], words.split()):
                if i != j:
                    net_wpm -=1
                    mistakes += 1

        acc = int(net_wpm/wpm*100)
        params = {'wpm':wpm, 'net_wpm':net_wpm, 'mistakes':mistakes, 'acc': acc}
    return render(request, 'projbeta/result.html',params)

# Create your views here.

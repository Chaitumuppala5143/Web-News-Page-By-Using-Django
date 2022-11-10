from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Folder/index.html')

def india (request):
    dict= {
        'mainmsg':'Head Lines ',
        'submsg1': 'Media needs to be vigilant, flag govt’s shortcomings: Former PM Manmohan Singh',
        'submsg2': 'Cracks on Vande Bharat window pane when Owaisi was traveling, probe begins',
        'submsg3': 'Electoral bonds sale window: Oppn slams govt, calls it ‘poll code violation, bid to legalise corruption',
        'submsg4' : 'On buying oil from Russia, Jaishankar says ‘it works to India’s advantage',
        'photo'  : 'images/imageA.jpg',
    }
    return render(request,'Folder/news.html',context=dict)

def sports (request):
    dict= {
        'mainmsg':'Head Lines',
        'submsg1': 'The growing impact of the coronavirus has shuttered the sports world for the foreseeable future and the chances of the events restarting soon remains a distant dream. While Bundesliga is about to kick-off soon, fans are surely missing out on the other sporting events, with no concrete announcement coming from the Premier League or UEFA.',
        'submsg2': 'AB de Villers Predicts India Will Defeat This Team In T20 World Cup Final',
        'submsg3': 'India "Have Underperformed In World Tournaments": Ex England Captain',
        'submsg4': 'Team India Enjoys Dinner At British Raj Ahead of T20 WC Semis vs England.',
        'photo'  : 'images/imageB.jpg',
    }
    return render(request, 'Folder/news.html', context=dict)

def tech (request):
    dict= {
        'mainmsg':'Head Lines',
        'submsg1': 'First Privately Built Indian Rocket To Take Its Maiden Flight From Sriharikota With 3 Payloads',
        'submsg2': 'YouTube Shorts To Be Available On TVs',
        'submsg3': 'Elon Musk Twitter Saga Live Updates: If You Already Have Blue Tick On Twitter Then You Need ',
        'submsg4':'Governemtn of India’s Ministry of Earth Sciences created the well-known app known as System.',
        'photo'  : 'images/imageC.jpg',
    }
    return render(request, 'Folder/news.html', context=dict)

def business (request):
    dict= {
        'mainmsg':'Head Lines',
        'submsg1': 'Early Flipkart backer Chiratae Ventures marks first close of maiden growth fund at Rs 759 cr',
        'submsg2': 'Gold, silver prices today: Gold prices dip to Rs 46,790, silver prices surge to Rs 61,700 amid rising US dollar',
        'submsg3': 'Share Market LIVE: Sensex, Nifty give up early gains, trading flat; Investors eye U',
        'submsg4' : 'Shares of pharma major Divis Laboratories plunged over 4% to Rs 3,275 after the company on Monday reported an 18.5% year-on-year (YoY) drop in its September quarter consolidated profit after tax to Rs 494 crore. The Hyderabad-based drugmaker disappointed the Street which was estimating a profit of Rs 630 crore.',
        'photo'  : 'images/imageD.jpg',
    }
    return render(request, 'Folder/news.html', context=dict)

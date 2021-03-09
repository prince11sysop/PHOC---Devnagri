import matplotlib.pyplot as plt

def print_histogram (word):   
    char_freq = {} 
    for keys in word: 
        char_freq[keys] = char_freq.get(keys, 0) + 1    

    plt.bar(char_freq.keys(), char_freq.values(), width=0.3, color='c')

    plt.title("PHOC")
    plt.ylabel("Characters count")
    plt.xlabel("Characters")
    plt.show()
    return

upper_letters_set = set(["0900", "0901", "0902", "0904", "0908", "090C", "090D", "090E", "0910", "0911", "0912", "0913", "0914", "093A", "093F", "0940", "0945", "0946", "0947", "0948", "0949", "094A", "094B", "094C", "094F", "0950", "0951", "0953", "0954", "0955", "0960", "0961", "0972", "0973", "0974", "0975"]) 
lower_letters_set = set(["0929", "0931", "0934", "093C", "0941", "0942", "0943", "0944", "094D", "0952", "0956", "0957", "0958", "0959", "095A", "095B", "095C", "095D", "095F", "0962", "0963", "0976", "0977", "0979", "097B", "097C", "097E", "097F"])
hindi_word_list = ["फॉर्ब्स", "रस्ता", "कुलाबा", "मु", "चौका", "वायलेट", "दुर्घटना", "संभावित", "क्षेत्र", "चशमे","नजर", "धुप", "प्रित्त", "मंदिर", "सावधान", "सावधा",
                   "भेट", "पात्र", "शी", "विदे", "देश", "र", "ऋषिकेश", "टिहरी", "क्लब", "रिचमन्ड", "बसन्त", "ब्लॉक", "जी", "कॉलोनी", "टीचर्स","कृष्ण", "श्रीराधा",
                   "्री", "चाँदी", "एसोसिएशन", "उदयपुर", "कार्यालय", "अध्यसक्ष", "महमंत्री", "तानसेन", "मकबरा", "प्रसिधद", "निर्माण", "शताब्दी", "आयताकार", "स्तभयुक्त",
                   "अभिवादन", "अतिथियों", "आरती", "धरोहर", "लक्ष्मी", "नारायण", "भक्ति", "दशनाथियो", "स्वागत", "व्दितीय", "श्रेणी", "मक्ग्रील", "टिक्की", "सॉप्ट", "हमारी",
                   "मुछो", "पुरनी", "आइलैंणड", "मैक्डोलड्", "एफ", "करोल", "परंपरा", "वर्ष", "क्वालिटी", "हम", "शालीका", "कुली", "सिटी", "स्पेशल", "घोटुवा", "रासमलई","मिल्ककेद",
                   "कानपूर", "सेन्टल", "उपलब्ध", "थोक", "हार्दिक", "माकैट", "हरिद्वार", "गंगापुर", "कावली", "इग्राविंग", "निगम", "शिमला", "प्राधिकरण", "दिल्ली"]

for hindi_word in hindi_word_list:
    upper_letters_list = []
    lower_letters_list = []
    middle_letters_list = []

    for i in hindi_word:
        ucode = 'U+%04X' % (ord(i),)
        ucode = ucode[2:]

        if ucode in upper_letters_set:
            upper_letters_list.append(i)
        elif ucode in lower_letters_set:
            lower_letters_list.append(i)
        else:
            middle_letters_list.append(i)

    print("Original hindi word: ", hindi_word)
    print("Upper letters: " , upper_letters_list)
    print_histogram(upper_letters_list)
    print("Middle letters: ", middle_letters_list)
    print_histogram(middle_letters_list)
    print("Lower letters: ", lower_letters_list)
    print_histogram(lower_letters_list)


_EMOTES = []


class Emote:

    def __init__(self, *names):
        self.name = names[0]
        self.aliases = []
        for alias in names:
            self.aliases.append(alias)
            self.aliases.append('r' + alias)
            _EMOTES.append(self)

    def __str__(self):
        return "[](/%s)" % self.name


def getEmote(name):
    for item in _EMOTES:
        if name in item.aliases:
            return item
    return None

# ######################
# # Default Ponymotes ##
# ######################
# non-emotes
SPACE = Emote('sp')
SPOILER = Emote('spoiler')
SPOILER2 = Emote('s')

# Table A
AJ_LIE = Emote('ajlie', 'a00')
TWI_PRIDE = Emote('twipride', 'a01')
LUNA_TEE_HEE = Emote('lunateehee', 'a02')
AJ_HAPPY = Emote('ajhappy', 'a03', 'happlejack')
RARITY_DAWW = Emote('raritydaww', 'a04', 'raritydaw')
AJ_SUP = Emote('ajsup', 'a05', 'ajwhatsgood')
OH_COME_ON = Emote('ohcomeon', 'a06', 'sbcomeon')
RARITY_NEWS = Emote('raritynews', 'a07', 'raritypaper')
TWI_RIGHT = Emote('twiright', 'a08', 'satisfiedtwi', 'satistwied')
SHINING_ARMOR = Emote('shiningarmor', 'a09', 'shiningarmour')
PRICELESS = Emote('priceless', 'a10')
CELESTIA_MAD = Emote('celestiamad', 'a11')
LUNA_WAIT = Emote('lunawait', 'a12')
PINKIE_FEAR = Emote('pinkiefear', 'a13', 'ppfear')
SCOOTA_CHEER = Emote('scootacheer', 'a14', 'lootascoo')
FLUTTER_WHOA = Emote('flutterwhoa', 'a15', 'flutterwoah')
PP_CUTE = Emote('ppcute', 'a16', 'cutiepie')
SB_BOOK = Emote('sbbook', 'a17', 'sweetiebook', 'sbook')
CELESTIA_WUT = Emote('celestiawut', 'a18', 'wutlestia')
CHRYSALIS = Emote('chrysalis', 'a19', 'queenchrysalis', 'changelingqueen')
FLUTTER_JERK = Emote('flutterjerk', 'a20')
TWI_CRAZY = Emote('twicrazy', 'a21')
DERP_WIZARD = Emote('derpwizard', 'a22', 'paperbagderpy',
                    'paperbagmuffins', 'paperbagwizard')
TWI_BEAM = Emote('twibeam', 'a23')
SWAGINTOSH = Emote('swagintosh', 'a24')
RD_CRY = Emote('rdcry', 'a25')
AB_BORED = Emote('abbored', 'a26', 'abmerp')
SCOOTA_PLEASE = Emote('scootaplease', 'a27', 'scootappeal', 'scootaplz')
GRANNY_SMITH = Emote('grannysmith', 'a28', 'granny', 'oldmareyellsatcloud')
CADANCE = Emote('cadance', 'a29', 'cadence', 'princesscadance',
                'princesscadence', 'princessmiamorecadenza')
FLUTTER_ROLL = Emote('flutterroll', 'a30')
SPIKE_MEH = Emote('spikemeh', 'a31')
AB_MEH = Emote('abmeh', 'a32')
SCOOTA_DERP = Emote('scootaderp', 'a33', 'didneyworl', 'DIDNEYWORL')
PINKIE_AWE = Emote('pinkieawe', 'a34', 'areyouawizard', 'ppawe')
SILVER_SPOON = Emote('silverspoon', 'a35', 'sspout')
RARITY_REALLY = Emote('rarityreally', 'a36')
APPLE_GASP = Emote('applegasp', 'a37')
RARI_SHOCK = Emote('rarishock', 'a38')
APPLE_DERP = Emote('applederp', 'a39')

# Table B
FLUTTER_FEAR = Emote('flutterfear', 'b00')
AJ_COWER = Emote('ajcower', 'b01')
FLUTTER_SRS = Emote('fluttersrs', 'b02')
PP_SHRUG = Emote('ppshrug', 'b03')
FLUTTER_SHH = Emote('fluttershh', 'b04')
AJ_UGH = Emote('ajugh', 'b05')
TRIXIE_SMUG = Emote('trixiesmug', 'b06')
AJ_WUT = Emote('ajwut', 'b07')
AB_WUT = Emote('abwut', 'b08')
RARITY_JUDGE = Emote('rarityjudge', 'b09')
PP_BORING = Emote('ppboring', 'b10')
AJ_SLY = Emote('ajsly', 'b11')
RARITY_DRESS = Emote('raritydress', 'b12')
SPIKE_NERVOUS = Emote('spikenervous', 'b13', 'newrainbowdash')
FLUTTER_YAY = Emote('flutteryay', 'b14')
RARITY_WUT = Emote('raritywut', 'b15')
FLUTTER_WINK = Emote('flutterwink', 'b16')
TWI_SQUINT = Emote('twisquint', 'b17')
MAN_SPIKE = Emote('manspike', 'b18')
RARITY_PRIMP = Emote('rarityprimp', 'b19')
RARITY_YELL = Emote('rarityyell', 'b20')
EEYUP = Emote('eeyup', 'b21', 'bigmac')
TAKE_A_LETTER = Emote('takealetter', 'b22')
NOOOO = Emote('noooo', 'b23')
SQUINTY_JACK = Emote('squintyjack', 'b24')
DUMB_FABRIC = Emote('dumbfabric', 'b25')
RARITY_ANNOYED = Emote('rarityannoyed', 'b26')
RARITY_WHINE = Emote('raritywhine', 'b27')
COCKATRICE = Emote('cockatrice', 'b28')
TWI_RAGE = Emote('twirage', 'b29', 'ponyta')
FLUTTERSHY = Emote('fluttershy', 'b30')
RD_SMILE = Emote('rdsmile', 'b31')
RD_WUT = Emote('rdwut', 'b32')
DJ = Emote('dj', 'b33', 'threedog')
SPIKE_PUSHY = Emote('spikepushy', 'b34')
RARITY_WHY = Emote('raritywhy', 'b35')
SO_AWESOME = Emote('soawesome', 'b36')
RD_COOL = Emote('rdcool', 'b37')
FACE_HOOF = Emote('facehoof', 'b38')
PP_SEES_YOU = Emote('ppseesyou', 'b39')

# Table C
RD_SITTING = Emote('rdsitting', 'c00')
TWI_SMUG = Emote('twismug', 'c01')
OH_HI = Emote('ohhi', 'c02')
FLUTTER_BLUSH = Emote('flutterblush', 'c03')
AJ_FROWN = Emote('ajfrown', 'c04')
RARITY_SAD = Emote('raritysad', 'c05')
LOUDER = Emote('louder', 'c06')
PINKAMINA = Emote('pinkamina', 'c07')
SCOOTALOO = Emote('scootaloo', 'c08')
ALL_MY_BITS = Emote('allmybits', 'c09')
RD_HAPPY = Emote('rdhappy', 'c10')
TWI_SMILE = Emote('twismile', 'c11')
PARTY = Emote('party', 'c12')
GROSS = Emote('gross', 'c13')
HMMM = Emote('hmmm', 'c14')
FABULOUS = Emote('fabulous', 'c15')
LUNA_SAD = Emote('lunasad', 'c16')
LOVE_ME = Emote('loveme', 'c17')
CELESTIA = Emote('celestia', 'c18')
ZECORA = Emote('zecora', 'c19')
RD_ANNOYED = Emote('rdannoyed', 'c20')
TWI_STARE = Emote('twistare', 'c21')
HA_HA_HA = Emote('hahaha', 'c22')
DERPY_HAPPY = Emote('derpyhappy', 'c23', 'muffinshappy')
JOY = Emote('joy', 'c24')
DERP = Emote('derp', 'c25')
DERPY_SHOCK = Emote('derpyshock', 'c26', 'muffinsshock')
LUNA_GASP = Emote('lunagasp', 'c27')
ANGEL = Emote('angel', 'c28')
PHOTO_FINISH = Emote('photofinish', 'c29')
TRIXIE_SAD = Emote('trixiesad', 'c30')
CHANGELING = Emote('changeling', 'c31')
RD_SCARED = Emote('rdscared', 'c32')
TWI_DAW = Emote('twidaw', 'c33', 'twidaww')
WHAT_THE_FLUT = Emote('whattheflut', 'c34')
CADENCE_SMILE = Emote('cadencesmile', 'c35', 'cadancesmile')
SHINING_PRIDE = Emote('shiningpride', 'c36')
FLUTTER_CRY = Emote('fluttercry', 'c37')
SNEAKY_BELLE = Emote('sneakybelle', 'c38')
PP_REALLY = Emote('ppreally', 'c39')

# Table E
FILLY_TGAP = Emote('fillytgap', 'e00', 't00')
LYRA = Emote('lyra', 'e01', 'l00')
CUTEALOO = Emote('cutealoo', 'e02')
WA_HA_HA = Emote('wahaha', 'e03')
HUH_HUH = Emote('huhhuh', 'e04')
NMM = Emote('nmm', 'e05', 'blacksnooty', 'queenmeanie', 'hokeysmokes')
OCTAVIA = Emote('octavia', 'e06', 'whomeverthisis')
AJ_BAFFLE = Emote('ajbaffle', 'e07', 'ajconfused', 'ajtherapy')
TWI_PONDER = Emote('twiponder', 'e08')
GILDA = Emote('gilda', 'e09')
RD_HUH = Emote('rdhuh', 'e10')
BON_BON = Emote('bonbon', 'e11')
HAPPY_LUNA = Emote('happyluna', 'e12', 'lunahappy')
SB_STARE = Emote('sbstare', 'e13')  # Hi, Plounge!
AB_SMILE = Emote('absmile', 'e14')
WHOOVES = Emote('whooves', 'e15')
COLGATE = Emote('colgate', 'e16', 'minuette')
AB_HUH = Emote('abhuh', 'e17')
SPIKE_WTF = Emote('spikewtf', 'e18')
DISCENTIA = Emote('discentia', 'e19', 'discentiastare', 'disstare')
SNAILS = Emote('snails', 'e20')
SPITFIRE = Emote('spitfire', 'e21')
SO_TRUE = Emote('sotrue', 'e22')
PUNCH_DRUNK = Emote('punchdrunk', 'e23', 'berry')
DEAL_WITH_IT = Emote('dealwithit', 'e24')
RD_SALUTE = Emote('rdsalute', 'e25')
CHEERILEE = Emote('cheerilee', 'e26')
THE_HORROR = Emote('thehorror', 'e27', 'lily')
AWW_YEAH = Emote('awwyeah', 'e28')
MACINTEARS = Emote('macintears', 'e29', 'bigmactears')
TWI_SAD = Emote('twisad', 'e30')
LUNA_MAD = Emote('lunamad', 'e31')
DISCORD_SAD = Emote('discordsad', 'e32')
MAUD = Emote('maud', 'e33')
PINKIE_POUT = Emote('pinkiepout', 'e34')
TWI_SECRET = Emote('twisecret', 'e35', 'twiaside', 'smackafilly')
SUNSET_SHIMMER = Emote('sunsetshimmer', 'e36', 'ssshimmer')
SUNSET_SNEAKY = Emote('sunsetsneaky', 'e37', 'sneakyss', 'sneakysunset')
SCOOTABLUE = Emote('scootablue', 'e38', 'orphan', 'noparents')
SPIKE_HAPPY = Emote('spikehappy', 'e39')

# Table F
PINKIE_SAD = Emote('pinkiesad', 'f00', 'ppsad')
DIAMOND_TIARA = Emote('diamondtiara', 'f01', 'dt')
SOMBRA = Emote('sombra', 'f02')
SB_SHOCKED = Emote('sbshocked', 'f03')
GUARD = Emote('guard', 'f04')
AB_STERN = Emote('abstern', 'f05')  # Reddit's down? Hit this!
APATHIA = Emote('apathia', 'f06')
AJ_CRY = Emote('ajcry', 'f07')
RARITY_EWW = Emote('rarityeww', 'f08')
FLUTTER_KAY = Emote('flutterkay', 'f09', 'flutter:I', 'pokershy')
STARLIGHT_RAGE = Emote('starlightrage', 'f10')
BULK_BICEPS = Emote('bulkbiceps', 'f11', 'yeah')
SCOOTA_EWW = Emote('scootaeww', 'f12')
DISCORD_GRUMP = Emote('discordgrump', 'f13')
TROUBLESHOES = Emote('troubleshoes', 'f14')
RD_SNIRK = Emote('rdsnrk', 'f15')
TH_CALM = Emote('thcalm', 'f16', 'thc')
OOH = Emote('ooh', 'f17', 'pinkieooh')
RARITY_TIRED = Emote('raritytired', 'f18')
NOT_ANGRY = Emote('notangry', 'f19')
AJ_DOUBT = Emote('ajdoubt', 'f20')
SPIKE_WHOA = Emote('spikewhoa', 'f21', 'spikewoah', 'justaprankbro')
WASNT_ME = Emote('wasntme', 'f22', 'seafoam', 'seaswirl')
TWI_PBBT = Emote('twipbbt', 'f23')
FLIM_FLAM = Emote('flimflam', 'f24', 'flim')
COCO_SMILE = Emote('cocosmile', 'f25')
SKEPTILOO = Emote('skeptiloo', 'f26')
LIMESTONE_GRIN = Emote('limestonegrin', 'f27')
RARITY_GRUMP = Emote('raritygrump', 'f28')
GOOD_JOB = Emote('goodjob', 'f29', 'starlightgj', 'starlightgoodjob')
FLUTTER_HAY = Emote('flutterhay', 'f30')
SB_WTF = Emote('sbwtf', 'f31')
NIGHTMARE_GRIN = Emote('nightmaregrin', 'f32')
SPIKE_APPROVES = Emote('spikeapproves', 'f33')
FLUTTER_NICE = Emote('flutternice', 'f34', 'flutterheadtilt')
PP_DONT = Emote('ppdont', 'f35', 'pinkiedont')
AJ_GRUMP = Emote('ajgrump', 'f36')
SL_POPCORN = Emote('sgpopcorn', 'f37')
RARITY_SQUEE = Emote('raritysquee', 'f38')
GUMMY_STARE = Emote('gummystare', 'f39')

# Table G
KARMA = Emote('karma', 'g00')
DISCENTIA_JUDGE = Emote('discentiajudge', 'g01')
TWI_SNIDE = Emote('twisnide', 'g02')
PINKIE = Emote('pinkie', 'g03', 'pp')
COCO_COLD = Emote('cococold', 'g04')
QUIBBLE = Emote('quibble', 'g05')
RD_THIS = Emote('rdthis', 'g06')
FLUTTER_BROW = Emote('flutterbrow', 'g07')

# Other
POPSTAR = Emote('popstar')
SMOOZE = Emote('smooze')
FLAM = Emote('flam')

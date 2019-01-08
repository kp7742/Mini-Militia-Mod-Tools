import fileinput

num = 0
fn = ""
fn2 = ""
fn3 = ""
hx = ""
orig = ""
patch = ""
file = open("Patch-4.2.8-Beta.txt","w")
file2 = open("Code-4.2.8-Beta.txt","w")

def hexW(o):    
	for functionAddr in Functions():
		global fn
		global fn2
		global hx
		global num
		global orig
		global patch
		func = GetFunctionName(functionAddr)
		hx = hex(functionAddr).replace("L","")
		if fn2 == func:
			i = int(hx, 16)
			i += o
			hx = hex(i)
			num += 1
			if fn3 != "":
				file2.write("public final static int {0} = {1};\n\n".format(fn3,hx))
				
			file.write("{0}) {1}\n".format(num,fn))
			file.write("Offset: {0}\n".format(hx))
			file.write("Original: {0}\n".format(orig))
			file.write("Replaced: {0}\n\n".format(patch))
			break

file.write("""Doodle Army 2: Mini Militia

Version: v4.2.8

Modification Files: libcocos2dcpp.so

Note(Disclaimer): This is freely available patch list for public usage. if you want to share or use it in your mod then always give credits.
	              we are not responsible for any strike given by appsomniacs ltd. on your content. No support for any update in future.

-> Main Mods <-\n\n""")

#Main
fn = "Remove Early Quit Ads(First BL)"
fn2 = "_ZN20ApplicationInterface16checkQuitEarlyAdEP20QuitAdCheckInterface"
fn3 = "quitad"
orig = "4F 00 00 0A"
patch = "4F 00 00 EA"
hexW(0x28)

fn = "Game Run In Background"
fn2 = "_ZN11AppDelegate36applicationDidEnterBackgroundAndroidEPN7cocos2d8CCObjectE"
fn3 = "bkgrndplay"
orig = "00 48 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Lan Player Limit 256"
fn2 = "_ZN14PlayerLobbyLAN4initEv"
fn3 = "lan256"
orig = "10 10 A0 E3"
patch = "FF 10 A0 E3"
hexW(0xD0)

fn = "Custom Player Limit 12(LDR before Compare)"
fn2 = "_ZN18GameCustomizeLayer9addPlayerEPN7cocos2d8CCObjectE"
fn3 = "playerlobby12"
orig = "04 11 94 E5"
patch = "0C 10 A0 E3"
hexW(0x28)

fn = "Unlimited Health"
fn2 = "_ZN22SoldierLocalController9addDamageEfNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEib"
fn3 = "unlimitedhlth"
orig = "F0 4B 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Unlocked Propack"
fn2 = "_ZN10IapManager18isProductPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE"
fn3 = "propack"
orig = "30 48 2D E9 08 B0 8D E2"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Store Item Unlocked"
fn2 = "_ZN12ItemPurchase15isItemPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE"
fn3 = "storeitem"
orig = "70 4C 2D E9 10 B0 8D E2"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Unlimited Flying Power"
fn2 = "_ZN22SoldierLocalController8hasPowerEv"
fn3 = "ulimitednitro"
orig = "00 48 2D E9 0D B0 A0 E1"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Bullets Per Shots(00 to FF)"
fn2 = "_ZN6Weapon16getRoundsPerFireEv"
fn3 = "bulletpershot"
orig = "D8 01 90 E5"
patch = "** 00 A0 E3"
hexW(0x0)

fn = "Unlimited Ammo"
fn2 = "_ZN6Weapon7getAmmoEv"
fn3 = "unltdamo1"
orig = "83 1F A0 E3 F1 00 90 E1 00 00 50 E3 00 00 A0 D3"
patch = "83 1F A0 E3 04 20 A0 E3 B1 20 80 E1 F1 00 90 E1"
hexW(0x0)
fn = "Unlimited Clip"
fn2 = "_ZN6Weapon7getClipEv"
fn3 = "unltdamo2"
orig = "0E 12 00 E3 F1 00 90 E1 00 00 50 E3 00 00 A0 D3"
patch = "0E 12 00 E3 04 20 A0 E3 B1 20 80 E1 F1 00 90 E1"
hexW(0x0)

fn = "Weapon Reload Time"
fn2 = "_ZN6Weapon13getReloadTimeEv"
fn3 = "noreload"
orig = "60 0A 90 ED 67 1A 90 ED"
patch = "00 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Anti Gravity"
fn2 = "_ZN10MapManager16getGravityFactorEv"
fn3 = "nogravity"
orig = "74 00 90 E5"
patch = "00 00 A0 E3"
hexW(0x0)

fn = "Any Gun Dual Wield"
fn2 = "_ZN6Weapon11isDualWieldEv"
fn3 = "anydualgun1"
orig = "A7 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)
fn = "Any Gun Dual Wield2"
fn2 = "_ZN6Weapon22isDualWieldPrimaryOnlyEv"
fn3 = "anydualgun2"
orig = "A8 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)

fn = "Fly Through Walls"
fn2 = "_ZN10MapManager18addStaticBodyShapeEii"
fn3 = "flythwall"
orig = "F0 4F 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Robots Can't See"
fn2 = "_ZN5Enemy12canSeeTargetEv"
fn3 = "rinvisible"
orig = "F0 4B 2D E9 18 B0 8D E2"
patch = "00 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "All Weapon Laser"
fn2 = "_ZN13WeaponFactory12isLaserSightE8ItemType"
fn3 = "lasersight"
orig = "03 00 41 E2 07 00 50 E3"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Respawn Time Mod(MOV)"
fn2 = "_ZN14SoldierManager13respawnPlayerEPN7cocos2d8CCObjectE"
fn3 = "instantrespwn"
orig = "00 10 00 E3 10 11 44 E3"
patch = """00 7A F7 EE 90 1A 17 EE
		  00 10 00 E3 80 1F 43 E3"""
hexW(0x28)

fn = "Invisible Mod"
fn2 = "_ZN14NetworkManager16sendPositionDataEfb"
fn3 = "invisibleplayer"
orig = "70 4C 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Die By Guns Only"
fn2 = "_ZN9Explosion11applyDamageEf"
fn3 = "explosiondmg"
orig = "F0 4F 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)
fn = "Die By Guns Only2"
fn2 = "_ZN8GasCloud11applyDamageEf"
fn3 = "gasdmg"
orig = "F0 48 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)
fn = "Die By Guns Only3"
fn2 = "_ZN10PlasmaBall11applyDamageEf"
fn3 = "empdmg"
orig = "F0 4D 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Custom Skills(** - 0 to 99)"
fn2 = "_ZN17LeaderBoardBridge15calcPlayerSkillEv"
fn3 = "skill1"
orig = "10 4C 2D E9 08 B0 8D E2"
patch = "** 00 A0 E3 1E FF 2F E1"
hexW(0x0)
fn = "Custom Skills2"
fn2 = "_ZN17LeaderBoardBridge20getCachedPlayerSkillEv"
fn3 = "skill2"
orig = "0C 00 9F E5 00 00 9F E7"
patch = "** 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Custom Symbol(0=IOS, 1=Android, 2=Amazon Fire, 3=Windows)"
fn2 = "_ZN20ApplicationInterface9getOSTypeEv"
fn3 = "os"
orig = "01 00 A0 E3"
patch = "** 00 A0 E3"
hexW(0x0)

fn = "Bullet Speed Hack"
fn2 = "_ZN6Weapon14getBulletSpeedEv"
fn3 = "bulletspeed"
orig = "E0 01 90 E5"
patch = "FF 0F 0F E3"
hexW(0x0)

fn = "Speed Hack(Near =0.0001, #1.5)"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "flyspeed"
orig = "08 0A B7 EE"
patch = "08 0A B1 EE"
hexW(0xDCC)

fn = "Bullet Range Hack"
fn2 = "_ZN6Weapon8getRangeEv"
fn3 = "bulletrange"
orig = "C8 01 90 E5"
patch = "FF 0F 0F E3"
hexW(0x0)

fn = "Zoom Selector"
fn2 = "_ZN6Weapon12getZoomScaleEv"
fn3 = "zoomscale"
orig = "04 0A BA EE 68 2A 90 ED 58 1A 90 ED"
patch = "CD 0C 0C E3 CC 0E 43 E3 1E FF 2F E1"
hexW(0x0)

#Weapon Selector
file.write("-> Weapon Selector <-\n\n")
fn = "First Gun(LDR R1)"
fn2 = "_ZN13WeaponFactory23createRandomStartWeaponEv"
fn3 = "firstgun"
orig = "14 10 90 E5"
patch = "** 10 A0 E3"
hexW(0x68)
fn = "First Gun2"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "firstgun2"
orig = "1C 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x104)

fn = "Second Gun"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "secondgun"
orig = "00 10 A0 E1"
patch = "** 10 A0 E3"
hexW(0xC0)

fn = "First Bomb"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "firstbomb"
orig = "02 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x140)

fn = "Second Bomb"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "secondbomb"
orig = "00 10 A0 E1"
patch = "** 10 A0 E3"
hexW(0x1AC)

fn = "Weapon in Survival"
fn2 = "_ZN13SurvivalStage9playRoundEf"
fn3 = "survivalwep"
orig = "02 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x5C)

#Other
file.write("-> Other <-\n\n")
fn = "Bullet Through Walls"
fn2 = "_ZN6Tracer7onSparkE18cpSegmentQueryInfo"
fn3 = "bulletpasswall"
orig = "F0 4F 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Infinite Proxy Throw"
fn2 = "_ZN9PROXYNADE14updateItemStepEf"
fn3 = "infiproxy"
orig = "08 0A 30 EE"
patch = "00 F0 20 E3"
hexW(0x118)

fn = "Attach Proxy"
fn2 = "_ZN9PROXYNADE14updateItemStepEf"
fn3 = "proxystick"
orig = "6E 00 00 0A"
patch = "00 F0 20 E3"
hexW(0x168)

fn = "Auto Fire"
fn2 = "_ZN6Joypad4fireEv"
fn3 = "autofire"
orig = "2E 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)

fn = "No Bullet Spread"
fn2 = "_ZN6Weapon20getRandomFiringAngleEv"
fn3 = "nobulletspread"
orig = "10 0A 10 EE"
patch = "00 00 A0 E3"
hexW(0x70)

fn = "Any Weapon Lobby"
fn2 = "_ZN13WeaponManager22getWeaponForSpawnPointEPN7cocos2d12CCDictionaryE"
fn3 = "anyweapnlobby"
orig = "04 10 A0 E1"
patch = "** 10 A0 E3"
hexW(0x3C8)
fn = "Any Weapon Lobby2"
fn2 = "_ZN13WeaponFactory18createRandomWeaponEv"
fn3 = "anyweapnlobby2"
orig = "14 10 90 E5"
patch = "** 10 A0 E3"
hexW(0x68)

fn = "Instant Weapon Spawn"
fn2 = "_ZN13WeaponManager14setSpawnPeriodEPN7cocos2d12CCDictionaryEf"
fn3 = "instantwep1"
orig = "10 0A 10 EE"
patch = "00 00 A0 E3"
hexW(0xB0)
fn = "Instant Weapon Spawn2"
fn2 = "_ZN14NetworkManager13isLocalLeaderEv"
fn3 = "instwephost"
orig = "F0 4D 2D E9 18 B0 8D E2"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Maximum Game Time(CMP)"
fn2 = "_ZN18GameCustomizeLayer7addTimeEPN7cocos2d8CCObjectE"
fn3 = "gametime1"
orig = "E1 0F 50 E3 B4 00 00 C3"
patch = "00 F0 20 E3 00 F0 20 E3"
hexW(0x28)
fn = "Maximum Game Time2"
fn2 = "_ZN18GameCustomizeLayer7subTimeEPN7cocos2d8CCObjectE"
fn3 = "gametime2"
orig = "B4 00 50 E3"
patch = "00 00 50 E3"
hexW(0x28)

fn = "No Dual Throw"
fn2 = "_ZN22SoldierLocalController9throwDualEv"
fn3 = "nodualthrow"
orig = "08 00 00 0A"
patch = "08 00 00 EA"
hexW(0x94)

fn = "Magic Bomb Throw"
fn2 = "_ZN3HUD9onGrenadeEPN7cocos2d8CCObjectE"
fn3 = "fastbomb"
orig = "6B 1A 94 ED"
patch = "08 1A B7 EE"
hexW(0x54)

fn = "Magic Melee Punch"
fn2 = "_ZN3HUD7onPunchEPN7cocos2d8CCObjectE"
fn3 = "fastpunch"
orig = "6C 1A 94 ED"
patch = "08 1A B7 EE"
hexW(0x10)

fn = "Endless Saw(VADD)"
fn2 = "_ZN3SAW14updateItemStepEf"
fn3 = "endlesssaw"
orig = "00 1A 31 EE"
patch = "00 F0 20 E3"
hexW(0x38)

fn = "Hide Your Weapons"
fn2 = "_ZN14NetworkManager16sendWeaponChangeEPN7cocos2d8CCObjectE"
fn3 = "weaponhide"
orig = "70 4C 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Survival Play Count(00 to FF)"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "survivalround"
orig = "03 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x3C)

fn = "Sarge Weapon(00 to FF)"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "sargewep1"
orig = "05 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x1F0)
fn = "Sarge Weapon2"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "sargewep2"
orig = "05 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x214)

fn = "Any Map Survival"
fn2 = "_ZN14LocalGameLayer10onSurvivalEPN7cocos2d8CCObjectE"
fn3 = "survivalmap"
orig = "02 00 A0 E3"
patch = "03 00 A0 E3"
hexW(0x68)

fn = "Saw Damage Remove"
fn2 = "_ZN3SAW17checkMapCollisionEP17SoldierController"
fn3 = "nosawdamage"
orig = "F0 4B 2D E9 18 B0 8D E2"
patch = "00 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Hide from Proxy"
fn2 = "_ZN9ProxyMine10updateStepEf"
fn3 = "hideproxy"
orig = "0A 0A 30 EE"
patch = "00 F0 20 E3"
hexW(0x20)

fn = "Endless Proxy"
fn2 = "_ZN9ProxyMine10updateStepEf"
fn3 = "endlessproxy"
orig = "03 00 00 DA"
patch = "03 00 00 EA"
hexW(0xAC)

fn = "Fake Skills(00 to FF)"
fn2 = "_ZN14NetworkManager15sendPlayerSetupENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEiS6_iS6_"
fn3 = "fakeskill"
orig = "00 50 A0 E1"
patch = "** 50 A0 E3"
hexW(0x74)

fn = "High Damage Melee"
fn2 = "_ZN6Weapon14getMeleeDamageEv"
fn3 = "meleedamage"
orig = "C0 01 90 E5"
patch = "23 00 A0 E3"
hexW(0x0)

fn = "High Melee Length"
fn2 = "_ZN6Weapon14getMeleeLengthEv"
fn3 = "meleelength"
orig = "C4 01 90 E5"
patch = "FF 0F 0F E3"
hexW(0x0)

fn = "Dual Gun On Spawn"
fn2 = "_ZN6Weapon12pickupAsDualEv"
fn3 = "dualspawn"
orig = "E8 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)

fn = "Instant Health Fill(#0x1AC])"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "instanthealth"
orig = "09 00 00 DA"
patch = "09 00 00 EA"
hexW(0x638)

fn = "Kill Team Mate"
fn2 = "_ZN22SoldierLocalController10isSameTeamEi"
fn3 = "killteam"
orig = "10 4C 2D E9 08 B0 8D E2"
patch = "01 00 A0 E3 1E FF 2F E1"
hexW(0x0)

fn = "Custom Rank"
fn2 = "_ZN17LeaderBoardBridge13calcPlayerExpEv"
fn3 = "ranks"
orig = "00 48 2D E9 0D B0 A0 E1 87 B1 F9 EB 00 10 A0 E3 00 48 BD E8"
patch = "64 00 B0 E3 0A 10 B0 E3 90 00 10 E0 91 00 10 E0 1E FF 2F E1"
hexW(0x0)

fn = "Health And Nitro Charging EMP"
fn2 = "_ZN10PlasmaBall11applyDamageEf"
fn3 = "empreward"
orig = "16 10 A0 E3"
patch = """0E 10 A0 E3(Health)
          0F 10 A0 E3(Nitro)"""
hexW(0xC4)

fn = "No Damage Crouch"
fn2 = "_ZN22SoldierLocalController9addDamageEfNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEib"
fn3 = "nodamgduck"
orig = "9E E2 F9 EB 08 00 9B E5 00 00 8D E5"
patch = "66 01 D4 E5 00 00 50 E3 00 90 A0 13"
hexW(0x50)

fn = "Gas From Any Bomb"
fn2 = "_ZN14EffectsManager11onExplosionEPN7cocos2d8CCObjectE"
fn3 = "anybombgas"
orig = "14 00 9A E5"
patch = "14 00 A0 E3"
hexW(0xBC)

fn = "Half Damage"
fn2 = "_ZN22SoldierLocalController9addDamageEfNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEib"
fn3 = "halfdamage"
orig = "06 00 A0 E1 9E E2 F9 EB 08 00 9B E5 00 00 8D E5"
patch = "10 9A 08 EE 00 0A B0 EE 00 8A 88 EE 10 9A 18 EE"
hexW(0x4C)

fn = "Hide Bomb Throw"
fn2 = "_ZN14NetworkManager16sendWeaponCreateEPN7cocos2d8CCObjectE"
fn3 = "hidebombthrow"
orig = "70 4C 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

#Weapon Troll
file.write("-> Weapon Trolls <-\n\n")
fn = "Any Weapon as Granade"
fn2 = "_ZN17ProjectileManager10addGrenadeE6cpVectfS0_bNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEi"
fn3 = "fakebomb"
orig = "04 10 A0 E1"
patch = "** 10 A0 E3"
hexW(0x38)

fn = "Any Weapon from SMAW(Rocket Launcher)"
fn2 = "_ZN17ProjectileManager9addRocketE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromrocket"
orig = "0C 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x34)

fn = "Any Weapon from SAW Gun"
fn2 = "_ZN17ProjectileManager6addSawE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromsaw"
orig = "18 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x34)

fn = "Any Weapon from RG6(MortarLauncher)"
fn2 = "_ZN17ProjectileManager8addShellE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromrg6"
orig = "20 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x34)

#Death Sprayer
file.write("-> Death Sprayer <-\n\n")
fn = "Rocket Sprayer(SMAW)"
fn2 = "_ZN4SMAW11triggerPullEf"
fn3 = "dsprayrckt"
orig = "33 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "Saw Sprayer"
fn2 = "_ZN6SAWGUN11triggerPullEf"
fn3 = "dspraysaw"
orig = "4C 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x88)

fn = "MiniGun Sprayer"
fn2 = "_ZN7MINIGUN11triggerPullEf"
fn3 = "dspraymini"
orig = "39 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x7C)
fn = "MiniGun Sprayer2"
fn2 = "_ZN7MINIGUN11triggerPullEf"
fn3 = "dspraymini2"
orig = "34 00 00 BA"
patch = "00 F0 20 E3"
hexW(0x90)

fn = "EMP Sprayer"
fn2 = "_ZN3EMP11triggerPullEf"
fn3 = "dsprayemp"
orig = "4F 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x88)

fn = "Mortar Sprayer(RG6)"
fn2 = "_ZN3RG611triggerPullEf"
fn3 = "dsprayrg6"
orig = "33 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "Sniper Sprayer"
fn2 = "_ZN5M93BA11triggerPullEf"
fn3 = "dspraysnpr"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "Magnum Sprayer"
fn2 = "_ZN6MAGNUM11triggerPullEf"
fn3 = "dspraymgnm"
orig = "33 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "MP5 Sprayer"
fn2 = "_ZN3MP511triggerPullEf"
fn3 = "dspraymp5"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "TAVOR Sprayer"
fn2 = "_ZN5TAVOR11triggerPullEf"
fn3 = "dspraytavor"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "AK47 Sprayer"
fn2 = "_ZN4AK4711triggerPullEf"
fn3 = "dsprayak47"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "TEC9 Sprayer"
fn2 = "_ZN4TEC911triggerPullEf"
fn3 = "dspraytec9"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "AA12 Sprayer"
fn2 = "_ZN4AA1211triggerPullEf"
fn3 = "dsprayaa12"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

fn = "HuntingPistol Sprayer"
fn2 = "_ZN13HuntingPistol11triggerPullEf"
fn3 = "dsprayhunting"
orig = "37 00 00 DA"
patch = "00 F0 20 E3"
hexW(0x30)

#Testing
file.write("-> Test Mods <-\n\n")

fn = "Flag Rewarded Gun"
fn2 = "_ZN13WeaponManager10updateStepEf"
fn3 = "flagrewardedgun"
orig = "1C 10 A0 E3"
patch = "** 10 A0 E3"
hexW(0x3BC)

fn = "CTF always WIN"
fn2 = "_ZN13WeaponManager10updateStepEf"
fn3 = "ctfwinalways"
orig = "CB 00 00 0A"
patch = "00 F0 20 E3"
hexW(0x9C)

fn = "New Dual Wield1"
fn2 = "_ZN6Weapon11isDualWieldEv"
fn3 = "dualgun1"
orig = "A7 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)
fn = "New Dual Wield2"
fn2 = "_ZN6Weapon22isDualWieldPrimaryOnlyEv"
fn3 = "dualgun2"
orig = "A8 01 D0 E5"
patch = "01 00 A0 E3"
hexW(0x0)
fn = "New Dual Wield3"
fn2 = "_ZN14NetworkManager16sendWeaponChangeEPN7cocos2d8CCObjectE"
fn3 = "dualgun3"
orig = "70 4C 2D E9"
patch = "1E FF 2F E1"
hexW(0x0)

fn = "Walking Speed(Under =0.0001, #3.0)"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "walkspeed"
orig = "08 0A B0 EE"
patch = "0F 7A F3 EE"
hexW(0xAF4)

fn = "M16 Sprayer"
fn2 = "_ZN3M1614updateItemStepEf"
fn3 = "dspraym16"
orig = "2C 02 C4 E5 28 02 84 E5"
patch = "00 F0 20 E3 00 F0 20 E3"
hexW(0xEC)

fn = "Gas Cloud Color(Green and Red)(00 to FF)"
fn2 = "_ZN8GasCloudC2Ev"
fn3 = "gascloudcolor1"
orig = "64 1F 0F E3"
patch = "** 1* 0* E3"
hexW(0x98)
fn = "Gas Cloud Color(Blue)(00 to FF)"
fn2 = "_ZN8GasCloudC2Ev"
fn3 = "gascloudcolor2"
orig = "00 60 A0 E3"
patch = "00 ** A0 E3"
hexW(0x84)

fn = "No Color GasCloud"
fn2 = "_ZN8GasCloudC2Ev"
fn3 = "invisiblegas"
orig = "32 FF 2F E1"
patch = "00 F0 20 E3"
hexW(0xA8)

fn = "Die By Bombs Only"
fn2 = "_ZN24NetworkMessageDispatcher16updatePeerDamageEPN7cocos2d9extension6CCDataENSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE"
fn3 = "gundmg"
orig = "07 90 40 E0"
patch = "00 F0 20 E3"
hexW(0x80)

fn = "Magik Zoom1"
fn2 = "_ZN6Weapon15changeZoomLevelEv"
fn3 = "magikzoom1"
orig = "01 00 80 E2 5C 01 84 E5"
patch = "01 50 80 E2 5C 51 84 E5"
hexW(0x14)
fn = "Magik Zoom2"
fn2 = "_ZN6Weapon15changeZoomLevelEv"
fn3 = "magikzoom2"
orig = "68 01 94 E5 5C 51 94 E5 77 46 F9 EB 00 00 55 E1 00 10 A0 23 5C 11 84 25"
patch = "00 00 55 E1 FA 15 A0 03 60 11 84 05 07 00 00 0A 00 10 A0 83 5C 11 84 85"
hexW(0x30)

file.write("""-> Some Assembly Codes <-

MOV R0, #*(Value)(0 to 255)
BX   LR
= ** 00 A0 E3 1E FF 2F E1

BX   LR = 1E FF 2F E1

NOP = 00 F0 20 E3

BEQ - ** ** ** 0A
BNE - ** ** ** 1A
BHS - ** ** ** 2A
BLO - ** ** ** 3A
BMI - ** ** ** 4A
BPL - ** ** ** 5A
BVS - ** ** ** 6A
BVC - ** ** ** 7A
BHI - ** ** ** 8A
BLS - ** ** ** 9A
BGE - ** ** ** AA
BLT - ** ** ** BA
BGT - ** ** ** CA
BLE - ** ** ** DA
B   - ** ** ** EA

VADD.F32 S15, S14, S15 - 27 7A 77 EE
VSUB.F32 S15, S14, S15 - 67 7A 77 EE
VMUL.F32 S15, S14, S15 - 27 7A 67 EE
VDIV.F32 S15, S14, S15 - 27 7A C7 EE

VADD.F64 D7, D6, D7 - 07 7B 36 EE
VSUB.F64 D7, D6, D7 - 47 7B 36 EE
VMUL.F64 D7, D6, D7 - 07 7B 26 EE
VDIV.F64 D7, D6, D7 - 07 7B 86 EE

VMOV.F32 S15, #1.5 - 08 7A F7 EE
VMOV.F32 S15, #2.0 - 00 7A F0 EE
VMOV.F32 S15, #-1.5 - 08 7A FF EE
VMOV.F32 S15, #-2.0 - 00 7A F8 EE

VMOV.F32 S15, #1.0|
VMOV R0, S15      | - 00 7A F7 EE 90 0A 17 EE

-> Gun Mods Codes <-

MOVS R1,#*
WeaponFactory::createWeaponFromAmmoType
Codes:
MACHETE - 1
FRAGNADE - 2
DEAGLE - 3
MAGNUM - 4
UZI - 5
MP5 - 6
AK47 - 7
M16 - 8
SHOTGUN - 9
M93BA - 10 (A)
SMAW(ROCKETGUN) - 11 (B)
ROCKET - 12 (C)
RIOTSHIELD - 13 (D)
Healthpack - 14 (E)
Boosttank - 15 (F)
M14 - 16 (10)
PHASR - 17 (11)
GDEAGLE - 18 (12)
FLAMETHROWER - 19 (13)
GASNADE - 20 (14)
EMP - 21 (15)
PROXYNADE - 23 (17)
SAW - 24 (18)
SAWGUN - 25 (19)
TAVOR - 26 (1A)
MINIGUN - 27 (1B)
TEC9 - 28 (1C)
RG6(Mortar Launcher) - 29 (1D)
EMPNADE - 30 (1E)
XM8 - 31 (1F)
Mortar - 32 (20)
Flag Blue - 33 (21)
Flag Orange - 34 (22)
Hunting Pistol - 35 (23)
AA12 - 36 (24)

-> Zoom Mods Codes <-

0x3F800000 - 1x - 00 00 00 E3 80 0F 43 E3 1E FF 2F E1
0x3F666666 - 2x - 66 06 06 E3 66 0F 43 E3 1E FF 2F E1
0x3F4CCCCD - 3x - CD 0C 0C E3 4C 0F 43 E3 1E FF 2F E1
0x3F333333 - 4x - 33 03 03 E3 33 0F 43 E3 1E FF 2F E1
0x3F19999A - 5x - 9A 09 09 E3 19 0F 43 E3 1E FF 2F E1
0x3F000000 - 6x - 00 00 00 E3 00 0F 43 E3 1E FF 2F E1
0x3ECCCCCD - 7x - CD 0C 0C E3 CC 0E 43 E3 1E FF 2F E1
0x3E800000 - 8x - 00 00 00 E3 80 0E 43 E3 1E FF 2F E1
0x3E666666 - 9x - 0A 0A 01 E3 66 0E 43 E3 1E FF 2F E1
0x3E4CCCCD - 10x - CD 0C 0C E3 4C 0E 43 E3 1E FF 2F E1
0x3E333333 - 11x - 33 03 03 E3 33 0E 43 E3 1E FF 2F E1

-> SpawnTime Mods Codes <-

VMOV.F32 S15, #1.0 - 1s - 00 7A F7 EE
VMOV.F32 S15, #2.0 - 2s - 00 7A F0 EE
VMOV.F32 S15, #3.0 - 3s - 08 7A F0 EE
VMOV.F32 S15, #4.0 - 4s - 00 7A F1 EE
VMOV.F32 S15, #5.0 - 5s - 04 7A F1 EE
VMOV.F32 S15, #6.0 - 6s - 08 7A F1 EE
VMOV.F32 S15, #7.0 - 7s - 0C 7A F1 EE
VMOV.F32 S15, #8.0 - 8s - 00 7A F2 EE
VMOV.F32 S15, #9.0 - 9s - 02 7A F2 EE
VMOV.F32 S15, #10.0 - 10s - 04 7A F2 EE
VMOV.F32 S15, #11.0 - 11s - 06 7A F2 EE
VMOV.F32 S15, #30.0 - 30s - 0E 7A F3 EE
VMOV.F32 S15, #31.0 - 31s - 0F 7A F3 EE""")

print "\n\nTotal number of mods extracted:-"
print num
print "\n\t\tScript Created by KMODs...:)"

file.close()
file2.close()

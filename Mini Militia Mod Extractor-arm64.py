import fileinput

num = 0
fn = ""
fn2 = ""
fn3 = ""
hx = ""
orig = ""
patch = ""
file = open("Patch-4.3.3-arm64.txt","w")
file2 = open("Code-4.3.3-arm64.txt","w")

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

Lib Type: arm64-v8a : ARM64(64bit)

Version: v4.3.3 

Modification Files: libcocos2dcpp.so

Note(Disclaimer): This is freely available patch list for public usage. if you want to share or use it in your mod then always give credits.
	              we are not responsible for any strike given by appsomniacs ltd. on your content. No support for any update in future.

-> Main Mods <-\n\n""")

#Main
fn = "Remove Early Quit Ads(First BL)"
fn2 = "_ZN20ApplicationInterface16checkQuitEarlyAdEP20QuitAdCheckInterface"
fn3 = "quitad"
orig = "C8 09 00 34"
patch = "4E 00 00 14"
hexW(0x34)

fn = "Game Run In Background"
fn2 = "_ZN11AppDelegate36applicationDidEnterBackgroundAndroidEPN7cocos2d8CCObjectE"
fn3 = "bkgrndplay"
orig = "FD 7B BF A9"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Lan Player Limit 256"
fn2 = "_ZN14PlayerLobbyLAN4initEv"
fn3 = "lan256"
orig = "E1 03 1C 32"
patch = "A1 4A 80 52"
hexW(0xD0)

fn = "Custom Player Limit 12(LDR before Compare)"
fn2 = "_ZN18GameCustomizeLayer9addPlayerEPN7cocos2d8CCObjectE"
fn3 = "playerlobby12"
orig = "69 42 41 B9"
patch = "89 01 80 52"
hexW(0x2C)

fn = "Unlimited Health"
fn2 = "_ZN22SoldierLocalController9addDamageEfNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEib"
fn3 = "unlimitedhlth"
orig = "FF 83 01 D1"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Unlocked Propack"
fn2 = "_ZN10IapManager18isProductPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE"
fn3 = "propack"
orig = "F4 4F BE A9 FD 7B 01 A9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Store Item Unlocked"
fn2 = "_ZN12ItemPurchase15isItemPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE"
fn3 = "storeitem"
orig = "F5 0F 1D F8 F4 4F 01 A9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Unlimited Flying Power"
fn2 = "_ZN22SoldierLocalController8hasPowerEv"
fn3 = "ulimitednitro"
orig = "FD 7B BF A9 FD 03 00 91"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Bullets Per Shots"
fn2 = "_ZN6Weapon16getRoundsPerFireEv"
fn3 = "bulletpershot"
orig = "00 60 42 B9"
patch = "60 00 80 52"
hexW(0x0)

"""
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
"""

fn = "Weapon Reload Time"
fn2 = "_ZN6Weapon13getReloadTimeEv"
fn3 = "noreload"
orig = "00 08 42 BD 01 24 42 BD"
patch = "E0 03 1F 2A C0 03 5F D6"
hexW(0x0)

fn = "Anti Gravity"
fn2 = "_ZN10MapManager16getGravityFactorEv"
fn3 = "nogravity"
orig = "00 C0 40 BD"
patch = "E0 03 1F 2A"
hexW(0x0)

fn = "Any Gun Dual Wield"
fn2 = "_ZN6Weapon11isDualWieldEv"
fn3 = "anydualgun1"
orig = "00 BC 48 39"
patch = "20 00 80 52"
hexW(0x0)
fn = "Any Gun Dual Wield2"
fn2 = "_ZN6Weapon22isDualWieldPrimaryOnlyEv"
fn3 = "anydualgun2"
orig = "00 C0 48 39"
patch = "20 00 80 52"
hexW(0x0)

fn = "Fly Through Walls"
fn2 = "_ZN10MapManager18addStaticBodyShapeEii"
fn3 = "flythwall"
orig = "FF 83 03 D1"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Robots Can't See"
fn2 = "_ZN5Enemy12canSeeTargetEv"
fn3 = "rinvisible"
orig = "FF 83 01 D1 E9 23 03 6D"
patch = "E0 03 1F 2A C0 03 5F D6"
hexW(0x0)

fn = "All Weapon Laser"
fn2 = "_ZN13WeaponFactory12isLaserSightE8ItemType"
fn3 = "lasersight"
orig = "28 0C 00 51 1F 85 00 71"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Respawn Time Mod(MOV)"
fn2 = "_ZN14SoldierManager13respawnPlayerEPN7cocos2d8CCObjectE"
fn3 = "instantrespwn"
orig = "09 22 A8 52"
patch = "09 F0 A7 52"
hexW(0x1C)

fn = "Invisible Mod"
fn2 = "_ZN14NetworkManager16sendPositionDataEfb"
fn3 = "invisibleplayer"
orig = "F5 0F 1D F8"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Die By Guns Only"
fn2 = "_ZN9Explosion11applyDamageEf"
fn3 = "explosiondmg"
orig = "FF C3 03 D1"
patch = "C0 03 5F D6"
hexW(0x0)
fn = "Die By Guns Only2"
fn2 = "_ZN8GasCloud11applyDamageEf"
fn3 = "gasdmg"
orig = "FF C3 01 D1"
patch = "C0 03 5F D6"
hexW(0x0)
fn = "Die By Guns Only3"
fn2 = "_ZN10PlasmaBall11applyDamageEf"
fn3 = "empdmg"
orig = "FF 83 01 D1"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Custom Skills(** - 0 to 99)"
fn2 = "_ZN17LeaderBoardBridge15calcPlayerSkillEv"
fn3 = "skill1"
orig = "E8 0F 1E FC F3 07 00 F9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)
fn = "Custom Skills2"
fn2 = "_ZN17LeaderBoardBridge20getCachedPlayerSkillEv"
fn3 = "skill2"
orig = "88 55 00 90 08 45 42 F9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Custom Symbol(00=IOS, 02=Android, 04=Amazon Fire, 06=Windows)"
fn2 = "_ZN20ApplicationInterface9getOSTypeEv"
fn3 = "os"
orig = "E0 03 00 32"
patch = "** 00 80 52"
hexW(0x0)

fn = "Bullet Speed Hack"
fn2 = "_ZN6Weapon14getBulletSpeedEv"
fn3 = "bulletspeed"
orig = "00 68 42 B9"
patch = "E0 FF 9F 52"
hexW(0x0)

fn = "Speed Hack(Near =0.0001, #1.5)"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "flyspeed"
orig = "01 10 2F 1E"
patch = "01 10 23 1E"
hexW(0x93C)

fn = "Bullet Range Hack"
fn2 = "_ZN6Weapon8getRangeEv"
fn3 = "bulletrange"
orig = "00 50 42 B9"
patch = "E0 FF 9F 52"
hexW(0x0)

fn = "Zoom Selector"
fn2 = "_ZN6Weapon12getZoomScaleEv"
fn3 = "zoomscale"
orig = "00 28 42 BD 01 D4 41 BD 02 90 34 1E"
patch = "80 D9 A7 52 A0 99 99 72 C0 03 5F D6"
hexW(0x0)

#Weapon Selector
file.write("-> Weapon Selector <-\n\n")
fn = "First Gun(LDR R1)"
fn2 = "_ZN13WeaponFactory23createRandomStartWeaponEv"
fn3 = "firstgun"
orig = "01 18 40 B9"
patch = "41 00 80 52"
hexW(0x64)
fn = "First Gun2"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "firstgun2"
orig = "E1 0B 1E 32"
patch = "81 03 80 52"
hexW(0xF0)

fn = "Second Gun"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "secondgun"
orig = "E1 03 00 2A"
patch = "81 03 80 52"
hexW(0xAC)

fn = "First Bomb"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "firstbomb"
orig = "E1 03 1F 32"
patch = "81 03 80 52"
hexW(0x124)

fn = "Second Bomb"
fn2 = "_ZN14SoldierManager11spawnPlayerEv"
fn3 = "secondbomb"
orig = "E1 03 00 2A"
patch = "81 03 80 52"
hexW(0x188)

fn = "Weapon in Survival"
fn2 = "_ZN13SurvivalStage9playRoundEf"
fn3 = "survivalwep"
orig = "E1 03 1F 32"
patch = "81 03 80 52"
hexW(0x5C)

#Other
file.write("-> Other <-\n\n")
fn = "Bullet Through Walls"
fn2 = "_ZN6Tracer7onSparkE18cpSegmentQueryInfo"
fn3 = "bulletpasswall"
orig = "FF 03 02 D1"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Infinite Proxy Throw"
fn2 = "_ZN9PROXYNADE14updateItemStepEf"
fn3 = "infiproxy"
orig = "00 28 28 1E"
patch = "1F 20 03 D5"
hexW(0x104)

fn = "Attach Proxy"
fn2 = "_ZN9PROXYNADE14updateItemStepEf"
fn3 = "proxystick"
orig = "A8 0D 00 34"
patch = "1F 20 03 D5"
hexW(0x140)

fn = "Auto Fire"
fn2 = "_ZN6Joypad4fireEv"
fn3 = "autofire"
orig = "00 28 46 39"
patch = "20 00 80 52"
hexW(0x0)

fn = "No Bullet Spread"
fn2 = "_ZN6Weapon20getRandomFiringAngleEv"
fn3 = "nobulletspread"
orig = "08 00 38 1E"
patch = "08 00 80 52"
hexW(0x2C)

fn = "Any Weapon Lobby"
fn2 = "_ZN13WeaponManager22getWeaponForSpawnPointEPN7cocos2d12CCDictionaryE"
fn3 = "anyweapnlobby"
orig = "E1 03 13 2A"
patch = "41 00 80 52"
hexW(0x3FC)
fn = "Any Weapon Lobby2"
fn2 = "_ZN13WeaponFactory18createRandomWeaponEv"
fn3 = "anyweapnlobby2"
orig = "01 18 40 B9"
patch = "41 00 80 52"
hexW(0x64)

fn = "Instant Weapon Spawn"
fn2 = "_ZN13WeaponManager14setSpawnPeriodEPN7cocos2d12CCDictionaryEf"
fn3 = "instantwep1"
orig = "00 29 20 1E"
patch = "E0 03 27 1E"
hexW(0x98)
fn = "Instant Weapon Spawn2"
fn2 = "_ZN14NetworkManager13isLocalLeaderEv"
fn3 = "instwephost"
orig = "FF 83 01 D1 F7 13 00 F9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Maximum Game Time(CMP)"
fn2 = "_ZN18GameCustomizeLayer7addTimeEPN7cocos2d8CCObjectE"
fn3 = "gametime1"
orig = "1F 11 0E 71 28 C1 88 1A"
patch = "1F 20 03 D5 1F 20 03 D5"
hexW(0x34)
fn = "Maximum Game Time2"
fn2 = "_ZN18GameCustomizeLayer7subTimeEPN7cocos2d8CCObjectE"
fn3 = "gametime2"
orig = "1F D1 02 71"
patch = "1F 01 00 71"
hexW(0x34)

fn = "No Dual Throw"
fn2 = "_ZN22SoldierLocalController9throwDualEv"
fn3 = "nodualthrow"
orig = "48 01 00 B4"
patch = "0A 00 00 14"
hexW(0x9C)

fn = "Magic Bomb Throw"
fn2 = "_ZN3HUD9onGrenadeEPN7cocos2d8CCObjectE"
fn3 = "fastbomb"
orig = "CD 00 00 54"
patch = "1F 20 03 D5"
hexW(0x5C)

fn = "Magic Melee Punch"
fn2 = "_ZN3HUD7onPunchEPN7cocos2d8CCObjectE"
fn3 = "fastpunch"
orig = "AD 01 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "Endless Saw(VADD)"
fn2 = "_ZN3SAW14updateItemStepEf"
fn3 = "endlesssaw"
orig = "00 28 28 1E"
patch = "1F 20 03 D5"
hexW(0x44)

fn = "Hide Your Weapons"
fn2 = "_ZN14NetworkManager16sendWeaponChangeEPN7cocos2d8CCObjectE"
fn3 = "weaponhide"
orig = "F5 0F 1D F8"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Survival Play Count(00 to FF)"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "survivalround"
orig = "E1 07 00 32"
patch = "81 01 80 52"
hexW(0x38)

fn = "Sarge Weapon(00 to FF)"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "sargewep1"
orig = "A1 00 80 52"
patch = "81 01 80 52"
hexW(0x1F4)
fn = "Sarge Weapon2"
fn2 = "_ZN13SurvivalStage10setupStageEv"
fn3 = "sargewep2"
orig = "A1 00 80 52"
patch = "81 01 80 52"
hexW(0x218)

fn = "Any Map Survival"
fn2 = "_ZN14LocalGameLayer10onSurvivalEPN7cocos2d8CCObjectE"
fn3 = "survivalmap"
orig = "EA 03 1F 32"
patch = "EA 07 00 32"
hexW(0x5C)

fn = "Saw Damage Remove"
fn2 = "_ZN3SAW17checkMapCollisionEP17SoldierController"
fn3 = "nosawdamage"
orig = "FF C3 01 D1 EA 1B 00 FD"
patch = "01 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Hide from Proxy"
fn2 = "_ZN9ProxyMine10updateStepEf"
fn3 = "hideproxy"
orig = "20 28 28 1E"
patch = "1F 20 03 D5"
hexW(0x34)

fn = "Endless Proxy"
fn2 = "_ZN9ProxyMine10updateStepEf"
fn3 = "endlessproxy"
orig = "AD 00 00 54"
patch = "05 00 00 14"
hexW(0xB0)

fn = "Fake Skills(00 to FF)"
fn2 = "_ZN14NetworkManager15sendPlayerSetupENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEiS6_iS6_"
fn3 = "fakeskill"
orig = "FA 03 00 2A"
patch = "1A 00 80 52"
hexW(0xA0)

fn = "High Damage Melee"
fn2 = "_ZN6Weapon14getMeleeDamageEv"
fn3 = "meleedamage"
orig = "00 48 42 B9"
patch = "60 04 80 52"
hexW(0x0)

fn = "High Melee Length"
fn2 = "_ZN6Weapon14getMeleeLengthEv"
fn3 = "meleelength"
orig = "00 4C 42 B9"
patch = "E0 FF 81 52"
hexW(0x0)

fn = "Dual Gun On Spawn"
fn2 = "_ZN6Weapon12pickupAsDualEv"
fn3 = "dualspawn"
orig = "00 C0 49 39"
patch = "20 00 80 52"
hexW(0x0)

fn = "Instant Health Fill(#0x1AC])"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "instanthealth"
orig = "2D 01 00 54"
patch = "09 00 00 14"
hexW(0x5D8)

fn = "Kill Team Mate"
fn2 = "_ZN22SoldierLocalController10isSameTeamEi"
fn3 = "killteam"
orig = "F3 0F 1E F8 FD 7B 01 A9"
patch = "20 00 80 52 C0 03 5F D6"
hexW(0x0)

fn = "Custom Rank"
fn2 = "_ZN17LeaderBoardBridge13calcPlayerExpEv"
fn3 = "ranks"
orig = "FD 7B BF A9 FD 03 00 91 26 03 FA 97 E1 03 1F 2A FD 7B C1 A8"
patch = "80 0C 80 52 41 01 80 52 00 7C 00 1B 20 7C 00 1B C0 03 5F D6"
hexW(0x0)

fn = "Health And Nitro Charging EMP"
fn2 = "_ZN10PlasmaBall11applyDamageEf"
fn3 = "empreward"
orig = "C1 02 80 52"
patch = """C1 01 80 52(Health)
          E1 01 80 52(Nitro)"""
hexW(0xA4)

fn = "Gas From Any Bomb"
fn2 = "_ZN14EffectsManager11onExplosionEPN7cocos2d8CCObjectE"
fn3 = "anybombgas"
orig = "88 1A 40 B9"
patch = "88 02 80 52"
hexW(0xC4)

fn = "Hide Bomb Throw"
fn2 = "_ZN14NetworkManager16sendWeaponCreateEPN7cocos2d8CCObjectE"
fn3 = "hidebombthrow"
orig = "F5 0F 1D F8"
patch = "C0 03 5F D6"
hexW(0x0)

#Weapon Troll
file.write("-> Weapon Trolls <-\n\n")
fn = "Any Weapon as Granade"
fn2 = "_ZN17ProjectileManager10addGrenadeE6cpVectfS0_bNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEi"
fn3 = "fakebomb"
orig = "E1 03 13 2A"
patch = "81 02 80 52"
hexW(0x54)

fn = "Any Weapon from SMAW(Rocket Launcher)"
fn2 = "_ZN17ProjectileManager9addRocketE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromrocket"
orig = "E1 07 1E 32"
patch = "81 01 80 52"
hexW(0x50)

fn = "Any Weapon from SAW Gun"
fn2 = "_ZN17ProjectileManager6addSawE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromsaw"
orig = "E1 07 1D 32"
patch = "01 03 80 52"
hexW(0x50)

fn = "Any Weapon from RG6(MortarLauncher)"
fn2 = "_ZN17ProjectileManager8addShellE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE"
fn3 = "fromrg6"
orig = "E1 03 1B 32"
patch = "01 04 80 52"
hexW(0x50)

#Death Sprayer
file.write("-> Death Sprayer <-\n\n")
fn = "Rocket Sprayer(SMAW)"
fn2 = "_ZN4SMAW11triggerPullEf"
fn3 = "dsprayrckt"
orig = "4D 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "Saw Sprayer"
fn2 = "_ZN6SAWGUN11triggerPullEf"
fn3 = "dspraysaw"
orig = "2D 08 00 54"
patch = "1F 20 03 D5"
hexW(0x68)

fn = "MiniGun Sprayer"
fn2 = "_ZN7MINIGUN11triggerPullEf"
fn3 = "dspraymini"
orig = "2D 06 00 54"
patch = "1F 20 03 D5"
hexW(0x50)
fn = "MiniGun Sprayer2"
fn2 = "_ZN7MINIGUN11triggerPullEf"
fn3 = "dspraymini2"
orig = "AB 05 00 54"
patch = "1F 20 03 D5"
hexW(0x60)

fn = "EMP Sprayer"
fn2 = "_ZN3EMP11triggerPullEf"
fn3 = "dsprayemp"
orig = "ED 08 00 54"
patch = "1F 20 03 D5"
hexW(0x6C)

fn = "Mortar Sprayer(RG6)"
fn2 = "_ZN3RG611triggerPullEf"
fn3 = "dsprayrg6"
orig = "4D 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "Sniper Sprayer"
fn2 = "_ZN5M93BA11triggerPullEf"
fn3 = "dspraysnpr"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "Magnum Sprayer"
fn2 = "_ZN6MAGNUM11triggerPullEf"
fn3 = "dspraymgnm"
orig = "4D 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "MP5 Sprayer"
fn2 = "_ZN3MP511triggerPullEf"
fn3 = "dspraymp5"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "TAVOR Sprayer"
fn2 = "_ZN5TAVOR11triggerPullEf"
fn3 = "dspraytavor"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "AK47 Sprayer"
fn2 = "_ZN4AK4711triggerPullEf"
fn3 = "dsprayak47"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "TEC9 Sprayer"
fn2 = "_ZN4TEC911triggerPullEf"
fn3 = "dspraytec9"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "AA12 Sprayer"
fn2 = "_ZN4AA1211triggerPullEf"
fn3 = "dsprayaa12"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

fn = "HuntingPistol Sprayer"
fn2 = "_ZN13HuntingPistol11triggerPullEf"
fn3 = "dsprayhunting"
orig = "CD 05 00 54"
patch = "1F 20 03 D5"
hexW(0x1C)

#Testing
file.write("-> Test Mods <-\n\n")

fn = "Flag Rewarded Gun"
fn2 = "_ZN13WeaponManager10updateStepEf"
fn3 = "flagrewardedgun"
orig = "E1 0B 1E 32"
patch = "81 01 80 52"
hexW(0x910)

fn = "CTF always WIN"
fn2 = "_ZN13WeaponManager10updateStepEf"
fn3 = "ctfwinalways"
orig = "F7 0D 00 B4"
patch = "1F 20 03 D5"
hexW(0x90)

fn = "New Dual Wield1"
fn2 = "_ZN6Weapon11isDualWieldEv"
fn3 = "dualgun1"
orig = "00 BC 48 39"
patch = "20 00 80 52"
hexW(0x0)
fn = "New Dual Wield2"
fn2 = "_ZN6Weapon22isDualWieldPrimaryOnlyEv"
fn3 = "dualgun2"
orig = "00 C0 48 39"
patch = "20 00 80 52"
hexW(0x0)
fn = "New Dual Wield3"
fn2 = "_ZN14NetworkManager16sendWeaponChangeEPN7cocos2d8CCObjectE"
fn3 = "dualgun3"
orig = "F5 0F 1D F8"
patch = "C0 03 5F D6"
hexW(0x0)

fn = "Walking Speed(Under =0.0001, #3.0)"
fn2 = "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f"
fn3 = "walkspeed"
orig = "01 10 21 1E"
patch = "01 F0 27 1E"
hexW(0xAB0)

fn = "M16 Sprayer"
fn2 = "_ZN3M1614updateItemStepEf"
fn3 = "dspraym16"
orig = "7F 32 0B 39 7F CA 02 B9"
patch = "1F 20 03 D5 1F 20 03 D5"
hexW(0xC0)

fn = "Gas Cloud Color(Green and Red and Blue)(00 to FF)"
fn2 = "_ZN8GasCloudC2Ev"
fn3 = "gascloudcolor1"
orig = "89 EC 9F 52 08 00 40 F9 08 BD 41 F9 FF 0B 00 39 E9 03 00 79"
patch = "08 00 40 F9 08 BD 41 F9 89 05 80 52 89 EC BF 72 E9 03 00 B9"
hexW(0x8C)

fn = "No Color GasCloud"
fn2 = "_ZN8GasCloudC2Ev"
fn3 = "invisiblegas"
orig = "00 01 3F D6"
patch = "1F 20 03 D5"
hexW(0xA4)

fn = "Die By Bombs Only"
fn2 = "_ZN24NetworkMessageDispatcher16updatePeerDamageEPN7cocos2d9extension6CCDataENSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE"
fn3 = "gundmg"
orig = "08 03 16 CB"
patch = "1F 20 03 D5"
hexW(0x8C)

"""
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
"""

file.write("""-> Some Assembly Codes <-

MOV W0, #*(Value)(0 to 255)
RET
= ** 00 80 52 C0 03 5F D6

RET = C0 03 5F D6

NOP = 1F 20 03 D5

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

0x3F800000 - 1x - 09 00 80 52 09 F0 A7 72 C0 03 5F D6
0x3F666666 - 2x - C9 CC 8C 52 C9 EC A7 72 C0 03 5F D6
0x3F4CCCCD - 3x - A9 99 99 52 89 E9 A7 72 C0 03 5F D6
0x3F333333 - 4x - 69 66 86 52 69 E6 A7 72 C0 03 5F D6
0x3F19999A - 5x - 49 33 93 52 29 E3 A7 72 C0 03 5F D6
0x3F000000 - 6x - 09 00 80 52 09 E0 A7 72 C0 03 5F D6
0x3ECCCCCD - 7x - A9 99 99 52 89 D9 A7 72 C0 03 5F D6
0x3E800000 - 8x - 09 00 80 52 09 D0 A7 72 C0 03 5F D6
0x3E666666 - 9x - C9 CC 8C 52 C9 CC A7 72 C0 03 5F D6
0x3E4CCCCD - 10x - A9 99 99 52 89 C9 A7 72 C0 03 5F D6
0x3E333333 - 11x - 69 66 86 52 69 C6 A7 72 C0 03 5F D6

-> SpawnTime Mods Codes <-

FMOV S0, #1.0 - 1s - 00 10 2E 1E
FMOV S0, #2.0 - 2s - 00 10 20 1E
FMOV S0, #3.0 - 3s - 00 10 21 1E
FMOV S0, #4.0 - 4s - 00 10 22 1E
FMOV S0, #5.0 - 5s - 00 90 22 1E
FMOV S0, #6.0 - 6s - 00 10 23 1E
FMOV S0, #7.0 - 7s - 00 90 23 1E
FMOV S0, #8.0 - 8s - 00 10 24 1E
FMOV S0, #9.0 - 9s - 00 50 24 1E
FMOV S0, #10.0 - 10s - 00 90 24 1E
FMOV S0, #11.0 - 11s - 00 D0 24 1E
FMOV S0, #30.0 - 30s - 00 D0 27 1E
FMOV S0, #31.0 - 31s - 00 F0 27 1E""")

print "\n\nTotal number of mods extracted:-"
print num
print "\n\t\tScript Created by KMODs...:)"

file.close()
file2.close()

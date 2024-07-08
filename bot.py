import telebot
import time
import os
import zipfile
from urllib.parse import urlparse
from telebot import types
import requests
import psutil
import json
import random
nigger = "6301231502:AAFiTEgtwhDbTJNWvTa-S1Z8kb3peM0oAgw"
linkbuoi = "https://t.me/sieunhansex"
idad = "5990807551"
bot = telebot.TeleBot(nigger)
@bot.message_handler(commands=["help"])
def buoi(message):
	danhsach = [
		"/attack - [Host] [Time] [Methods] | Lệnh ddos free",
		"/methods - Methods ddos",
		"/profile - xem profile của bạn",
		"/check - Dùng để check website",
		"/ask - Dùng để hỏi gemini ai",
		"/askv2 - Api thứ 2",
		"/admin - Thông tin owner và developer",
		"/proxies - get proxyscrape",
		"/informationmanager - Xem thông tin của admin và owner",
		"/anime - random 1 bức ảnh anime",
		"/status - Xem thông tin vps",
		"/install - tải một số thứ"
	]
	concac = "Danh sách lệnh có thể sử dụng: \n"
	for cailon in danhsach:
		concac += cailon + "\n"
	bot.reply_to(message, concac)
@bot.message_handler(commands=['start'])
def buoi(message):
        bot.reply_to(message, "Danh sách các lệnh:\n/help: xem các lệnh có thể sử dụng");
@bot.message_handler(commands=["methods"])
def buoi(message):
	method = [
		"FLOOD | Free",
		"TCPRAW | FREE",
		"",
		"TLS | VIP",
		"RAPIDRESET | VIP",
		"HTTP2 | VIP",
		"TLSV2 | VIP",
		"TCPFAMOD | VIP",
	]
	phonglon = "Danh sách methods:\n"
	for ngu in method:
		phonglon += ngu + "\n"
	bot.reply_to(message, phonglon)
@bot.message_handler(commands=["check"])
def buoi(message):
	try:
		url = message.text.split(" ")[1]
	except IndexError:
		bot.reply_to(message, "🚫 Sai cách sử dụng, /check <target>")
		return
	try:
		cac = requests.get(url)
		print(cac.headers)
		protocol = urlparse(cac.request.url).scheme
		response = cac.status_code
		authority = urlparse(url).hostname
		date = cac.headers["Date"]
		scheme = urlparse(url).scheme
		path = cac.headers.get("path")
		isp = cac.headers.get("Server", "Invalid")
		domain = cac.headers.get("Domain", "Invalid")
		xamlon = f"Host: {authority}\nProtocol: {protocol}\nResponse: {response}\nScheme: {scheme}\nPath: {path}\nISP: {isp}\nDate: {date}\nDomain: {domain}"
		bot.reply_to(message, xamlon)
	except requests.exceptions.RequestException:
		bot.reply_to(message, "Hostname không tồn tại")
#@bot.message_handler(commands=["register"])
#def buoi(message):
#	idng = message.from_user.id
#	username = message.from_user.username
#	if (idng == 7338336630):
#		bot.reply_to(message, "🚫 Đéo tiếp rác,vô học thức!")
#	try:
#		with open("user.json", "r") as file:
#			usex = json.load(file)
##	except FileNotFoundError:
#		print("Tạo file đi thằng nguuu")
#		exit()
#	check = next((usex for usex in usex if usex["id"] == idng), None)
#	if check:
#		bot.reply_to(message, "🚫 Bạn đã có tài khoản,không thể tạo thêm")
#	else:
#		newus = {
#			"id": idng,
#			"username": username,
#			"VIP": False,
#		}
##		usex.insert(index, newus)
#		with open("user.json", "w") as file:
#			json.dump(usex, file)
#		if (idng == 5544589325):
#			bot.reply_to(message, "Cute thía")
#		bot.reply_to(message, f"Tạo tài khoản thành công ✅\nThông tin tài khoản:\nID: {idng}\nUsername: {username}\nVIP: False")
@bot.message_handler(commands=["profile"])
def buoi(message):
	try:
		if message.reply_to_message and message.reply_to_message.from_user:
			id = message.reply_to_message.from_user.id
			username = message.reply_to_message.from_user.username
			name = message.reply_to_message.from_user.first_name
			bio = message.reply_to_message.from_user.bio if hasattr(message.reply_to_message.from_user, 'bio') else "Bio not available"
		else:
			args = message.text.split(" ")
			if len(args) > 1:
				ditloncode = args[1]
				if ditloncode.startswith("@"):
					ditloncode = ditloncode[1:]
					loncd = bot.get_chat(ditloncode)
					if loncd:
						try:
							id = loncd.id
							username = loncd.username
							name = loncd.first_name
							bio = loncd.bio if hasattr(loncd, 'bio') else "Bio not available"
						except telebot.apihelper.ApiTelegramException as e:
							if "chat not found" in e.message:
								bot.reply_to(message, "🚫 Không thể get thông tin người dùng này")
								return
				else:
					bot.reply_to(message, "🚫 Username không tồn tại")
					return
			else:
				id = message.from_user.id
				username = message.from_user.username
				name = message.from_user.first_name
				bio = message.from_user.bio if hasattr(message.from_user, 'bio') else "Bio not available"
		bot.reply_to(message, f"`⚖ Thông tin người dùng ⚖:\nID: {id}\nUsername: {username}\nName: {name}\nBio: {bio}`", parse_mode="MarkdownV2")
	except telebot.apihelper.ApiTelegramException as e:
		bot.reply_to(message, "🚫 Không thể get thông tin người dùng này")
		return
def postcauhoi(cauhoi):
	phongnguchibietbucudauhang = {
		"contents": [
			{
				"parts": [
					{
						"text": cauhoi
					}
				]
			}
		]
	}
	upcauhoi = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDMnyPdgAbctOMwx0pnXKDyR3bldXAzhaA", json= phongnguchibietbucudauhang)
	if upcauhoi.status_code == 200:
		dapan = upcauhoi.json()
		skibidi = dapan["candidates"][0]["content"]["parts"][0]["text"]
		return skibidi
@bot.message_handler(commands=["ask"])
def buoi(message):
	cauhoi = message.text.split(" ", 1)
	if len(cauhoi) < 2:
		bot.reply_to(message, "Baby à,em phải nhập câu hỏi sau lệnh ask chứ!")
		return
	up = postcauhoi(cauhoi[1])
	sex = bot.reply_to(message, "⏳Đợi để lấy câu trả lời ...")
	time.sleep(3)
	bot.delete_message(chat_id=message.chat.id, message_id=sex.message_id)
	bot.reply_to(message, f"🌸 Đáp án:\n{up}")
@bot.message_handler(commands=["admin"])
def buoi(message):
	phongnguchibietbucuxintha = types.InlineKeyboardMarkup(row_width=1)
	dev = types.InlineKeyboardButton("☕ developer personal page ☕", url="t.me/imWiliams")
	owner = types.InlineKeyboardButton("🚀 Owner 🚀", url="t.me/nminhniee")
	group1 = types.InlineKeyboardButton("🧸powerproof channel 🧸", url="t.me/Famod_Channel")
	group2 = types.InlineKeyboardButton("🍷 Messaging channel 🍷", url="t.me/Famod_Service")
	phongnguchibietbucuxintha.add(dev, owner, group1, group2)
	bot.reply_to(message, "Thông tin admin và developer:", reply_markup=phongnguchibietbucuxintha)
user_state = {}
@bot.message_handler(commands=["proxies"])
def buoi(message):
    vanhgay = types.InlineKeyboardMarkup()
    vanhgay.row(
        types.InlineKeyboardButton("🍬 socks4 🍬", callback_data="socks4"),
        types.InlineKeyboardButton("🛰️ socks5 🛰️", callback_data="socks5"),
    )
    vanhgay.row(
        types.InlineKeyboardButton("🎄http 🎄", callback_data="http"),
        types.InlineKeyboardButton("🌍 all 🌍", callback_data="all"),
    )
    bot.send_message(message.chat.id, "💦 Chọn protocol 💦:", reply_markup=vanhgay)

@bot.callback_query_handler(func=lambda call: call.data in ["socks4", "socks5", "http", "all"])
def protocol_chosen(call):
    protocolchose = call.data
    user_state[call.message.chat.id] = {'protocol': protocolchose}
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    vanhngu = types.InlineKeyboardMarkup()
    for i in range(1, 11):
        vanhngu.row(types.InlineKeyboardButton(str(i * 1000), callback_data=str(i * 1000)))
    bot.send_message(call.message.chat.id, "⏰ chọn timeout ⏰:", reply_markup=vanhngu)

@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def timeout_chosen(call):
    timeoutchose = call.data
    user_state[call.message.chat.id]['timeout'] = timeoutchose
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    xukacodderngunhucho = types.InlineKeyboardMarkup()
    xukacodderngunhucho.row(
        types.InlineKeyboardButton("👑 Yes 👑", callback_data="yes"),
        types.InlineKeyboardButton("🌴 No 🌴", callback_data="no"),
        types.InlineKeyboardButton("❄️ All ❄", callback_data="all"),
    )
    bot.send_message(call.message.chat.id, "🌴 Vui lòng chọn ssl 🌴: ", reply_markup=xukacodderngunhucho)

@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no", "all"])
def ssl_chosen(call):
    sslchose = call.data
    user_state[call.message.chat.id]['ssl'] = sslchose
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    ngao = bot.send_message(call.message.chat.id, "⏳Vui lòng đợi để lấy proxy ⏳")
    time.sleep(4)

    state = user_state[call.message.chat.id]
    protocol = state['protocol']
    timeout = state['timeout']
    ssl = state['ssl']
    proxies = requests.get(
        f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={timeout}&country=all&ssl={ssl}&anonymity=all"
    ).text

    with open("proxies.txt", "w") as file:
        file.write(proxies)

    bot.delete_message(chat_id=call.message.chat.id, message_id=ngao.message_id)

    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(8))
    with zipfile.ZipFile("proxies.zip", "w") as zip_file:
        zip_file.write("proxies.txt")
        zip_file.setpassword(password.encode())

    bot.send_document(
        call.message.chat.id, 
        open("proxies.zip", "rb"), 
        caption=f"🌴 Thông tin chi tiết:\n🌿 Số proxy 🌿: {len(proxies.splitlines())}\n🍁Timeout 🍁: {timeout}\n🍇 Ssl 🍇: {ssl}\n🔒Password 🔒: {password}"
    )
    del user_state[call.message.chat.id]
def postcauhoiv2(cauhoi):
	phongnguchibietbucudauhang = {
		"contents": [
			{
				"parts": [
					{
						"text": cauhoi
					}
				]
			}
		]
	}
	upcauhoi = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCXqgUyrwyrzvrNcd7FITHPL6eFYiIF3JQ ", json= phongnguchibietbucudauhang)
	if upcauhoi.status_code == 200:
		dapan = upcauhoi.json()
		skibidi = dapan["candidates"][0]["content"]["parts"][0]["text"]
		return skibidi
@bot.message_handler(commands=["askv2"])
def buoi(message):
	cauhoi = message.text.split(" ", 1)
	if len(cauhoi) < 2:
		bot.reply_to(message, "Baby à,em phải nhập câu hỏi sau lệnh ask chứ!")
		return
	up = postcauhoiv2(cauhoi[1])
	sex = bot.reply_to(message, "⏳Đợi để lấy câu trả lời ...")
	time.sleep(3)
	bot.delete_message(chat_id=message.chat.id, message_id=sex.message_id)
	bot.reply_to(message, f"🌸 Đáp án:\n{up}")
@bot.message_handler(commands=["informationmanager"])
def buoi(message):
	if message.chat.type == "private":
		bot.reply_to(message, "🚫 Câu lệnh này không thể dùng được khi nhắn riêng đâu cô bé à 🚫")
		return
	try:
		phongnguchibucuxindauhang = message.chat.id
		owad = bot.get_chat_administrators(phongnguchibucuxindauhang)
		if not owad:
			bot.reply_to(message, "🚫 Tại sao phải làm bố trong khi ta có thể bỏ con?")
			return
		thnguxuka = ""
		for phongngu in owad:
			if phongngu.status in ["creator", "administrator"]:
				thnguxuka += f"💤 Tên: {phongngu.user.first_name}\n"
				thnguxuka += f"🚀 ID Telegram 🚀: {phongngu.user.id}\n"
				thnguxuka += f"🍷 Username 🍷: @{phongngu.user.username}\n"
		if thnguxuka:
			bot.reply_to(message, f"`{thnguxuka}`", parse_mode="MarkdownV2")
		else:
			bot.reply_to(message, "🚫 Không thể tìm thấy thông tin của 2 thằng ngu owner và admin 🚫")
	except:
		bot.reply_to(message, "🚫 Jack 5 củ bỏ con ❤ Lôn phòng 🚫")
@bot.message_handler(commands=["anime"])
def buoi(message):
	linkanh = [
		"https://i.pinimg.com/236x/d3/8c/c7/d38cc72d3f35fadc1b1a1f5e2c21eea1.jpg",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4H-LSWWxrTndrqiXCDkyxhwjVErOx862rMg&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG4y83tdO41FW-tqirmMh2PWNtPDMWDsnugw&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNwX09mJD7upbMp9xRwxJpa5r-MVUqRv9zow&s",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9KDVnsojTPLmqg7nX1WMEmyC1hv5yt8T5ZA&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLONOR1xIvsJI-Ih7_XmHBPuetPn64bEwRyQ&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiPg89-F-AsKdM5Tw-U2oAHDpM7-rxGzc7-A&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlbLMOQJkhe8GnuKT5g5-fVOyx3c1ycCbEKQ&usqp=CAU",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXen8XriobQuTTcHVqr3x3z6DR7vUISopewA&usqp=CAU",
	]
	chonanh = random.choice(linkanh)
	taianh = requests.get(chonanh)
	if taianh.status_code == 200:
		with open("nigger.jpg", "wb") as file:
			file.write(taianh.content)
		with open("nigger.jpg", "rb") as file:
			bot.send_photo(message.chat.id, file, caption="❤ Ảnh anime của bạn đã random xong ❤")
	else:
		bot.reply_to(message, "🚫 Không thể tải ảnh anime")
@bot.message_handler(commands=["status"])
def buoi(message):
	ram = psutil.virtual_memory()
	ramdung = ram.used / (1024 ** 3)
	tatcaram = ram.total / (1024 ** 3)
	phantram = (ram.used / ram.total) * 100
	guitinnhan = (
		f"📊 Thông tin về ram 📊:\n"
		f"🚀 Ram đã dùng 🚀: {ramdung:.2f} GB\n"
		f"🚀 Tất cả ram 🚀: {tatcaram:.2f} GB\n"
		f"🚀 Phần trăm ram đã dùng 🚀: {phantram:.2f}%"
	)
	bot.reply_to(message, guitinnhan)
@bot.message_handler(content_types=["new_chat_members"])
def buoicaclondai(message):
	for ngdungmoi in message.new_chat_members:
		ten = ngdungmoi.first_name
		if ngdungmoi.last_name:
			ten += f"{ngdungmoi.last_name}"
		tennhom = message.chat.title
		bot.send_video(message.chat.id, open("chaomung.mp4", "rb"), caption=f"Chào mừng {ten} đã tới nhóm {tennhom}")
@bot.message_handler(content_types=["left_chat_member"])
def buoicaclondai(message):
	roinhom = message.left_chat_member
	ten = roinhom.first_name
	if roinhom.last_name:
		ten += f"{roinhom.last_name}"
	tennhom = message.chat.title
	bot.send_video(message.chat.id, open("roinhom.mp4", "rb"), caption=f"🔆 Tạm biệt {ten} đã rời khỏi nhóm {tennhom},chúc bạn luôn khỏe mạnh 😊")
#@bot.message_handler()
#def lonbuoicacdai(message):
#	status = message.new_chat_member
#	if status.status == "kicked":
#		kick = status_user
#		ten = kick.first_name
#		if kick.last_name:#
#			ten += f"{kick.last_name}"
#		tennhom = message.chat.title
#	bot.send_video(message.chat.id, open("kick.mp4", "rb"), caption=f"🔆 người dùng {ten} đã bị kick khỏi nhóm {tennhom}")
@bot.message_handler(commands=["install"])
def buoi(message):
	phongngu = types.InlineKeyboardMarkup()
	ddos = types.InlineKeyboardButton("🚀 Script ddos 🚀", callback_data="scriptddos")
	tool = types.InlineKeyboardButton("💠 Tool TDS 💠", callback_data="tds")
	prx = types.InlineKeyboardButton("🌴 Proxy 🌴", callback_data="proxy")
	sim = types.InlineKeyboardButton("❄ Tool spam sms ❄", callback_data="sms")
	tele = types.InlineKeyboardButton("🧸 Source bot telegram 🧸", callback_data="telegram")
	src2 = types.InlineKeyboardButton("🛰️ Source C2 🛰️", callback_data="c2")
	tik = types.InlineKeyboardButton("🌍 Tiktok 🌍", callback_data="tiktok")
	phongngu.add(ddos)
	phongngu.add(src2)
	phongngu.add(tool)
	phongngu.add(prx)
	phongngu.add(sim)
	phongngu.add(tele, tik)
	bot.reply_to(message, " 🚀 Chọn lựa chọn sau 🚀:", reply_markup=phongngu)
@bot.callback_query_handler(func=lambda call: True)
def call(call):
	if call.data == "scriptddos":
		sex = types.InlineKeyboardMarkup()
		layer7 = types.InlineKeyboardButton("👑 Layer 7 👑", callback_data="l7")
		layer4 = types.InlineKeyboardButton("🚀 Layer 4 🚀", callback_data="l4")
		sex.add(layer7)
		sex.add(layer4)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🌍 Vui lòng chọn layer 🌍:",reply_markup=sex)
	elif call.data == "l7":
		oc = types.InlineKeyboardMarkup()
		storm = types.InlineKeyboardButton("💥 Storm 💥", callback_data="nm1")
		mars = types.InlineKeyboardButton("🚀 HTTP-MARS 🚀", callback_data="nm2")
		h2 = types.InlineKeyboardButton("🚀 H2 🚀", callback_data="nm3")
		tls = types.InlineKeyboardButton("🚀 TLS 🚀", callback_data="nm4")
		tlsv2 = types.InlineKeyboardButton("🚀 TLS SUPER 🚀", callback_data="nm5")
		reset = types.InlineKeyboardButton("🚀 Rapid Reset 🚀", callback_data="nm6")
		bypass = types.InlineKeyboardButton("🚀 Bypass 🚀", callback_data="nm7")
		oc.add(storm, mars)
		oc.add(h2, tls)
		oc.add(tlsv2, reset)
		oc.add(bypass)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🍷 Vui lòng chọn methods 🍷:", reply_markup=oc)
	elif call.data == "nm1":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/storm.js", "rb"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm2":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/HTTP-MARS.js"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm3":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/h2.js", "rb"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm4":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/tls.js", "rb"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm5":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/tls-super.js", "rb"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm6":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/rapid-reset.js", "rb"), caption="❄ Đây là script của bạn ❄")
	elif call.data == "nm7":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer7/bypass.js", "rb"), caption="❄ Đây là script của bạn ❄")
	if call.data == "l4":
		ngu = types.InlineKeyboardMarkup()
		tp = types.InlineKeyboardButton("🚀 TCP 🚀", callback_data="tcp")
		ov = types.InlineKeyboardButton("🚀 TCP-OVH 🚀", callback_data="ovh")
		ud = types.InlineKeyboardButton("🚀 UDP 🚀", callback_data="udp")
		ac = types.InlineKeyboardButton("🚀 ACK 🚀", callback_data="ack")
		ngu.add(tp, ov)
		ngu.add(ud, ac)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🍷 Chọn 1 methods 🍷", reply_markup=ngu)
	elif call.data == "tcp":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer4/TCP", "rb"), caption="🍷Đây là script của bạn 🍷")
	elif call.data == "ovh":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer4/tcp-ovh.c", "rb"), caption="🍷Đây là script của bạn 🍷")
	elif call.data == "udp":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer4/UDP", "rb"), caption="🍷Đây là script của bạn 🍷")
	elif call.data == "ack":
		bot.send_document(call.message.chat.id, open("stable/script_ddos/layer4/ACK", "rb"), caption="🍷Đây là script của bạn 🍷")
	if call.data == "tds":
		skid = types.InlineKeyboardMarkup()
		s1 = types.InlineKeyboardButton("🚀 TOOL TDS 🚀", callback_data="sex1")
		s2 = types.InlineKeyboardButton("🚀 ZYTHTOOL 🚀", callback_data="sex2")
		s3 = types.InlineKeyboardButton("🚀 XUATDEV 🚀", callback_data="sex3")
		s4 = types.InlineKeyboardButton("🚀 VLONG 🚀", callback_data="sex4")
		s5 = types.InlineKeyboardButton("🚀 CTOOL 🚀", callback_data="sex5")
		skid.add(s1, s2)
		skid.add(s3, s4)
		skid.add(s5)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="☄ Chọn một trong những người làm tool sau ☄:", reply_markup=skid)
	elif call.data == "sex1":
		bot.send_document(call.message.chat.id, open("stable/tool/tds.7z", "rb"), caption="🍷Đây là tool của bạn 🍷")
	elif call.data == "sex2":
		bot.send_document(call.message.chat.id, open("stable/tool/zythtool.7z", "rb"), caption="🍷Đây là tool của bạn 🍷")
	elif call.data == "sex3":
		bot.send_document(call.message.chat.id, open("stable/tool/xuatdev.7z", "rb"), caption="🍷Đây là tool của bạn 🍷")
	elif call.data == "sex4":
		bot.send_document(call.message.chat.id, open("stable/tool/vlong.7z", "rb"), caption="🍷Đây là tool của bạn 🍷")
	elif call.data == "sex5":
		bot.send_document(call.message.chat.id, open("stable/tool/ctool.7z", "rb"), caption="🍷Đây là tool của bạn 🍷")
	if call.data == "proxy":
		bot.send_document(call.message.chat.id, open("stable/proxy/proxies.txt", "rb"), caption="🔆 Đây là proxies của bạn 🔆")
	if call.data == "telegram":
		j97 = types.InlineKeyboardMarkup()
		ddos = types.InlineKeyboardButton("📈 SOURCE BOT DDOS 📈", callback_data="srcddos")
		spam = types.InlineKeyboardButton("📊 SOURCE BOT SPAM SMS 📊", callback_data="srcspam")
		taixiu = types.InlineKeyboardButton("💠 SOURCE BOT TÀI XỈU 💠", callback_data="srctaixiu")
		j97.add(taixiu)
		j97.add(ddos, spam)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="☕ Chọn 1 source ☕:", reply_markup=j97)
	elif call.data == "srcddos":
		bot.send_document(call.message.chat.id, open("stable/src/ddos.zip", "rb"), caption="☕ Đây là source bot ddos của bạn ☕")
	elif call.data == "srcspam":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Sorry, nhưng mà tui chưa thể tìm thấy src nào ngon như src bot ddos cả 💤")
	elif call.data == "srctaixiu":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Sorry, nhưng mà tui chưa thể tìm thấy src nào ngon như src bot ddos cả 💤")
	if call.data == "sms":
		bot.send_document(call.message.chat.id, open("stable/sms/sms.py", "rb"), caption="🌴 Đây là file spam sms của bạn 🌴")
bot.polling()

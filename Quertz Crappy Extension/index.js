let url;
let protocol;
let domain;
let path;
let https;
let http;
let certified;
let bypass;


document.getElementById("submit").onclick = function(){
url = document.getElementById("URLInput").value;
url = url.toLowerCase();
console.log(url)
https = Boolean(url.search("https://") + 1)
http = Boolean(url.search("http://") + 1)
console.log("https: ", https)
console.log("http: ", http)

switch(true){
    case https == true:
        protocol = true
        domain = url.slice(url.indexOf("//") + 2);
        path = domain.slice(domain.indexOf("/") + 1);
        domain = domain.slice(0, domain.indexOf("/"));

        break;
    case http == true:
        protocol = false
        domain = url.slice(url.indexOf("//") + 2);
        path = domain.slice(domain.indexOf("/") + 1);
        domain = domain.slice(0, domain.indexOf("/"));
        break;
    case http == false && https == false:
        domain = url
        path = domain.slice(domain.indexOf("/") + 1);
        domain = domain.slice(0, domain.indexOf("/"));
        bypass = true
        break;
}


console.log("Domain: ", domain)
console.log("Path: ", path)
console.log("Safe protocol = ", protocol)
console.log("Bypass = ", bypass)


let domainnumbers = Number(0);
let domainperiod = Number(0);
let domaindash = Number(0);
let domainweirdchara = Number(0);
let domainlength;
let domainfiltered;
let position;
let tempdomain = domain;
let tempbool;

//Domain number count

tempbool = Boolean(tempdomain.search(/0|1|2|3|4|5|6|7|8|9/) + 1)

while(tempbool == true){
    position = (tempdomain.search(/0|1|2|3|4|5|6|7|8|9/) + 1)
    tempdomain = tempdomain.slice(position)
    domainnumbers += 1
    tempbool = Boolean(tempdomain.search(/0|1|2|3|4|5|6|7|8|9/) + 1)
}

console.log("Numbers in Domain:", domainnumbers)

//Periods in Domain
tempdomain = domain
tempbool = Boolean(tempdomain.indexOf(".") + 1)

while(tempbool == true){
    tempdomain = tempdomain.slice(tempdomain.indexOf(".") + 1)
    domainperiod = domainperiod + 1;
    tempbool = Boolean(tempdomain.indexOf(".") + 1)
}

console.log("Number of Periods in Domain:", domainperiod)

//Dashes in Domain
tempdomain = domain
tempbool = Boolean(tempdomain.indexOf("-") + 1)

while(tempbool == true){
    tempdomain = tempdomain.slice(tempdomain.indexOf("-") + 1)
    domaindash = domaindash + 1;
    tempbool = Boolean(tempdomain.indexOf("-") + 1)
}

console.log("Number of Dashes in Domain:", domaindash)

//Weird Characters in Domain
tempdomain = domain
tempbool = Boolean(tempdomain.search(/[;?:@&=+$,]/) + 1)


while(tempbool == true){
    position = (tempdomain.search(/[;?:@&=+$,]/) + 1)
    tempdomain = tempdomain.slice(position)
    console.log(tempdomain)
    domainweirdchara = domainweirdchara + 1
    tempbool = Boolean(tempdomain.search(/[;?:@&=+$,]/) + 1)
}

console.log("Number of Weird Characters: ", domainweirdchara)


//Domain length
domainlength = Number(domain.length)
console.log("Length of Domain: ", domainlength)

//Submits results to frontend
document.getElementById("Numbers").innerHTML = domainnumbers;
document.getElementById("Periods").innerHTML = domainperiod;
document.getElementById("Dashes").innerHTML = domaindash;
document.getElementById("Weird").innerHTML = domainweirdchara;
document.getElementById("Length").innerHTML = domainlength;



let level = Number(0)

if  (domainnumbers >= 3){
    level = level + 1
}

if (domainperiod >= 3){
    level = level + 1
}

if (domaindash >= 1){
    level = level + 1
}

if (domainweirdchara >= 1){
    level = level + 1
}

if (domainlength > 25){
    level = level + 1
}

if (protocol == false){
    level = level + 3
}

if (bypass == true){
    level = level - 8
}

console.log("Failed score is: ", level)
score = 8 - level;
console.log("Score is: ", score, "/8")
let Pass;
if (level < 3){
    Pass = true
}

else{
    Pass = false
}

document.getElementById("Pass").innerHTML = Pass;
document.getElementById("https").innerHTML = protocol;
document.getElementById("Score").innerHTML = score;
}
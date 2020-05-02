#!/usr/bin/env node

const coap = require("node-coap-client").CoapClient;

var args = process.argv.slice(2);

var options = {
    "host": "localhost",
    "port": "5683",
    "query": "profile/card",
}

function createOptions() {

    var rgx = /(^--)/;

    for( var i = 0; i < args.length; i++ ) {
        if( args[i].match(rgx) ) {
            options[args[i].slice(2)] = args[i + 1] || "<no-value>";
        }
    }
};

function measureCoap() {
    // [seconds, nanoseconds]
    hrstart = process.hrtime();
    //console.log(options);

    if (options.method == "get" || options.method == "delete") {
        payload = Buffer.from("")
    } else {
        payload = Buffer.from("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>. @prefix sosa: <http://www.w3.org/ns/sosa/> . @prefix ssn: <http://www.w3.org/ns/ssn/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> . @prefix cdt: <http://w3id.org/lindt/custom_datatypes#> . @prefix idsSensor: <http://www.iml.fraunhofer.de/ids/sensor#> .         <./> rdf:type sosa:Result ;     sosa:isResultOf <120636/2020-10-24T01:22:30.866Z> ;     sosa:hasSimpleResult \"42 Cel\"^^cdt:ucum .")
    }
    
    coap
    .request(
        options.uri,
        options.method,
        payload
    )
    .then(response => { 
        hrend = process.hrtime(hrstart);
        console.log('%s, %f, %s, %s, %s', response.code.toString(), (hrend[0] + hrend[1] / 1e9).toFixed(3) * 1000, options.uri, options.method, new Date(Date.now()).toLocaleString());
        //console.log(response.payload.toString());
        process.exit();
    })
    .catch(err => { console.log(err); });
}


createOptions();
measureCoap();

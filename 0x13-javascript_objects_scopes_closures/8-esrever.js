#!/usr/bin/node

const esrever = (list) => list.reduceRight((acc, element) => [...acc, element], []);

module.exports = { esrever };

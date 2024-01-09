#!/usr/bin/node

const { readFile, appendFile } = require('fs/promises');
const [, , source1, source2, destenation] = process.argv;

readFile(source1).then(content => appendFile(destenation, content));
readFile(source2).then(content => appendFile(destenation, content));

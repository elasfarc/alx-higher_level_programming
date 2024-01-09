#!/usr/bin/node

const firstArg = process.argv[2];

if (parseInt(firstArg)) {
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

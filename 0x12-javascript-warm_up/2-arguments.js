#!/usr/bin/node

const { argv } = require('node:process');

const argc = argv.length;

if (argc > 3) {
  console.log('Arguments found');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

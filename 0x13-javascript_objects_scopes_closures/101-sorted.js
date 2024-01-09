#!/usr/bin/node

const occurrencesByUser = require('./101-data').dict;

const userByOccurrences = Object.entries(occurrencesByUser).reduce((acc, [userId, occurrence]) => ({
  ...acc,
  [occurrence]: acc[occurrence] ? [...acc[occurrence], userId] : [userId]
}), {});

console.log(userByOccurrences);

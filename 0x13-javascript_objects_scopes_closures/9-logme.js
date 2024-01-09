#!/usr/bin/node

exports.logMe = (() => {
  let counter = 0;
  return (item) => {
    console.log(`${counter++}: ${item}`);
  };
})();

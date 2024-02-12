#!/usr/bin/node
const { argv } = process;
if (argv.length > 2) {
  if (typeof (parseInt(argv[2])) === 'number') {
    console.log('My number: ' + argv[2]);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('No argument');
}

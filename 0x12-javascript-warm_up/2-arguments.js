#!/usr/bin/node
const { argv } = process;
if (argv.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}

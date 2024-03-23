#!/usr/bin/node
const argsVar = process.argv.length - 2;
if (argsVar == 0) {
    console.log("No argument");
  } else if (argsVar== 1) {
    console.log("Argument found");
  } else {
    console.log("Arguments found");
  }

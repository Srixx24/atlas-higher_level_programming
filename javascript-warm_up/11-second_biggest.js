#!/usr/bin/node
if (process.argv[3] == undefined) {
  console.log(0);
}else {
  const numb = process.argv.slice(2);
  numb.sort(( a, b) => b - a);
  const secnBig = numb[1]
  console.log(secnBig);
}

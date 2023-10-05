// 8-clean_set.js

export default function cleanSet(set, startString) {
  const restString = [];

  if (startString) {
    for (const value of set) {
      if (value.startsWith(startString)) {
        const restOfString = value.slice(startString.length);
        restString.push(restOfString);
      }
    }

    const cleanRestString = restString.join('-');

    return cleanRestString;
  }
  return '';
}

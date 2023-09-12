/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    const dataArray = [];
    for (const idx of array) {
      dataArray.push(appendString + idx);
    }
  
    return dataArray;
  }
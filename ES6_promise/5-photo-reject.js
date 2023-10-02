// 5-photo-reject.js

export default function uploadPhoto(fileName) {
  return new Promise((reject) => {
    reject(`${fileName} cannot be processed`);
  });
}

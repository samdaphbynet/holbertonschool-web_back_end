// 3-all.js

import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const first = await uploadPhoto();
  const second = await createUser();

  console.log(`${first.body} ${second.firstName} ${second.lastName}`);
}
